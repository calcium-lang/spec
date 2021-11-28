# Semantics
## CompilationUnit
This is the start symbol of the grammar. It is equivalent to an entire source file. It always has a single top level type declaration/definition, inside of which all other declarations/definitions are put. This type always belongs to a package, that may or may not be named. The required types from external sources are imported through import declarations, although the top level types from the same package are always imported automatically.

---

## PackageDeclaration
This declaration names the package the declared top level type belongs to. When ommited, the package is left unnamed. There can be only one unnamed package per project, and as it does not have a name, its types cannot be imported by other packages.

## ImportDeclarations
This is a list of all the import declarations required for the proper function of the declared top level type and its eventual internal types. Those declarations are not separated by any symbol.

## TopLevelTypeDeclaration
This declaration defines the top level type of the compilation unit. Its name must be the same as the source file's (minus the extension). The type has an encapsulation level that will determine its visibility outside the compilation unit.

---

## PackageName
This is a dot-separated sequence of identifiers that compose the name of the top level type's package. In the file system, this name is translated into a hierarchy of folders, where the source files of the package are stored. This translation is done following this procedure, written in Python for convenience:

```python
# This code snippet is part of Cesium.
#
# Copyright (C) 2021  Natan Junges <natanajunges@gmail.com>
#
# This code snippet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code snippet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this code snippet.  If not, see <https://www.gnu.org/licenses/>.

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
This import allows the programmer to explicitly list all the types it needs to import from a specific source (be it a package or a type inside a package). Each imported type may be aliased to avoid name conflict. If the source is ommited, it is assumed to be the current package, making it possible to explicitly import its types for clarity.

## ImportOnDemand
This import allows the programmer to import needed types from a specific source (a package or a type inside a package) without having to list each one of them. None of the imported types can be aliased, which might lead to name conflicts. The source is never ommited.

## TypedefDeclaration
This declaration defines an alias for a base type. They cannot be used interchangeably, but explicit casts are required. Casts in both directions are allowed, but casting between two aliases of the same base type is not. As the defined alias is also a type, it can itself be aliased, behaving like any other type. To enforce encapsulation, the type alias cannot have a weaker encapsulation than that of the base type.

## EnumDeclaration
This declaration defines an enumeration type. It is composed of constants, whose type is the enumeration's base type. It is implicitly casted to the base type when required, but casting the base type to the enumeration type is not allowed. To enforce encapsulation, the enumeration type cannot have a weaker encapsulation than that of the base type. Each constant must be different from all the other ones (of the same enumeration type), both in name and value. As this type is constant, only the methods from the base type that do not change its value can be invoked.

If the base type's size is lesser than or equal to the simple pointer size in the target architecture, the enumeration value is the constant value. If it is greater than the pointer size, the enumeration value is a pointer to the actual constant, stored in a static location. It is done like so to ensure the enumeration value is never longer than a pointer, making comparison trivial and atomic. It is also very space efficient. But this difference in value must be mostly transparent to the programmer. The exception is when an enumeration of the second kind is referenced by a pointer and the pointer is casted to the base type, in which case the pointer value will be the address of the actual constant.

When the base type is also an enumeration type, the derived enumeration aliases the base's constants, keeping the same memory layout and being even able to have fewer (never more) constants.

## UnionDeclaration

## StructDeclaration

## InterfaceDeclaration
This declaration defines an interface type, which is an abstract type, since an object of such type is impossible, and only a pointer to this type can be used. This pointer must always be fat, storing the address of the actual object and its interface's implementation object. The only non-static members this type has are methods, and everything else is (implicitly) static. It supports multiple inheritance, and can only inherit from other interface types. Its implementation object is composed of pointers to its parents' implementation objects and pointers to its (non-static and non-private) methods' implementations. This object is only defined by the structs that implement this interface type.

---

## ImportNames
This is a comma-separated list of all the types it needs to import from a specific source.

## PackageOrTypeName
This is a dot-separated sequence of identifiers that compose the name of the import source, that can be either a package or a type inside a package (top-level or nested).

## BaseType

## EnumBody
This is the enum's body, where its constants are defined, along with optional extra declarations.

## UnionLayout

## UnionRawness
This modifier determines whether (when ommited) or not (when present) the union's memory layout will have a suffix, which indicates the type of the current value. The suffix will be of the smallest unsigned integer type that can hold the number of types the union has minus one, and the types will be identified by their order of declaration (zero-indexed and increasing). As a reinterpret cast is possible when there is no such suffix, this modifier is considered unsafe.

## UnionBody
This is the union's body, where its types are defined, along with optional extra declarations.

## StructExtensibility
This modifier determines whether (when present) or not (when ommited) the struct can be extended. When "open" is present, extending is allowed. When "abstract" is present, extending is mandatory for the struct to be useful, as an object of an incomplete type cannot exist (although a pointer to one can). When a base struct is extended it becomes the prefix of the derived struct, and its original field layout cannot be changed.

## StructLayout
This modifier determines how the struct's  own fields (not derived from a base struct) will be laid out in memory. When present, the fields will be laid out after the base struct's prefix (if any), in the order they were declared, with no padding to properly align them. When ommited, the fields will be sorted by size, from the largest to the smallest, making sure they are all properly aligned with little to no padding needed. Their positioning is done following this procedure, written in Python for convenience:

```python
# This code snippet is part of Cesium.
#
# Copyright (C) 2021  Natan Junges <natanajunges@gmail.com>
#
# This code snippet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code snippet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this code snippet.  If not, see <https://www.gnu.org/licenses/>.

from typing import Optional

def FieldsToMemory(fields: list[tuple[str, int]], base: Optional[list[tuple[Optional[str], int]]] = None) -> list[tuple[Optional[str], int]]:
    memory: list[tuple[Optional[str], int]] = base.copy() if base != None else []
    ord_fields: list[tuple[str, int]] = sorted(fields, key = lambda field: -field[1])
    base_size: int = 0
    i: int = 0

    while i < len(memory):
        if memory[i][0] == None:
            j: int = 0

            while j < len(ord_fields):
                if base_size % ord_fields[j][1] == 0:
                    if ord_fields[j][1] < memory[i][1]:
                        memory = memory[:i] + [ord_fields[j], (None, memory[i][1] - ord_fields[j][1])] + memory[i + 1:]
                        ord_fields = ord_fields[:j] + ord_fields[j + 1:]
                        break
                    elif ord_fields[j][1] == memory[i][1]:
                        memory = memory[:i] + [ord_fields[j]] + memory[i + 1:]
                        ord_fields = ord_fields[:j] + ord_fields[j + 1:]
                        break

                j += 1

            if memory[i][0] == None:
                base_size += memory[i][1]
                i += 1
        else:
            base_size += memory[i][1]
            i += 1

    if base_size % ord_fields[0][1] != 0:
        memory.append((None, ord_fields[0][1] - base_size % ord_fields[0][1]))

        while i < len(memory):
            if memory[i][0] == None:
                j: int = 1

                while j < len(ord_fields):
                    if base_size % ord_fields[j][1] == 0:
                        if ord_fields[j][1] < memory[-1][1]:
                            memory = memory[:-1] + [ord_fields[j], (None, memory[-1][1] - ord_fields[j][1])]
                            ord_fields = ord_fields[:j] + ord_fields[j + 1:]
                            break
                        elif ord_fields[j][1] == memory[-1][1]:
                            memory = memory[:-1] + [ord_fields[j]]
                            ord_fields = ord_fields[:j] + ord_fields[j + 1:]
                            break

                    j += 1

                if memory[i][0] == None:
                    break
            else:
                base_size += memory[i][1]
                i += 1

    memory += ord_fields

    return memory
```

## BaseTypes

## StructBody

## BaseInterfaces

## InterfaceBody

---

## ImportName

## Type

## EnumConstants

## BodyDeclarations

## UnionTypes

## TypeNames

## StructBodyDeclarations

## InterfaceBodyDeclarations

---

## PrimitiveType

## PointerOrArraySuffix

## TypeName

## VoidPointer

## FunctionType

## EnumConstant

## BodyDeclaration

## UnionType

## StructBodyDeclaration

## InterfaceBodyDeclaration

---

## NumericType

## TypeAtomicity

## PointerSuffix

## ArrayDim

## ValueMutability

## ValueVolatility

## ParameterTypes

## Result

## Block

## NestedEncapsulation

## MemberDeclaration

## StructNestedEncapsulation

## StructMemberDeclaration

## InterfaceNestedEncapsulation

## InterfaceMemberDeclaration

---

## IntegralType

## FloatingPointType

## ReferenceAliasability

## PointerSize

## ArrayLayout

## ArrayRawness

## FixedParameterTypes

## VariableArityParameterType

## BlockStatements

## FieldDeclaration

## MethodDeclaration

## StaticInitializer

## MemberStaticity

## ConstructorDeclaration

---

## FixedParameterType

## FieldMutability

## MethodExtensibility

## MethodOverride

## MethodHeader

## MethodBody

## ConstructorHeader

---

## Parameters

---

## ThisParameter

## FixedParameters

## VariableArityParameter

---

## FixedParameter
