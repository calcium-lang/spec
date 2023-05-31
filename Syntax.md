<!--[[[cog
import cog

from calcium.lexicon import (Identifier, StringIdentifier, Abstract, Aliasable, As, Atomic, Bare, Bool, C, Const, Enum, Final, From, Func, Import,
                             Local, Noreturn, Override, Package, Packed, Plain, Private, Protected, Public, Pure, Restrict, Sealed, Stable, Static,
                             Strict, Struct, This, Typedef, Union, Unsafe, Unused, Var, Void, Volatile, Wide, _Byte, _Char, _Double, _Float, _Int,
                             _Long, _Short, _Ubyte, _Uint, _Ulong, _Ushort, BlockStatement, Expression, Integer, LeftSquareBracket, RightSquareBracket
                             , LeftParenthesis, RightParenthesis, LeftCurlyBracket, RightCurlyBracket, FullStop, HyphenGreaterThan, Ampersand,
                             Question, Colon, Semicolon, TripleFullStop, Equals, Comma, At)
from calcium.syntax import (CompilationUnit, PackageDeclaration, ImportDeclarations, TopLevelTypeDeclaration, ImportDeclaration,
                            DeclarationEncapsulation, TypeDeclaration, ImportNames, FromName, PackageName, ImportName, PackageOrTypeName,
                            TypedefDeclaration, EnumDeclaration, UnionDeclaration, StructDeclaration, Version, BaseType, TypedefBody, EnumLayout,
                            EnumBody, UnionBody, DeclarationExtensibility, StructSeal, StructLayout, StructBody, BodyDeclarations, EnumConstants,
                            UnionTypes, TypeNames, BodyDeclaration, EnumConstant, StaticInitializer, MemberDeclaration, VariableInitializer,
                            SymbolNaming, MemberStaticity, FieldDeclaration, MethodDeclaration, MethodOverride, MethodHeader, MethodBody,
                            MethodDeclarator, Parameters, FixedParameters, VariableArityParameter, FixedParameter, Type, PrimitiveType,
                            PointerOrArraySuffix, TypeName, VoidPointerType, FunctionType, PointerNullity, TypeAtomicity, NumericType, PointerSuffix,
                            ArrayDim, TypeStrictness, ParameterTypes, TypeBareness, FunctionStrictness, FunctionPurity, Result, IntegralType,
                            FloatingPointType, ValueMutability, ValueVolatility, PointerWidth, ReferenceAliasability, ThisParameter,
                            FixedParameterTypes, VariableArityParameterType, FixedParameterType, VariableArityParameterLayout, Block, BlockStatements,
                            ArrayInitializer, StructInitializer, VariableInitializers, FieldInitializers, FieldInitializer)

level = 3
terminals = [
    Identifier, StringIdentifier, Abstract, Aliasable, As, Atomic, Bare, Bool, C, Const, Enum, Final, From, Func, Import, Local, Noreturn, Override,
    Package, Packed, Plain, Private, Protected, Public, Pure, Restrict, Sealed, Stable, Static, Strict, Struct, This, Typedef, Union, Unsafe, Unused,
    Var, Void, Volatile, Wide, _Byte, _Char, _Double, _Float, _Int, _Long, _Short, _Ubyte, _Uint, _Ulong, _Ushort, BlockStatement, Expression, Integer
    , LeftSquareBracket, RightSquareBracket, LeftParenthesis, RightParenthesis, LeftCurlyBracket, RightCurlyBracket, FullStop, HyphenGreaterThan,
    Ampersand, Question, Colon, Semicolon, TripleFullStop, Equals, Comma, At
]
terminals = {terminal.__name__: (terminal._pattern if isinstance(terminal._pattern, str) else None) for terminal in terminals}
]]]-->
<!--[[[end]]]-->

# Syntax
## [Packages](Semantics/Packages.md)
<!--[[[cog link = "Semantics/Packages.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(CompilationUnit.generate_md(level, terminals, link))
]]]-->
### [CompilationUnit](Semantics/Packages.md#CompilationUnit):
&emsp;&emsp;_[[PackageDeclaration](#PackageDeclaration)] [[ImportDeclarations](#ImportDeclarations)] [TopLevelTypeDeclaration](#TopLevelTypeDeclaration)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(PackageDeclaration.generate_md(level, terminals, link))
]]]-->
### [PackageDeclaration](Semantics/Packages.md#PackageDeclaration):
&emsp;&emsp;**package** _[PackageName](#PackageName) [_**;**_]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ImportDeclarations.generate_md(level, terminals, link))
]]]-->
### [ImportDeclarations](Semantics/Packages.md#ImportDeclarations):
&emsp;&emsp;_[ImportDeclaration](#ImportDeclaration) {[ImportDeclaration](#ImportDeclaration)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TopLevelTypeDeclaration.generate_md(level, terminals, link))
]]]-->
### [TopLevelTypeDeclaration](Semantics/Packages.md#TopLevelTypeDeclaration):
&emsp;&emsp;_[[DeclarationEncapsulation](#DeclarationEncapsulation)] [TypeDeclaration](#TypeDeclaration)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(ImportDeclaration.generate_md(level, terminals, link))
]]]-->
### [ImportDeclaration](Semantics/Packages.md#ImportDeclaration):
&emsp;&emsp;**import** _[ImportNames](#ImportNames) [[FromName](#FromName)] [_**;**_]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(DeclarationEncapsulation.generate_md(level, terminals, link))
]]]-->
### [DeclarationEncapsulation](Semantics/Packages.md#DeclarationEncapsulation):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**public protected private**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypeDeclaration.generate_md(level, terminals, link))
]]]-->
### [TypeDeclaration](Semantics/Packages.md#TypeDeclaration):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;_[TypedefDeclaration](#TypedefDeclaration) [EnumDeclaration](#EnumDeclaration) [UnionDeclaration](#UnionDeclaration) [StructDeclaration](#StructDeclaration)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(ImportNames.generate_md(level, terminals, link))
]]]-->
### [ImportNames](Semantics/Packages.md#ImportNames):
&emsp;&emsp;_[ImportName](#ImportName) {_**,** _[ImportName](#ImportName)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FromName.generate_md(level, terminals, link))
]]]-->
### [FromName](Semantics/Packages.md#FromName):
&emsp;&emsp;**from** _[PackageOrTypeName](#PackageOrTypeName)_  
<!--[[[end]]]-->

## [Names](Semantics/Names.md)
<!--[[[cog link = "Semantics/Names.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(PackageName.generate_md(level, terminals, link))
]]]-->
### [PackageName](Semantics/Names.md#PackageName):
&emsp;&emsp;_Identifier {_**.** _Identifier}_ <code>_[[Version](#Version)]_</code>[^low]  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ImportName.generate_md(level, terminals, link))
]]]-->
### [ImportName](Semantics/Names.md#ImportName):
&emsp;&emsp;_Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[_**as** _Identifier]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(PackageOrTypeName.generate_md(level, terminals, link))
]]]-->
### [PackageOrTypeName](Semantics/Names.md#PackageOrTypeName):
&emsp;&emsp;_Identifier_ <code>_[[Version](#Version)]_</code>[^low] _{_**.** _Identifier_ <code>_[[Version](#Version)]_</code>[^low]_}_  
<!--[[[end]]]-->

## [Typedefs, Enums, Unions and Structs](Semantics/Typedefs_Enums_Unions_and_Structs.md)
<!--[[[cog link = "Semantics/Typedefs_Enums_Unions_and_Structs.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypedefDeclaration.generate_md(level, terminals, link))
]]]-->
### [TypedefDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#TypedefDeclaration):
&emsp;&emsp;**typedef** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[BaseType](#BaseType) [[TypedefBody](#TypedefBody)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(EnumDeclaration.generate_md(level, terminals, link))
]]]-->
### [EnumDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#EnumDeclaration):
&emsp;&emsp;<code>_[[EnumLayout](#EnumLayout)]_</code>[^low] **enum** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[[BaseType](#BaseType)] [EnumBody](#EnumBody)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(UnionDeclaration.generate_md(level, terminals, link))
]]]-->
### [UnionDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#UnionDeclaration):
&emsp;&emsp;**union** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[UnionBody](#UnionBody)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(StructDeclaration.generate_md(level, terminals, link))
]]]-->
### [StructDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#StructDeclaration):
&emsp;&emsp;_[[DeclarationExtensibility](#DeclarationExtensibility)] [[StructSeal](#StructSeal)]_ <code>_[[StructLayout](#StructLayout)]_</code>[^low] **struct** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[[BaseType](#BaseType)] [StructBody](#StructBody)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(Version.generate_md(level, terminals, link))
]]]-->
### [Version](Semantics/Typedefs_Enums_Unions_and_Structs.md#Version):
&emsp;&emsp;**@** _Integer_ **.** _Integer_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(BaseType.generate_md(level, terminals, link))
]]]-->
### [BaseType](Semantics/Typedefs_Enums_Unions_and_Structs.md#BaseType):
&emsp;&emsp;**:** _[Type](#Type)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypedefBody.generate_md(level, terminals, link))
]]]-->
### [TypedefBody](Semantics/Typedefs_Enums_Unions_and_Structs.md#TypedefBody):
&emsp;&emsp;**{** _[BodyDeclarations](#BodyDeclarations)_ **}**  
&emsp;&emsp;**;**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(EnumLayout.generate_md(level, terminals, link))
]]]-->
### [EnumLayout](Semantics/Typedefs_Enums_Unions_and_Structs.md#EnumLayout):
&emsp;&emsp;**strict**  
&emsp;&emsp;**unsafe C**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(EnumBody.generate_md(level, terminals, link))
]]]-->
### [EnumBody](Semantics/Typedefs_Enums_Unions_and_Structs.md#EnumBody):
&emsp;&emsp;**{** _[EnumConstants](#EnumConstants) [_**;** _[BodyDeclarations](#BodyDeclarations)]_ **}**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(UnionBody.generate_md(level, terminals, link))
]]]-->
### [UnionBody](Semantics/Typedefs_Enums_Unions_and_Structs.md#UnionBody):
&emsp;&emsp;**{** _[UnionTypes](#UnionTypes) [_**;** _[BodyDeclarations](#BodyDeclarations)]_ **}**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(DeclarationExtensibility.generate_md(level, terminals, link))
]]]-->
### [DeclarationExtensibility](Semantics/Typedefs_Enums_Unions_and_Structs.md#DeclarationExtensibility):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**final abstract**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(StructSeal.generate_md(level, terminals, link))
]]]-->
### [StructSeal](Semantics/Typedefs_Enums_Unions_and_Structs.md#StructSeal):
&emsp;&emsp;**sealed** _[_**(** _[TypeNames](#TypeNames)_ **)**_]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(StructLayout.generate_md(level, terminals, link))
]]]-->
### [StructLayout](Semantics/Typedefs_Enums_Unions_and_Structs.md#StructLayout):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**strict C packed**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(StructBody.generate_md(level, terminals, link))
]]]-->
### [StructBody](Semantics/Typedefs_Enums_Unions_and_Structs.md#StructBody):
&emsp;&emsp;**{** _[[BodyDeclarations](#BodyDeclarations)]_ **}**  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(BodyDeclarations.generate_md(level, terminals, link))
]]]-->
### [BodyDeclarations](Semantics/Typedefs_Enums_Unions_and_Structs.md#BodyDeclarations):
&emsp;&emsp;_[BodyDeclaration](#BodyDeclaration) {[BodyDeclaration](#BodyDeclaration)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(EnumConstants.generate_md(level, terminals, link))
]]]-->
### [EnumConstants](Semantics/Typedefs_Enums_Unions_and_Structs.md#EnumConstants):
&emsp;&emsp;_[EnumConstant](#EnumConstant) {_**,** _[EnumConstant](#EnumConstant)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(UnionTypes.generate_md(level, terminals, link))
]]]-->
### [UnionTypes](Semantics/Typedefs_Enums_Unions_and_Structs.md#UnionTypes):
&emsp;&emsp;_[TypeDeclaration](#TypeDeclaration) {_**,** _[TypeDeclaration](#TypeDeclaration)}_  
<!--[[[end]]]-->

> The semicolon in TypedefBody must never be found in TypedefDeclaration.

<!--[[[cog
cog.out(TypeNames.generate_md(level, terminals, link))
]]]-->
### [TypeNames](Semantics/Typedefs_Enums_Unions_and_Structs.md#TypeNames):
&emsp;&emsp;_[TypeName](#TypeName) {_**,** _[TypeName](#TypeName)}_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(BodyDeclaration.generate_md(level, terminals, link))
]]]-->
### [BodyDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#BodyDeclaration):
&emsp;&emsp;_[StaticInitializer](#StaticInitializer)_  
&emsp;&emsp;_[[DeclarationEncapsulation](#DeclarationEncapsulation)] ([MemberDeclaration](#MemberDeclaration) | [TypeDeclaration](#TypeDeclaration))_  
<!--[[[end]]]-->

> TypedefBody must always be found in TypedefDeclaration.

<!--[[[cog
cog.out(EnumConstant.generate_md(level, terminals, link))
]]]-->
### [EnumConstant](Semantics/Typedefs_Enums_Unions_and_Structs.md#EnumConstant):
&emsp;&emsp;_[_**.**_] Identifier [(_**=** _|_ **:**_) [VariableInitializer](#VariableInitializer)]_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(StaticInitializer.generate_md(level, terminals, link))
]]]-->
### [StaticInitializer](Semantics/Typedefs_Enums_Unions_and_Structs.md#StaticInitializer):
&emsp;&emsp;<code>_[[SymbolNaming](#SymbolNaming)]_</code>[^low] **static** <code>_[[Version](#Version)] [StringIdentifier]_</code>[^low] _[Block](#Block)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(MemberDeclaration.generate_md(level, terminals, link))
]]]-->
### [MemberDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#MemberDeclaration):
&emsp;&emsp;_[[MemberStaticity](#MemberStaticity)] ([FieldDeclaration](#FieldDeclaration) | [MethodDeclaration](#MethodDeclaration))_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(VariableInitializer.generate_md(level, terminals, link))
]]]-->
### [VariableInitializer](Semantics/Typedefs_Enums_Unions_and_Structs.md#VariableInitializer):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;_Expression [ArrayInitializer](#ArrayInitializer) [StructInitializer](#StructInitializer)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(SymbolNaming.generate_md(level, terminals, link))
]]]-->
### [SymbolNaming](Semantics/Typedefs_Enums_Unions_and_Structs.md#SymbolNaming):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**strict plain**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(MemberStaticity.generate_md(level, terminals, link))
]]]-->
### [MemberStaticity](Semantics/Typedefs_Enums_Unions_and_Structs.md#MemberStaticity):
&emsp;&emsp;**static**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FieldDeclaration.generate_md(level, terminals, link))
]]]-->
### [FieldDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#FieldDeclaration):
&emsp;&emsp;_[ValueMutability](#ValueMutability)_ <code>_[[ValueVolatility](#ValueVolatility)] [[SymbolNaming](#SymbolNaming)]_</code>[^low] _Identifier_ <code>_[StringIdentifier]_</code>[^low] **:** _[Type](#Type) [_**=** _[VariableInitializer](#VariableInitializer)]_ **;**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(MethodDeclaration.generate_md(level, terminals, link))
]]]-->
### [MethodDeclaration](Semantics/Typedefs_Enums_Unions_and_Structs.md#MethodDeclaration):
&emsp;&emsp;_[[DeclarationExtensibility](#DeclarationExtensibility)] [[MethodOverride](#MethodOverride)]_ <code>_[[FunctionStrictness](#FunctionStrictness)]_</code>[^low] _[[FunctionPurity](#FunctionPurity)]_ **func** _[MethodHeader](#MethodHeader) [MethodBody](#MethodBody)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(MethodOverride.generate_md(level, terminals, link))
]]]-->
### [MethodOverride](Semantics/Typedefs_Enums_Unions_and_Structs.md#MethodOverride):
&emsp;&emsp;**override**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(MethodHeader.generate_md(level, terminals, link))
]]]-->
### [MethodHeader](Semantics/Typedefs_Enums_Unions_and_Structs.md#MethodHeader):
&emsp;&emsp;_[MethodDeclarator](#MethodDeclarator) [_**->** _[Result](#Result)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(MethodBody.generate_md(level, terminals, link))
]]]-->
### [MethodBody](Semantics/Typedefs_Enums_Unions_and_Structs.md#MethodBody):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;_[Block](#Block)_ **;**  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(MethodDeclarator.generate_md(level, terminals, link))
]]]-->
### [MethodDeclarator](Semantics/Typedefs_Enums_Unions_and_Structs.md#MethodDeclarator):
&emsp;&emsp;<code>_[[SymbolNaming](#SymbolNaming)]_</code>[^low] _Identifier_ <code>_[[Version](#Version)] [StringIdentifier]_</code>[^low] _[_**:** _[TypeName](#TypeName)]_ **(** _[[Parameters](#Parameters)]_ **)**  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(Parameters.generate_md(level, terminals, link))
]]]-->
### [Parameters](Semantics/Typedefs_Enums_Unions_and_Structs.md#Parameters):
&emsp;&emsp;_[ThisParameter](#ThisParameter) [_**,** _[FixedParameters](#FixedParameters)] [_**,** _[VariableArityParameter](#VariableArityParameter)]_  
&emsp;&emsp;_[FixedParameters](#FixedParameters) [_**,** _[VariableArityParameter](#VariableArityParameter)]_  
&emsp;&emsp;_[VariableArityParameter](#VariableArityParameter)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(FixedParameters.generate_md(level, terminals, link))
]]]-->
### [FixedParameters](Semantics/Typedefs_Enums_Unions_and_Structs.md#FixedParameters):
&emsp;&emsp;_[FixedParameter](#FixedParameter) {_**,** _[FixedParameter](#FixedParameter)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(VariableArityParameter.generate_md(level, terminals, link))
]]]-->
### [VariableArityParameter](Semantics/Typedefs_Enums_Unions_and_Structs.md#VariableArityParameter):
&emsp;&emsp;**...** <code>_[[VariableArityParameterLayout](#VariableArityParameterLayout)]_</code>[^low] _Identifier [_**:** _[Type](#Type)]_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(FixedParameter.generate_md(level, terminals, link))
]]]-->
### [FixedParameter](Semantics/Typedefs_Enums_Unions_and_Structs.md#FixedParameter):
&emsp;&emsp;_Identifier [_**:** _[Type](#Type)]_  
<!--[[[end]]]-->

## [Types](Semantics/Types.md)
<!--[[[cog link = "Semantics/Types.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(Type.generate_md(level, terminals, link))
]]]-->
### [Type](Semantics/Types.md#Type):
&emsp;&emsp;_([PrimitiveType](#PrimitiveType) | [TypeName](#TypeName) |_ <code>_[VoidPointerType](#VoidPointerType)_</code>[^low]_) [[PointerOrArraySuffix](#PointerOrArraySuffix)]_  
&emsp;&emsp;_[FunctionType](#FunctionType)_  
&emsp;&emsp;**(** _[FunctionType](#FunctionType)_ **)** _([PointerNullity](#PointerNullity) | [PointerOrArraySuffix](#PointerOrArraySuffix))_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(PrimitiveType.generate_md(level, terminals, link))
]]]-->
### [PrimitiveType](Semantics/Types.md#PrimitiveType):
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)]_</code>[^low] _([NumericType](#NumericType) |_ **bool** _|_ **\_char**_)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(PointerOrArraySuffix.generate_md(level, terminals, link))
]]]-->
### [PointerOrArraySuffix](Semantics/Types.md#PointerOrArraySuffix):
&emsp;&emsp;_([PointerSuffix](#PointerSuffix) | [ArrayDim](#ArrayDim)) [PointerOrArraySuffix]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypeName.generate_md(level, terminals, link))
]]]-->
### [TypeName](Semantics/Types.md#TypeName):
&emsp;&emsp;<code>_[[TypeStrictness](#TypeStrictness) | [TypeBareness](#TypeBareness)]_</code>[^low] _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _{_**.** _Identifier_ <code>_[[Version](#Version)]_</code>[^low]_} [_**(** _[[ParameterTypes](#ParameterTypes)]_ **)**_]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(VoidPointerType.generate_md(level, terminals, link))
]]]-->
### [VoidPointerType](Semantics/Types.md#VoidPointerType):
&emsp;&emsp;**unsafe void** _[[ValueMutability](#ValueMutability)] [[ValueVolatility](#ValueVolatility)]_ **&** _[[TypeAtomicity](#TypeAtomicity)] [[ReferenceAliasability](#ReferenceAliasability)] [[PointerNullity](#PointerNullity)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FunctionType.generate_md(level, terminals, link))
]]]-->
### [FunctionType](Semantics/Types.md#FunctionType):
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)] [[FunctionStrictness](#FunctionStrictness)]_</code>[^low] _[[FunctionPurity](#FunctionPurity)]_ **func (** _[[ParameterTypes](#ParameterTypes)]_ **) ->** _[Result](#Result)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(PointerNullity.generate_md(level, terminals, link))
]]]-->
### [PointerNullity](Semantics/Types.md#PointerNullity):
&emsp;&emsp;_[_**local**_]_ **?**  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(TypeAtomicity.generate_md(level, terminals, link))
]]]-->
### [TypeAtomicity](Semantics/Types.md#TypeAtomicity):
&emsp;&emsp;**atomic**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(NumericType.generate_md(level, terminals, link))
]]]-->
### [NumericType](Semantics/Types.md#NumericType):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;_[IntegralType](#IntegralType) [FloatingPointType](#FloatingPointType)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(PointerSuffix.generate_md(level, terminals, link))
]]]-->
### [PointerSuffix](Semantics/Types.md#PointerSuffix):
&emsp;&emsp;_[[ValueMutability](#ValueMutability)]_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] **&** <code>_[[PointerWidth](#PointerWidth) | [TypeAtomicity](#TypeAtomicity)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low] _[[PointerNullity](#PointerNullity)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ArrayDim.generate_md(level, terminals, link))
]]]-->
### [ArrayDim](Semantics/Types.md#ArrayDim):
&emsp;&emsp;**[** _(_<code>_[[TypeStrictness](#TypeStrictness)]_</code>[^low] _[Expression] |_ <code>_[TypeBareness](#TypeBareness)_</code>[^low]_)_ **]** _[[PointerNullity](#PointerNullity)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypeStrictness.generate_md(level, terminals, link))
]]]-->
### [TypeStrictness](Semantics/Types.md#TypeStrictness):
&emsp;&emsp;**strict**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ParameterTypes.generate_md(level, terminals, link))
]]]-->
### [ParameterTypes](Semantics/Types.md#ParameterTypes):
&emsp;&emsp;_[ThisParameter](#ThisParameter) [_**,** _[FixedParameterTypes](#FixedParameterTypes)] [_**,** _[VariableArityParameterType](#VariableArityParameterType)]_  
&emsp;&emsp;_[FixedParameterTypes](#FixedParameterTypes) [_**,** _[VariableArityParameterType](#VariableArityParameterType)]_  
&emsp;&emsp;_[VariableArityParameterType](#VariableArityParameterType)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(TypeBareness.generate_md(level, terminals, link))
]]]-->
### [TypeBareness](Semantics/Types.md#TypeBareness):
&emsp;&emsp;**unsafe bare**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FunctionStrictness.generate_md(level, terminals, link))
]]]-->
### [FunctionStrictness](Semantics/Types.md#FunctionStrictness):
&emsp;&emsp;**strict**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FunctionPurity.generate_md(level, terminals, link))
]]]-->
### [FunctionPurity](Semantics/Types.md#FunctionPurity):
&emsp;&emsp;_[_**local**_] (_**const** _|_ **pure**_)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(Result.generate_md(level, terminals, link))
]]]-->
### [Result](Semantics/Types.md#Result):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**noreturn void** _[Type](#Type)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(IntegralType.generate_md(level, terminals, link))
]]]-->
### [IntegralType](Semantics/Types.md#IntegralType):
&emsp;&emsp;<code>_(_**\_ubyte** _|_ **\_byte** _|_ **\_ushort** _|_ **\_short** _|_ **\_uint**_)_</code>[^low]  
&emsp;&emsp;**\_int**  
&emsp;&emsp;<code>_(_**\_ulong** _|_ **\_long**_)_</code>[^low]  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FloatingPointType.generate_md(level, terminals, link))
]]]-->
### [FloatingPointType](Semantics/Types.md#FloatingPointType):
&emsp;&emsp;**\_float**  
&emsp;&emsp;<code>**\_double**</code>[^low]  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ValueMutability.generate_md(level, terminals, link))
]]]-->
### [ValueMutability](Semantics/Types.md#ValueMutability):
&emsp;&emsp;_[_**unsafe**_]_ **var**  
&emsp;&emsp;_[_**local**_]_ **const**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ValueVolatility.generate_md(level, terminals, link))
]]]-->
### [ValueVolatility](Semantics/Types.md#ValueVolatility):
&emsp;&emsp;_[_**local**_]_ **volatile**  
&emsp;&emsp;_[_**unsafe**_]_ **stable**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(PointerWidth.generate_md(level, terminals, link))
]]]-->
### [PointerWidth](Semantics/Types.md#PointerWidth):
&emsp;&emsp;_[[_**unsafe**_]_ **unused**_] [[TypeStrictness](#TypeStrictness)]_ **wide**  
&emsp;&emsp;_[TypeBareness](#TypeBareness)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ReferenceAliasability.generate_md(level, terminals, link))
]]]-->
### [ReferenceAliasability](Semantics/Types.md#ReferenceAliasability):
&emsp;&emsp;_[_**local**_]_ **aliasable**  
&emsp;&emsp;_[_**unsafe**_]_ **restrict**  
<!--[[[end]]]-->

<!--[[[cog
cog.out(ThisParameter.generate_md(level, terminals, link))
]]]-->
### [ThisParameter](Semantics/Types.md#ThisParameter):
&emsp;&emsp;**this** _[_**:** _[TypeName](#TypeName) [[ValueMutability](#ValueMutability)]_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] _[_**&** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]_]]_  
&emsp;&emsp;**this :** _[ValueMutability](#ValueMutability)_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] _[_**&** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]_]_  
&emsp;&emsp;<code>**this :** _[ValueVolatility](#ValueVolatility) [_**&** _[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]]_</code>[^low]  
&emsp;&emsp;**this : &** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FixedParameterTypes.generate_md(level, terminals, link))
]]]-->
### [FixedParameterTypes](Semantics/Types.md#FixedParameterTypes):
&emsp;&emsp;_[FixedParameterType](#FixedParameterType) {_**,** _[FixedParameterType](#FixedParameterType)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(VariableArityParameterType.generate_md(level, terminals, link))
]]]-->
### [VariableArityParameterType](Semantics/Types.md#VariableArityParameterType):
&emsp;&emsp;**...** <code>_[[VariableArityParameterLayout](#VariableArityParameterLayout)]_</code>[^low] **:** _[Type](#Type)_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(FixedParameterType.generate_md(level, terminals, link))
]]]-->
### [FixedParameterType](Semantics/Types.md#FixedParameterType):
&emsp;&emsp;**:** _[Type](#Type)_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(VariableArityParameterLayout.generate_md(level, terminals, link))
]]]-->
### [VariableArityParameterLayout](Semantics/Types.md#VariableArityParameterLayout):
&emsp;&emsp;**strict**  
&emsp;&emsp;**unsafe C**  
<!--[[[end]]]-->

## [Blocks and Statements](Semantics/Blocks_and_Statements.md)
<!--[[[cog link = "Semantics/Blocks_and_Statements.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(Block.generate_md(level, terminals, link))
]]]-->
### [Block](Semantics/Blocks_and_Statements.md#Block):
&emsp;&emsp;**{** _[[BlockStatements](#BlockStatements)]_ **}**  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(BlockStatements.generate_md(level, terminals, link))
]]]-->
### [BlockStatements](Semantics/Blocks_and_Statements.md#BlockStatements):
&emsp;&emsp;_BlockStatement {BlockStatement}_  
<!--[[[end]]]-->

## [Expressions](Semantics/Expressions.md)
<!--[[[cog link = "Semantics/Expressions.md" ]]]-->
<!--[[[end]]]-->

## [Array and Struct Initializers](Semantics/Array_and_Struct_Initializers.md)
<!--[[[cog link = "Semantics/Array_and_Struct_Initializers.md" ]]]-->
<!--[[[end]]]-->

<!--[[[cog
cog.out(ArrayInitializer.generate_md(level, terminals, link))
]]]-->
### [ArrayInitializer](Semantics/Array_and_Struct_Initializers.md#ArrayInitializer):
&emsp;&emsp;**[** _[[VariableInitializers](#VariableInitializers)]_ **]** _[_**:** _[Type](#Type)]_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(StructInitializer.generate_md(level, terminals, link))
]]]-->
### [StructInitializer](Semantics/Array_and_Struct_Initializers.md#StructInitializer):
&emsp;&emsp;**{** _[[FieldInitializers](#FieldInitializers)]_ **}** _[_**:** _[TypeName](#TypeName)]_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(VariableInitializers.generate_md(level, terminals, link))
]]]-->
### [VariableInitializers](Semantics/Array_and_Struct_Initializers.md#VariableInitializers):
&emsp;&emsp;_[VariableInitializer](#VariableInitializer) {_**,** _[VariableInitializer](#VariableInitializer)}_  
<!--[[[end]]]-->

<!--[[[cog
cog.out(FieldInitializers.generate_md(level, terminals, link))
]]]-->
### [FieldInitializers](Semantics/Array_and_Struct_Initializers.md#FieldInitializers):
&emsp;&emsp;_[FieldInitializer](#FieldInitializer) {_**,** _[FieldInitializer](#FieldInitializer)}_  
<!--[[[end]]]-->

\---

<!--[[[cog
cog.out(FieldInitializer.generate_md(level, terminals, link))
]]]-->
### [FieldInitializer](Semantics/Array_and_Struct_Initializers.md#FieldInitializer):
&emsp;&emsp;_[_**.**_] Identifier (_**=** _|_ **:**_) [VariableInitializer](#VariableInitializer)_  
<!--[[[end]]]-->

[^low]: Low level syntax.
