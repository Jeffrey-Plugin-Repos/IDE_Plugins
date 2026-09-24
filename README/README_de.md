# IDE_Plugins

Plugins für [JEditor](https://github.com/Integration-Automation/JEDITOR) und
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). Dies ist das Standard-Repository
ihres *Plugins → Plugin Browser*.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <strong>Deutsch</strong> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

Wie man ein Plugin schreibt (API, metadata, Ausführungskonfigurationen, Erkennungsregeln):
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
der eine Leitfaden für beide Editoren.

## Plugins

| Plugin | Datei | Highlights | Ausführen mit… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | mit `gcc` kompilieren, dann ausführen (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | mit `g++` kompilieren, dann ausführen (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (Einzeldatei-Quelle, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | mit `rustc` kompilieren, dann ausführen |
| French Translation | `languages/french.py` | UI-Sprache *Francais* | — |

Die Ausführungseinträge benötigen den Compiler oder Interpreter im `PATH`.

## Installation

- **Plugin Browser** (empfohlen): Öffne *Plugins → Plugin Browser* in JEditor oder PyBreeze, klicke
  auf *Fetch Plugins*, wähle eine Datei und klicke auf *Download & Install*. Die Datei wird unter
  `jeditor_plugins/` im Arbeitsverzeichnis des Editors gespeichert; starte den Editor neu, um sie zu
  laden.
- **Von Hand**: Kopiere eine Datei nach `jeditor_plugins/`, oder klone dieses Repository hinein.
  Ordner ohne `__init__.py` (wie `program_languages/`) werden rekursiv gescannt, sodass der gesamte
  Checkout geladen wird.

## Ein Plugin beitragen

- Eine `.py`-Datei pro Plugin, die nur `PySide6` und `je_editor.plugins` importiert, mit einer
  `register()`-Funktion; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` und `PLUGIN_RUN_CONFIG`
  sind optional.
- Lege Sprach-Plugins in `program_languages/` und UI-Übersetzungen in `languages/` ab.
- Der Plugin Browser listet jede `.py`-Datei in diesem Repository auf und überspringt nur Namen, die
  mit `.` beginnen, sowie `LICENSE` und `README.md`. Füge daher hier keine Hilfsskripte oder Tests
  als `.py`-Dateien hinzu.
