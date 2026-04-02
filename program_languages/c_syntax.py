"""C 語法高亮插件 / C Syntax Highlighting Plugin"""
from PySide6.QtGui import QColor

from je_editor.plugins import register_programming_language

PLUGIN_NAME = "C Syntax Highlighting"
PLUGIN_AUTHOR = "JeffreyChen"
PLUGIN_VERSION = "1.0.0"

PLUGIN_RUN_CONFIG = {
    "name": "C (GCC)",
    "suffixes": (".c",),
    "compiler": "gcc",
    "args": (),
    "compile_then_run": True,
    "output_flag": "-o",
}

c_syntax_words: dict = {
    "keywords": {
        "words": (
            "auto", "break", "case", "const", "continue",
            "default", "do", "else", "enum", "extern",
            "for", "goto", "if", "inline", "register",
            "restrict", "return", "sizeof", "static", "struct",
            "switch", "typedef", "union", "volatile", "while",
            "_Alignas", "_Alignof", "_Atomic", "_Bool",
            "_Complex", "_Generic", "_Imaginary", "_Noreturn",
            "_Static_assert", "_Thread_local",
        ),
        "color": QColor(86, 156, 214),
    },
    "types": {
        "words": (
            "char", "double", "float", "int", "long",
            "short", "signed", "unsigned", "void",
            "size_t", "ssize_t", "ptrdiff_t", "intptr_t", "uintptr_t",
            "int8_t", "int16_t", "int32_t", "int64_t",
            "uint8_t", "uint16_t", "uint32_t", "uint64_t",
            "bool", "FILE", "NULL",
        ),
        "color": QColor(78, 201, 176),
    },
    "preprocessor_keywords": {
        "words": (
            "include", "define", "undef", "ifdef", "ifndef",
            "if", "elif", "else", "endif", "pragma",
            "error", "warning", "line",
        ),
        "color": QColor(155, 155, 155),
    },
    "stdlib": {
        "words": (
            "printf", "scanf", "fprintf", "fscanf", "sprintf",
            "snprintf", "malloc", "calloc", "realloc", "free",
            "memcpy", "memmove", "memset", "memcmp",
            "strlen", "strcpy", "strncpy", "strcat", "strcmp",
            "strncmp", "strstr", "strtok",
            "fopen", "fclose", "fread", "fwrite", "fgets",
            "fputs", "fseek", "ftell", "rewind",
            "exit", "abort", "atexit", "atoi", "atof", "atol",
            "abs", "rand", "srand",
        ),
        "color": QColor(220, 220, 170),
    },
}

c_syntax_rules: dict = {
    "single_line_comment": {
        "rules": (r"//[^\n]*",),
        "color": QColor(106, 153, 85),
    },
    "multi_line_comment": {
        "rules": (r"/\*.*?\*/",),
        "color": QColor(106, 153, 85),
    },
    "preprocessor_directive": {
        "rules": (r"#\s*\w+",),
        "color": QColor(155, 155, 155),
    },
    "char_literal": {
        "rules": (r"'[^'\\]*(\\.[^'\\]*)*'",),
        "color": QColor(206, 145, 120),
    },
}


def register() -> None:
    for suffix in (".c", ".i"):
        register_programming_language(
            suffix=suffix,
            syntax_words=c_syntax_words,
            syntax_rules=c_syntax_rules,
        )
