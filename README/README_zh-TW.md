# IDE_Plugins

[JEditor](https://github.com/Integration-Automation/JEDITOR) 與
[PyBreeze](https://github.com/Integration-Automation/PyBreeze) 的插件，也是它們 *插件 → Plugin Browser* 的預設來源。

<p align="center">
  <a href="../README.md">English</a> ·
  <strong>繁體中文</strong> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

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
