# CLAUDE.md - IDE_Plugins

Remote plugin repository for JEditor and PyBreeze: syntax-highlighting and run-configuration plugins for C, C++, Go, Java and Rust, plus a French translation. JEditor's plugin browser (`je_editor/pyside_ui/main_ui/plugin_browser/`) lists this repository recursively through the GitHub contents API and downloads every `.py` file into the user's `jeditor_plugins/` directory. See `architecture.md`.

## Plugin contract

- Every language plugin module defines `PLUGIN_RUN_CONFIG` and `register()`; translation plugins define `register()`. The loader is `je_editor/plugins/plugin_loader.py` in JEditor.
- Only `.py` files are downloaded, so documentation files (`*.md`, `docs/`) never reach users.

## README (keep current)

**`README.md` must stay in sync with the code.** README is the only user-facing doc this repo ships
(the plugin browser downloads `.py` files only). This repo now ships a nine-language README set:
English `README.md` plus `README/README_<lang>.md` for `zh-TW`, `zh-CN`, `ja`, `ko`, `es`, `fr`,
`de`, `pt-BR`, `ru`. Any user-facing change — new or changed plugins, the plugin contract, supported
languages, install/setup — updates `README.md` **and every one of the nine language variants in the
same commit**, structure and content aligned, never one language ahead of the others. No test guards
this, so it is a manual check.

## Git commits

- Commit messages, PR titles and bodies must not mention any AI tool or model, and never carry `Co-Authored-By` or "Generated with" lines.
- Publish plugin changes on `main`: that is the branch the plugin browser reads.

## Stage commits, `progress.md`, `docs/updates/` and `architecture.md`

Workspace rule shared by every repository under `D:\Codes` (full text: `D:\Codes\CLAUDE.md`).

- **Commit at every stage.** A stage is the smallest piece of work that leaves the repository consistent and passes this project's checks (definition of done, tests, lint): one finished `progress.md` item, or one self-contained step of a larger one. Commit it before starting the next stage, before switching to another repository, and before the session ends. Do not leave work uncommitted across sessions; if a stage cannot be finished, commit the consistent part and record the rest in `progress.md`.
  - Stage only the files that stage touched (`git add <path>`, never `git add -A`), follow this file's commit-message rules, and never add AI attribution.
  - Committing is not pushing: push or open a PR only as this project's branch flow says or when asked.
- **`progress.md`** (repository root, tracked) holds outstanding work only: no finished items, no history, no rules.
- **`docs/updates/`** records finished work: one batch file per month (`YYYY-MM.md`), one entry per piece of work headed `## U-YYYYMMDD-NN · date · title · #tags`, and an index with query commands in `docs/updates/README.md`. When a `progress.md` item is done, delete it and add a `#done` entry plus its index row in the same commit.
- **`architecture.md`** (repository root) is the short architecture overview: layers, entry points, main flows, extension points, cross-project boundaries. Update it in the same commit whenever a change alters any of those.
- **Cross-project contracts** are listed in `architecture.md` §6: what other repositories rely on here (CLI flags, import paths, constructor arguments, file layouts) and what this repository relies on elsewhere. No test here protects them, so never rename or remove one without changing its consumers in the same round, and update §6 whenever a contract is added or changes.
