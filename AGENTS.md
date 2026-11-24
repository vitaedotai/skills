# Historical recruiting skills snapshot

The canonical source for all ten skills and the unified connector plugin is `vitaedotai/agent`. Make future recruiting workflow changes there. This repository retains the original 0.1.0 snapshot; do not create another active plugin application or release from it.

Keep its retained files readable and individually self-contained. Snapshot corrections must preserve catalog and manifest parity, fictional examples, user authorization, live-tool checks and human hiring decisions. Run affected checks on the authorized verification host; required current-head CI governs merge. Separate model reviewers require an explicit user request.

## Claude model routing

- Standard implementation: Claude Sonnet 5.5.
- Big implementation (large or cross-cutting changes) and planning: Claude Opus 5.5 or newer.
- Audits, major or minor: the latest Claude Fable (5.2 today). Fable never implements or edits code.
