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

from alchemist.front.parser.generator import Switch, repeat, oneof, ProductionTemplate

# pylint: disable=line-too-long, missing-class-docstring
# mypy: disable-error-code="assignment, arg-type"


class low(Switch):  # pylint: disable=invalid-name
    enabled = True

# Packages


class CompilationUnit(ProductionTemplate):
    _template = ["PackageDeclaration"], ["ImportDeclarations"], "TopLevelTypeDeclaration"

###


class PackageDeclaration(ProductionTemplate):
    _template = "Package", "PackageName", ["Semicolon"]


class ImportDeclarations(ProductionTemplate):
    _template = "ImportDeclaration", repeat("ImportDeclaration")


class TopLevelTypeDeclaration(ProductionTemplate):
    _template = ["DeclarationEncapsulation"], "TypeDeclaration"

###


class ImportDeclaration(ProductionTemplate):
    _template = "Import", "ImportNames", ["FromName"], ["Semicolon"]


class DeclarationEncapsulation(ProductionTemplate):
    _template = oneof("Public", "Protected", "Private")


class TypeDeclaration(ProductionTemplate):
    _template = oneof("TypedefDeclaration", "EnumDeclaration", "UnionDeclaration", "StructDeclaration")

###


class ImportNames(ProductionTemplate):
    _template = "ImportName", repeat("Comma", "ImportName")


class FromName(ProductionTemplate):
    _template = "From", "PackageOrTypeName"

# Names


class PackageName(ProductionTemplate):
    _template = "Identifier", repeat("FullStop", "Identifier"), low(["Version"])


class ImportName(ProductionTemplate):
    _template = "Identifier", low(["Version"]), ["As", "Identifier"]


class PackageOrTypeName(ProductionTemplate):
    _template = "Identifier", low(["Version"]), repeat("FullStop", "Identifier", low(["Version"]))

# Typedefs, Enums, Unions and Structs


class TypedefDeclaration(ProductionTemplate):
    _template = "Typedef", "Identifier", low(["Version"]), "BaseType", ["TypedefBody"]


class EnumDeclaration(ProductionTemplate):
    _template = low(["EnumLayout"]), "Enum", "Identifier", low(["Version"]), ["BaseType"], "EnumBody"


class UnionDeclaration(ProductionTemplate):
    _template = "Union", "Identifier", low(["Version"]), "UnionBody"


class StructDeclaration(ProductionTemplate):
    _template = ["DeclarationExtensibility"], ["StructSeal"], low(["StructLayout"]), "Struct", "Identifier", low(["Version"]), ["BaseType"], "StructBody"  # noqa: E501

###


class Version(ProductionTemplate):
    _template = "At", "Integer", "FullStop", "Integer"


class BaseType(ProductionTemplate):
    _template = "Colon", "Type"


class TypedefBody(ProductionTemplate):
    _template = oneof(
        ("LeftCurlyBracket", "BodyDeclarations", "RightCurlyBracket"),
        "Semicolon"
    )


class EnumLayout(ProductionTemplate):
    _template = oneof(
        "Strict",
        ("Unsafe", "C")
    )


class EnumBody(ProductionTemplate):
    _template = "LeftCurlyBracket", "EnumConstants", ["Semicolon", "BodyDeclarations"], "RightCurlyBracket"


class UnionBody(ProductionTemplate):
    _template = "LeftCurlyBracket", "UnionTypes", ["Semicolon", "BodyDeclarations"], "RightCurlyBracket"


class DeclarationExtensibility(ProductionTemplate):
    _template = oneof("Final", "Abstract")


class StructSeal(ProductionTemplate):
    _template = "Sealed", ["LeftParenthesis", "TypeNames", "RightParenthesis"]


class StructLayout(ProductionTemplate):
    _template = oneof("Strict", "C", "Packed")


class StructBody(ProductionTemplate):
    _template = "LeftCurlyBracket", ["BodyDeclarations"], "RightCurlyBracket"

###


class BodyDeclarations(ProductionTemplate):
    _template = "BodyDeclaration", repeat("BodyDeclaration")


class EnumConstants(ProductionTemplate):
    _template = "EnumConstant", repeat("Comma", "EnumConstant")


class UnionTypes(ProductionTemplate):
    _template = "TypeDeclaration", repeat("Comma", "TypeDeclaration")

# The semicolon in TypedefBody must never be found in TypedefDeclaration.


class TypeNames(ProductionTemplate):
    _template = "TypeName", repeat("Comma", "TypeName")

###


class BodyDeclaration(ProductionTemplate):
    _template = oneof(
        "StaticInitializer",
        (["DeclarationEncapsulation"], oneof("MemberDeclaration", "TypeDeclaration"))
    )

# TypedefBody must always be found in TypedefDeclaration.


class EnumConstant(ProductionTemplate):
    _template = ["FullStop"], "Identifier", [oneof("Equals", "Colon"), "VariableInitializer"]

###


class StaticInitializer(ProductionTemplate):
    _template = low(["SymbolNaming"]), "Static", low(["Version"], ["StringIdentifier"]), "Block"


class MemberDeclaration(ProductionTemplate):
    _template = ["MemberStaticity"], oneof("FieldDeclaration", "MethodDeclaration")


class VariableInitializer(ProductionTemplate):
    _template = oneof("Expression", "ArrayInitializer", "StructInitializer")

###


class SymbolNaming(ProductionTemplate):
    _template = oneof("Strict", "Plain")


class MemberStaticity(ProductionTemplate):
    _template = "Static"


class FieldDeclaration(ProductionTemplate):
    _template = "ValueMutability", low(["ValueVolatility"], ["SymbolNaming"]), "Identifier", low(["StringIdentifier"]), "Colon", "Type", ["Equals", "VariableInitializer"], "Semicolon"  # noqa: E501


class MethodDeclaration(ProductionTemplate):
    _template = ["DeclarationExtensibility"], ["MethodOverride"], low(["FunctionStrictness"]), ["FunctionPurity"], "Func", "MethodHeader", "MethodBody"  # noqa: E501

###


class MethodOverride(ProductionTemplate):
    _template = "Override"


class MethodHeader(ProductionTemplate):
    _template = "MethodDeclarator", ["HyphenGreaterThan", "Result"]


class MethodBody(ProductionTemplate):
    _template = oneof("Block", "Semicolon")

###


class MethodDeclarator(ProductionTemplate):
    _template = low(["SymbolNaming"]), "Identifier", low(["Version"], ["StringIdentifier"]), ["Colon", "TypeName"], "LeftParenthesis", ["Parameters"], "RightParenthesis"  # noqa: E501

###


class Parameters(ProductionTemplate):
    _template = oneof(
        ("ThisParameter", ["Comma", "FixedParameters"], ["Comma", "VariableArityParameter"]),
        ("FixedParameters", ["Comma", "VariableArityParameter"]),
        "VariableArityParameter"
    )

###


class FixedParameters(ProductionTemplate):
    _template = "FixedParameter", repeat("Comma", "FixedParameter")


class VariableArityParameter(ProductionTemplate):
    _template = "TripleFullStop", low(["VariableArityParameterLayout"]), "Identifier", ["Colon", "Type"]

###


class FixedParameter(ProductionTemplate):
    _template = "Identifier", ["Colon", "Type"]

# Types


class Type(ProductionTemplate):
    _template = oneof(
        (oneof("PrimitiveType", "TypeName", low("VoidPointerType")), ["PointerOrArraySuffix"]),
        "FunctionType",
        ("LeftParenthesis", "FunctionType", "RightParenthesis", oneof("PointerNullity", "PointerOrArraySuffix"))
    )

###


class PrimitiveType(ProductionTemplate):
    _template = low(["TypeAtomicity"]), oneof("NumericType", "Bool", "_Char")


class PointerOrArraySuffix(ProductionTemplate):
    _template = oneof("PointerSuffix", "ArrayDim"), ["PointerOrArraySuffix"]


class TypeName(ProductionTemplate):
    _template = low([oneof("TypeStrictness", "TypeBareness")]), "Identifier", low(["Version"]), repeat("FullStop", "Identifier", low(["Version"])), ["LeftParenthesis", ["ParameterTypes"], "RightParenthesis"]  # noqa: E501


class VoidPointerType(ProductionTemplate):
    _template = "Unsafe", "Void", ["ValueMutability"], ["ValueVolatility"], "Ampersand", ["TypeAtomicity"], ["ReferenceAliasability"], ["PointerNullity"]  # noqa: E501


class FunctionType(ProductionTemplate):
    _template = low(["TypeAtomicity"], ["FunctionStrictness"]), ["FunctionPurity"], "Func", "LeftParenthesis", ["ParameterTypes"], "RightParenthesis", "HyphenGreaterThan", "Result"  # noqa: E501


class PointerNullity(ProductionTemplate):
    _template = ["Local"], "Question"

###


class TypeAtomicity(ProductionTemplate):
    _template = "Atomic"


class NumericType(ProductionTemplate):
    _template = oneof("IntegralType", "FloatingPointType")


class PointerSuffix(ProductionTemplate):
    _template = ["ValueMutability"], low(["ValueVolatility"]), "Ampersand", low([oneof("PointerWidth", "TypeAtomicity")], ["ReferenceAliasability"]), ["PointerNullity"]  # noqa: E501


class ArrayDim(ProductionTemplate):
    _template = "LeftSquareBracket", oneof((low(["TypeStrictness"]), ["Expression"]), low("TypeBareness")), "RightSquareBracket", ["PointerNullity"]


class TypeStrictness(ProductionTemplate):
    _template = "Strict"


class ParameterTypes(ProductionTemplate):
    _template = oneof(
        ("ThisParameter", ["Comma", "FixedParameterTypes"], ["Comma", "VariableArityParameterType"]),
        ("FixedParameterTypes", ["Comma", "VariableArityParameterType"]),
        "VariableArityParameterType"
    )


class TypeBareness(ProductionTemplate):
    _template = "Unsafe", "Bare"


class FunctionStrictness(ProductionTemplate):
    _template = "Strict"


class FunctionPurity(ProductionTemplate):
    _template = ["Local"], oneof("Const", "Pure")


class Result(ProductionTemplate):
    _template = oneof("Noreturn", "Void", "Type")

###


class IntegralType(ProductionTemplate):
    _template = oneof(
        low(oneof(
            "_Ubyte",
            "_Byte",
            "_Ushort",
            "_Short",
            "_Uint"
        )),
        "_Int",
        low(oneof(
            "_Ulong",
            "_Long"
        ))
    )


class FloatingPointType(ProductionTemplate):
    _template = oneof(
        "_Float",
        low("_Double")
    )


class ValueMutability(ProductionTemplate):
    _template = oneof(
        (["Unsafe"], "Var"),
        (["Local"], "Const")
    )


class ValueVolatility(ProductionTemplate):
    _template = oneof(
        (["Local"], "Volatile"),
        (["Unsafe"], "Stable")
    )


class PointerWidth(ProductionTemplate):
    _template = oneof(
        ([["Unsafe"], "Unused"], ["TypeStrictness"], "Wide"),
        "TypeBareness"
    )


class ReferenceAliasability(ProductionTemplate):
    _template = oneof(
        (["Local"], "Aliasable"),
        (["Unsafe"], "Restrict")
    )


class ThisParameter(ProductionTemplate):
    _template = oneof(
        ("This", ["Colon", "TypeName", ["ValueMutability"], low(["ValueVolatility"]), ["Ampersand", low(["PointerWidth"], ["ReferenceAliasability"])]]),  # noqa: E501
        ("This", "Colon", "ValueMutability", low(["ValueVolatility"]), ["Ampersand", low(["PointerWidth"], ["ReferenceAliasability"])]),
        low("This", "Colon", "ValueVolatility", ["Ampersand", ["PointerWidth"], ["ReferenceAliasability"]]),
        ("This", "Colon", "Ampersand", low(["PointerWidth"], ["ReferenceAliasability"]))
    )


class FixedParameterTypes(ProductionTemplate):
    _template = "FixedParameterType", repeat("Comma", "FixedParameterType")


class VariableArityParameterType(ProductionTemplate):
    _template = "TripleFullStop", low(["VariableArityParameterLayout"]), "Colon", "Type"

###


class FixedParameterType(ProductionTemplate):
    _template = "Colon", "Type"


class VariableArityParameterLayout(ProductionTemplate):
    _template = oneof(
        "Strict",
        ("Unsafe", "C")
    )

# Blocks and Statements


class Block(ProductionTemplate):
    _template = "LeftCurlyBracket", ["BlockStatements"], "RightCurlyBracket"

###


class BlockStatements(ProductionTemplate):
    _template = "BlockStatement", repeat("BlockStatement")

# Expressions

# Array and Struct Initializers


class ArrayInitializer(ProductionTemplate):
    _template = "LeftSquareBracket", ["VariableInitializers"], "RightSquareBracket", ["Colon", "Type"]


class StructInitializer(ProductionTemplate):
    _template = "LeftCurlyBracket", ["FieldInitializers"], "RightCurlyBracket", ["Colon", "TypeName"]

###


class VariableInitializers(ProductionTemplate):
    _template = "VariableInitializer", repeat("Comma", "VariableInitializer")


class FieldInitializers(ProductionTemplate):
    _template = "FieldInitializer", repeat("Comma", "FieldInitializer")

###


class FieldInitializer(ProductionTemplate):
    _template = ["FullStop"], "Identifier", oneof("Equals", "Colon"), "VariableInitializer"
