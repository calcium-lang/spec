#!/usr/bin/env python3

from grammar2md.grammar2md import Syntax
import re

def main():
    input = open("Syntax.grammar")
    md = Syntax.generate(input.read(), {"Identifier", "ConstantExpression", "NumberLiteral", "BlockStatement"}, "Syntax")
    input.close()
    md = re.sub(r"## ([a-zA-Z]+):", r"## [\1](Semantics.md#\1):", md)
    output = open("Syntax.md", "w")
    output.write(md)
    output.close()

if __name__ == "__main__":
    main()
