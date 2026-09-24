# IDE_Plugins

Complementos para [JEditor](https://github.com/Integration-Automation/JEDITOR) y
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). Este es el repositorio
predeterminado de su *Plugins → Plugin Browser*.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <strong>Español</strong> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

Cómo escribir un complemento (API, metadata, configuraciones de ejecución, reglas de detección):
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
la guía única para ambos editores.

## Complementos

| Complemento | Archivo | Destacados | Ejecutar con… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | compilar con `gcc` y luego ejecutar (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | compilar con `g++` y luego ejecutar (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (fuente de un solo archivo, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | compilar con `rustc` y luego ejecutar |
| French Translation | `languages/french.py` | idioma de la interfaz *Francais* | — |

Las entradas de ejecución necesitan el compilador o intérprete en el `PATH`.

## Instalación

- **Plugin Browser** (recomendado): abre *Plugins → Plugin Browser* en JEditor o PyBreeze, pulsa
  *Fetch Plugins*, elige un archivo y pulsa *Download & Install*. El archivo se guarda en
  `jeditor_plugins/` dentro del directorio de trabajo del editor; reinicia el editor para cargarlo.
- **Manualmente**: copia un archivo en `jeditor_plugins/`, o clona este repositorio dentro de él.
  Las carpetas sin `__init__.py` (como `program_languages/`) se escanean de forma recursiva, por lo
  que se carga todo el checkout.

## Contribuir con un complemento

- Un archivo `.py` por complemento, importando solo `PySide6` y `je_editor.plugins`, con una función
  `register()`; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` y `PLUGIN_RUN_CONFIG` son opcionales.
- Coloca los complementos de lenguaje en `program_languages/` y las traducciones de la interfaz en
  `languages/`.
- El Plugin Browser lista todos los archivos `.py` de este repositorio y solo omite los nombres que
  empiezan por `.`, `LICENSE` y `README.md`, así que no añadas scripts auxiliares ni pruebas como
  archivos `.py` aquí.
