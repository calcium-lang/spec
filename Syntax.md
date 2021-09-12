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
    <i>[</i><i><a href="#PackageDeclaration">PackageDeclaration</a></i><i>]</i> <i>{</i><i><a href="#ImportDeclaration">ImportDeclaration</a></i><i>}</i> <i><a href="#TopLevelTypeDeclaration">TopLevelTypeDeclaration</a></i>
</pre>

---

<pre>
<a id="PackageDeclaration" href="Semantics.md#PackageDeclaration">PackageDeclaration</a>:
    <b>package</b> <i><a href="#PackageName">PackageName</a></i> <b>;</b>
</pre>

<pre>
<a id="ImportDeclaration" href="Semantics.md#ImportDeclaration">ImportDeclaration</a>:
    <b>import</b> <i><a href="#ExplicitImport">ExplicitImport</a></i>
    <b>import</b> <i><a href="#ImportOnDemand">ImportOnDemand</a></i>
</pre>

<pre>
<a id="TopLevelTypeDeclaration" href="Semantics.md#TopLevelTypeDeclaration">TopLevelTypeDeclaration</a>:
    <i>[</i><i><a href="#TopLevelEncapsulation">TopLevelEncapsulation</a></i><i>]</i> <i><a href="#TypeDeclaration">TypeDeclaration</a></i>
</pre>

---

<pre>
<a id="PackageName" href="Semantics.md#PackageName">PackageName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="ExplicitImport" href="Semantics.md#ExplicitImport">ExplicitImport</a>:
    <i><a href="#ImportNames">ImportNames</a></i> <i>[</i><b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i><i>]</i> <b>;</b>
</pre>

<pre>
<a id="ImportOnDemand" href="Semantics.md#ImportOnDemand">ImportOnDemand</a>:
    <b>*</b> <b>from</b> <i><a href="#PackageOrTypeName">PackageOrTypeName</a></i> <b>;</b>
</pre>

<pre>
<a id="TopLevelEncapsulation" href="Semantics.md#TopLevelEncapsulation">TopLevelEncapsulation</a>:
    <b>public</b>
</pre>

<pre>
<a id="TypeDeclaration" href="Semantics.md#TypeDeclaration">TypeDeclaration</a>:
    <i><a href="#TypedefDeclaration">TypedefDeclaration</a></i> <b>;</b>
    <i><a href="#EnumDeclaration">EnumDeclaration</a></i>
    <i><a href="#UnionDeclaration">UnionDeclaration</a></i>
    <i><a href="#StructDeclaration">StructDeclaration</a></i>
</pre>

---

<pre>
<a id="ImportNames" href="Semantics.md#ImportNames">ImportNames</a>:
    <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i> <i>{</i><b>,</b> <i>Identifier</i> <i>[</i><b>as</b> <i>Identifier</i><i>]</i><i>}</i>
</pre>

<pre>
<a id="PackageOrTypeName" href="Semantics.md#PackageOrTypeName">PackageOrTypeName</a>:
    <i>Identifier</i> <i>{</i><b>.</b> <i>Identifier</i><i>}</i>
</pre>

<pre>
<a id="TypedefDeclaration" href="Semantics.md#TypedefDeclaration">TypedefDeclaration</a>:
    <b>typedef</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="EnumDeclaration" href="Semantics.md#EnumDeclaration">EnumDeclaration</a>:
    <b>enum</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <i><a href="#EnumBody">EnumBody</a></i>
</pre>

<pre>
<a id="UnionDeclaration" href="Semantics.md#UnionDeclaration">UnionDeclaration</a>:
    <b>union</b> <i>Identifier</i> <i><a href="#UnionBody">UnionBody</a></i>
</pre>

<pre>
<a id="StructDeclaration" href="Semantics.md#StructDeclaration">StructDeclaration</a>:
    <i>[</i><i><a href="#StructExtensibility">StructExtensibility</a></i><i>]</i> <i>[</i><i><a href="#StructLayout">StructLayout</a></i><i>]</i> <b>struct</b> <i>Identifier</i> <i>[</i><b>:</b> <i><a href="#Type">Type</a></i><i>]</i> <i><a href="#StructBody">StructBody</a></i>
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
<a id="EnumBody" href="Semantics.md#EnumBody">EnumBody</a>:
    <b>{</b> <i><a href="#EnumConstants">EnumConstants</a></i> <i>[</i><i><a href="#EnumBodyDeclarations">EnumBodyDeclarations</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="UnionBody" href="Semantics.md#UnionBody">UnionBody</a>:
    <b>{</b> <i><a href="#UnionTypes">UnionTypes</a></i> <i>[</i><i><a href="#UnionBodyDeclarations">UnionBodyDeclarations</a></i><i>]</i> <b>}</b>
</pre>

<pre>
<a id="StructExtensibility" href="Semantics.md#StructExtensibility">StructExtensibility</a>:
    <i>(one of)</i>
    <b>open</b> <b>abstract</b>
</pre>

<pre>
<a id="StructLayout" href="Semantics.md#StructLayout">StructLayout</a>:
    <b>raw</b>
</pre>

<pre>
<a id="StructBody" href="Semantics.md#StructBody">StructBody</a>:
    <b>{</b> <i>[</i><i><a href="#StructBodyDeclarations">StructBodyDeclarations</a></i><i>]</i> <b>}</b>
</pre>

---

<pre>
<a id="PrimitiveType" href="Semantics.md#PrimitiveType">PrimitiveType</a>:
    <i><a href="#NumericType">NumericType</a></i> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
    <b>bool</b> <i>[</i><i><a href="#TypeAtomicity">TypeAtomicity</a></i><i>]</i>
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
    <b>(</b> <i>[</i><i><a href="#ParameterTypes">ParameterTypes</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Result">Result</a></i>
</pre>

<pre>
<a id="EnumConstants" href="Semantics.md#EnumConstants">EnumConstants</a>:
    <i><a href="#EnumConstant">EnumConstant</a></i> <i>{</i><b>,</b> <i><a href="#EnumConstant">EnumConstant</a></i><i>}</i>
</pre>

<pre>
<a id="EnumBodyDeclarations" href="Semantics.md#EnumBodyDeclarations">EnumBodyDeclarations</a>:
    <b>;</b> <i><a href="#StructBodyDeclarations">StructBodyDeclarations</a></i>
</pre>

<pre>
<a id="UnionTypes" href="Semantics.md#UnionTypes">UnionTypes</a>:
    <i><a href="#UnionType">UnionType</a></i> <i>{</i><b>,</b> <i><a href="#UnionType">UnionType</a></i><i>}</i>
</pre>

<pre>
<a id="UnionBodyDeclarations" href="Semantics.md#UnionBodyDeclarations">UnionBodyDeclarations</a>:
    <b>;</b> <i><a href="#StructBodyDeclarations">StructBodyDeclarations</a></i>
</pre>

<pre>
<a id="StructBodyDeclarations" href="Semantics.md#StructBodyDeclarations">StructBodyDeclarations</a>:
    <i><a href="#StructBodyDeclaration">StructBodyDeclaration</a></i> <i>{</i><i><a href="#StructBodyDeclaration">StructBodyDeclaration</a></i><i>}</i>
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
<a id="ParameterTypes" href="Semantics.md#ParameterTypes">ParameterTypes</a>:
    <i><a href="#FixedParameterTypes">FixedParameterTypes</a></i> <i>[</i><b>,</b> <i><a href="#VariableArityParameterType">VariableArityParameterType</a></i><i>]</i>
    <i><a href="#VariableArityParameterType">VariableArityParameterType</a></i>
</pre>

<pre>
<a id="Result" href="Semantics.md#Result">Result</a>:
    <b>noreturn</b>
    <b>void</b>
    <i><a href="#Type">Type</a></i>
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
<a id="StructBodyDeclaration" href="Semantics.md#StructBodyDeclaration">StructBodyDeclaration</a>:
    <i>[</i><i><a href="#NestedEncapsulation">NestedEncapsulation</a></i><i>]</i> <i><a href="#StructMemberDeclaration">StructMemberDeclaration</a></i>
    <i>[</i><i><a href="#NestedEncapsulation">NestedEncapsulation</a></i><i>]</i> <i><a href="#TypeDeclaration">TypeDeclaration</a></i>
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
    <b>aliasable</b>
</pre>

<pre>
<a id="FixedParameterTypes" href="Semantics.md#FixedParameterTypes">FixedParameterTypes</a>:
    <i><a href="#FixedParameterType">FixedParameterType</a></i> <i>{</i><b>,</b> <i><a href="#FixedParameterType">FixedParameterType</a></i><i>}</i>
</pre>

<pre>
<a id="VariableArityParameterType" href="Semantics.md#VariableArityParameterType">VariableArityParameterType</a>:
    <b>...</b> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="NestedEncapsulation" href="Semantics.md#NestedEncapsulation">NestedEncapsulation</a>:
    <i>(one of)</i>
    <b>public</b> <b>protected</b> <b>private</b>
</pre>

<pre>
<a id="StructMemberDeclaration" href="Semantics.md#StructMemberDeclaration">StructMemberDeclaration</a>:
    <i>[</i><i><a href="#MemberStaticity">MemberStaticity</a></i><i>]</i> <i><a href="#FieldDeclaration">FieldDeclaration</a></i>
    <i>[</i><i><a href="#MemberStaticity">MemberStaticity</a></i><i>]</i> <i><a href="#MethodDeclaration">MethodDeclaration</a></i>
</pre>

---

<pre>
<a id="FixedParameterType" href="Semantics.md#FixedParameterType">FixedParameterType</a>:
    <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

<pre>
<a id="MemberStaticity" href="Semantics.md#MemberStaticity">MemberStaticity</a>:
    <b>static</b>
</pre>

<pre>
<a id="FieldDeclaration" href="Semantics.md#FieldDeclaration">FieldDeclaration</a>:
    <i><a href="#FieldMutability">FieldMutability</a></i> <i>[</i><i><a href="#ValueVolatility">ValueVolatility</a></i><i>]</i> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i> <i>[</i><b>=</b> <i>ConstantExpression</i><i>]</i> <b>;</b>
</pre>

<pre>
<a id="MethodDeclaration" href="Semantics.md#MethodDeclaration">MethodDeclaration</a>:
    <i>[</i><i><a href="#MethodExtensibility">MethodExtensibility</a></i><i>]</i> <i>[</i><i><a href="#MethodOverride">MethodOverride</a></i><i>]</i> <b>func</b> <i><a href="#MethodHeader">MethodHeader</a></i> <i><a href="#MethodBody">MethodBody</a></i>
</pre>

---

<pre>
<a id="FieldMutability" href="Semantics.md#FieldMutability">FieldMutability</a>:
    <i>(one of)</i>
    <b>mut</b> <b>const</b>
</pre>

<pre>
<a id="MethodExtensibility" href="Semantics.md#MethodExtensibility">MethodExtensibility</a>:
    <i>(one of)</i>
    <b>open</b> <b>abstract</b>
</pre>

<pre>
<a id="MethodOverride" href="Semantics.md#MethodOverride">MethodOverride</a>:
    <b>override</b>
</pre>

<pre>
<a id="MethodHeader" href="Semantics.md#MethodHeader">MethodHeader</a>:
    <i>Identifier</i> <b>(</b> <i>[</i><i><a href="#Parameters">Parameters</a></i><i>]</i> <b>)</b> <b>-&gt;</b> <i><a href="#Result">Result</a></i>
</pre>

<pre>
<a id="MethodBody" href="Semantics.md#MethodBody">MethodBody</a>:
    <i><a href="#Block">Block</a></i>
    <b>;</b>
</pre>

---

<pre>
<a id="Parameters" href="Semantics.md#Parameters">Parameters</a>:
    <i><a href="#ThisParameter">ThisParameter</a></i> <i>[</i><b>,</b> <i><a href="#FixedParameters">FixedParameters</a></i><i>]</i> <i>[</i><b>,</b> <i><a href="#VariableArityParameter">VariableArityParameter</a></i><i>]</i>
    <i><a href="#FixedParameters">FixedParameters</a></i> <i>[</i><b>,</b> <i><a href="#VariableArityParameter">VariableArityParameter</a></i><i>]</i>
    <i><a href="#VariableArityParameter">VariableArityParameter</a></i>
</pre>

<pre>
<a id="Block" href="Semantics.md#Block">Block</a>:
    <b>{</b> <i>{</i><i>Statement</i><i>}</i> <b>}</b>
</pre>

---

<pre>
<a id="ThisParameter" href="Semantics.md#ThisParameter">ThisParameter</a>:
    <b>this</b> <i>[</i><b>:</b> <i><a href="#ValueMutability">ValueMutability</a></i> <i>[</i><b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i><i>]</i><i>]</i>
    <b>this</b> <b>:</b> <b>&</b> <i><a href="#ReferenceAliasability">ReferenceAliasability</a></i>
</pre>

<pre>
<a id="FixedParameters" href="Semantics.md#FixedParameters">FixedParameters</a>:
    <i><a href="#FixedParameter">FixedParameter</a></i> <i>{</i><b>,</b> <i><a href="#FixedParameter">FixedParameter</a></i><i>}</i>
</pre>

<pre>
<a id="VariableArityParameter" href="Semantics.md#VariableArityParameter">VariableArityParameter</a>:
    <b>...</b> <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>

---

<pre>
<a id="FixedParameter" href="Semantics.md#FixedParameter">FixedParameter</a>:
    <i>Identifier</i> <b>:</b> <i><a href="#Type">Type</a></i>
</pre>
