# Semantics
## Packages
### CompilationUnit

\---

### PackageDeclaration

### ImportDeclarations

### TopLevelTypeDeclaration

\---

### ImportDeclaration

### DeclarationEncapsulation

### TypeDeclaration

\---

### ImportNames

### FromName

## Names
### PackageName
```python
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

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

\---

### Version

### BaseType

### TypedefBody

### EnumLayout

### EnumBody

### UnionBody

### DeclarationExtensibility

### StructLayout
```python
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

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

\---

### BodyDeclarations

### EnumConstants

### UnionTypes

\---

### BodyDeclaration

### EnumConstant

\---

### StaticInitializer

### MemberDeclaration

### VariableInitializer

\---

### NameStrictness

### MemberStaticity

### FieldDeclaration

### MethodDeclaration

\---

### MethodOverride

### MethodHeader

### MethodBody

\---

### MethodDeclarator

\---

### Parameters

\---

### FixedParameters

### VariableArityParameter

\---

### FixedParameter

## Types
### Type

\---

### PrimitiveType

### PointerOrArraySuffix

### TypeName

### VoidPointerType

### FunctionType

### PointerNullity

\---

### TypeAtomicity

### NumericType

### PointerSuffix

### ArrayDim

### TypeStrictness

### ParameterTypes

### TypeBareness

### FunctionStrictness

### FunctionPurity

### Result

\---

### IntegralType

### FloatingPointType

### ValueMutability

### ValueVolatility

### PointerWidth

### ReferenceAliasability

### ThisParameter

### FixedParameterTypes

### VariableArityParameterType

\---

### FixedParameterType

## Blocks and Statements
### Block

\---

### BlockStatements

## Expressions

## Array and Struct Initializers
### ArrayInitializer

### StructInitializer

\---

### VariableInitializers

### FieldInitializers

\---

### FieldInitializer
