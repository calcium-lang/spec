# Syntax
## Packages
### [CompilationUnit](Semantics.md#CompilationUnit):
_[_[_PackageDeclaration_](#PackageDeclaration)_]_ _[_[_ImportDeclarations_](#ImportDeclarations)_]_ [_TopLevelTypeDeclaration_](#TopLevelTypeDeclaration)  

---

### [PackageDeclaration](Semantics.md#PackageDeclaration):
**package** [_PackageName_](#PackageName) _[_**;**_]_  

### [ImportDeclarations](Semantics.md#ImportDeclarations):
[_ImportDeclaration_](#ImportDeclaration) _{_[_ImportDeclaration_](#ImportDeclaration)_}_  

### [TopLevelTypeDeclaration](Semantics.md#TopLevelTypeDeclaration):
_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

---

### [ImportDeclaration](Semantics.md#ImportDeclaration):
[_ExplicitTypeImportDeclaration_](#ExplicitTypeImportDeclaration)  
[_TypeImportOnDemandDeclaration_](#TypeImportOnDemandDeclaration)  

### [DeclarationEncapsulation](Semantics.md#DeclarationEncapsulation):
_(one of)_  
**public** **protected** **private**  

### [TypeDeclaration](Semantics.md#TypeDeclaration):
[_TypedefDeclaration_](#TypedefDeclaration) _[_**;**_]_  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  

> TypedefBody and the semicolon after TypedefDeclaration are mutually exclusive, and exactly one of them must always be found in rule 1.

---

### [ExplicitTypeImportDeclaration](Semantics.md#ExplicitTypeImportDeclaration):
**import** [_ImportNames_](#ImportNames) _[_[_FromName_](#FromName)_]_ _[_**;**_]_  

### [TypeImportOnDemandDeclaration](Semantics.md#TypeImportOnDemandDeclaration):
**import** **\*** [_FromName_](#FromName) _[_**;**_]_  

---

### [ImportNames](Semantics.md#ImportNames):
[_ImportName_](#ImportName) _{_**,** [_ImportName_](#ImportName)_}_  

### [FromName](Semantics.md#FromName):
**from** [_PackageOrTypeName_](#PackageOrTypeName)  

## Names
### [PackageName](Semantics.md#PackageName):
_Identifier_ _{_**.** _Identifier}_  

### [ImportName](Semantics.md#ImportName):
_Identifier_ _[_**as** _Identifier]_  

### [PackageOrTypeName](Semantics.md#PackageOrTypeName):
_Identifier_ _{_**.** _Identifier}_  

## Typedefs, Enums, Unions and Structs
### [TypedefDeclaration](Semantics.md#TypedefDeclaration):
**typedef** _Identifier_ [_BaseType_](#BaseType) _[_[_TypedefBody_](#TypedefBody)_]_  

### [EnumDeclaration](Semantics.md#EnumDeclaration):
**enum** _Identifier_ _[_[_BaseType_](#BaseType)_]_ [_EnumBody_](#EnumBody)  

### [UnionDeclaration](Semantics.md#UnionDeclaration):
**union** _Identifier_ [_UnionBody_](#UnionBody)  

### [StructDeclaration](Semantics.md#StructDeclaration):
_[_[_DeclarationExtensibility_](#DeclarationExtensibility)_]_ _[_[_StructLayout_](#StructLayout)_]_ **struct** _Identifier_ _[_[_BaseType_](#BaseType)_]_ [_StructBody_](#StructBody)  

---

### [BaseType](Semantics.md#BaseType):
**:** [_Type_](#Type)  

### [TypedefBody](Semantics.md#TypedefBody):
**{** [_BodyDeclarations_](#BodyDeclarations) **}**  

### [EnumBody](Semantics.md#EnumBody):
**{** [_EnumConstants_](#EnumConstants) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

### [UnionBody](Semantics.md#UnionBody):
**{** [_UnionTypes_](#UnionTypes) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

### [DeclarationExtensibility](Semantics.md#DeclarationExtensibility):
_(one of)_  
**open** **abstract**  

### [StructLayout](Semantics.md#StructLayout):
_(one of)_  
**ordered** **packed**  

### [StructBody](Semantics.md#StructBody):
**{** _[_[_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

---

### [BodyDeclarations](Semantics.md#BodyDeclarations):
[_BodyDeclaration_](#BodyDeclaration) _{_[_BodyDeclaration_](#BodyDeclaration)_}_  

### [EnumConstants](Semantics.md#EnumConstants):
[_EnumConstant_](#EnumConstant) _{_**,** [_EnumConstant_](#EnumConstant)_}_  

### [UnionTypes](Semantics.md#UnionTypes):
[_UnionType_](#UnionType) _{_**,** [_UnionType_](#UnionType)_}_  

---

### [BodyDeclaration](Semantics.md#BodyDeclaration):
[_StaticInitializer_](#StaticInitializer)  
_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_MemberDeclaration_](#MemberDeclaration)  
_[_[_DeclarationEncapsulation_](#DeclarationEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

### [EnumConstant](Semantics.md#EnumConstant):
_Identifier_ _[_**=** [_VariableInitializer_](#VariableInitializer)_]_  

### [UnionType](Semantics.md#UnionType):
[_TypedefDeclaration_](#TypedefDeclaration)  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  

---

### [StaticInitializer](Semantics.md#StaticInitializer):
**static** _[StringIdentifier]_ [_Block_](#Block)  

### [MemberDeclaration](Semantics.md#MemberDeclaration):
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_FieldDeclaration_](#FieldDeclaration)  
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_MethodDeclaration_](#MethodDeclaration)  

### [VariableInitializer](Semantics.md#VariableInitializer):
_Expression_  
[_ArrayInitializer_](#ArrayInitializer)  
[_StructInitializer_](#StructInitializer)  

---

### [MemberStaticity](Semantics.md#MemberStaticity):
**static**  

### [FieldDeclaration](Semantics.md#FieldDeclaration):
[_ValueMutability_](#ValueMutability) _[_[_ValueVolatility_](#ValueVolatility)_]_ _Identifier_ _[StringIdentifier]_ **:** [_Type_](#Type) _[_**=** [_VariableInitializer_](#VariableInitializer)_]_ **;**  

### [MethodDeclaration](Semantics.md#MethodDeclaration):
_[_[_DeclarationExtensibility_](#DeclarationExtensibility)_]_ _[_[_MethodOverride_](#MethodOverride)_]_ _[_[_FunctionPurity_](#FunctionPurity)_]_ **func** [_MethodHeader_](#MethodHeader) [_MethodBody_](#MethodBody)  

---

### [MethodOverride](Semantics.md#MethodOverride):
**override**  

### [MethodHeader](Semantics.md#MethodHeader):
[_MethodDeclarator_](#MethodDeclarator) _[_**->** [_Result_](#Result)_]_  

### [MethodBody](Semantics.md#MethodBody):
[_Block_](#Block)  
**;**  

---

### [MethodDeclarator](Semantics.md#MethodDeclarator):
_Identifier_ _[StringIdentifier]_ _[_**:** [_TypeName_](#TypeName)_]_ **(** _[_[_Parameters_](#Parameters)_]_ **)**  

---

### [Parameters](Semantics.md#Parameters):
[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameters_](#FixedParameters)_]_ _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_FixedParameters_](#FixedParameters) _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_VariableArityParameter_](#VariableArityParameter)  

---

### [FixedParameters](Semantics.md#FixedParameters):
[_FixedParameter_](#FixedParameter) _{_**,** [_FixedParameter_](#FixedParameter)_}_  

### [VariableArityParameter](Semantics.md#VariableArityParameter):
**...** _Identifier_ _[_**:** [_Type_](#Type)_]_  

---

### [FixedParameter](Semantics.md#FixedParameter):
_Identifier_ _[_**:** [_Type_](#Type)_]_  

## Types
### [Type](Semantics.md#Type):
[_PrimitiveType_](#PrimitiveType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_TypeName_](#TypeName) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_VoidPointerType_](#VoidPointerType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_FunctionType_](#FunctionType)  
**(** [_FunctionType_](#FunctionType) **)** [_PointerOrArraySuffix_](#PointerOrArraySuffix)  

---

### [PrimitiveType](Semantics.md#PrimitiveType):
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ [_NumericType_](#NumericType)  
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ **bool**  
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ **\_char**  

### [PointerOrArraySuffix](Semantics.md#PointerOrArraySuffix):
[_PointerSuffix_](#PointerSuffix) _[PointerOrArraySuffix]_  
[_ArrayDim_](#ArrayDim) _[PointerOrArraySuffix]_  

### [TypeName](Semantics.md#TypeName):
_[_[_TypeBareness_](#TypeBareness)_]_ _Identifier_ _{_**.** _Identifier}_  

### [VoidPointerType](Semantics.md#VoidPointerType):
**unsafe** **void** **&** _[_[_TypeAtomicity_](#TypeAtomicity)_]_  

### [FunctionType](Semantics.md#FunctionType):
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ _[_[_FunctionPurity_](#FunctionPurity)_]_ **(** _[_[_ParameterTypes_](#ParameterTypes)_]_ **)** **->** [_Result_](#Result)  

---

### [TypeAtomicity](Semantics.md#TypeAtomicity):
**atomic**  

### [NumericType](Semantics.md#NumericType):
[_IntegralType_](#IntegralType)  
[_FloatingPointType_](#FloatingPointType)  

### [PointerSuffix](Semantics.md#PointerSuffix):
_[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  
_[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** [_TypeAtomicity_](#TypeAtomicity) _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  

### [ArrayDim](Semantics.md#ArrayDim):
**[** _[Expression]_ **]**  
**[** [_TypeBareness_](#TypeBareness) **]**  

### [TypeBareness](Semantics.md#TypeBareness):
**unsafe** **bare**  

### [FunctionPurity](Semantics.md#FunctionPurity):
_[_**local**_]_ **const**  
_[_**local**_]_ **pure**  

### [ParameterTypes](Semantics.md#ParameterTypes):
[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameterTypes_](#FixedParameterTypes)_]_ _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
[_FixedParameterTypes_](#FixedParameterTypes) _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
[_VariableArityParameterType_](#VariableArityParameterType)  

### [Result](Semantics.md#Result):
**noreturn**  
**void**  
[_Type_](#Type)  

---

### [IntegralType](Semantics.md#IntegralType):
_(one of)_  
**\_ubyte** **\_byte** **\_ushort** **\_short** **\_uint** **\_int** **\_ulong** **\_long**  

### [FloatingPointType](Semantics.md#FloatingPointType):
_(one of)_  
**\_float** **\_double**  

### [ValueMutability](Semantics.md#ValueMutability):
_[_**unused**_]_ **var**  
_[_**local**_]_ **const**  

### [ValueVolatility](Semantics.md#ValueVolatility):
_[_**local**_]_ **volatile**  

### [PointerWidth](Semantics.md#PointerWidth):
_[[_**unsafe**_]_ **unused**_]_ **wide**  
**unsafe** **bare**  

### [ReferenceAliasability](Semantics.md#ReferenceAliasability):
_[_**local**_]_ **aliasable**  

### [ThisParameter](Semantics.md#ThisParameter):
**this** _[_**:** [_TypeName_](#TypeName) _[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]]]_  
**this** **:** [_ValueMutability_](#ValueMutability) _[_[_ValueVolatility_](#ValueVolatility)_]_ _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]]_  
**this** **:** [_ValueVolatility_](#ValueVolatility) _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]]_  
**this** **:** **&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  

### [FixedParameterTypes](Semantics.md#FixedParameterTypes):
[_FixedParameterType_](#FixedParameterType) _{_**,** [_FixedParameterType_](#FixedParameterType)_}_  

### [VariableArityParameterType](Semantics.md#VariableArityParameterType):
**...** **:** [_Type_](#Type)  

---

### [FixedParameterType](Semantics.md#FixedParameterType):
**:** [_Type_](#Type)  

## Blocks and Statements
### [Block](Semantics.md#Block):
**{** _[_[_BlockStatements_](#BlockStatements)_]_ **}**  

---

### [BlockStatements](Semantics.md#BlockStatements):
_BlockStatement_ _{BlockStatement}_  

## Expressions

## Array and Struct Initializers
### [ArrayInitializer](Semantics.md#ArrayInitializer):
**[** _[_[_VariableInitializers_](#VariableInitializers)_]_ **]**  

### [StructInitializer](Semantics.md#StructInitializer):
**{** _[_[_FieldInitializers_](#FieldInitializers)_]_ **}**  

---

### [VariableInitializers](Semantics.md#VariableInitializers):
[_VariableInitializer_](#VariableInitializer) _{_**,** [_VariableInitializer_](#VariableInitializer)_}_  

### [FieldInitializers](Semantics.md#FieldInitializers):
[_FieldInitializer_](#FieldInitializer) _{_**,** [_FieldInitializer_](#FieldInitializer)_}_  

---

### [FieldInitializer](Semantics.md#FieldInitializer):
_Identifier_ **=** [_VariableInitializer_](#VariableInitializer)  
