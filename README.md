# Cesium
A C-like memory- and thread-safe systems programming language with near-zero-cost object-orientation.

Its name is after the chemical element Cesium(Cs).

It is heavily inspired by C, and tries to support all its features. It is also inspired by Java, and implements a subset of its object-orientation model, while trying to remove the space- and time-costs of such abstractions. Some of its syntax is inspired by Kotlin, Python, JavaScript/TypeScript and Rust.

# Building
To properly build the most recent Syntax.md file, first make sure you have the grammar2md submodule:

```shell
git submodule update --init
```

You need to run this command every time the repository is updated. Once you have the most recent grammar2md submodule, run the build script:

```shell
./build.py
```

# License
<pre>
Copyright (c)  2021  Natan Junges.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "<a href="LICENSE">GNU
Free Documentation License</a>".
</pre>

The code snippets and the build script are licensed under the [GNU GPLv3](LICENSE).
