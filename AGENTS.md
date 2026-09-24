# Maintaining Vitae recruiting skills

This is the canonical public recruiter skill catalog. Connection packaging and the one platform operating skill belong in `vitaedotai/agent`. Do not copy internal engineering skills here.

Each skill must be individually installable through the Skills CLI. Keep references inside its directory; never require sibling files at runtime. Use the Agent Skills specification for frontmatter and the repository authoring guide for content.

Use fictional examples and verified tool names. Do not publish customer data, credentials, private policies, or copied third-party content without its license. A model-generated assessment is not a hiring decision.

Validate with `python3 scripts/validate.py`, the regression suite, and Skills CLI discovery on an authorized host. Keep catalog paths and versions aligned. Use scoped PRs and independent review; never call an unrun behavioral evaluation a pass.
