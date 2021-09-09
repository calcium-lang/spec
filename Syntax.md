<pre>
Cesium, a C-like memory- and thread-safe systems programming language with near-zero-cost object-orientation.
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
<a id="PackageDeclaration">PackageDeclaration</a>:
    <b>package</b> <i><a href="#PackageName">PackageName</a></i> <b>;</b>
</pre>

<pre>
<a id="ImportDeclaration">ImportDeclaration</a>:
    <b>import</b> <i><a href="#ImportList">ImportList</a></i> <i>[</i><b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i><i>]</i> <b>;</b>
    <b>import</b> <b>*</b> <b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i> <b>;</b>
</pre>

<pre>
<a id="TypeDeclaration">TypeDeclaration</a>:
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i> <b>;</b>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a id="PackageName">PackageName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="ImportList">ImportList</a>:
    <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i> <i>{</i><b>,</b> <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i><i>}</i>
</pre>

<pre>
<a id="PackageOrTypeName">PackageOrTypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="TypeAccessibility">TypeAccessibility</a>:
    <b>public</b>
</pre>

<pre>
<a id="TypedefDeclaration">TypedefDeclaration</a>:
    <b>typedef</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="EnumDeclaration">EnumDeclaration</a>:
    <b>enum</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <b>{</b> <i><a href="#EnumConstants">EnumConstants</a></i> <i>[</i><i><a href="#EnumMembers">EnumMembers</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="UnionDeclaration">UnionDeclaration</a>:
    <b>union</b> <i>Identifier</i> <b>{</b> <i><a href="#UnionTypes">UnionTypes</a></i> <i>[</i><i><a href="#UnionMembers">UnionMembers</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="StructDeclaration">StructDeclaration</a>:
    <i>[</i><i><a href="#StructOpenness">StructOpenness</a></i><i>]</i> <i>[</i><i><a href="#StructLayout">StructLayout</a></i><i>]</i> <b>struct</b> <i>Identifier</i> <i>[</i><b>:</b> <i><a href="#Type">Type</a></i><i>]</i> <b>{</b> <i>[</i><i><a href="#StructMembers">StructMembers</a></i><i>]</i> <b>}</b>
</pre>

---

<pre>
<a id="Type">Type</a>:
    <i><a href="#PrimitiveType">PrimitiveType</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#TypeName">TypeName</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#VoidPointer">VoidPointer</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#FunctionType">FunctionType</a></i>
    <b>(</b> <i><a href="#FunctionType">FunctionType</a></i> <b>)</b> <i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i>
</pre>

<pre>
<a id="EnumConstants">EnumConstants</a>:
    <i><a href="#EnumConstant">EnumConstant</a></i> <i>{</i><b>,</b> <i><a href="#EnumConstant">EnumConstant</a></i><i>}</i>
</pre>

<pre>
<a id="EnumMembers">EnumMembers</a>:
    <b>;</b> <i><a href="#StructMembers">StructMembers</a></i>
</pre>

<pre>
<a id="UnionTypes">UnionTypes</a>:
    <i><a href="#UnionType">UnionType</a></i> <i>{</i><b>,</b> <i><a href="#UnionType">UnionType</a></i><i>}</i>
</pre>

<pre>
<a id="UnionMembers">UnionMembers</a>:
    <b>;</b> <i><a href="#StructMembers">StructMembers</a></i>
</pre>

<pre>
<a id="StructOpenness">StructOpenness</a>:
    <b>open</b>
</pre>

<pre>
<a id="StructLayout">StructLayout</a>:
    <i>(one of)</i>
    <b>packed</b> <b>ordered</b>
</pre>

<pre>
<a id="StructMembers">StructMembers</a>:
    <i><a href="#StructMember">StructMember</a></i> <i>{</i><i><a href="#StructMember">StructMember</a></i><i>}</i>
</pre>

---

<pre>
<a id="PrimitiveType">PrimitiveType</a>:
    <i><a href="#NumericType">NumericType</a></i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>_bool</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>_char</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="PointerOrArraySuffix">PointerOrArraySuffix</a>:
    <i><a href="#PointerSuffix">PointerSuffix</a></i> <i>[</i><i>PointerOrArraySuffix</i><i>]</i>
    <i><a href="#Dim">Dim</a></i> <i>[</i><i>PointerOrArraySuffix</i><i>]</i>
</pre>

<pre>
<a id="TypeName">TypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="VoidPointer">VoidPointer</a>:
    <b>unsafe</b> <b>void</b> <b>&</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="FunctionType">FunctionType</a>:
    <b>(</b> <i>[</i><i><a href="#ArgumentTypes">ArgumentTypes</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Return">Return</a></i>
</pre>

<pre>
<a id="EnumConstant">EnumConstant</a>:
    <i>Identifier</i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i>
</pre>

<pre>
<a id="UnionType">UnionType</a>:
    <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i>
    <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

<pre>
<a id="StructMember">StructMember</a>:
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#FieldDeclaration">FieldDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#MethodDeclaration">MethodDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i> <b>;</b>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a id="NumericType">NumericType</a>:
    <i><a href="#IntegralType">IntegralType</a></i>
    <i><a href="#FloatingPointType">FloatingPointType</a></i>
</pre>

<pre>
<a id="TypeAtomicity">TypeAtomicity</a>:
    <b>atomic</b>
</pre>

<pre>
<a id="PointerSuffix">PointerSuffix</a>:
    <i>[</i><i><a href="#ValueMutability">ValueMutability</a></i><i>]</i> <i>[</i><i><a href="#ValueVolatility">ValueVolatility</a></i><i>]</i> <b>&</b> <i>[</i><i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="Dim">Dim</a>:
    <b>[</b> <i>[</i><i>ConstantExpression</i><i>]</i> <b>]</b>
</pre>

<pre>
<a id="ArgumentTypes">ArgumentTypes</a>:
    <i><a href="#FixedArgumentTypes">FixedArgumentTypes</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i><i>]</i>
    <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i>
</pre>

<pre>
<a id="Return">Return</a>:
    <b>noreturn</b>
    <b>void</b>
    <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="MemberAccessibility">MemberAccessibility</a>:
    <i>(one of)</i>
    <b>public</b> <b>protected</b> <b>private</b>
</pre>

<pre>
<a id="FieldDeclaration">FieldDeclaration</a>:
    <i>[</i><i><a href="#MemberStaticity">MemberStaticity</a></i><i>]</i> <i><a href="#FieldMutability">FieldMutability</a></i> <i>[</i><i><a href="#ValueVolatility">ValueVolatility</a></i><i>]</i> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i> <b>;</b>
</pre>

<pre>
<a id="MethodDeclaration">MethodDeclaration</a>:
    <i>[</i><i><a href="#MemberStaticity">MemberStaticity</a></i><i>]</i> <i>[</i><i><a href="#MethodOpenness">MethodOpenness</a></i><i>]</i> <i>[</i><i><a href="#MethodOverride">MethodOverride</a></i><i>]</i> <b>func</b> <i>Identifier</i> <b>(</b> <i>[</i><i><a href="#Arguments">Arguments</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Return">Return</a></i> <i><a href="#Block">Block</a></i>
</pre>

---

<pre>
<a id="IntegralType">IntegralType</a>:
    <i>(one of)</i>
    <b>_ubyte</b> <b>_byte</b> <b>_ushort</b> <b>_short</b> <b>_uint</b> <b>_int</b> <b>_ulong</b> <b>_long</b>
</pre>

<pre>
<a id="FloatingPointType">FloatingPointType</a>:
    <i>(one of)</i>
    <b>_float</b> <b>_double</b>
</pre>

<pre>
<a id="ValueMutability">ValueMutability</a>:
    <b>mut</b>
</pre>

<pre>
<a id="ValueVolatility">ValueVolatility</a>:
    <b>volatile</b>
</pre>

<pre>
<a id="ReferenceAliasability">ReferenceAliasability</a>:
    <b>aliased</b>
</pre>

<pre>
<a id="FixedArgumentTypes">FixedArgumentTypes</a>:
    <i><a href="#FixedArgumentType">FixedArgumentType</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgumentType">FixedArgumentType</a></i><i>}</i>
</pre>

<pre>
<a id="VariadicArgumentType">VariadicArgumentType</a>:
    <b>...</b> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="MemberStaticity">MemberStaticity</a>:
    <b>static</b>
</pre>

<pre>
<a id="FieldMutability">FieldMutability</a>:
    <i>(one of)</i>
    <b>mut</b> <b>const</b>
</pre>

<pre>
<a id="MethodOpenness">MethodOpenness</a>:
    <b>open</b>
</pre>

<pre>
<a id="MethodOverride">MethodOverride</a>:
    <b>override</b>
</pre>

<pre>
<a id="Arguments">Arguments</a>:
    <i><a href="#ThisArgument">ThisArgument</a></i> <i>[</i><b>,</b> <i><a href="#FixedArguments">FixedArguments</a></i><i>]</i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#FixedArguments">FixedArguments</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#VariadicArgument">VariadicArgument</a></i>
</pre>

<pre>
<a id="Block">Block</a>:
    <b>{</b> <i>{</i><i>Statement</i><i>}</i> <b>}</b>
</pre>

---

<pre>
<a id="FixedArgumentType">FixedArgumentType</a>:
    <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="ThisArgument">ThisArgument</a>:
    <b>this</b> <i>[</i><b>:</b> <i><a href="#ValueMutability">ValueMutability</a></i> <i>[</i><b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i><i>]</i>
    <b>this</b> <b>:</b> <b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i>
</pre>

<pre>
<a id="FixedArguments">FixedArguments</a>:
    <i><a href="#FixedArgument">FixedArgument</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgument">FixedArgument</a></i><i>}</i>
</pre>

<pre>
<a id="VariadicArgument">VariadicArgument</a>:
    <b>...</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

---

<pre>
<a id="FixedArgument">FixedArgument</a>:
    <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>
