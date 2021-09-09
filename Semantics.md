<pre>
Cesium, a C-like memory- and thread-safe systems programming language with near-zero-cost object-orientation.
Copyright (C) 2021  Natan Junges

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see &lt;<a href="https://www.gnu.org/licenses/">https://www.gnu.org/licenses/</a>&gt;.
</pre>

# Semantics
## CompilationUnit
This is the start symbol of the grammar. It is equivalent to an entire source file. It always has a single type declaration/definition, inside of which all other declarations/definitions are put. This type always belongs to a package, that may or may not be named. The required types from external sources are imported through import declarations, although the types from the same package are always imported automatically.

---

## PackageDeclaration
This declaration names the package the declared type belongs to. When ommited, the package is left unnamed. There can be only one unnamed package per project. As it does not have a name, its types cannot be imported by other packages.

## ImportDeclaration

## TypeDeclaration

---

## PackageName

## ImportList

## PackageOrTypeName

## TypeAccessibility

## TypedefDeclaration

## EnumDeclaration

## UnionDeclaration

## StructDeclaration

---

## Type

## EnumConstants

## EnumMembers

## UnionTypes

## UnionMembers

## StructOpenness

## StructLayout

## StructMembers

---

## PrimitiveType

## PointerOrArraySuffix

## TypeName

## VoidPointer

## FunctionType

## EnumConstant

## UnionType

## StructMember

---

## NumericType

## TypeAtomicity

## PointerSuffix

## Dim

## ArgumentTypes

## Return

## MemberAccessibility

## FieldDeclaration

## MethodDeclaration

---

## IntegralType

## FloatingPointType

## ValueMutability

## ValueVolatility

## ReferenceAliasability

## FixedArgumentTypes

## VariadicArgumentType

## MemberStaticity

## FieldMutability

## MethodOpenness

## MethodOverride

## MethodDeclarator

---

## FixedArgumentType

## Arguments

## Block

---

## ThisArgument

## FixedArguments

## VariadicArgument

---

## FixedArgument
