"""Validate portable metadata, catalog parity, and standalone references."""
import json
from pathlib import Path
import re
import sys
from skill_format import validate_skill, validate_links

ROOT=Path(__file__).resolve().parents[1]

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
        errors.extend(validate_links(root))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        errors.append(f'invalid catalog: {exc}')
    return errors

if __name__=='__main__':
    errors=validate()
    print('\n'.join(errors) if errors else 'Recruiter catalog validation passed')
    sys.exit(bool(errors))
