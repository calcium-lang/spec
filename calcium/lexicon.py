# This file is part of the Calcium language specification
# Copyright (C) 2023  Natan Junges <natanajunges@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# pylint: disable=missing-class-docstring

import re

from alchemist.front.lexer import Terminal

WHITESPACES: re.Pattern = re.compile(r"[\t\n\v\f\r ]+")
SINGLELINE_COMMENT: re.Pattern = re.compile(r"(?://|#).*")
MULTILINE_COMMENT: re.Pattern = re.compile(r"/\*(?:[^*]|\*+[^*/])*\*+/", re.MULTILINE)


class Identifier(Terminal):
    _pattern: str | re.Pattern = re.compile(
        r"(?:[A-Z_a-z]|\\(?:u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8}))(?:[0-9A-Z_a-z]|\\(?:u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8}))*"
    )


class Keyword(Identifier):
    _pattern = ""


class Constant(Terminal):
    _pattern: str | re.Pattern = ""


class StringLiteral(Terminal):
    _pattern = re.compile(r"\"(?:[\t\v\f !#-[\]-~]|\\(?:['\"?\\abfnrtv]|[0-7]{1,3}|x[0-9A-Fa-f]+|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8}))*\"")


class StringIdentifier(StringLiteral):
    _pattern = re.compile(r"\"(?:[A-Z_a-z]|\\(?:u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8}))(?:[0-9A-Z_a-z]|\\(?:u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8}))*\"")


class Punctuator(Terminal):
    _pattern = ""


class Abstract(Keyword):
    _pattern = "abstract"


class Aliasable(Keyword):
    _pattern = "aliasable"


class As(Keyword):
    _pattern = "as"


class Atomic(Keyword):
    _pattern = "atomic"


class Bare(Keyword):
    _pattern = "bare"


class Bool(Keyword):
    _pattern = "bool"


class C(Keyword):  # pylint: disable=invalid-name
    _pattern = "C"


class Const(Keyword):
    _pattern = "const"


class Enum(Keyword):
    _pattern = "enum"


class Final(Keyword):
    _pattern = "final"


class From(Keyword):
    _pattern = "from"


class Func(Keyword):
    _pattern = "func"


class Import(Keyword):
    _pattern = "import"


class Local(Keyword):
    _pattern = "local"


class Noreturn(Keyword):
    _pattern = "noreturn"


class Override(Keyword):
    _pattern = "override"


class Package(Keyword):
    _pattern = "package"


class Packed(Keyword):
    _pattern = "packed"


class Plain(Keyword):
    _pattern = "plain"


class Private(Keyword):
    _pattern = "private"


class Protected(Keyword):
    _pattern = "protected"


class Public(Keyword):
    _pattern = "public"


class Pure(Keyword):
    _pattern = "pure"


class Restrict(Keyword):
    _pattern = "restrict"


class Sealed(Keyword):
    _pattern = "sealed"


class Stable(Keyword):
    _pattern = "stable"


class Static(Keyword):
    _pattern = "static"


class Strict(Keyword):
    _pattern = "strict"


class Struct(Keyword):
    _pattern = "struct"


class This(Keyword):
    _pattern = "this"


class Typedef(Keyword):
    _pattern = "typedef"


class Union(Keyword):
    _pattern = "union"


class Unsafe(Keyword):
    _pattern = "unsafe"


class Unused(Keyword):
    _pattern = "unused"


class Var(Keyword):
    _pattern = "var"


class Void(Keyword):
    _pattern = "void"


class Volatile(Keyword):
    _pattern = "volatile"


class Wide(Keyword):
    _pattern = "wide"


class _Byte(Keyword):
    _pattern = "_byte"


class _Char(Keyword):
    _pattern = "_char"


class _Double(Keyword):
    _pattern = "_double"


class _Float(Keyword):
    _pattern = "_float"


class _Int(Keyword):
    _pattern = "_int"


class _Long(Keyword):
    _pattern = "_long"


class _Short(Keyword):
    _pattern = "_short"


class _Ubyte(Keyword):
    _pattern = "_ubyte"


class _Uint(Keyword):
    _pattern = "_uint"


class _Ulong(Keyword):
    _pattern = "_ulong"


class _Ushort(Keyword):
    _pattern = "_ushort"


class BlockStatement(Keyword):
    _pattern = re.compile("BlockStatement")


class Expression(Keyword):
    _pattern = re.compile("Expression")


class Integer(Constant):
    _pattern = re.compile(r"(?:[1-9][0-9]*|0(?:[0-7]+|[Xx][0-9A-Fa-f]+)?)")


class LeftSquareBracket(Punctuator):
    _pattern = "["


class RightSquareBracket(Punctuator):
    _pattern = "]"


class LeftParenthesis(Punctuator):
    _pattern = "("


class RightParenthesis(Punctuator):
    _pattern = ")"


class LeftCurlyBracket(Punctuator):
    _pattern = "{"


class RightCurlyBracket(Punctuator):
    _pattern = "}"


class FullStop(Punctuator):
    _pattern = "."


class HyphenGreaterThan(Punctuator):
    _pattern = "->"


class Ampersand(Punctuator):
    _pattern = "&"


class Question(Punctuator):
    _pattern = "?"


class Colon(Punctuator):
    _pattern = ":"


class Semicolon(Punctuator):
    _pattern = ";"


class TripleFullStop(Punctuator):
    _pattern = "..."


class Equals(Punctuator):
    _pattern = "="


class Comma(Punctuator):
    _pattern = ","


class At(Punctuator):
    _pattern = "@"
