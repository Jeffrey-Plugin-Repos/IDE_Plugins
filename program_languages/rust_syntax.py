"""Rust 語法高亮插件 / Rust Syntax Highlighting Plugin"""
from PySide6.QtGui import QColor

from je_editor.plugins import register_programming_language

PLUGIN_NAME = "Rust Syntax Highlighting"
PLUGIN_AUTHOR = "JeffreyChen"
PLUGIN_VERSION = "1.0.0"

PLUGIN_RUN_CONFIG = {
    "name": "Rust (rustc)",
    "suffixes": (".rs",),
    "compiler": "rustc",
    "args": (),
    "compile_then_run": True,
    "output_flag": "-o",
}

rust_syntax_words: dict = {
    "keywords": {
        "words": (
            "as", "async", "await", "break", "const",
            "continue", "crate", "dyn", "else", "enum",
            "extern", "fn", "for", "if", "impl",
            "in", "let", "loop", "match", "mod",
            "move", "mut", "pub", "ref", "return",
            "self", "Self", "static", "struct", "super",
            "trait", "type", "unsafe", "use", "where",
            "while", "yield",
        ),
        "color": QColor(86, 156, 214),
    },
    "types": {
        "words": (
            "bool", "char", "f32", "f64",
            "i8", "i16", "i32", "i64", "i128", "isize",
            "u8", "u16", "u32", "u64", "u128", "usize",
            "str", "String", "Vec", "Box", "Rc", "Arc",
            "Option", "Result", "Ok", "Err", "Some", "None",
            "HashMap", "HashSet", "BTreeMap", "BTreeSet",
            "VecDeque", "LinkedList", "BinaryHeap",
            "Cell", "RefCell", "Mutex", "RwLock",
            "Pin", "Future", "Poll", "Waker",
            "Iterator", "IntoIterator", "FromIterator",
            "Display", "Debug", "Clone", "Copy",
            "Send", "Sync", "Sized", "Drop",
            "Fn", "FnMut", "FnOnce",
            "From", "Into", "TryFrom", "TryInto",
            "AsRef", "AsMut", "Deref", "DerefMut",
        ),
        "color": QColor(78, 201, 176),
    },
    "constants": {
        "words": (
            "true", "false",
        ),
        "color": QColor(181, 206, 168),
    },
    "macros": {
        "words": (
            "println", "print", "eprintln", "eprint",
            "format", "write", "writeln",
            "vec", "todo", "unimplemented", "unreachable",
            "panic", "assert", "assert_eq", "assert_ne",
            "debug_assert", "debug_assert_eq", "debug_assert_ne",
            "cfg", "env", "file", "line", "column",
            "include", "include_str", "include_bytes",
            "concat", "stringify", "module_path",
        ),
        "color": QColor(220, 220, 170),
    },
}

rust_syntax_rules: dict = {
    "single_line_comment": {
        "rules": (r"//[^\n]*",),
        "color": QColor(106, 153, 85),
    },
    "multi_line_comment": {
        "rules": (r"/\*.*?\*/",),
        "color": QColor(106, 153, 85),
    },
    "attribute": {
        "rules": (r"#!?\[[\w:(),\s=\"']*\]",),
        "color": QColor(155, 155, 155),
    },
    "lifetime": {
        "rules": (r"'\w+",),
        "color": QColor(86, 156, 214),
    },
    "macro_invocation": {
        "rules": (r"\w+!",),
        "color": QColor(220, 220, 170),
    },
}


def register() -> None:
    register_programming_language(
        suffix=".rs",
        syntax_words=rust_syntax_words,
        syntax_rules=rust_syntax_rules,
    )
