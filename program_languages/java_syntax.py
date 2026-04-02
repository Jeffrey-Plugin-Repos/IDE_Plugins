"""Java 語法高亮插件 / Java Syntax Highlighting Plugin"""
from PySide6.QtGui import QColor

from je_editor.plugins import register_programming_language

PLUGIN_NAME = "Java Syntax Highlighting"
PLUGIN_AUTHOR = "JeffreyChen"
PLUGIN_VERSION = "1.0.0"

PLUGIN_RUN_CONFIG = {
    "name": "Java",
    "suffixes": (".java",),
    "compiler": "java",
    "args": (),
}

java_syntax_words: dict = {
    "keywords": {
        "words": (
            "abstract", "assert", "break", "case", "catch",
            "class", "const", "continue", "default", "do",
            "else", "enum", "extends", "final", "finally",
            "for", "goto", "if", "implements", "import",
            "instanceof", "interface", "native", "new", "package",
            "private", "protected", "public", "return", "static",
            "strictfp", "super", "switch", "synchronized", "this",
            "throw", "throws", "transient", "try", "volatile",
            "while", "yield", "record", "sealed", "non-sealed",
            "permits", "var", "when",
        ),
        "color": QColor(86, 156, 214),
    },
    "types": {
        "words": (
            "boolean", "byte", "char", "double", "float",
            "int", "long", "short", "void",
            "String", "Integer", "Long", "Double", "Float",
            "Boolean", "Character", "Byte", "Short", "Object",
            "List", "Map", "Set", "ArrayList", "HashMap",
            "HashSet", "LinkedList", "TreeMap", "TreeSet",
            "Optional", "Stream", "Collection", "Iterator",
            "Comparable", "Runnable", "Callable", "Future",
            "Exception", "RuntimeException", "Throwable", "Error",
        ),
        "color": QColor(78, 201, 176),
    },
    "constants": {
        "words": (
            "true", "false", "null",
        ),
        "color": QColor(181, 206, 168),
    },
    "annotations": {
        "words": (
            "Override", "Deprecated", "SuppressWarnings",
            "FunctionalInterface", "SafeVarargs",
        ),
        "color": QColor(220, 220, 170),
    },
}

java_syntax_rules: dict = {
    "single_line_comment": {
        "rules": (r"//[^\n]*",),
        "color": QColor(106, 153, 85),
    },
    "multi_line_comment": {
        "rules": (r"/\*.*?\*/",),
        "color": QColor(106, 153, 85),
    },
    "annotation": {
        "rules": (r"@\w+",),
        "color": QColor(220, 220, 170),
    },
}


def register() -> None:
    for suffix in (".java", ".jav"):
        register_programming_language(
            suffix=suffix,
            syntax_words=java_syntax_words,
            syntax_rules=java_syntax_rules,
        )
