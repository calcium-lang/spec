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
This is the start symbol of the grammar. It is equivalent to an entire source file. It always has a single top level type declaration/definition, inside of which all other declarations/definitions are put. This type always belongs to a package, that may or may not be named. The required types from external sources are imported through import declarations, although the top level types from the same package are always imported automatically.

---

## PackageDeclaration
This declaration names the package the declared top level type belongs to. When ommited, the package is left unnamed. There can be only one unnamed package per project. As it does not have a name, its types cannot be imported by other packages.

## ImportDeclarations

## TopLevelTypeDeclaration
This declaration defines the top level type of the compilation unit. Its name must be the same as the source file's (minus the extension). The type has an encapsulation level that will determine its visibility outside the compilation unit.

---

## PackageName

## ImportDeclaration
This declaration imports the types required for the proper function of the declared top level type and its eventual internal types. When a type is imported, it becomes available to the entire compilation unit, being referenced by its simple name (or an alias for it). The types can be explicitly imported, or imported on demand.

## TopLevelEncapsulation

## TypeDeclaration

---

## ExplicitImport

## ImportOnDemand

## TypedefDeclaration

## EnumDeclaration

## UnionDeclaration

## StructDeclaration

---

## ImportNames

## PackageOrTypeName

## Type

## EnumBody

## UnionLayout

## UnionBody

## StructExtensibility

## StructLayout

## StructBody

---

## ImportName

## PrimitiveType

## PointerOrArraySuffix

## TypeName

## VoidPointer

## FunctionType

## EnumConstants

## EnumBodyDeclarations

## UnionTypes

## UnionBodyDeclarations

## StructBodyDeclarations

---

## NumericType

## TypeAtomicity

## PointerSuffix

## Dim

## ParameterTypes

## Result

## EnumConstant

## UnionType

## StructBodyDeclaration

---

## IntegralType

## FloatingPointType

## ValueMutability

## ValueVolatility

## ReferenceAliasability

## PointerSize

## FixedParameterTypes

## VariableArityParameterType

## Block

## NestedEncapsulation

## StructMemberDeclaration

---

## FixedParameterType

## BlockStatements

## MemberStaticity

## FieldDeclaration

## MethodDeclaration

---

## FieldMutability

## MethodExtensibility

## MethodOverride

## MethodHeader

## MethodBody

---

## Parameters

---

## ThisParameter

## FixedParameters

## VariableArityParameter

---

## FixedParameter
