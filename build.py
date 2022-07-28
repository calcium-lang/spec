#!/usr/bin/env python3

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

from grammar2md.alchemist.grammar2md import Syntax

def main():
    with open("Syntax.grammar") as input:
        md = Syntax.generate(input.read(), 3, {"Identifier", "Expression", "StringIdentifier", "BlockStatement", "IntegerLiteral"}, "Semantics.md")

    with open("Syntax.md", "w") as output:
        output.write(md)

if __name__ == "__main__":
    main()
