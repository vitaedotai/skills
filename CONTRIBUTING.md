# Contributions moved

Submit new workflows, fixes and release changes to [vitaedotai/agent](https://github.com/vitaedotai/agent). Follow its [authoring guide](https://github.com/vitaedotai/agent/blob/main/docs/recruiter-authoring.md) and [verification instructions](https://github.com/vitaedotai/agent/blob/main/CONTRIBUTING.md).

The retained 0.1.0 snapshot can be checked on the authorized verification host with:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
```

Do not create a second active plugin release here. The current portable upload ZIP is built in the unified agent repository.
