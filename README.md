<p align="center"><a href="https://vitae.ai"><img src="assets/logo.png" width="96" height="96" alt="Vitae.ai" /></a></p>

# Vitae recruiting skills

Practical recruiting workflows for people and AI assistants. Use them with supplied context, or connect Vitae to work with authorized records.

## Install with the Skills CLI

```bash
bunx skills add vitaedotai/skills
```

Choose one skill or target specific agents:

```bash
bunx skills add vitaedotai/skills --skill candidate-outreach
bunx skills add vitaedotai/skills --agent codex --agent claude-code
bunx skills add vitaedotai/skills --list
```

The CLI installs from this GitHub repository. [skills.sh](https://skills.sh) provides discovery; a repository does not need an npm package to supply skills. Installations do not configure a Vitae connector or authenticate an account. Use [vitaedotai/agent](https://github.com/vitaedotai/agent) for that.

## Install the recruiting skills plugin

The **Vitae Recruiting Skills** plugin bundles all nine workflows. It contains instructions only; use the separate [Vitae connector plugin](https://github.com/vitaedotai/agent) for authenticated access to Vitae records.

### Claude Code

```text
/plugin marketplace add vitaedotai/skills
/plugin install vitae-recruiting-skills@vitae-recruiting-skills
```

### Codex

```bash
codex plugin marketplace add vitaedotai/skills
```

Refresh plugin sources and install **Vitae Recruiting Skills** in a supported client. Adding the source alone does not install the plugin.

### Cursor and public directories

This repository includes a native Cursor manifest. Public Cursor, Claude, and OpenAI listings remain pending until their directories approve and publish the package. The manifests do not establish marketplace availability or client acceptance.

For an OpenAI upload ZIP, run `python3 scripts/package.py`. The package includes the Codex manifest and the existing skill folders without copying or relocating their source. See [contribution checks](CONTRIBUTING.md) for verification.

## Catalog

| Skill | Use it to |
| --- | --- |
| [job-intake](job-intake/SKILL.md) | Turn a recruiting vacancy or hiring-manager conversation into an agreed job brief, with requirements, constraints, and open questions. |
| [hiring-scorecard](hiring-scorecard/SKILL.md) | Build a job-related evaluation scorecard with evidence criteria and anchored ratings before screening or interviews. |
| [sourcing-strategy](sourcing-strategy/SKILL.md) | Translate an agreed hiring brief into candidate search hypotheses, search queries, channels, and a measurable sourcing plan. |
| [candidate-screening](candidate-screening/SKILL.md) | Compare candidate evidence with an agreed role scorecard, identify missing information, and prepare a recruiter review without making automatic hiring decisions. |
| [candidate-outreach](candidate-outreach/SKILL.md) | Write personalized initial recruiting invitations and follow-ups using verified role and candidate facts, with clear calls to action and respectful stop conditions. |
| [interview-invitation](interview-invitation/SKILL.md) | Draft a clear interview invitation or rescheduling message with confirmed stage, time zone, duration, format, participants, and preparation. |
| [interview-kit](interview-kit/SKILL.md) | Prepare a structured interview plan with job-related questions, follow-up probes, evidence notes, and calibrated assessment guidance. |
| [candidate-presentation](candidate-presentation/SKILL.md) | Create a factual candidate shortlist or client presentation from authorized candidate records, role criteria, and screening or interview evidence. |
| [recruitment-workflow](recruitment-workflow/SKILL.md) | Coordinate a recruitment assignment from intake to candidate presentation, select the appropriate recruiter skill, and track evidence, owners, approvals, and next actions. |

## Try a skill

“Use candidate-outreach to draft an invitation for this role and candidate. Use only the facts I supply, flag missing details, and do not send it.”

Each skill includes inputs, a practical procedure, output expectations, an example, quality checks, and handoff guidance. The workflow coordinator uses only the specialist skills needed for the current stage.

## With Vitae

The recruiting methods work from supplied documents without an account. Connected actions require a separately installed connector, the intended workspace, live tool availability, and the user's authorization. The current public connector can read many recruiting records and request governed changes, but it does not expose direct email sending or calendar booking. The skills return drafts and precise manual handoffs where tools are unavailable.

Candidate assessments support recruiter review. They do not make automatic hiring decisions. Examples are fictional. Keep real candidate and client data out of this repository.

## Privacy and support

This plugin contains readable recruiting instructions and static assets. It has no MCP server, service credentials, telemetry, or storage service of its own. The assistant processes the context you authorize under its provider's terms and privacy policy. The instructions can use personal recruiting information, so supply only the context needed for the task.

Connecting the separate Vitae connector gives the assistant access to records in the workspace you authorize. Those actions and any records saved through that connector are governed by the workspace's permissions, approvals, and applicable privacy notices. See [Vitae's privacy notice](https://vitae.ai/privacy) and [terms](https://vitae.ai/terms). Report plugin issues through [GitHub support](https://github.com/vitaedotai/skills/issues), using fictional examples rather than candidate data or credentials.

## Quality and contributions

Follow [the authoring guide](docs/authoring.md) and [contribution checks](CONTRIBUTING.md). CI validates portable metadata, catalog consistency, local references, and Skills CLI discovery. Behavioral evaluation cases are in [evals/cases.md](evals/cases.md).

The initial catalog covers intake through candidate presentation. Later lifecycle steps are described as recruiter handoffs, not falsely advertised as implemented skills.

[Vitae.ai](https://vitae.ai) · [Connect your assistant](https://github.com/vitaedotai/agent) · [Agent Skills format](https://agentskills.io/specification)

[LinkedIn](https://www.linkedin.com/company/vitae-ai) · [X](https://x.com/vitaeai) · [Open Vitae](https://app.vitae.ai)
