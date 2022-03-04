# Semantics
## Packages
### CompilationUnit

---

### PackageDeclaration

### ImportDeclarations

### TopLevelTypeDeclaration

---

### ImportDeclaration

### Encapsulation

### TypeDeclaration

---

### ExplicitTypeImportDeclaration

### TypeImportOnDemandDeclaration

---

### ImportNames

### FromName

## Names
### PackageName
```python
# This code snippet is part of Cesium.
#
# Copyright (C) 2022  Natan Junges <natanajunges@gmail.com>
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

### ImportName

### PackageOrTypeName

## Typedefs, Enums, Unions and Structs
### TypedefDeclaration

### EnumDeclaration

### UnionDeclaration

### StructDeclaration

---

### BaseType

### TypedefBody

### EnumBody

### UnionBody

### Extensibility

### StructLayout
```python
# This code snippet is part of Cesium.
#
# Copyright (C) 2022  Natan Junges <natanajunges@gmail.com>
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

### StructBody

---

### BodyDeclarations

### EnumConstants

### UnionTypes

---

### BodyDeclaration

### EnumConstant

### UnionType

---

### StaticInitializer

### MemberDeclaration

### VariableInitializer

---

### MemberStaticity

### FieldDeclaration

### MethodDeclaration

---

### MethodOverride

### MethodHeader

### MethodBody

---

### MethodDeclarator

---

### Parameters

---

### FixedParameters

### VariableArityParameter

---

### FixedParameter

## Types
### Type

---

### PrimitiveType

### PointerOrArraySuffix

### TypeName

### VoidPointerType

### FunctionType

---

### TypeAtomicity

### NumericType

### PointerSuffix

### ArrayDim

### TypeBareness

### FunctionPurity

### ParameterTypes

### Result

---

### IntegralType

### FloatingPointType

### ValueMutability

### ValueVolatility

### PointerWidth

### ReferenceAliasability

### ThisParameter

### FixedParameterTypes

### VariableArityParameterType

---

### FixedParameterType

## Blocks and Statements
### Block

---

### BlockStatements

## Expressions

## Array and Struct Initializers
### ArrayInitializer

### StructInitializer

---

### VariableInitializers

### FieldInitializers

---

### FieldInitializer
