#!/usr/bin/env python3

# This script is part of Cesium.
#
# Copyright (C) 2022  Natan Junges <natanajunges@gmail.com>
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this script.  If not, see <https://www.gnu.org/licenses/>.

from grammar2md.alchemist.grammar2md import Syntax
from typing import TextIO

def main() -> None:
    input: TextIO = open("Syntax.grammar")
    md: str = Syntax.generate(input.read(), {"Identifier", "Expression", "NumberLiteral", "StringIdentifier", "BlockStatement"}, "Semantics.md")
    input.close()
    output: TextIO = open("Syntax.md", "w")
    output.write(md)
    output.close()

if __name__ == "__main__":
    main()
