# IDE_Plugins Architecture

> Short overview for people and agents.
> Last verified: 2026-09-22 against `6650862` on `main`.

## 1. Purpose

This is the default plugin repository for JEditor's plugin browser. PyBreeze reuses the same plugin
system. It holds syntax-highlighting and run-config plugins for C, C++, Go, Java and Rust, plus a
French UI translation. Nothing here is packaged, tested or imported: users download files through
the plugin browser or copy them into `jeditor_plugins/`.

## 2. Layers and directories

| Path | Responsibility |
| --- | --- |
| `program_languages/{c,cpp,go,java,rust}_syntax.py` | Keyword and rule tables. `register()` calls `register_programming_language()` for each suffix. `PLUGIN_RUN_CONFIG`: C, C++ and Rust compile then run; Go runs `go run`; Java runs `java` |
| `languages/french.py` | `french_word_dict` and a `register()` that calls `register_natural_language()`. No run config |

## 3. How plugins are loaded

```
Plugin browser (je_editor/pyside_ui/main_ui/plugin_browser/) lists this repo's .py files
  → download into ./jeditor_plugins/ → restart → load_external_plugins() (je_editor/plugins/plugin_loader.py)
    scans jeditor_plugins/, recursing into folders without __init__.py, so a copy of the whole repo also loads
  → reads PLUGIN_NAME / PLUGIN_AUTHOR / PLUGIN_VERSION / PLUGIN_RUN_CONFIG → calls register()
```

Each file imports only `PySide6` and `je_editor.plugins` and must define `register()`. The other
attributes are optional. Run-config keys (`name`, `suffixes`, `compiler`, `args`, `compile_then_run`,
`output_flag`) are documented in JEditor's `PLUGIN_GUIDE.md`.

## 6. Cross-project boundaries

- **Registry API**: `register_programming_language(suffix, syntax_words, syntax_rules)` and
  `register_natural_language(language_key, display_name, word_dict)` in `je_editor/plugins/__init__.py`.
  A signature change there breaks these files.
- **Repo URL**: `_DEFAULT_REPO_URL` in `je_editor/pyside_ui/main_ui/plugin_browser/plugin_browser_widget.py`.
  Moving or renaming this repo needs a JEditor change.
- **Translation keys**: `french.py` follows the keys of `je_editor/utils/multi_language/english.py`.
  Missing keys fall back to English.
- **Run configs**: JEditor runs them via `ExecManager.exec_with_plugin_config()`, PyBreeze via
  `FileRunnerProcess`. Compilers are called by bare name, so they must be on `PATH`.

## 8. When to update this file

Update it when a plugin file or folder is added, removed or renamed; when JEditor's plugin convention
changes (loader rules, registry signatures, run-config keys); or when the default plugin repo moves.
Refresh the "Last verified" line when you re-check this file.
