| [<Names](./Names.md) | [Index](../README.md#Index) | [Types>](./Types.md) |
|----------------------|-----------------------------|----------------------|

# Typedefs, Enums, Unions and Structs

## TypedefDeclaration

## EnumDeclaration

## UnionDeclaration

## StructDeclaration

\---

## Version

## BaseType

## TypedefBody

## EnumLayout

## EnumBody

## UnionBody

## DeclarationExtensibility

## StructSeal

## StructLayout

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

## StructBody

\---

## BodyDeclarations

## EnumConstants

## UnionTypes

## TypeNames

\---

## BodyDeclaration

## EnumConstant

\---

## StaticInitializer

## MemberDeclaration

## VariableInitializer

\---

## SymbolNaming

## MemberStaticity

## FieldDeclaration

## MethodDeclaration

\---

## MethodOverride

## MethodHeader

## MethodBody

\---

## MethodDeclarator

\---

## Parameters

\---

## FixedParameters

## VariableArityParameter

\---

## FixedParameter

| [<Names](./Names.md) | [Index](../README.md#Index) | [Types>](./Types.md) |
|----------------------|-----------------------------|----------------------|
