# IDE_Plugins

Plugins for [JEditor](https://github.com/Integration-Automation/JEDITOR) and
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). This is the default repository of
their *Plugins → Plugin Browser*.

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

---

# IDE_Plugins（繁體中文）

[JEditor](https://github.com/Integration-Automation/JEDITOR) 與
[PyBreeze](https://github.com/Integration-Automation/PyBreeze) 的插件，也是它們 *插件 → Plugin Browser* 的預設來源。

怎麼寫插件（API、metadata、執行設定、載入規則）請看兩個編輯器共用的
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**。

## 插件清單

| 插件 | 檔案 | 語法高亮 | 執行 |
|---|---|---|---|
| C 語法高亮 | `program_languages/c_syntax.py` | `.c`、`.i` | `gcc` 編譯後執行（`.c`） |
| C++ 語法高亮 | `program_languages/cpp_syntax.py` | `.cpp`、`.cxx`、`.cc`、`.h`、`.hpp`、`.hxx` | `g++` 編譯後執行（`.cpp`、`.cxx`、`.cc`） |
| Go 語法高亮 | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java 語法高亮 | `program_languages/java_syntax.py` | `.java`、`.jav` | `java`（單檔原始碼，Java 11 以上） |
| Rust 語法高亮 | `program_languages/rust_syntax.py` | `.rs` | `rustc` 編譯後執行 |
| 法文翻譯 | `languages/french.py` | 介面語言 *Francais* | — |

執行功能需要對應的編譯器或直譯器在 `PATH` 上。

## 安裝

- **插件瀏覽器**（建議）：在 JEditor 或 PyBreeze 開 *插件 → Plugin Browser*，按 *Fetch Plugins*，選好檔案後按
  *Download & Install*。檔案會存到編輯器工作目錄下的 `jeditor_plugins/`，重新啟動編輯器後生效。
- **手動**：把檔案複製到 `jeditor_plugins/`，或直接把整個 repo clone 進去。沒有 `__init__.py` 的資料夾
  （例如 `program_languages/`）會被遞迴掃描，所以整份 checkout 都會載入。

## 貢獻插件

- 一個插件一個 `.py` 檔，只 import `PySide6` 與 `je_editor.plugins`，並提供 `register()`；
  `PLUGIN_NAME`、`PLUGIN_AUTHOR`、`PLUGIN_VERSION`、`PLUGIN_RUN_CONFIG` 可選。
- 程式語言插件放 `program_languages/`，介面翻譯放 `languages/`。
- 插件瀏覽器會列出本 repo 的每一個 `.py` 檔，只略過 `.` 開頭、`LICENSE` 與 `README.md`，所以不要在這裡放
  輔助腳本或測試用的 `.py` 檔。
