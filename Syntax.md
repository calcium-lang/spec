# Syntax
## Packages
### [CompilationUnit](Semantics.md#CompilationUnit):
&emsp;&emsp;_[[PackageDeclaration](#PackageDeclaration)] [[ImportDeclarations](#ImportDeclarations)] [TopLevelTypeDeclaration](#TopLevelTypeDeclaration)_  

\---

### [PackageDeclaration](Semantics.md#PackageDeclaration):
&emsp;&emsp;**package** _[PackageName](#PackageName) [_**;**_]_  

### [ImportDeclarations](Semantics.md#ImportDeclarations):
&emsp;&emsp;_[ImportDeclaration](#ImportDeclaration) {[ImportDeclaration](#ImportDeclaration)}_  

### [TopLevelTypeDeclaration](Semantics.md#TopLevelTypeDeclaration):
&emsp;&emsp;_[[DeclarationEncapsulation](#DeclarationEncapsulation)] [TypeDeclaration](#TypeDeclaration)_  

\---

### [ImportDeclaration](Semantics.md#ImportDeclaration):
&emsp;&emsp;**import** _[ImportNames](#ImportNames) [[FromName](#FromName)] [_**;**_]_  

### [DeclarationEncapsulation](Semantics.md#DeclarationEncapsulation):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**public protected private**  

### [TypeDeclaration](Semantics.md#TypeDeclaration):
&emsp;&emsp;_[TypedefDeclaration](#TypedefDeclaration)_  
&emsp;&emsp;_[EnumDeclaration](#EnumDeclaration)_  
&emsp;&emsp;_[UnionDeclaration](#UnionDeclaration)_  
&emsp;&emsp;_[StructDeclaration](#StructDeclaration)_  

\---

### [ImportNames](Semantics.md#ImportNames):
&emsp;&emsp;_[ImportName](#ImportName) {_**,** _[ImportName](#ImportName)}_  

### [FromName](Semantics.md#FromName):
&emsp;&emsp;**from** _[PackageOrTypeName](#PackageOrTypeName)_  

## Names
### [PackageName](Semantics.md#PackageName):
&emsp;&emsp;_Identifier {_**.** _Identifier}_ <code>_[[Version](#Version)]_</code>[^low]  

### [ImportName](Semantics.md#ImportName):
&emsp;&emsp;_Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[_**as** _Identifier]_  

### [PackageOrTypeName](Semantics.md#PackageOrTypeName):
&emsp;&emsp;_Identifier_ <code>_[[Version](#Version)]_</code>[^low] _{_**.** _Identifier_ <code>_[[Version](#Version)]_</code>[^low]_}_  

## Typedefs, Enums, Unions and Structs
### [TypedefDeclaration](Semantics.md#TypedefDeclaration):
&emsp;&emsp;**typedef** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[BaseType](#BaseType) [[TypedefBody](#TypedefBody)]_  

### [EnumDeclaration](Semantics.md#EnumDeclaration):
&emsp;&emsp;<code>_[[EnumLayout](#EnumLayout)]_</code>[^low] **enum** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[[BaseType](#BaseType)] [EnumBody](#EnumBody)_  

### [UnionDeclaration](Semantics.md#UnionDeclaration):
&emsp;&emsp;**union** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[UnionBody](#UnionBody)_  

### [StructDeclaration](Semantics.md#StructDeclaration):
&emsp;&emsp;_[[DeclarationExtensibility](#DeclarationExtensibility)]_ <code>_[[StructLayout](#StructLayout)]_</code>[^low] **struct** _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _[[BaseType](#BaseType)] [StructBody](#StructBody)_  

\---

### [Version](Semantics.md#Version):
&emsp;&emsp;<code>**@** _IntegerLiteral_ **.** _IntegerLiteral_</code>[^low]  

### [BaseType](Semantics.md#BaseType):
&emsp;&emsp;**:** _[Type](#Type)_  

### [TypedefBody](Semantics.md#TypedefBody):
&emsp;&emsp;**{** _[BodyDeclarations](#BodyDeclarations)_ **}**  
&emsp;&emsp;**;**  

### [EnumLayout](Semantics.md#EnumLayout):
&emsp;&emsp;<code>**strict**</code>[^low]  
&emsp;&emsp;<code>**unsafe C**</code>[^low]  

### [EnumBody](Semantics.md#EnumBody):
&emsp;&emsp;**{** _[EnumConstants](#EnumConstants) [_**;** _[BodyDeclarations](#BodyDeclarations)]_ **}**  

### [UnionBody](Semantics.md#UnionBody):
&emsp;&emsp;**{** _[UnionTypes](#UnionTypes) [_**;** _[BodyDeclarations](#BodyDeclarations)]_ **}**  

### [DeclarationExtensibility](Semantics.md#DeclarationExtensibility):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**final abstract**  

### [StructLayout](Semantics.md#StructLayout):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;<code>**strict C packed**</code>[^low]  

### [StructBody](Semantics.md#StructBody):
&emsp;&emsp;**{** _[[BodyDeclarations](#BodyDeclarations)]_ **}**  

\---

### [BodyDeclarations](Semantics.md#BodyDeclarations):
&emsp;&emsp;_[BodyDeclaration](#BodyDeclaration) {[BodyDeclaration](#BodyDeclaration)}_  

### [EnumConstants](Semantics.md#EnumConstants):
&emsp;&emsp;_[EnumConstant](#EnumConstant) {_**,** _[EnumConstant](#EnumConstant)}_  

### [UnionTypes](Semantics.md#UnionTypes):
&emsp;&emsp;_[TypeDeclaration](#TypeDeclaration) {_**,** _[TypeDeclaration](#TypeDeclaration)}_  

> The semicolon in TypedefBody must never be found in TypedefDeclaration.

\---

### [BodyDeclaration](Semantics.md#BodyDeclaration):
&emsp;&emsp;_[StaticInitializer](#StaticInitializer)_  
&emsp;&emsp;_[[DeclarationEncapsulation](#DeclarationEncapsulation)] [MemberDeclaration](#MemberDeclaration)_  
&emsp;&emsp;_[[DeclarationEncapsulation](#DeclarationEncapsulation)] [TypeDeclaration](#TypeDeclaration)_  

> TypedefBody must always be found in TypedefDeclaration.

### [EnumConstant](Semantics.md#EnumConstant):
&emsp;&emsp;_[_**.**_] Identifier [(_**=**_|_**:**_) [VariableInitializer](#VariableInitializer)]_  

\---

### [StaticInitializer](Semantics.md#StaticInitializer):
&emsp;&emsp;<code>_[[SymbolNaming](#SymbolNaming)]_</code>[^low] **static** <code>_[[Version](#Version)] [StringIdentifier]_</code>[^low] _[Block](#Block)_  

### [MemberDeclaration](Semantics.md#MemberDeclaration):
&emsp;&emsp;_[[MemberStaticity](#MemberStaticity)] [FieldDeclaration](#FieldDeclaration)_  
&emsp;&emsp;_[[MemberStaticity](#MemberStaticity)] [MethodDeclaration](#MethodDeclaration)_  

### [VariableInitializer](Semantics.md#VariableInitializer):
&emsp;&emsp;_Expression_  
&emsp;&emsp;_[ArrayInitializer](#ArrayInitializer)_  
&emsp;&emsp;_[StructInitializer](#StructInitializer)_  

\---

### [SymbolNaming](Semantics.md#SymbolNaming):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;<code>**strict plain**</code>[^low]  

### [MemberStaticity](Semantics.md#MemberStaticity):
&emsp;&emsp;**static**  

### [FieldDeclaration](Semantics.md#FieldDeclaration):
&emsp;&emsp;_[ValueMutability](#ValueMutability)_ <code>_[[ValueVolatility](#ValueVolatility)] [[SymbolNaming](#SymbolNaming)]_</code>[^low] _Identifier_ <code>_[StringIdentifier]_</code>[^low] **:** _[Type](#Type) [_**=** _[VariableInitializer](#VariableInitializer)]_ **;**  

### [MethodDeclaration](Semantics.md#MethodDeclaration):
&emsp;&emsp;_[[DeclarationExtensibility](#DeclarationExtensibility)] [[MethodOverride](#MethodOverride)]_ <code>_[[FunctionStrictness](#FunctionStrictness)]_</code>[^low] _[[FunctionPurity](#FunctionPurity)]_ **func** _[MethodHeader](#MethodHeader) [MethodBody](#MethodBody)_  

\---

### [MethodOverride](Semantics.md#MethodOverride):
&emsp;&emsp;**override**  

### [MethodHeader](Semantics.md#MethodHeader):
&emsp;&emsp;_[MethodDeclarator](#MethodDeclarator) [_**->** _[Result](#Result)]_  

### [MethodBody](Semantics.md#MethodBody):
&emsp;&emsp;_[Block](#Block)_  
&emsp;&emsp;**;**  

\---

### [MethodDeclarator](Semantics.md#MethodDeclarator):
&emsp;&emsp;<code>_[[SymbolNaming](#SymbolNaming)]_</code>[^low] _Identifier_ <code>_[[Version](#Version)] [StringIdentifier]_</code>[^low] _[_**:** _[TypeName](#TypeName)]_ **(** _[[Parameters](#Parameters)]_ **)**  

\---

### [Parameters](Semantics.md#Parameters):
&emsp;&emsp;_[ThisParameter](#ThisParameter) [_**,** _[FixedParameters](#FixedParameters)] [_**,** _[VariableArityParameter](#VariableArityParameter)]_  
&emsp;&emsp;_[FixedParameters](#FixedParameters) [_**,** _[VariableArityParameter](#VariableArityParameter)]_  
&emsp;&emsp;_[VariableArityParameter](#VariableArityParameter)_  

\---

### [FixedParameters](Semantics.md#FixedParameters):
&emsp;&emsp;_[FixedParameter](#FixedParameter) {_**,** _[FixedParameter](#FixedParameter)}_  

### [VariableArityParameter](Semantics.md#VariableArityParameter):
&emsp;&emsp;**...** <code>_[[VariableArityParameterLayout](#VariableArityParameterLayout)]_</code>[^low] _Identifier [_**:** _[Type](#Type)]_  

\---

### [FixedParameter](Semantics.md#FixedParameter):
&emsp;&emsp;_Identifier [_**:** _[Type](#Type)]_  

## Types
### [Type](Semantics.md#Type):
&emsp;&emsp;_[PrimitiveType](#PrimitiveType) [[PointerOrArraySuffix](#PointerOrArraySuffix)]_  
&emsp;&emsp;_[TypeName](#TypeName) [[PointerOrArraySuffix](#PointerOrArraySuffix)]_  
&emsp;&emsp;<code>_[VoidPointerType](#VoidPointerType) [[PointerOrArraySuffix](#PointerOrArraySuffix)]_</code>[^low]  
&emsp;&emsp;_[FunctionType](#FunctionType)_  
&emsp;&emsp;**(** _[FunctionType](#FunctionType)_ **)** _[PointerNullity](#PointerNullity)_  
&emsp;&emsp;**(** _[FunctionType](#FunctionType)_ **)** _[PointerOrArraySuffix](#PointerOrArraySuffix)_  

\---

### [PrimitiveType](Semantics.md#PrimitiveType):
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)]_</code>[^low] _[NumericType](#NumericType)_  
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)]_</code>[^low] **bool**  
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)]_</code>[^low] **\_char**  

### [PointerOrArraySuffix](Semantics.md#PointerOrArraySuffix):
&emsp;&emsp;_[PointerSuffix](#PointerSuffix) [PointerOrArraySuffix]_  
&emsp;&emsp;_[ArrayDim](#ArrayDim) [PointerOrArraySuffix]_  

### [TypeName](Semantics.md#TypeName):
&emsp;&emsp;<code>_[[TypeStrictness](#TypeStrictness)|[TypeBareness](#TypeBareness)]_</code>[^low] _Identifier_ <code>_[[Version](#Version)]_</code>[^low] _{_**.** _Identifier_ <code>_[[Version](#Version)]_</code>[^low]_} [_**(** _[[ParameterTypes](#ParameterTypes)]_ **)**_]_  

### [VoidPointerType](Semantics.md#VoidPointerType):
&emsp;&emsp;<code>**unsafe void** _[[ValueMutability](#ValueMutability)] [[ValueVolatility](#ValueVolatility)]_ **&** _[[TypeAtomicity](#TypeAtomicity)] [[ReferenceAliasability](#ReferenceAliasability)] [[PointerNullity](#PointerNullity)]_</code>[^low]  

### [FunctionType](Semantics.md#FunctionType):
&emsp;&emsp;<code>_[[TypeAtomicity](#TypeAtomicity)] [[FunctionStrictness](#FunctionStrictness)]_</code>[^low] _[[FunctionPurity](#FunctionPurity)]_ **func (** _[[ParameterTypes](#ParameterTypes)]_ **) ->** _[Result](#Result)_  

### [PointerNullity](Semantics.md#PointerNullity):
&emsp;&emsp;_[_**local**_]_ **?**  

\---

### [TypeAtomicity](Semantics.md#TypeAtomicity):
&emsp;&emsp;<code>**atomic**</code>[^low]  

### [NumericType](Semantics.md#NumericType):
&emsp;&emsp;_[IntegralType](#IntegralType)_  
&emsp;&emsp;_[FloatingPointType](#FloatingPointType)_  

### [PointerSuffix](Semantics.md#PointerSuffix):
&emsp;&emsp;_[[ValueMutability](#ValueMutability)]_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] **&** <code>_[[PointerWidth](#PointerWidth)|[TypeAtomicity](#TypeAtomicity)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low] _[[PointerNullity](#PointerNullity)]_  

### [ArrayDim](Semantics.md#ArrayDim):
&emsp;&emsp;**[** _(_<code>_[[TypeStrictness](#TypeStrictness)]_</code>[^low] _[Expression]|_<code>_[TypeBareness](#TypeBareness)_</code>[^low]_)_ **]** _[[PointerNullity](#PointerNullity)]_  

### [TypeStrictness](Semantics.md#TypeStrictness):
&emsp;&emsp;<code>**strict**</code>[^low]  

### [ParameterTypes](Semantics.md#ParameterTypes):
&emsp;&emsp;_[ThisParameter](#ThisParameter) [_**,** _[FixedParameterTypes](#FixedParameterTypes)] [_**,** _[VariableArityParameterType](#VariableArityParameterType)]_  
&emsp;&emsp;_[FixedParameterTypes](#FixedParameterTypes) [_**,** _[VariableArityParameterType](#VariableArityParameterType)]_  
&emsp;&emsp;_[VariableArityParameterType](#VariableArityParameterType)_  

### [TypeBareness](Semantics.md#TypeBareness):
&emsp;&emsp;<code>**unsafe bare**</code>[^low]  

### [FunctionStrictness](Semantics.md#FunctionStrictness):
&emsp;&emsp;<code>**strict**</code>[^low]  

### [FunctionPurity](Semantics.md#FunctionPurity):
&emsp;&emsp;_[_**local**_]_ **const**  
&emsp;&emsp;_[_**local**_]_ **pure**  

### [Result](Semantics.md#Result):
&emsp;&emsp;**noreturn**  
&emsp;&emsp;**void**  
&emsp;&emsp;_[Type](#Type)_  

\---

### [IntegralType](Semantics.md#IntegralType):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;<code>**\_ubyte \_byte \_ushort \_short \_uint**</code>[^low] **\_int** <code>**\_ulong \_long**</code>[^low]  

### [FloatingPointType](Semantics.md#FloatingPointType):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**\_float** <code>**\_double**</code>[^low]  

### [ValueMutability](Semantics.md#ValueMutability):
&emsp;&emsp;_[_**unsafe**_]_ **var**  
&emsp;&emsp;_[_**local**_]_ **const**  

### [ValueVolatility](Semantics.md#ValueVolatility):
&emsp;&emsp;<code>_[_**local**_]_ **volatile**</code>[^low]  
&emsp;&emsp;<code>_[_**unsafe**_]_ **stable**</code>[^low]  

### [PointerWidth](Semantics.md#PointerWidth):
&emsp;&emsp;<code>_[[_**unsafe**_]_ **unused**_] [[TypeStrictness](#TypeStrictness)]_ **wide**</code>[^low]  
&emsp;&emsp;<code>_[TypeBareness](#TypeBareness)_</code>[^low]  

### [ReferenceAliasability](Semantics.md#ReferenceAliasability):
&emsp;&emsp;<code>_[_**local**_]_ **aliasable**</code>[^low]  
&emsp;&emsp;<code>_[_**unsafe**_]_ **restrict**</code>[^low]  

### [ThisParameter](Semantics.md#ThisParameter):
&emsp;&emsp;**this** _[_**:** _[TypeName](#TypeName) [[ValueMutability](#ValueMutability)]_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] _[_**&** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]_]]_  
&emsp;&emsp;**this :** _[ValueMutability](#ValueMutability)_ <code>_[[ValueVolatility](#ValueVolatility)]_</code>[^low] _[_**&** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]_]_  
&emsp;&emsp;<code>**this :** _[ValueVolatility](#ValueVolatility) [_**&** _[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]]_</code>[^low]  
&emsp;&emsp;**this : &** <code>_[[PointerWidth](#PointerWidth)] [[ReferenceAliasability](#ReferenceAliasability)]_</code>[^low]  

### [FixedParameterTypes](Semantics.md#FixedParameterTypes):
&emsp;&emsp;_[FixedParameterType](#FixedParameterType) {_**,** _[FixedParameterType](#FixedParameterType)}_  

### [VariableArityParameterType](Semantics.md#VariableArityParameterType):
&emsp;&emsp;**...** <code>_[[VariableArityParameterLayout](#VariableArityParameterLayout)]_</code>[^low] **:** _[Type](#Type)_  

\---

### [FixedParameterType](Semantics.md#FixedParameterType):
&emsp;&emsp;**:** _[Type](#Type)_  

### [VariableArityParameterLayout](Semantics.md#VariableArityParameterLayout):
&emsp;&emsp;<code>**strict**</code>[^low]  
&emsp;&emsp;<code>**unsafe C**</code>[^low]  

## Blocks and Statements
### [Block](Semantics.md#Block):
&emsp;&emsp;**{** _[[BlockStatements](#BlockStatements)]_ **}**  

\---

### [BlockStatements](Semantics.md#BlockStatements):
&emsp;&emsp;_BlockStatement {BlockStatement}_  

## Expressions

## Array and Struct Initializers
### [ArrayInitializer](Semantics.md#ArrayInitializer):
&emsp;&emsp;**[** _[[VariableInitializers](#VariableInitializers)]_ **]** _[_**:** _[Type](#Type)]_  

### [StructInitializer](Semantics.md#StructInitializer):
&emsp;&emsp;**{** _[[FieldInitializers](#FieldInitializers)]_ **}** _[_**:** _[TypeName](#TypeName)]_  

\---

### [VariableInitializers](Semantics.md#VariableInitializers):
&emsp;&emsp;_[VariableInitializer](#VariableInitializer) {_**,** _[VariableInitializer](#VariableInitializer)}_  

### [FieldInitializers](Semantics.md#FieldInitializers):
&emsp;&emsp;_[FieldInitializer](#FieldInitializer) {_**,** _[FieldInitializer](#FieldInitializer)}_  

\---

### [FieldInitializer](Semantics.md#FieldInitializer):
&emsp;&emsp;_[_**.**_] Identifier (_**=**_|_**:**_) [VariableInitializer](#VariableInitializer)_  

[^low]: Low level syntax.
