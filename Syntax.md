# Syntax
## Packages
### [CompilationUnit](Semantics.md#CompilationUnit):
&emsp;&emsp;_[_[_PackageDeclaration_](#PackageDeclaration)_] [_[_ImportDeclarations_](#ImportDeclarations)_]_ [_TopLevelTypeDeclaration_](#TopLevelTypeDeclaration)  

\---

### [PackageDeclaration](Semantics.md#PackageDeclaration):
&emsp;&emsp;**package** [_PackageName_](#PackageName) _[_**;**_]_  

### [ImportDeclarations](Semantics.md#ImportDeclarations):
&emsp;&emsp;[_ImportDeclaration_](#ImportDeclaration) _{_[_ImportDeclaration_](#ImportDeclaration)_}_  

### [TopLevelTypeDeclaration](Semantics.md#TopLevelTypeDeclaration):
&emsp;&emsp;_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

\---

### [ImportDeclaration](Semantics.md#ImportDeclaration):
&emsp;&emsp;**import** [_ImportNames_](#ImportNames) _[_[_FromName_](#FromName)_] [_**;**_]_  

### [DeclarationEncapsulation](Semantics.md#DeclarationEncapsulation):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**public protected private**  

### [TypeDeclaration](Semantics.md#TypeDeclaration):
&emsp;&emsp;[_TypedefDeclaration_](#TypedefDeclaration)  
&emsp;&emsp;[_EnumDeclaration_](#EnumDeclaration)  
&emsp;&emsp;[_UnionDeclaration_](#UnionDeclaration)  
&emsp;&emsp;[_StructDeclaration_](#StructDeclaration)  

\---

### [ImportNames](Semantics.md#ImportNames):
&emsp;&emsp;[_ImportName_](#ImportName) _{_**,** [_ImportName_](#ImportName)_}_  

### [FromName](Semantics.md#FromName):
&emsp;&emsp;**from** [_PackageOrTypeName_](#PackageOrTypeName)  

## Names
### [PackageName](Semantics.md#PackageName):
&emsp;&emsp;_Identifier {_**.** _Identifier}_ <code>_[_[_Version_](#Version)_]_</code>[^low]  

### [ImportName](Semantics.md#ImportName):
&emsp;&emsp;_Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] _[_**as** _Identifier]_  

### [PackageOrTypeName](Semantics.md#PackageOrTypeName):
&emsp;&emsp;_Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] _{_**.** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low]_}_  

## Typedefs, Enums, Unions and Structs
### [TypedefDeclaration](Semantics.md#TypedefDeclaration):
&emsp;&emsp;**typedef** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] [_BaseType_](#BaseType) _[_[_TypedefBody_](#TypedefBody)_]_  

### [EnumDeclaration](Semantics.md#EnumDeclaration):
&emsp;&emsp;<code>_[_[_EnumLayout_](#EnumLayout)_]_</code>[^low] **enum** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] _[_[_BaseType_](#BaseType)_]_ [_EnumBody_](#EnumBody)  

### [UnionDeclaration](Semantics.md#UnionDeclaration):
&emsp;&emsp;**union** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] [_UnionBody_](#UnionBody)  

### [StructDeclaration](Semantics.md#StructDeclaration):
&emsp;&emsp;_[_[_DeclarationExtensibility_](#DeclarationExtensibility)_]_ <code>_[_[_StructLayout_](#StructLayout)_]_</code>[^low] **struct** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] _[_[_BaseType_](#BaseType)_]_ [_StructBody_](#StructBody)  

\---

### [Version](Semantics.md#Version):
&emsp;&emsp;<code>**@** _IntegerLiteral_ **.** _IntegerLiteral_</code>[^low]  

### [BaseType](Semantics.md#BaseType):
&emsp;&emsp;**:** [_Type_](#Type)  

### [TypedefBody](Semantics.md#TypedefBody):
&emsp;&emsp;**{** [_BodyDeclarations_](#BodyDeclarations) **}**  
&emsp;&emsp;**;**  

### [EnumLayout](Semantics.md#EnumLayout):
&emsp;&emsp;<code>**strict**</code>[^low]  
&emsp;&emsp;<code>**unsafe C**</code>[^low]  

### [EnumBody](Semantics.md#EnumBody):
&emsp;&emsp;**{** [_EnumConstants_](#EnumConstants) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

### [UnionBody](Semantics.md#UnionBody):
&emsp;&emsp;**{** [_UnionTypes_](#UnionTypes) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

### [DeclarationExtensibility](Semantics.md#DeclarationExtensibility):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;**open abstract**  

### [StructLayout](Semantics.md#StructLayout):
&emsp;&emsp;_(one of)_  
&emsp;&emsp;<code>**strict C packed**</code>[^low]  

### [StructBody](Semantics.md#StructBody):
&emsp;&emsp;**{** _[_[_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

\---

### [BodyDeclarations](Semantics.md#BodyDeclarations):
&emsp;&emsp;[_BodyDeclaration_](#BodyDeclaration) _{_[_BodyDeclaration_](#BodyDeclaration)_}_  

### [EnumConstants](Semantics.md#EnumConstants):
&emsp;&emsp;[_EnumConstant_](#EnumConstant) _{_**,** [_EnumConstant_](#EnumConstant)_}_  

### [UnionTypes](Semantics.md#UnionTypes):
&emsp;&emsp;[_TypeDeclaration_](#TypeDeclaration) _{_**,** [_TypeDeclaration_](#TypeDeclaration)_}_  

> The semicolon in TypedefBody must never be found in TypedefDeclaration.

\---

### [BodyDeclaration](Semantics.md#BodyDeclaration):
&emsp;&emsp;[_StaticInitializer_](#StaticInitializer)  
&emsp;&emsp;_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_MemberDeclaration_](#MemberDeclaration)  
&emsp;&emsp;_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

> TypedefBody must always be found in TypedefDeclaration.

### [EnumConstant](Semantics.md#EnumConstant):
&emsp;&emsp;_[_**.**_] Identifier [_**=** [_VariableInitializer_](#VariableInitializer)_]_  
&emsp;&emsp;_[_**.**_] Identifier_ **:** [_VariableInitializer_](#VariableInitializer)  

\---

### [StaticInitializer](Semantics.md#StaticInitializer):
&emsp;&emsp;<code>_[_[_NameStrictness_](#NameStrictness)_]_</code>[^low] **static** <code>_[_[_Version_](#Version)_] [StringIdentifier]_</code>[^low] [_Block_](#Block)  

### [MemberDeclaration](Semantics.md#MemberDeclaration):
&emsp;&emsp;_[_[_MemberStaticity_](#MemberStaticity)_]_ [_FieldDeclaration_](#FieldDeclaration)  
&emsp;&emsp;_[_[_MemberStaticity_](#MemberStaticity)_]_ [_MethodDeclaration_](#MethodDeclaration)  

### [VariableInitializer](Semantics.md#VariableInitializer):
&emsp;&emsp;_Expression_  
&emsp;&emsp;[_ArrayInitializer_](#ArrayInitializer)  
&emsp;&emsp;[_StructInitializer_](#StructInitializer)  

\---

### [NameStrictness](Semantics.md#NameStrictness):
&emsp;&emsp;<code>**strict**</code>[^low]  

### [MemberStaticity](Semantics.md#MemberStaticity):
&emsp;&emsp;**static**  

### [FieldDeclaration](Semantics.md#FieldDeclaration):
&emsp;&emsp;[_ValueMutability_](#ValueMutability) <code>_[_[_ValueVolatility_](#ValueVolatility)_] [_[_NameStrictness_](#NameStrictness)_]_</code>[^low] _Identifier_ <code>_[StringIdentifier]_</code>[^low] **:** [_Type_](#Type) _[_**=** [_VariableInitializer_](#VariableInitializer)_]_ **;**  

### [MethodDeclaration](Semantics.md#MethodDeclaration):
&emsp;&emsp;_[_[_DeclarationExtensibility_](#DeclarationExtensibility)_] [_[_MethodOverride_](#MethodOverride)_]_ <code>_[_[_FunctionStrictness_](#FunctionStrictness)_]_</code>[^low] _[_[_FunctionPurity_](#FunctionPurity)_]_ **func** [_MethodHeader_](#MethodHeader) [_MethodBody_](#MethodBody)  

\---

### [MethodOverride](Semantics.md#MethodOverride):
&emsp;&emsp;**override**  

### [MethodHeader](Semantics.md#MethodHeader):
&emsp;&emsp;[_MethodDeclarator_](#MethodDeclarator) _[_**->** [_Result_](#Result)_]_  

### [MethodBody](Semantics.md#MethodBody):
&emsp;&emsp;[_Block_](#Block)  
&emsp;&emsp;**;**  

\---

### [MethodDeclarator](Semantics.md#MethodDeclarator):
&emsp;&emsp;<code>_[_[_NameStrictness_](#NameStrictness)_]_</code>[^low] _Identifier_ <code>_[_[_Version_](#Version)_] [StringIdentifier]_</code>[^low] _[_**:** [_TypeName_](#TypeName)_]_ **(** _[_[_Parameters_](#Parameters)_]_ **)**  

\---

### [Parameters](Semantics.md#Parameters):
&emsp;&emsp;[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameters_](#FixedParameters)_] [_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
&emsp;&emsp;[_FixedParameters_](#FixedParameters) _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
&emsp;&emsp;[_VariableArityParameter_](#VariableArityParameter)  

\---

### [FixedParameters](Semantics.md#FixedParameters):
&emsp;&emsp;[_FixedParameter_](#FixedParameter) _{_**,** [_FixedParameter_](#FixedParameter)_}_  

### [VariableArityParameter](Semantics.md#VariableArityParameter):
&emsp;&emsp;**...** <code>_[_[_VariableArityParameterLayout_](#VariableArityParameterLayout)_]_</code>[^low] _Identifier [_**:** [_Type_](#Type)_]_  

\---

### [FixedParameter](Semantics.md#FixedParameter):
&emsp;&emsp;_Identifier [_**:** [_Type_](#Type)_]_  

## Types
### [Type](Semantics.md#Type):
&emsp;&emsp;[_PrimitiveType_](#PrimitiveType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
&emsp;&emsp;[_TypeName_](#TypeName) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
&emsp;&emsp;<code>[_VoidPointerType_](#VoidPointerType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_</code>[^low]  
&emsp;&emsp;[_FunctionType_](#FunctionType)  
&emsp;&emsp;**(** [_FunctionType_](#FunctionType) **)** [_PointerNullity_](#PointerNullity)  
&emsp;&emsp;**(** [_FunctionType_](#FunctionType) **)** [_PointerOrArraySuffix_](#PointerOrArraySuffix)  

\---

### [PrimitiveType](Semantics.md#PrimitiveType):
&emsp;&emsp;<code>_[_[_TypeAtomicity_](#TypeAtomicity)_]_</code>[^low] [_NumericType_](#NumericType)  
&emsp;&emsp;<code>_[_[_TypeAtomicity_](#TypeAtomicity)_]_</code>[^low] **bool**  
&emsp;&emsp;<code>_[_[_TypeAtomicity_](#TypeAtomicity)_]_</code>[^low] **\_char**  

### [PointerOrArraySuffix](Semantics.md#PointerOrArraySuffix):
&emsp;&emsp;[_PointerSuffix_](#PointerSuffix) _[PointerOrArraySuffix]_  
&emsp;&emsp;[_ArrayDim_](#ArrayDim) _[PointerOrArraySuffix]_  

### [TypeName](Semantics.md#TypeName):
&emsp;&emsp;<code>_[_[_TypeStrictness_](#TypeStrictness)_]_</code>[^low] _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low] _{_**.** _Identifier_ <code>_[_[_Version_](#Version)_]_</code>[^low]_} [_**(** _[_[_ParameterTypes_](#ParameterTypes)_]_ **)**_]_  
&emsp;&emsp;<code>[_TypeBareness_](#TypeBareness) _Identifier [_[_Version_](#Version)_] {_**.** _Identifier [_[_Version_](#Version)_]} [_**(** _[_[_ParameterTypes_](#ParameterTypes)_]_ **)**_]_</code>[^low]  

### [VoidPointerType](Semantics.md#VoidPointerType):
&emsp;&emsp;<code>**unsafe void** _[_[_ValueMutability_](#ValueMutability)_] [_[_ValueVolatility_](#ValueVolatility)_]_ **&** _[_[_TypeAtomicity_](#TypeAtomicity)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_] [_[_PointerNullity_](#PointerNullity)_]_</code>[^low]  

### [FunctionType](Semantics.md#FunctionType):
&emsp;&emsp;<code>_[_[_TypeAtomicity_](#TypeAtomicity)_] [_[_FunctionStrictness_](#FunctionStrictness)_]_</code>[^low] _[_[_FunctionPurity_](#FunctionPurity)_]_ **func (** _[_[_ParameterTypes_](#ParameterTypes)_]_ **) ->** [_Result_](#Result)  
&emsp;&emsp;<code>_[_[_TypeAtomicity_](#TypeAtomicity)_] [_[_FunctionStrictness_](#FunctionStrictness)_]_</code>[^low] _[_[_FunctionPurity_](#FunctionPurity)_]_ **func** _[_[_ParameterTypes_](#ParameterTypes)_]_ **->** [_Result_](#Result)  

### [PointerNullity](Semantics.md#PointerNullity):
&emsp;&emsp;_[_**local**_]_ **?**  

\---

### [TypeAtomicity](Semantics.md#TypeAtomicity):
&emsp;&emsp;<code>**atomic**</code>[^low]  

### [NumericType](Semantics.md#NumericType):
&emsp;&emsp;[_IntegralType_](#IntegralType)  
&emsp;&emsp;[_FloatingPointType_](#FloatingPointType)  

### [PointerSuffix](Semantics.md#PointerSuffix):
&emsp;&emsp;_[_[_ValueMutability_](#ValueMutability)_]_ <code>_[_[_ValueVolatility_](#ValueVolatility)_]_</code>[^low] **&** <code>_[_[_PointerWidth_](#PointerWidth)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_]_</code>[^low] _[_[_PointerNullity_](#PointerNullity)_]_  
&emsp;&emsp;<code>_[_[_ValueMutability_](#ValueMutability)_] [_[_ValueVolatility_](#ValueVolatility)_]_ **&** [_TypeAtomicity_](#TypeAtomicity) _[_[_ReferenceAliasability_](#ReferenceAliasability)_] [_[_PointerNullity_](#PointerNullity)_]_</code>[^low]  

### [ArrayDim](Semantics.md#ArrayDim):
&emsp;&emsp;**[** <code>_[_[_TypeStrictness_](#TypeStrictness)_]_</code>[^low] _[Expression]_ **]** _[_[_PointerNullity_](#PointerNullity)_]_  
&emsp;&emsp;<code>**[** [_TypeBareness_](#TypeBareness) **]** _[_[_PointerNullity_](#PointerNullity)_]_</code>[^low]  

### [TypeStrictness](Semantics.md#TypeStrictness):
&emsp;&emsp;<code>**strict**</code>[^low]  

### [ParameterTypes](Semantics.md#ParameterTypes):
&emsp;&emsp;[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameterTypes_](#FixedParameterTypes)_] [_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
&emsp;&emsp;[_FixedParameterTypes_](#FixedParameterTypes) _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
&emsp;&emsp;[_VariableArityParameterType_](#VariableArityParameterType)  

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
&emsp;&emsp;[_Type_](#Type)  

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
&emsp;&emsp;<code>_[[_**unsafe**_]_ **unused**_] [_[_TypeStrictness_](#TypeStrictness)_]_ **wide**</code>[^low]  
&emsp;&emsp;<code>[_TypeBareness_](#TypeBareness)</code>[^low]  

### [ReferenceAliasability](Semantics.md#ReferenceAliasability):
&emsp;&emsp;<code>_[_**local**_]_ **aliasable**</code>[^low]  
&emsp;&emsp;<code>_[_**unsafe**_]_ **restrict**</code>[^low]  

### [ThisParameter](Semantics.md#ThisParameter):
&emsp;&emsp;**this** _[_**:** [_TypeName_](#TypeName) _[_[_ValueMutability_](#ValueMutability)_]_ <code>_[_[_ValueVolatility_](#ValueVolatility)_]_</code>[^low] _[_**&** <code>_[_[_PointerWidth_](#PointerWidth)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_]_</code>[^low]_]]_  
&emsp;&emsp;**this :** [_ValueMutability_](#ValueMutability) <code>_[_[_ValueVolatility_](#ValueVolatility)_]_</code>[^low] _[_**&** <code>_[_[_PointerWidth_](#PointerWidth)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_]_</code>[^low]_]_  
&emsp;&emsp;<code>**this :** [_ValueVolatility_](#ValueVolatility) _[_**&** _[_[_PointerWidth_](#PointerWidth)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_]]_</code>[^low]  
&emsp;&emsp;**this : &** <code>_[_[_PointerWidth_](#PointerWidth)_] [_[_ReferenceAliasability_](#ReferenceAliasability)_]_</code>[^low]  

### [FixedParameterTypes](Semantics.md#FixedParameterTypes):
&emsp;&emsp;[_FixedParameterType_](#FixedParameterType) _{_**,** [_FixedParameterType_](#FixedParameterType)_}_  

### [VariableArityParameterType](Semantics.md#VariableArityParameterType):
&emsp;&emsp;**...** <code>_[_[_VariableArityParameterLayout_](#VariableArityParameterLayout)_]_</code>[^low] **:** [_Type_](#Type)  

\---

### [FixedParameterType](Semantics.md#FixedParameterType):
&emsp;&emsp;**:** [_Type_](#Type)  

### [VariableArityParameterLayout](Semantics.md#VariableArityParameterLayout):
&emsp;&emsp;<code>**unsafe C**</code>[^low]  

## Blocks and Statements
### [Block](Semantics.md#Block):
&emsp;&emsp;**{** _[_[_BlockStatements_](#BlockStatements)_]_ **}**  

\---

### [BlockStatements](Semantics.md#BlockStatements):
&emsp;&emsp;_BlockStatement {BlockStatement}_  

## Expressions

## Array and Struct Initializers
### [ArrayInitializer](Semantics.md#ArrayInitializer):
&emsp;&emsp;**[** _[_[_VariableInitializers_](#VariableInitializers)_]_ **]** _[_**:** [_Type_](#Type)_]_  

### [StructInitializer](Semantics.md#StructInitializer):
&emsp;&emsp;**{** _[_[_FieldInitializers_](#FieldInitializers)_]_ **}** _[_**:** [_TypeName_](#TypeName)_]_  

\---

### [VariableInitializers](Semantics.md#VariableInitializers):
&emsp;&emsp;[_VariableInitializer_](#VariableInitializer) _{_**,** [_VariableInitializer_](#VariableInitializer)_}_  

### [FieldInitializers](Semantics.md#FieldInitializers):
&emsp;&emsp;[_FieldInitializer_](#FieldInitializer) _{_**,** [_FieldInitializer_](#FieldInitializer)_}_  

\---

### [FieldInitializer](Semantics.md#FieldInitializer):
&emsp;&emsp;_[_**.**_] Identifier_ **=** [_VariableInitializer_](#VariableInitializer)  
&emsp;&emsp;_[_**.**_] Identifier_ **:** [_VariableInitializer_](#VariableInitializer)  

[^low]: Low level syntax.
