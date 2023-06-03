# Calcium

A C-like type-, memory- and thread-safe systems programming language with zero-cost object-orientation.

It is heavily inspired by C, and tries to support all its features. It is also inspired by Java, and implements a subset of its object-orientation model, while trying to remove the space- and time-costs of such abstractions. Some of its syntax is inspired by Kotlin, Python, JavaScript/TypeScript and Rust.

Its name is after the chemical element Calcium(Ca), the third most abundant metal in Earth's crust and the main component of bones, the structural support of all vertebrates. It was chosen because it evokes solidity and stability, concepts that fit well with systems development.

## Design Principles

In decreasing order of importance:

1. Type-safety;
2. Memory-safety;
3. Thread-safety;
4. [Suckless philosophy](https://suckless.org/philosophy);
5. [<q>Keep it simple stupid</q>](https://en.wikipedia.org/wiki/KISS_principle);
6. [Principle of least astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment);
7. [Gang of Four Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns);
8. C interoperability;
9. Runtime space efficiency;
10. Runtime time efficiency;
11. Binary size efficiency;

## Building

To build the most recent Syntax.md file, first make sure you have [Alchemist's front-end library](https://github.com/alchemist-compiler/front) and [`cog`](https://pypi.org/project/cogapp) installed:

```shell
git clone https://github.com/alchemist-compiler/front.git alchemist-front
pip3 install cogapp
```

Once you have installed all requirements, run:

```shell
cog -I./:./alchemist-front -r Syntax.md
```

## License

<pre>
Copyright (c)  2021-2023  Natan Junges.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "<a href="LICENSE.FDL">GNU
Free Documentation License</a>".
</pre>

The lexicon and syntax files are licensed under the [GNU General Public License v3](LICENSE.GPL).

The code snippets are licensed under the [Unlicense](UNLICENSE).

## Index

1. [Packages](Semantics/Packages.md)
2. [Names](Semantics/Names.md)
3. [Typedefs, Enums, Unions and Structs](Semantics/Typedefs_Enums_Unions_and_Structs.md)
4. [Types](Semantics/Types.md)
5. [Blocks and Statements](Semantics/Blocks_and_Statements.md)
6. [Expressions](Semantics/Expressions.md)
7. [Array and Struct Initializers](Semantics/Array_and_Struct_Initializers.md)
8. [Syntax](Syntax.md)
9. [Syntax (source code)](calcium/syntax.py)
10. [Lexicon (source code)](calcium/lexicon.py)
