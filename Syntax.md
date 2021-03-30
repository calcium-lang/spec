<pre>
Caesium, a C-like memory- and thread-safe systems programming language with zero-cost object-orientation.
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

# Syntax

<pre>
CompilationUnit:
    <i>[</i><i><a href="#PackageDeclaration">PackageDeclaration</a></i><i>]</i> <i>{</i><i><a href="#ImportDeclaration">ImportDeclaration</a></i><i>}</i> <i><a href="#TypeDeclaration">TypeDeclaration</a></i>
</pre>

---

<pre>
<a name="PackageDeclaration">PackageDeclaration</a>:
    <b>package</b> <i><a href="#PackageName">PackageName</a></i> <b>;</b>
</pre>

<pre>
<a name="ImportDeclaration">ImportDeclaration</a>:
    <b>import</b> <i><a href="#ImportList">ImportList</a></i> <i>[</i><b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i><i>]</i> <b>;</b>
    <b>import</b> <b>*</b> <b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i> <b>;</b>
</pre>

<pre>
<a name="TypeDeclaration">TypeDeclaration</a>:
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#AliasDeclaration">AliasDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a name="PackageName">PackageName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a name="ImportList">ImportList</a>:
    <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i>
    <i>ImportList</i> <b>,</b> <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i>
</pre>

<pre>
<a name="PackageOrTypeName">PackageOrTypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a name="TypeAccessibility">TypeAccessibility</a>:
    <b>public</b>
</pre>

<pre>
<a name="AliasDeclaration">AliasDeclaration</a>:
    <b>alias</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <b>;</b>
</pre>

<pre>
<a name="EnumDeclaration">EnumDeclaration</a>:
    <b>enum</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <b>{</b> <i><a href="#EnumConstants">EnumConstants</a></i> <i>[</i><i><a href="#EnumElements">EnumElements</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a name="UnionDeclaration">UnionDeclaration</a>:
    <b>union</b> <i>Identifier</i> <b>{</b> <i><a href="#UnionTypes">UnionTypes</a></i> <i>[</i><i><a href="#UnionElements">UnionElements</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a name="StructDeclaration">StructDeclaration</a>:
    <i>[</i><i><a href="#StructOpenness">StructOpenness</a></i><i>]</i> <i>[</i><i><a href="#StructLayout">StructLayout</a></i><i>]</i> <b>struct</b> <i>Identifier</i> <i>[</i><b>:</b> <i><a href="#Type">Type</a></i><i>]</i> <b>{</b> <i>[</i><i><a href="#StructElements">StructElements</a></i><i>]</i> <b>}</b>
</pre>

---

<pre>
<a name="Type">Type</a>:
    <i><a href="#PrimitiveType">PrimitiveType</a></i>
    <i><a href="#CompoundType">CompoundType</a></i>
    <i><a href="#ReferenceType">ReferenceType</a></i>
</pre>

<pre>
<a name="EnumConstants">EnumConstants</a>:
    <i><a href="#EnumConstant">EnumConstant</a></i> <i>{</i><b>,</b> <i><a href="#EnumConstant">EnumConstant</a></i><i>}</i>
</pre>

<pre>
<a name="EnumElements">EnumElements</a>:
    <b>;</b> <i><a href="#StructElements">StructElements</a></i>
</pre>

<pre>
<a name="UnionTypes">UnionTypes</a>:
    <i><a href="#UnionType">UnionType</a></i> <i>{</i><b>,</b> <i><a href="#UnionType">UnionType</a></i><i>}</i>
</pre>

<pre>
<a name="UnionElements">UnionElements</a>:
    <b>;</b> <i><a href="#StructElements">StructElements</a></i>
</pre>

<pre>
<a name="StructOpenness">StructOpenness</a>:
    <b>open</b>
</pre>

<pre>
<a name="StructLayout">StructLayout</a>:
    <i>(one of)</i>
    <b>packed</b> <b>ordered</b>
</pre>

<pre>
<a name="StructElements">StructElements</a>:
    <i><a href="#StructElement">StructElement</a></i> <i>{</i><i><a href="#StructElement">StructElement</a></i><i>}</i>
</pre>

---

<pre>
<a name="PrimitiveType">PrimitiveType</a>:
    <i><a href="#NumericType">NumericType</a></i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>_bool</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a name="CompoundType">CompoundType</a>:
    <i><a href="#TypeName">TypeName</a></i>
    <i><a href="#ArrayType">ArrayType</a></i>
</pre>

<pre>
<a name="ReferenceType">ReferenceType</a>:
    <b>unsafe</b> <b>void</b> <b>&</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <i><a href="#Type">Type</a></i> <i>[</i><i><a href="#TypeConstancy">TypeConstancy</a></i><i>]</i> <i>[</i><i><a href="#TypeVolatility">TypeVolatility</a></i><i>]</i> <i>[</i><i><a href="#ValueInitialization">ValueInitialization</a></i><i>]</i> <b>&</b> <i>[</i><i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <i><a href="#FunctionType">FunctionType</a></i>
</pre>

<pre>
<a name="EnumConstant">EnumConstant</a>:
    <i>Identifier</i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i>
</pre>

<pre>
<a name="UnionType">UnionType</a>:
    <i><a href="#AliasDeclaration">AliasDeclaration</a></i>
    <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

<pre>
<a name="StructElement">StructElement</a>:
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#FieldDeclaration">FieldDeclaration</a></i>
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#MethodDeclaration">MethodDeclaration</a></i>
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#AliasDeclaration">AliasDeclaration</a></i>
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#ElementAccessibility">ElementAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a name="NumericType">NumericType</a>:
    <i><a href="#IntegralType">IntegralType</a></i>
    <i><a href="#FloatingPointType">FloatingPointType</a></i>
</pre>

<pre>
<a name="TypeAtomicity">TypeAtomicity</a>:
    <b>atomic</b>
</pre>

<pre>
<a name="TypeName">TypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a name="ArrayType">ArrayType</a>:
    <i><a href="#PrimitiveType">PrimitiveType</a></i> <i><a href="#Dims">Dims</a></i>
    <i><a href="#TypeName">TypeName</a></i> <i><a href="#Dims">Dims</a></i>
    <i><a href="#ReferenceType">ReferenceType</a></i> <i><a href="#Dims">Dims</a></i>
</pre>

<pre>
<a name="TypeConstancy">TypeConstancy</a>:
    <b>const</b>
</pre>

<pre>
<a name="TypeVolatility">TypeVolatility</a>:
    <b>volatile</b>
</pre>

<pre>
<a name="ValueInitialization">ValueInitialization</a>:
    <b>init</b>
</pre>

<pre>
<a name="ReferenceAliasability">ReferenceAliasability</a>:
    <b>aliased</b>
</pre>

<pre>
<a name="FunctionType">FunctionType</a>:
    <b>(</b> <i>[</i><i><a href="#ArgumentTypes">ArgumentTypes</a></i><i>]</i> <b>)</b> <b>-></b> <i><a href="#Return">Return</a></i>
</pre>

<pre>
<a name="ElementAccessibility">ElementAccessibility</a>:
    <i>(one of)</i>
    <b>public</b> <b>protected</b> <b>private</b>
</pre>

<pre>
<a name="FieldDeclaration">FieldDeclaration</a>:
    <i>[</i><i><a href="#ElementStaticity">ElementStaticity</a></i><i>]</i> <i><a href="#FieldConstancy">FieldConstancy</a></i> <i>[</i><i><a href="#FieldVolatility">FieldVolatility</a></i><i>]</i> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i> <b>;</b>
</pre>

<pre>
<a name="MethodDeclaration">MethodDeclaration</a>:
    <i>[</i><i><a href="#ElementStaticity">ElementStaticity</a></i><i>]</i> <b>func</b> <i>Identifier</i> <b>(</b> <i>[</i><i><a href="#Arguments">Arguments</a></i><i>]</i> <b>)</b> <b>-></b> <i><a href="#Return">Return</a></i> <i><a href="#Block">Block</a></i>
</pre>

---

<pre>
<a name="IntegralType">IntegralType</a>:
    <i>(one of)</i>
    <b>_ubyte</b> <b>_byte</b> <b>_ushort</b> <b>_short</b> <b>_uint</b> <b>_int</b> <b>_ulong</b> <b>_long</b>
</pre>

<pre>
<a name="FloatingPointType">FloatingPointType</a>:
    <i>(one of)</i>
    <b>_float</b> <b>_double</b>
</pre>

<pre>
<a name="Dims">Dims</a>:
    <b>[</b> <i>[</i><i>ConstantExpression</i><i>]</i> <b>]</b> <i>{</i><b>[</b> <i>ConstantExpression</i> <b>]</b><i>}</i>
</pre>

<pre>
<a name="ArgumentTypes">ArgumentTypes</a>:
    <i><a href="#ThisArgument">ThisArgument</a></i> <i>[</i><b>,</b> <i><a href="#FixedArgumentTypes">FixedArgumentTypes</a></i><i>]</i> <i>[</i><b>,</b> <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i><i>]</i>
    <i><a href="#FixedArgumentTypes">FixedArgumentTypes</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i><i>]</i>
    <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i>
</pre>

<pre>
<a name="Return">Return</a>:
    <b>noreturn</b>
    <b>void</b>
    <i><a href="#PrimitiveType">PrimitiveType</a></i>
    <i><a href="#TypeName">TypeName</a></i>
    <i><a href="#FunctionType">FunctionType</a></i>
    <b>(</b> <b>noreturn</b> <b>)</b>
    <b>(</b> <b>void</b> <b>)</b>
    <b>(</b> <i><a href="#Type">Type</a></i> <b>)</b>
</pre>

<pre>
<a name="ElementStaticity">ElementStaticity</a>:
    <b>static</b>
</pre>

<pre>
<a name="FieldConstancy">FieldConstancy</a>:
    <i>(one of)</i>
    <b>var</b> <b>const</b>
</pre>

<pre>
<a name="FieldVolatility">FieldVolatility</a>:
    <b>volatile</b>
</pre>

<pre>
<a name="Arguments">Arguments</a>:
    <i><a href="#ThisArgument">ThisArgument</a></i> <i>[</i><b>,</b> <i><a href="#FixedArguments">FixedArguments</a></i><i>]</i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#FixedArguments">FixedArguments</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#VariadicArgument">VariadicArgument</a></i>
</pre>

<pre>
<a name="Block">Block</a>:
    <b>{</b> <i>{</i><i>Statement</i><i>}</i> <b>}</b>
</pre>

---

<pre>
<a name="ThisArgument">ThisArgument</a>:
    <b>this</b> <b>:</b> <i><a href="#TypeConstancy">TypeConstancy</a></i> <i>[</i><i><a href="#ValueInitialization">ValueInitialization</a></i><i>]</i> <i>[</i><b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i>
    <b>this</b> <b>:</b> <i><a href="#ValueInitialization">ValueInitialization</a></i> <i>[</i><b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i>
    <b>this</b> <b>:</b> <b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i>
</pre>

<pre>
<a name="FixedArgumentTypes">FixedArgumentTypes</a>:
    <i><a href="#FixedArgumentType">FixedArgumentType</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgumentType">FixedArgumentType</a></i><i>}</i>
</pre>

<pre>
<a name="VariadicArgumentType">VariadicArgumentType</a>:
    <b>...</b> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a name="FixedArguments">FixedArguments</a>:
    <i><a href="#FixedArgument">FixedArgument</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgument">FixedArgument</a></i><i>}</i>
</pre>

<pre>
<a name="VariadicArgument">VariadicArgument</a>:
    <b>...</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

---

<pre>
<a name="FixedArgumentType">FixedArgumentType</a>:
    <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a name="FixedArgument">FixedArgument</a>:
    <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>
