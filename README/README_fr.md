# IDE_Plugins

Extensions pour [JEditor](https://github.com/Integration-Automation/JEDITOR) et
[PyBreeze](https://github.com/Integration-Automation/PyBreeze). Il s'agit du dépôt par défaut de
leur *Plugins → Plugin Browser*.

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="README_zh-TW.md">繁體中文</a> ·
  <a href="README_zh-CN.md">简体中文</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_es.md">Español</a> ·
  <strong>Français</strong> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_pt-BR.md">Português (BR)</a> ·
  <a href="README_ru.md">Русский</a>
</p>

Comment écrire une extension (API, metadata, configurations d'exécution, règles de détection) :
**[JEditor `PLUGIN_GUIDE.md`](https://github.com/Integration-Automation/JEDITOR/blob/main/PLUGIN_GUIDE.md)**,
le guide unique pour les deux éditeurs.

## Extensions

| Extension | Fichier | Points forts | Exécuter avec… |
|---|---|---|---|
| C Syntax Highlighting | `program_languages/c_syntax.py` | `.c`, `.i` | compiler avec `gcc`, puis exécuter (`.c`) |
| C++ Syntax Highlighting | `program_languages/cpp_syntax.py` | `.cpp`, `.cxx`, `.cc`, `.h`, `.hpp`, `.hxx` | compiler avec `g++`, puis exécuter (`.cpp`, `.cxx`, `.cc`) |
| Go Syntax Highlighting | `program_languages/go_syntax.py` | `.go` | `go run` |
| Java Syntax Highlighting | `program_languages/java_syntax.py` | `.java`, `.jav` | `java` (source à fichier unique, Java 11+) |
| Rust Syntax Highlighting | `program_languages/rust_syntax.py` | `.rs` | compiler avec `rustc`, puis exécuter |
| French Translation | `languages/french.py` | langue de l'interface *Francais* | — |

Les entrées d'exécution nécessitent le compilateur ou l'interpréteur dans le `PATH`.

## Installation

- **Plugin Browser** (recommandé) : ouvrez *Plugins → Plugin Browser* dans JEditor ou PyBreeze,
  appuyez sur *Fetch Plugins*, choisissez un fichier et appuyez sur *Download & Install*. Le fichier
  est enregistré dans `jeditor_plugins/` sous le répertoire de travail de l'éditeur ; redémarrez
  l'éditeur pour le charger.
- **À la main** : copiez un fichier dans `jeditor_plugins/`, ou clonez ce dépôt à l'intérieur. Les
  dossiers sans `__init__.py` (tels que `program_languages/`) sont analysés de manière récursive,
  donc tout le checkout est chargé.

## Contribuer une extension

- Un fichier `.py` par extension, n'important que `PySide6` et `je_editor.plugins`, avec une fonction
  `register()` ; `PLUGIN_NAME`, `PLUGIN_AUTHOR`, `PLUGIN_VERSION` et `PLUGIN_RUN_CONFIG` sont
  facultatifs.
- Placez les extensions de langage dans `program_languages/` et les traductions de l'interface dans
  `languages/`.
- Le Plugin Browser liste tous les fichiers `.py` de ce dépôt et n'ignore que les noms commençant par
  `.`, `LICENSE` et `README.md`, donc n'ajoutez pas de scripts utilitaires ni de tests sous forme de
  fichiers `.py` ici.
