"""Go 語法高亮插件 / Go Syntax Highlighting Plugin"""
from PySide6.QtGui import QColor

from je_editor.plugins import register_programming_language

PLUGIN_NAME = "Go Syntax Highlighting"
PLUGIN_AUTHOR = "JeffreyChen"
PLUGIN_VERSION = "1.0.0"

PLUGIN_RUN_CONFIG = {
    "name": "Go",
    "suffixes": (".go",),
    "compiler": "go",
    "args": ("run",),
}

go_syntax_words: dict = {
    "keywords": {
        "words": (
            "break", "case", "chan", "const", "continue",
            "default", "defer", "else", "fallthrough", "for",
            "func", "go", "goto", "if", "import",
            "interface", "map", "package", "range", "return",
            "select", "struct", "switch", "type", "var",
        ),
        "color": QColor(86, 156, 214),
    },
    "types": {
        "words": (
            "bool", "byte", "complex64", "complex128", "error",
            "float32", "float64", "int", "int8", "int16",
            "int32", "int64", "rune", "string", "uint",
            "uint8", "uint16", "uint32", "uint64", "uintptr",
            "any", "comparable",
        ),
        "color": QColor(78, 201, 176),
    },
    "builtin": {
        "words": (
            "append", "cap", "clear", "close", "complex",
            "copy", "delete", "imag", "len", "make",
            "max", "min", "new", "panic", "print",
            "println", "real", "recover",
        ),
        "color": QColor(220, 220, 170),
    },
    "constants": {
        "words": (
            "true", "false", "nil", "iota",
        ),
        "color": QColor(181, 206, 168),
    },
}

go_syntax_rules: dict = {
    "single_line_comment": {
        "rules": (r"//[^\n]*",),
        "color": QColor(106, 153, 85),
    },
    "multi_line_comment": {
        "rules": (r"/\*.*?\*/",),
        "color": QColor(106, 153, 85),
    },
    "backtick_string": {
        "rules": (r"`[^`]*`",),
        "color": QColor(206, 145, 120),
    },
}


def register() -> None:
    register_programming_language(
        suffix=".go",
        syntax_words=go_syntax_words,
        syntax_rules=go_syntax_rules,
    )
