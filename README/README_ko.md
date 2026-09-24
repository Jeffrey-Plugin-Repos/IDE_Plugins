# IDE_Plugins

[JEditor](https://github.com/Integration-Automation/JEDITOR) 및
[PyBreeze](https://github.com/Integration-Automation/PyBreeze)용 플러그인이며, 두 편집기의 *Plugins → Plugin Browser* 기본 저장소이기도 합니다.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <strong>한국어</strong> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

플러그인 작성 방법(API, metadata, 실행 구성, 검색 규칙)은 두 편집기가 공유하는
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)** 를 참고하세요.

## 플러그인

| 플러그인 | 파일 | 지원 확장자 | 실행 |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | `gcc` 컴파일 후 실행(`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | `g++` 컴파일 후 실행(`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java`(단일 파일 소스, Java 11 이상) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | `rustc` 컴파일 후 실행 |
| French Translation | `languages/french.py` | UI 언어 *Francais* | — |

실행 항목을 사용하려면 해당 컴파일러 또는 인터프리터가 `PATH`에 있어야 합니다.

## 설치

- **Plugin Browser**(권장): JEditor 또는 PyBreeze에서 *Plugins → Plugin Browser* 를 열고 *Fetch Plugins* 를 누른 뒤,
  파일을 선택하고 *Download & Install* 을 누릅니다. 파일은 편집기 작업 디렉터리 아래
  `jeditor_plugins/` 에 저장되며, 편집기를 다시 시작하면 로드됩니다.
- **수동**: 파일을 `jeditor_plugins/` 에 복사하거나, 이 저장소를 그 안에 clone 합니다. `__init__.py` 가 없는
  폴더(예: `program_languages/`)는 재귀적으로 스캔되므로 체크아웃 전체가 로드됩니다.

## 플러그인 기여하기

- 플러그인 하나당 `.py` 파일 하나이며, `PySide6` 와 `je_editor.plugins` 만 import 하고 `register()`
  함수를 제공합니다. `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION`, `PLUGIN_RUN_CONFIG` 는 선택 사항입니다.
- 프로그래밍 언어 플러그인은 `program_languages/` 에, UI 번역은 `languages/` 에 둡니다.
- Plugin Browser 는 이 저장소의 모든 `.py` 파일을 나열하고 `.` 로 시작하는 이름, `LICENSE`, `README.md` 만
  건너뜁니다. 따라서 헬퍼 스크립트나 테스트용 `.py` 파일을 여기에 추가하지 마세요.
