"""Validate portable metadata, catalog parity, and standalone references."""
import json
from pathlib import Path
import re
import sys
from skill_format import validate_skill, validate_links

ROOT=Path(__file__).resolve().parents[1]
PLUGIN_MANIFESTS=['.claude-plugin/plugin.json','.cursor-plugin/plugin.json',
                  '.codex-plugin/plugin.json']

def validate_plugins(root,catalog):
    errors=[]
    paths=[f"./{entry['name']}" for entry in catalog['skills']]
    identity='vitae-recruiting-skills'
    for name in PLUGIN_MANIFESTS:
        manifest=json.loads((root/name).read_text())
        if manifest.get('name')!=identity or manifest.get('version')!=catalog['version']:
            errors.append(f'{name}: plugin identity or version drift')
        if manifest.get('skills')!=paths:
            errors.append(f'{name}: plugin skills do not match catalog')
        if any(key in manifest for key in ('mcpServers','apps','hooks')):
            errors.append(f'{name}: recruiting plugin must contain skills only')
    claude=json.loads((root/'.claude-plugin/marketplace.json').read_text())
    entries=claude['plugins']
    if (claude.get('name')!=identity or claude['metadata'].get('version')!=catalog['version']
        or len(entries)!=1 or entries[0].get('name')!=identity
        or entries[0].get('source')!='./' or entries[0].get('version')!=catalog['version']):
        errors.append('Claude marketplace identity, source, or version drift')
    codex=json.loads((root/'.agents/plugins/marketplace.json').read_text())
    entries=codex['plugins']
    if (codex.get('name')!=identity or len(entries)!=1 or entries[0].get('name')!=identity
        or entries[0].get('source')!={'source':'local','path':'./'}
        or entries[0].get('policy')!={'installation':'AVAILABLE'}):
        errors.append('Codex marketplace source or policy drift')
    interface=json.loads((root/'.codex-plugin/plugin.json').read_text())['interface']
    for key in ('logo','composerIcon'):
        path=interface[key]
        target=(root/path).resolve()
        if not path.startswith('./') or not target.is_relative_to(root.resolve()) or not target.is_file():
            errors.append(f'Codex {key}: invalid asset path')
    return errors

def validate(root=ROOT):
    errors=[]
    try:
        catalog=json.loads((root/'catalog.json').read_text())
        entries=catalog['skills']
        names=[entry['name'] for entry in entries]
        if not names or len(names)!=len(set(names)):
            errors.append('catalog must have unique skill names')
        paths={str(p.relative_to(root)) for p in root.glob('*/SKILL.md')}
        if paths!={e['path'] for e in entries}:
            errors.append('catalog paths do not match installed skills')
        for entry in entries:
            path=root/entry['path']
            if entry['path']!=f"{entry['name']}/SKILL.md":
                errors.append('catalog path must match skill name')
                continue
            skill_errors,front=validate_skill(path)
            errors.extend(skill_errors)
            if front.get('metadata',{}).get('version')!=catalog['version']:
                errors.append(f'{path}: version drift')
            if front.get('description')!=entry['description']:
                errors.append(f'{path}: catalog description drift')
            for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' not in link and not link.startswith(('mailto:','#')):
                    target=(path.parent/link.split('#')[0]).resolve()
                    if not target.is_relative_to(path.parent.resolve()):
                        errors.append(f'{path}: runtime reference escapes individual skill')
        errors.extend(validate_plugins(root,catalog))
        errors.extend(validate_links(root))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        errors.append(f'invalid catalog: {exc}')
    return errors

if __name__=='__main__':
    errors=validate()
    print('\n'.join(errors) if errors else 'Recruiter catalog validation passed')
    sys.exit(bool(errors))
