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
This declaration names the package the declared top level type belongs to. When ommited, the package is left unnamed. There can be only one unnamed package per project, and as it does not have a name, its types cannot be imported by other packages.

## ImportDeclarations
This is a list of all the import declarations required for the proper function of the declared top level type and its eventual internal types. Those declarations are not separated by any symbol, as each import declaration already ends with a semicolon.

## TopLevelTypeDeclaration
This declaration defines the top level type of the compilation unit. Its name must be the same as the source file's (minus the extension). The type has an encapsulation level that will determine its visibility outside the compilation unit.

---

## PackageName
This is a dot-separated sequence of identifiers that compose the name of the top level type's package. In the file system, this name is translated into a hierarchy of folders, where the source files of the package are stored. This translation is done following this procedure, written in Python for convenience:

```python
import os
import errno

def PackageNameToPath(cwd: str, name: list[str]) -> str:
    path: str = cwd
    start: int = 0
    end: int = len(name)

    while start < len(name):
        folder: str = ".".join(name[start:end])

        if os.path.isdir(path + "/" + folder):
            path += "/" + folder
            start = end
            end = len(name)
        else:
            end -= 1

            if end <= start:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path + "/" + folder)

    return path
```

As each package is located inside a folder, which can itself contain folders, it is possible for a package to have subpackages, that have its name as a prefix to their own name. These subpackages are completely independent from the base package though, not having any special privileges or visibility.

## ImportDeclaration
This declaration imports the types required for the proper function of the declared top level type and its eventual internal types. Only the types that are visible to the compilation unit can be imported. When a type is imported, it becomes available to the entire compilation unit, being referenced by its simple name (or an alias for it). The types can be explicitly imported, or imported on demand.

## TopLevelEncapsulation
This modifier determines the top level type's visibility outside the compilation unit. When present, it will be visible to all other compilation units, inside and outside its package. When ommited, it will only be visible to the compilation units inside its package.

## TypeDeclaration
This declaration defines a type, along with its members and subtypes. It always has an encapsulation level, that will determine its visibility outside its scope, that can be another type or the compilation unit.

---

## ExplicitImport

## ImportOnDemand

## TypedefDeclaration

## EnumDeclaration

## UnionDeclaration

## StructDeclaration

## InterfaceDeclaration

---

## ImportNames

## PackageOrTypeName

## Type

## EnumBody

## UnionLayout

## UnionBody

## StructExtensibility

## StructLayout

## TypeNames

## StructBody

## InterfaceBody

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

## InterfaceBodyDeclarations

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

## InterfaceBodyDeclaration

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

## InterfaceNestedEncapsulation

## InterfaceMemberDeclaration

---

## FixedParameterType

## BlockStatements

## MemberStaticity

## FieldDeclaration

## MethodDeclaration

## InterfaceMethodDeclaration

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
