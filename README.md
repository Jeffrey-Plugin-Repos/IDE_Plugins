# IDE_Plugins

Plugins for [JEditor](https://github.com/Integration-Automation/JEDITOR) and
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). This is the default repository of
their *Plugins → Plugin Browser*.

<p align="center">
  <strong>English</strong> ·
  <a href="README/README_zh-TW.md">繁體中文</a> ·
  <a href="README/README_zh-CN.md">简体中文</a> ·
  <a href="README/README_ja.md">日本語</a> ·
  <a href="README/README_ko.md">한국어</a> ·
  <a href="README/README_es.md">Español</a> ·
  <a href="README/README_fr.md">Français</a> ·
  <a href="README/README_de.md">Deutsch</a> ·
  <a href="README/README_pt-BR.md">Português (BR)</a> ·
  <a href="README/README_ru.md">Русский</a>
</p>

How to write a plugin (API, metadata, run configurations, discovery rules):
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
the one guide for both editors.

## Plugins

| Plugin | File | Highlights | Run with… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | `gcc` compile, then run (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | `g++` compile, then run (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (single-file source, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | `rustc` compile, then run |
| French Translation | `languages/french.py` | UI language *Francais* | — |

The run entries need the compiler or interpreter on `PATH`.

## Installing

- **Plugin Browser** (recommended): open *Plugins → Plugin Browser* in JEditor or PyBreeze, press
  *Fetch Plugins*, pick a file and press *Download & Install*. The file is saved into
  `jeditor_plugins/` under the editor's working directory; restart the editor to load it.
- **By hand**: copy a file into `jeditor_plugins/`, or clone this repository into it. Folders without
  `__init__.py` (such as `program_languages/`) are scanned recursively, so the whole checkout loads.

## Contributing a plugin

- One `.py` file per plugin, importing only `PySide6` and `je_editor.plugins`, with a `register()`
  function; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` and `PLUGIN_RUN_CONFIG` are optional.
- Put language plugins in `program_languages/` and UI translations in `languages/`.
- The Plugin Browser lists every `.py` file in this repository and skips only names starting with
  `.`, `LICENSE` and `README.md`, so do not add helper scripts or tests as `.py` files here.
