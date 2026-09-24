# IDE_Plugins

[JEditor](https://github.com/Integration-Automation/JEDITOR) 与
[PyBreeze](https://github.com/Integration-Automation/PyBreeze) 的插件，也是它们 *插件 → Plugin Browser* 的默认来源。

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <strong>简体中文</strong> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

如何编写插件（API、metadata、运行配置、加载规则）请看两个编辑器共用的
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**。

## 插件列表

| 插件 | 文件 | 语法高亮 | 运行 |
|---|---|---|---|
| C 语法高亮 | `program_languages/c_syntax.py` | `.c`、`.i` | `gcc` 编译后运行（`.c`） |
| C++ 语法高亮 | `program_languages/cpp_syntax.py` | `.cpp`、`.cxx`、`.cc`、`.h`、`.hpp`、`.hxx` | `g++` 编译后运行（`.cpp`、`.cxx`、`.cc`） |
| Go 语法高亮 | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java 语法高亮 | `program_languages/java_syntax.py` | `.java`、`.jav` | `java`（单文件源码，Java 11 及以上） |
| Rust 语法高亮 | `program_languages/rust_syntax.py` | `.rs` | `rustc` 编译后运行 |
| 法文翻译 | `languages/french.py` | 界面语言 *Francais* | — |

运行功能需要对应的编译器或解释器在 `PATH` 上。

## 安装

- **插件浏览器**（推荐）：在 JEditor 或 PyBreeze 打开 *插件 → Plugin Browser*，点击 *Fetch Plugins*，选好文件后点击
  *Download & Install*。文件会保存到编辑器工作目录下的 `jeditor_plugins/`，重启编辑器后生效。
- **手动**：把文件复制到 `jeditor_plugins/`，或直接把整个 repo clone 进去。没有 `__init__.py` 的文件夹
  （例如 `program_languages/`）会被递归扫描，所以整份 checkout 都会加载。

## 贡献插件

- 一个插件一个 `.py` 文件，只 import `PySide6` 与 `je_editor.plugins`，并提供 `register()`；
  `PLUGIN_NAME`、`PLUGIN_AUTHOR`、`PLUGIN_VERSION`、`PLUGIN_RUN_CONFIG` 可选。
- 编程语言插件放 `program_languages/`，界面翻译放 `languages/`。
- 插件浏览器会列出本 repo 的每一个 `.py` 文件，只跳过 `.` 开头、`LICENSE` 与 `README.md`，所以不要在这里放
  辅助脚本或测试用的 `.py` 文件。
