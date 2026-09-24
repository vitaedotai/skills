# Contributing

See [the authoring guide](docs/authoring.md). Add a top-level directory with a real `SKILL.md`, update `catalog.json` and README, and include a fictional example.

On an authorized verification host:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
DISABLE_TELEMETRY=1 bunx skills add . --list
```

For installation acceptance, create an isolated working directory and install from an absolute path to this checkout with `--skill candidate-outreach --agent codex --agent claude-code --yes`. Confirm the installed files and their references exist. Do not install test packages globally into a recruiter's real environment.

CI validates format and discovery. The [behavioral cases](evals/cases.md) assess output quality separately. Release notes should distinguish automated checks, reviewer evaluation, and live product acceptance.

MIT applies to original catalog content. Brand assets identify Vitae and do not grant rights to imply affiliation or endorsement.
