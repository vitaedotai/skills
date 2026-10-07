# Recruiting skills have moved

The canonical source is now [vitaedotai/agent](https://github.com/vitaedotai/agent). One **Vitae** plugin includes the MCP connector, app usage and onboarding guidance, and all nine recruiting workflows. No separate Vitae Recruiter application or second plugin installation is needed.

## Install the unified plugin

Claude Code:

```text
/plugin marketplace add vitaedotai/agent
/plugin install vitae@vitae
```

Codex:

```bash
codex plugin marketplace add vitaedotai/agent
```

Refresh sources and install Vitae in a supported client. Source registration alone does not install the plugin. See [all client installation paths](https://github.com/vitaedotai/agent#install).

## Install individual skills

```bash
bunx skills add vitaedotai/agent --skill candidate-outreach
bunx skills add vitaedotai/agent --skill vitae
bunx skills add vitaedotai/agent --list
```

Individual skill installations provide instructions. Recruiting drafts can use supplied context without an account; connected Vitae actions require OAuth, the intended workspace, live tools and the user's authorization. Inspect the live catalog before a send or booking and distinguish drafts, pending approvals and completed actions.

## Repository status

This repository retains the original nine-skill 0.1.0 snapshot and its existing packaging for reference. Future skill changes, releases, contributions, directory applications and upload ZIPs belong in `vitaedotai/agent`. The retained manifests do not establish a separate live directory listing. Use the unified package for new installations.

- [Current skill catalog](https://github.com/vitaedotai/agent#included-skills)
- [Authoring guide](https://github.com/vitaedotai/agent/blob/main/docs/recruiter-authoring.md)
- [Contribution checks](https://github.com/vitaedotai/agent/blob/main/CONTRIBUTING.md)
- [Support](https://github.com/vitaedotai/agent/issues)

Candidate assessments support human recruiter review. Examples are fictional; keep candidate information and credentials out of public repositories.
