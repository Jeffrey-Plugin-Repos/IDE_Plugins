# IDE_Plugins

Plugins para [JEditor](https://github.com/Integration-Automation/JEDITOR) e
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). Este é o repositório padrão do
*Plugins → Plugin Browser* de ambos.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <strong>Português (BR)</strong> ·
  <a href="README_ru.md">Русский</a>
</p>

Como escrever um plugin (API, metadata, configurações de execução, regras de descoberta):
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
o guia único para os dois editores.

## Plugins

| Plugin | Arquivo | Destaques | Executar com… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | compilar com `gcc` e depois executar (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | compilar com `g++` e depois executar (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (fonte de arquivo único, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | compilar com `rustc` e depois executar |
| French Translation | `languages/french.py` | idioma da interface *Francais* | — |

As entradas de execução precisam do compilador ou interpretador no `PATH`.

## Instalação

- **Plugin Browser** (recomendado): abra *Plugins → Plugin Browser* no JEditor ou PyBreeze, pressione
  *Fetch Plugins*, escolha um arquivo e pressione *Download & Install*. O arquivo é salvo em
  `jeditor_plugins/` sob o diretório de trabalho do editor; reinicie o editor para carregá-lo.
- **Manualmente**: copie um arquivo para `jeditor_plugins/`, ou clone este repositório dentro dele.
  Pastas sem `__init__.py` (como `program_languages/`) são varridas recursivamente, então todo o
  checkout é carregado.

## Contribuir com um plugin

- Um arquivo `.py` por plugin, importando apenas `PySide6` e `je_editor.plugins`, com uma função
  `register()`; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` e `PLUGIN_RUN_CONFIG` são opcionais.
- Coloque plugins de linguagem em `program_languages/` e traduções da interface em `languages/`.
- O Plugin Browser lista todos os arquivos `.py` deste repositório e ignora apenas nomes que começam
  com `.`, `LICENSE` e `README.md`, então não adicione scripts auxiliares nem testes como arquivos
  `.py` aqui.
