# IDE_Plugins

[JEditor](https://github.com/Integration-Automation/JEDITOR) と
[PyBreeze](https://github.com/Integration-Automation/PyBreeze) のプラグイン。両者の *Plugins → Plugin Browser* のデフォルトリポジトリでもあります。

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <strong>日本語</strong> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

プラグインの書き方（API、metadata、実行設定、検出ルール）は、両エディタ共通の
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)** を参照してください。

## プラグイン

| プラグイン | ファイル | 対応拡張子 | 実行 |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`、`.i` | `gcc` でコンパイル後に実行（`.c`） |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`、`.cxx`、`.cc`、`.h`、`.hpp`、`.hxx` | `g++` でコンパイル後に実行（`.cpp`、`.cxx`、`.cc`） |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`、`.jav` | `java`（単一ファイルソース、Java 11 以上） |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | `rustc` でコンパイル後に実行 |
| French Translation | `languages/french.py` | UI 言語 *Francais* | — |

実行機能には、対応するコンパイラまたはインタープリタが `PATH` 上にある必要があります。

## インストール

- **Plugin Browser**（推奨）：JEditor または PyBreeze で *Plugins → Plugin Browser* を開き、*Fetch Plugins* を押して
  ファイルを選び、*Download & Install* を押します。ファイルはエディタの作業ディレクトリ下の
  `jeditor_plugins/` に保存され、エディタを再起動すると読み込まれます。
- **手動**：ファイルを `jeditor_plugins/` にコピーするか、このリポジトリをその中に clone します。`__init__.py` のない
  フォルダ（`program_languages/` など）は再帰的にスキャンされるため、チェックアウト全体が読み込まれます。

## プラグインの投稿

- プラグイン 1 つにつき `.py` ファイル 1 つ。`PySide6` と `je_editor.plugins` のみを import し、`register()`
  関数を持たせます。`PLUGIN_NAME`、`PLUGIN_AUTHOR`、`PLUGIN_VERSION`、`PLUGIN_RUN_CONFIG` は任意です。
- プログラミング言語プラグインは `program_languages/` に、UI 翻訳は `languages/` に置きます。
- Plugin Browser はこのリポジトリのすべての `.py` ファイルを一覧し、`.` で始まる名前・`LICENSE`・`README.md` のみを
  スキップします。そのため、ヘルパースクリプトやテスト用の `.py` ファイルをここに追加しないでください。
