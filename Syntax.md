# Syntax

## [CompilationUnit](Semantics.md#CompilationUnit):
_[_[_PackageDeclaration_](#PackageDeclaration)_]_ _[_[_ImportDeclarations_](#ImportDeclarations)_]_ [_TopLevelTypeDeclaration_](#TopLevelTypeDeclaration)  

---

## [PackageDeclaration](Semantics.md#PackageDeclaration):
**package** [_PackageName_](#PackageName) _[_**;**_]_  

## [ImportDeclarations](Semantics.md#ImportDeclarations):
[_ImportDeclaration_](#ImportDeclaration) _{_[_ImportDeclaration_](#ImportDeclaration)_}_  

## [TopLevelTypeDeclaration](Semantics.md#TopLevelTypeDeclaration):
_[_[_TopLevelEncapsulation_](#TopLevelEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

---

## [PackageName](Semantics.md#PackageName):
_Identifier_ _{_**.** _Identifier_*}*  

## [ImportDeclaration](Semantics.md#ImportDeclaration):
[_ExplicitTypeImportDeclaration_](#ExplicitTypeImportDeclaration)  
[_TypeImportOnDemandDeclaration_](#TypeImportOnDemandDeclaration)  

## [TopLevelEncapsulation](Semantics.md#TopLevelEncapsulation):
**public**  

## [TypeDeclaration](Semantics.md#TypeDeclaration):
[_TypedefDeclaration_](#TypedefDeclaration) _[_**;**_]_  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  

> TypedefBody and the semicolon after TypedefDeclaration are mutually exclusive, and exactly one of them must always be found in rule 1.

---

## [ExplicitTypeImportDeclaration](Semantics.md#ExplicitTypeImportDeclaration):
**import** [_ImportNames_](#ImportNames) _[_**from** [_PackageOrTypeName_](#PackageOrTypeName)_]_ _[_**;**_]_  

## [TypeImportOnDemandDeclaration](Semantics.md#TypeImportOnDemandDeclaration):
**import** **\*** **from** [_PackageOrTypeName_](#PackageOrTypeName) _[_**;**_]_  

## [TypedefDeclaration](Semantics.md#TypedefDeclaration):
**typedef** _Identifier_ [_BaseType_](#BaseType) _[_[_TypedefBody_](#TypedefBody)_]_  

## [EnumDeclaration](Semantics.md#EnumDeclaration):
**enum** _Identifier_ _[_[_BaseType_](#BaseType)_]_ [_EnumBody_](#EnumBody)  

## [UnionDeclaration](Semantics.md#UnionDeclaration):
**union** _Identifier_ [_UnionBody_](#UnionBody)  

## [StructDeclaration](Semantics.md#StructDeclaration):
_[_[_StructExtensibility_](#StructExtensibility)_]_ _[_[_StructLayout_](#StructLayout)_]_ **struct** _Identifier_ _[_[_BaseType_](#BaseType)_]_ [_StructBody_](#StructBody)  

---

## [ImportNames](Semantics.md#ImportNames):
[_ImportName_](#ImportName) _{_**,** [_ImportName_](#ImportName)_}_  

## [PackageOrTypeName](Semantics.md#PackageOrTypeName):
_Identifier_ _{_**.** _Identifier_*}*  

## [BaseType](Semantics.md#BaseType):
**:** [_Type_](#Type)  

## [TypedefBody](Semantics.md#TypedefBody):
**{** [_BodyDeclarations_](#BodyDeclarations) **}**  

## [EnumBody](Semantics.md#EnumBody):
**{** [_EnumConstants_](#EnumConstants) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

## [UnionBody](Semantics.md#UnionBody):
**{** [_UnionTypes_](#UnionTypes) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

## [StructExtensibility](Semantics.md#StructExtensibility):
_(one of)_  
**open** **abstract**  

## [StructLayout](Semantics.md#StructLayout):
_(one of)_  
**ordered** **packed**  

## [StructBody](Semantics.md#StructBody):
**{** _[_[_StructBodyDeclarations_](#StructBodyDeclarations)_]_ **}**  

---

## [ImportName](Semantics.md#ImportName):
_Identifier_ _[_**as** _Identifier_*]*  

## [Type](Semantics.md#Type):
[_PrimitiveType_](#PrimitiveType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_TypeName_](#TypeName) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_VoidPointerType_](#VoidPointerType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_FunctionType_](#FunctionType)  
**(** [_FunctionType_](#FunctionType) **)** [_PointerOrArraySuffix_](#PointerOrArraySuffix)  

## [BodyDeclarations](Semantics.md#BodyDeclarations):
[_BodyDeclaration_](#BodyDeclaration) _{_[_BodyDeclaration_](#BodyDeclaration)_}_  

## [EnumConstants](Semantics.md#EnumConstants):
[_EnumConstant_](#EnumConstant) _{_**,** [_EnumConstant_](#EnumConstant)_}_  

## [UnionTypes](Semantics.md#UnionTypes):
[_UnionType_](#UnionType) _{_**,** [_UnionType_](#UnionType)_}_  

## [StructBodyDeclarations](Semantics.md#StructBodyDeclarations):
[_StructBodyDeclaration_](#StructBodyDeclaration) _{_[_StructBodyDeclaration_](#StructBodyDeclaration)_}_  

---

## [PrimitiveType](Semantics.md#PrimitiveType):
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ [_NumericType_](#NumericType)  
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ **bool**  
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ **\_char**  

## [PointerOrArraySuffix](Semantics.md#PointerOrArraySuffix):
[_PointerSuffix_](#PointerSuffix) *[*_PointerOrArraySuffix_*]*  
[_ArrayDim_](#ArrayDim) *[*_PointerOrArraySuffix_*]*  

## [TypeName](Semantics.md#TypeName):
_[_**unsafe** **bare**_]_ _Identifier_ _{_**.** _Identifier_*}*  

## [VoidPointerType](Semantics.md#VoidPointerType):
**unsafe** **void** **&** _[_[_TypeAtomicity_](#TypeAtomicity)_]_  

## [FunctionType](Semantics.md#FunctionType):
_[_[_TypeAtomicity_](#TypeAtomicity)_]_ **(** _[_[_ParameterTypes_](#ParameterTypes)_]_ **)** **->** [_Result_](#Result)  

## [BodyDeclaration](Semantics.md#BodyDeclaration):
[_StaticInitializer_](#StaticInitializer)  
_[_[_NestedEncapsulation_](#NestedEncapsulation)_]_ [_MemberDeclaration_](#MemberDeclaration)  
_[_[_NestedEncapsulation_](#NestedEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

## [EnumConstant](Semantics.md#EnumConstant):
_Identifier_ _[_**=** [_VariableInitializer_](#VariableInitializer)_]_  

## [UnionType](Semantics.md#UnionType):
[_TypedefDeclaration_](#TypedefDeclaration)  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  

## [StructBodyDeclaration](Semantics.md#StructBodyDeclaration):
[_StaticInitializer_](#StaticInitializer)  
_[_[_StructNestedEncapsulation_](#StructNestedEncapsulation)_]_ [_StructMemberDeclaration_](#StructMemberDeclaration)  
_[_[_StructNestedEncapsulation_](#StructNestedEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

---

## [TypeAtomicity](Semantics.md#TypeAtomicity):
**atomic**  

## [NumericType](Semantics.md#NumericType):
[_IntegralType_](#IntegralType)  
[_FloatingPointType_](#FloatingPointType)  

## [PointerSuffix](Semantics.md#PointerSuffix):
_[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  
_[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** [_TypeAtomicity_](#TypeAtomicity) _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  

## [ArrayDim](Semantics.md#ArrayDim):
**[** _[_[_ArrayLayout_](#ArrayLayout)_]_ *[*_NumberLiteral_*]* **]**  
**[** _[_[_ArrayLayout_](#ArrayLayout)_]_ _Identifier_ **]**  
**[** _[_[_ArrayLayout_](#ArrayLayout)_]_ [_ArrayBareness_](#ArrayBareness) **]**  

## [ParameterTypes](Semantics.md#ParameterTypes):
[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameterTypes_](#FixedParameterTypes)_]_ _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
[_FixedParameterTypes_](#FixedParameterTypes) _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
[_VariableArityParameterType_](#VariableArityParameterType)  

## [Result](Semantics.md#Result):
**noreturn**  
**void**  
[_Type_](#Type)  

## [StaticInitializer](Semantics.md#StaticInitializer):
**static** *[*_StringIdentifier_*]* [_Block_](#Block)  

## [NestedEncapsulation](Semantics.md#NestedEncapsulation):
_(one of)_  
**public** **private**  

## [MemberDeclaration](Semantics.md#MemberDeclaration):
[_FieldDeclaration_](#FieldDeclaration)  
[_MethodDeclaration_](#MethodDeclaration)  

## [VariableInitializer](Semantics.md#VariableInitializer):
_Expression_  
[_ArrayInitializer_](#ArrayInitializer)  
[_StructInitializer_](#StructInitializer)  

## [StructNestedEncapsulation](Semantics.md#StructNestedEncapsulation):
_(one of)_  
**public** **protected** **private**  

## [StructMemberDeclaration](Semantics.md#StructMemberDeclaration):
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_FieldDeclaration_](#FieldDeclaration)  
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_MethodDeclaration_](#MethodDeclaration)  

---

## [IntegralType](Semantics.md#IntegralType):
_(one of)_  
**\_ubyte** **\_byte** **\_ushort** **\_short** **\_uint** **\_int** **\_ulong** **\_long**  

## [FloatingPointType](Semantics.md#FloatingPointType):
_(one of)_  
**\_float** **\_double**  

## [ValueMutability](Semantics.md#ValueMutability):
_[_**unused**_]_ **var**  

## [ValueVolatility](Semantics.md#ValueVolatility):
_[_**local**_]_ **volatile**  

## [PointerWidth](Semantics.md#PointerWidth):
_[_**unused**_]_ **wide**  
**unsafe** **bare**  

## [ReferenceAliasability](Semantics.md#ReferenceAliasability):
_[_**local**_]_ **aliasable**  

## [ArrayLayout](Semantics.md#ArrayLayout):
**packed**  

## [ArrayBareness](Semantics.md#ArrayBareness):
**unsafe** **bare**  

## [ThisParameter](Semantics.md#ThisParameter):
**this** _[_**:** [_TypeName_](#TypeName) _[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_*]*_]_  
**this** **:** [_ValueMutability_](#ValueMutability) _[_[_ValueVolatility_](#ValueVolatility)_]_ _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_*]*  
**this** **:** [_ValueVolatility_](#ValueVolatility) _[_**&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_*]*  
**this** **:** **&** _[_[_PointerWidth_](#PointerWidth)_]_ _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_  

## [FixedParameterTypes](Semantics.md#FixedParameterTypes):
[_FixedParameterType_](#FixedParameterType) _{_**,** [_FixedParameterType_](#FixedParameterType)_}_  

## [VariableArityParameterType](Semantics.md#VariableArityParameterType):
**...** **:** [_Type_](#Type)  

## [Block](Semantics.md#Block):
**{** _[_[_BlockStatements_](#BlockStatements)_]_ **}**  

## [FieldDeclaration](Semantics.md#FieldDeclaration):
[_FieldMutability_](#FieldMutability) _[_[_FieldVolatility_](#FieldVolatility)_]_ _Identifier_ *[*_StringIdentifier_*]* **:** [_Type_](#Type) _[_**=** [_VariableInitializer_](#VariableInitializer)_]_ **;**  

## [MethodDeclaration](Semantics.md#MethodDeclaration):
_[_[_MethodExtensibility_](#MethodExtensibility)_]_ _[_[_MethodOverride_](#MethodOverride)_]_ **func** [_MethodHeader_](#MethodHeader) [_MethodBody_](#MethodBody)  

## [ArrayInitializer](Semantics.md#ArrayInitializer):
**[** _[_[_VariableInitializers_](#VariableInitializers)_]_ **]**  

## [StructInitializer](Semantics.md#StructInitializer):
**{** _[_[_FieldInitializers_](#FieldInitializers)_]_ **}**  

## [MemberStaticity](Semantics.md#MemberStaticity):
**static**  

---

## [FixedParameterType](Semantics.md#FixedParameterType):
**:** [_Type_](#Type)  

## [BlockStatements](Semantics.md#BlockStatements):
_BlockStatement_ *{*_BlockStatement_*}*  

## [FieldMutability](Semantics.md#FieldMutability):
_(one of)_  
**var** **const**  

## [FieldVolatility](Semantics.md#FieldVolatility):
**volatile**  

## [MethodExtensibility](Semantics.md#MethodExtensibility):
_(one of)_  
**open** **abstract**  

## [MethodOverride](Semantics.md#MethodOverride):
**override**  

## [MethodHeader](Semantics.md#MethodHeader):
[_MethodDeclarator_](#MethodDeclarator) _[_**->** [_Result_](#Result)_]_  

## [MethodBody](Semantics.md#MethodBody):
[_Block_](#Block)  
**;**  

## [VariableInitializers](Semantics.md#VariableInitializers):
[_VariableInitializer_](#VariableInitializer) _{_**,** [_VariableInitializer_](#VariableInitializer)_}_  

## [FieldInitializers](Semantics.md#FieldInitializers):
[_FieldInitializer_](#FieldInitializer) _{_**,** [_FieldInitializer_](#FieldInitializer)_}_  

---

## [MethodDeclarator](Semantics.md#MethodDeclarator):
_Identifier_ *[*_StringIdentifier_*]* _[_**:** [_TypeName_](#TypeName)_]_ **(** _[_[_Parameters_](#Parameters)_]_ **)**  

## [FieldInitializer](Semantics.md#FieldInitializer):
_Identifier_ **=** [_VariableInitializer_](#VariableInitializer)  

---

## [Parameters](Semantics.md#Parameters):
[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameters_](#FixedParameters)_]_ _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_FixedParameters_](#FixedParameters) _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_VariableArityParameter_](#VariableArityParameter)  

---

## [FixedParameters](Semantics.md#FixedParameters):
[_FixedParameter_](#FixedParameter) _{_**,** [_FixedParameter_](#FixedParameter)_}_  

## [VariableArityParameter](Semantics.md#VariableArityParameter):
**...** _Identifier_ _[_**:** [_Type_](#Type)_]_  

---

## [FixedParameter](Semantics.md#FixedParameter):
_Identifier_ _[_**:** [_Type_](#Type)_]_  
