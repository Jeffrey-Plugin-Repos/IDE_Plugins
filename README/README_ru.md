# IDE_Plugins

Плагины для [JEditor](https://github.com/Integration-Automation/JEDITOR) и
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). Это репозиторий по умолчанию для их
*Plugins → Plugin Browser*.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <strong>Русский</strong>
</p>

Как написать плагин (API, metadata, конфигурации запуска, правила обнаружения):
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
единое руководство для обоих редакторов.

## Плагины

| Плагин | Файл | Особенности | Запуск через… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | компиляция `gcc`, затем запуск (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | компиляция `g++`, затем запуск (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (исходник из одного файла, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | компиляция `rustc`, затем запуск |
| French Translation | `languages/french.py` | язык интерфейса *Francais* | — |

Для записей запуска необходим компилятор или интерпретатор в `PATH`.

## Установка

- **Plugin Browser** (рекомендуется): откройте *Plugins → Plugin Browser* в JEditor или PyBreeze,
  нажмите *Fetch Plugins*, выберите файл и нажмите *Download & Install*. Файл сохраняется в
  `jeditor_plugins/` в рабочем каталоге редактора; перезапустите редактор, чтобы загрузить его.
- **Вручную**: скопируйте файл в `jeditor_plugins/` или клонируйте этот репозиторий внутрь него.
  Папки без `__init__.py` (например, `program_languages/`) сканируются рекурсивно, поэтому загружается
  весь checkout.

## Как добавить плагин

- Один файл `.py` на плагин, импортирующий только `PySide6` и `je_editor.plugins`, с функцией
  `register()`; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` и `PLUGIN_RUN_CONFIG` необязательны.
- Помещайте плагины языков программирования в `program_languages/`, а переводы интерфейса — в
  `languages/`.
- Plugin Browser перечисляет каждый файл `.py` в этом репозитории и пропускает только имена,
  начинающиеся с `.`, а также `LICENSE` и `README.md`, поэтому не добавляйте сюда вспомогательные
  скрипты или тесты в виде файлов `.py`.
