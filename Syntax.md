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
<a href="Semantics.md#CompilationUnit">CompilationUnit</a>:
    <i>[</i><i><a href="#PackageDeclaration">PackageDeclaration</a></i><i>]</i> <i>{</i><i><a href="#ImportDeclaration">ImportDeclaration</a></i><i>}</i> <i><a href="#TypeDeclaration">TypeDeclaration</a></i>
</pre>

---

<pre>
<a id="PackageDeclaration" href="Semantics.md#PackageDeclaration">PackageDeclaration</a>:
    <b>package</b> <i><a href="#PackageName">PackageName</a></i> <b>;</b>
</pre>

<pre>
<a id="ImportDeclaration" href="Semantics.md#ImportDeclaration">ImportDeclaration</a>:
    <b>import</b> <i><a href="#ImportList">ImportList</a></i> <i>[</i><b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i><i>]</i> <b>;</b>
    <b>import</b> <b>*</b> <b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i> <b>;</b>
</pre>

<pre>
<a id="TypeDeclaration" href="Semantics.md#TypeDeclaration">TypeDeclaration</a>:
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i> <b>;</b>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#TypeAccessibility">TypeAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a id="PackageName" href="Semantics.md#PackageName">PackageName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="ImportList" href="Semantics.md#ImportList">ImportList</a>:
    <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i> <i>{</i><b>,</b> <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i><i>}</i>
</pre>

<pre>
<a id="PackageOrTypeName" href="Semantics.md#PackageOrTypeName">PackageOrTypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="TypeAccessibility" href="Semantics.md#TypeAccessibility">TypeAccessibility</a>:
    <b>public</b>
</pre>

<pre>
<a id="TypedefDeclaration" href="Semantics.md#TypedefDeclaration">TypedefDeclaration</a>:
    <b>typedef</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="EnumDeclaration" href="Semantics.md#EnumDeclaration">EnumDeclaration</a>:
    <b>enum</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <b>{</b> <i><a href="#EnumConstants">EnumConstants</a></i> <i>[</i><i><a href="#EnumMembers">EnumMembers</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="UnionDeclaration" href="Semantics.md#UnionDeclaration">UnionDeclaration</a>:
    <b>union</b> <i>Identifier</i> <b>{</b> <i><a href="#UnionTypes">UnionTypes</a></i> <i>[</i><i><a href="#UnionMembers">UnionMembers</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="StructDeclaration" href="Semantics.md#StructDeclaration">StructDeclaration</a>:
    <i>[</i><i><a href="#StructOpenness">StructOpenness</a></i><i>]</i> <i>[</i><i><a href="#StructLayout">StructLayout</a></i><i>]</i> <b>struct</b> <i>Identifier</i> <i>[</i><b>:</b> <i><a href="#Type">Type</a></i><i>]</i> <b>{</b> <i>[</i><i><a href="#StructMembers">StructMembers</a></i><i>]</i> <b>}</b>
</pre>

---

<pre>
<a id="Type" href="Semantics.md#Type">Type</a>:
    <i><a href="#PrimitiveType">PrimitiveType</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#TypeName">TypeName</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#VoidPointer">VoidPointer</a></i> <i>[</i><i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i><i>]</i>
    <i><a href="#FunctionType">FunctionType</a></i>
    <b>(</b> <i><a href="#FunctionType">FunctionType</a></i> <b>)</b> <i><a href="#PointerOrArraySuffix">PointerOrArraySuffix</a></i>
</pre>

<pre>
<a id="EnumConstants" href="Semantics.md#EnumConstants">EnumConstants</a>:
    <i><a href="#EnumConstant">EnumConstant</a></i> <i>{</i><b>,</b> <i><a href="#EnumConstant">EnumConstant</a></i><i>}</i>
</pre>

<pre>
<a id="EnumMembers" href="Semantics.md#EnumMembers">EnumMembers</a>:
    <b>;</b> <i><a href="#StructMembers">StructMembers</a></i>
</pre>

<pre>
<a id="UnionTypes" href="Semantics.md#UnionTypes">UnionTypes</a>:
    <i><a href="#UnionType">UnionType</a></i> <i>{</i><b>,</b> <i><a href="#UnionType">UnionType</a></i><i>}</i>
</pre>

<pre>
<a id="UnionMembers" href="Semantics.md#UnionMembers">UnionMembers</a>:
    <b>;</b> <i><a href="#StructMembers">StructMembers</a></i>
</pre>

<pre>
<a id="StructOpenness" href="Semantics.md#StructOpenness">StructOpenness</a>:
    <i>(one of)</i>
    <b>open</b> <b>abstract</b>
</pre>

<pre>
<a id="StructLayout" href="Semantics.md#StructLayout">StructLayout</a>:
    <i>(one of)</i>
    <b>packed</b> <b>ordered</b>
</pre>

<pre>
<a id="StructMembers" href="Semantics.md#StructMembers">StructMembers</a>:
    <i><a href="#StructMember">StructMember</a></i> <i>{</i><i><a href="#StructMember">StructMember</a></i><i>}</i>
</pre>

---

<pre>
<a id="PrimitiveType" href="Semantics.md#PrimitiveType">PrimitiveType</a>:
    <i><a href="#NumericType">NumericType</a></i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>_bool</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>_char</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="PointerOrArraySuffix" href="Semantics.md#PointerOrArraySuffix">PointerOrArraySuffix</a>:
    <i><a href="#PointerSuffix">PointerSuffix</a></i> <i>[</i><i>PointerOrArraySuffix</i><i>]</i>
    <i><a href="#Dim">Dim</a></i> <i>[</i><i>PointerOrArraySuffix</i><i>]</i>
</pre>

<pre>
<a id="TypeName" href="Semantics.md#TypeName">TypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="VoidPointer" href="Semantics.md#VoidPointer">VoidPointer</a>:
    <b>unsafe</b> <b>void</b> <b>&</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="FunctionType" href="Semantics.md#FunctionType">FunctionType</a>:
    <b>(</b> <i>[</i><i><a href="#ArgumentTypes">ArgumentTypes</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Return">Return</a></i>
</pre>

<pre>
<a id="EnumConstant" href="Semantics.md#EnumConstant">EnumConstant</a>:
    <i>Identifier</i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i>
</pre>

<pre>
<a id="UnionType" href="Semantics.md#UnionType">UnionType</a>:
    <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i>
    <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

<pre>
<a id="StructMember" href="Semantics.md#StructMember">StructMember</a>:
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#FieldDeclaration">FieldDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#MethodDeclaration">MethodDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i> <b>;</b>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i>[</i><i><a href="#MemberAccessibility">MemberAccessibility</a></i><i>]</i> <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a id="NumericType" href="Semantics.md#NumericType">NumericType</a>:
    <i><a href="#IntegralType">IntegralType</a></i>
    <i><a href="#FloatingPointType">FloatingPointType</a></i>
</pre>

<pre>
<a id="TypeAtomicity" href="Semantics.md#TypeAtomicity">TypeAtomicity</a>:
    <b>atomic</b>
</pre>

<pre>
<a id="PointerSuffix" href="Semantics.md#PointerSuffix">PointerSuffix</a>:
    <i>[</i><i><a href="#ValueMutability">ValueMutability</a></i><i>]</i> <i>[</i><i><a href="#ValueVolatility">ValueVolatility</a></i><i>]</i> <b>&</b> <i>[</i><i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
</pre>

<pre>
<a id="Dim" href="Semantics.md#Dim">Dim</a>:
    <b>[</b> <i>[</i><i>ConstantExpression</i><i>]</i> <b>]</b>
</pre>

<pre>
<a id="ArgumentTypes" href="Semantics.md#ArgumentTypes">ArgumentTypes</a>:
    <i><a href="#FixedArgumentTypes">FixedArgumentTypes</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i><i>]</i>
    <i><a href="#VariadicArgumentType">VariadicArgumentType</a></i>
</pre>

<pre>
<a id="Return" href="Semantics.md#Return">Return</a>:
    <b>noreturn</b>
    <b>void</b>
    <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="MemberAccessibility" href="Semantics.md#MemberAccessibility">MemberAccessibility</a>:
    <i>(one of)</i>
    <b>public</b> <b>protected</b> <b>private</b>
</pre>

<pre>
<a id="FieldDeclaration" href="Semantics.md#FieldDeclaration">FieldDeclaration</a>:
    <i>[</i><i><a href="#MemberStaticity">MemberStaticity</a></i><i>]</i> <i><a href="#FieldMutability">FieldMutability</a></i> <i>[</i><i><a href="#ValueVolatility">ValueVolatility</a></i><i>]</i> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i> <b>;</b>
</pre>

<pre>
<a id="MethodDeclaration" href="Semantics.md#MethodDeclaration">MethodDeclaration</a>:
    <i>[</i><i><a href="#MethodOpenness">MethodOpenness</a></i><i>]</i> <i>[</i><i><a href="#MethodOverride">MethodOverride</a></i><i>]</i> <b>func</b> <i><a href="#MethodDeclarator">MethodDeclarator</a></i>
    <i><a href="#MemberStaticity">MemberStaticity</a></i> <b>func</b> <i><a href="#MethodDeclarator">MethodDeclarator</a></i>
</pre>

---

<pre>
<a id="IntegralType" href="Semantics.md#IntegralType">IntegralType</a>:
    <i>(one of)</i>
    <b>_ubyte</b> <b>_byte</b> <b>_ushort</b> <b>_short</b> <b>_uint</b> <b>_int</b> <b>_ulong</b> <b>_long</b>
</pre>

<pre>
<a id="FloatingPointType" href="Semantics.md#FloatingPointType">FloatingPointType</a>:
    <i>(one of)</i>
    <b>_float</b> <b>_double</b>
</pre>

<pre>
<a id="ValueMutability" href="Semantics.md#ValueMutability">ValueMutability</a>:
    <b>mut</b>
</pre>

<pre>
<a id="ValueVolatility" href="Semantics.md#ValueVolatility">ValueVolatility</a>:
    <b>volatile</b>
</pre>

<pre>
<a id="ReferenceAliasability" href="Semantics.md#ReferenceAliasability">ReferenceAliasability</a>:
    <b>aliased</b>
</pre>

<pre>
<a id="FixedArgumentTypes" href="Semantics.md#FixedArgumentTypes">FixedArgumentTypes</a>:
    <i><a href="#FixedArgumentType">FixedArgumentType</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgumentType">FixedArgumentType</a></i><i>}</i>
</pre>

<pre>
<a id="VariadicArgumentType" href="Semantics.md#VariadicArgumentType">VariadicArgumentType</a>:
    <b>...</b> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="MemberStaticity" href="Semantics.md#MemberStaticity">MemberStaticity</a>:
    <b>static</b>
</pre>

<pre>
<a id="FieldMutability" href="Semantics.md#FieldMutability">FieldMutability</a>:
    <i>(one of)</i>
    <b>mut</b> <b>const</b>
</pre>

<pre>
<a id="MethodOpenness" href="Semantics.md#MethodOpenness">MethodOpenness</a>:
    <i>(one of)</i>
    <b>open</b> <b>abstract</b>
</pre>

<pre>
<a id="MethodOverride" href="Semantics.md#MethodOverride">MethodOverride</a>:
    <b>override</b>
</pre>

<pre>
<a id="MethodDeclarator" href="Semantics.md#MethodDeclarator">MethodDeclarator</a>:
    <i>Identifier</i> <b>(</b> <i>[</i><i><a href="#Arguments">Arguments</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Return">Return</a></i> <i><a href="#Block">Block</a></i>
</pre>

---

<pre>
<a id="FixedArgumentType" href="Semantics.md#FixedArgumentType">FixedArgumentType</a>:
    <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="Arguments" href="Semantics.md#Arguments">Arguments</a>:
    <i><a href="#ThisArgument">ThisArgument</a></i> <i>[</i><b>,</b> <i><a href="#FixedArguments">FixedArguments</a></i><i>]</i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#FixedArguments">FixedArguments</a></i> <i>[</i><b>,</b> <i><a href="#VariadicArgument">VariadicArgument</a></i><i>]</i>
    <i><a href="#VariadicArgument">VariadicArgument</a></i>
</pre>

<pre>
<a id="Block" href="Semantics.md#Block">Block</a>:
    <b>{</b> <i>{</i><i>Statement</i><i>}</i> <b>}</b>
    <b>;</b>
</pre>

---

<pre>
<a id="ThisArgument" href="Semantics.md#ThisArgument">ThisArgument</a>:
    <b>this</b> <i>[</i><b>:</b> <i><a href="#ValueMutability">ValueMutability</a></i> <i>[</i><b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i><i>]</i>
    <b>this</b> <b>:</b> <b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i>
</pre>

<pre>
<a id="FixedArguments" href="Semantics.md#FixedArguments">FixedArguments</a>:
    <i><a href="#FixedArgument">FixedArgument</a></i> <i>{</i><b>,</b> <i><a href="#FixedArgument">FixedArgument</a></i><i>}</i>
</pre>

<pre>
<a id="VariadicArgument" href="Semantics.md#VariadicArgument">VariadicArgument</a>:
    <b>...</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

---

<pre>
<a id="FixedArgument" href="Semantics.md#FixedArgument">FixedArgument</a>:
    <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>
