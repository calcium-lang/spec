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
[_ExplicitImport_](#ExplicitImport)  
[_ImportOnDemand_](#ImportOnDemand)  

## [TopLevelEncapsulation](Semantics.md#TopLevelEncapsulation):
**public**  

## [TypeDeclaration](Semantics.md#TypeDeclaration):
[_TypedefDeclaration_](#TypedefDeclaration) **;**  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  
[_InterfaceDeclaration_](#InterfaceDeclaration)  

---

## [ExplicitImport](Semantics.md#ExplicitImport):
**import** [_ImportNames_](#ImportNames) _[_**from** [_PackageOrTypeName_](#PackageOrTypeName)_]_ _[_**;**_]_  

## [ImportOnDemand](Semantics.md#ImportOnDemand):
**import** **\*** **from** [_PackageOrTypeName_](#PackageOrTypeName) _[_**;**_]_  

## [TypedefDeclaration](Semantics.md#TypedefDeclaration):
**typedef** _Identifier_ [_BaseType_](#BaseType)  

## [EnumDeclaration](Semantics.md#EnumDeclaration):
**enum** _Identifier_ _[_[_BaseType_](#BaseType)_]_ [_EnumBody_](#EnumBody)  

## [UnionDeclaration](Semantics.md#UnionDeclaration):
_[_[_UnionLayout_](#UnionLayout)_]_ _[_[_UnionRawness_](#UnionRawness)_]_ **union** _Identifier_ [_UnionBody_](#UnionBody)  

## [StructDeclaration](Semantics.md#StructDeclaration):
_[_[_StructExtensibility_](#StructExtensibility)_]_ _[_[_StructLayout_](#StructLayout)_]_ **struct** _Identifier_ _[_[_BaseTypes_](#BaseTypes)_]_ [_StructBody_](#StructBody)  

## [InterfaceDeclaration](Semantics.md#InterfaceDeclaration):
**interface** _Identifier_ _[_[_BaseInterfaces_](#BaseInterfaces)_]_ [_InterfaceBody_](#InterfaceBody)  

---

## [ImportNames](Semantics.md#ImportNames):
[_ImportName_](#ImportName) _{_**,** [_ImportName_](#ImportName)_}_  

## [PackageOrTypeName](Semantics.md#PackageOrTypeName):
_Identifier_ _{_**.** _Identifier_*}*  

## [BaseType](Semantics.md#BaseType):
**:** [_Type_](#Type)  

## [EnumBody](Semantics.md#EnumBody):
**{** [_EnumConstants_](#EnumConstants) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

## [UnionLayout](Semantics.md#UnionLayout):
**packed**  

## [UnionRawness](Semantics.md#UnionRawness):
**unsafe** **raw**  

## [UnionBody](Semantics.md#UnionBody):
**{** [_UnionTypes_](#UnionTypes) _[_**;** [_BodyDeclarations_](#BodyDeclarations)_]_ **}**  

## [StructExtensibility](Semantics.md#StructExtensibility):
_(one of)_  
**open** **abstract**  

## [StructLayout](Semantics.md#StructLayout):
**packed**  

## [BaseTypes](Semantics.md#BaseTypes):
**:** [_Type_](#Type) _[_**,** [_TypeNames_](#TypeNames)_]_  

## [StructBody](Semantics.md#StructBody):
**{** _[_[_StructBodyDeclarations_](#StructBodyDeclarations)_]_ **}**  

## [BaseInterfaces](Semantics.md#BaseInterfaces):
**:** [_TypeNames_](#TypeNames)  

## [InterfaceBody](Semantics.md#InterfaceBody):
**{** [_InterfaceBodyDeclarations_](#InterfaceBodyDeclarations) **}**  

---

## [ImportName](Semantics.md#ImportName):
_Identifier_ _[_**as** _Identifier_*]*  

## [Type](Semantics.md#Type):
[_PrimitiveType_](#PrimitiveType) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_TypeName_](#TypeName) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_VoidPointer_](#VoidPointer) _[_[_PointerOrArraySuffix_](#PointerOrArraySuffix)_]_  
[_FunctionType_](#FunctionType)  
**(** [_FunctionType_](#FunctionType) **)** [_PointerOrArraySuffix_](#PointerOrArraySuffix)  

## [EnumConstants](Semantics.md#EnumConstants):
[_EnumConstant_](#EnumConstant) _{_**,** [_EnumConstant_](#EnumConstant)_}_  

## [BodyDeclarations](Semantics.md#BodyDeclarations):
[_BodyDeclaration_](#BodyDeclaration) _{_[_BodyDeclaration_](#BodyDeclaration)_}_  

## [UnionTypes](Semantics.md#UnionTypes):
[_UnionType_](#UnionType) _{_**,** [_UnionType_](#UnionType)_}_  

## [TypeNames](Semantics.md#TypeNames):
[_TypeName_](#TypeName) _{_**,** [_TypeName_](#TypeName)_}_  

## [StructBodyDeclarations](Semantics.md#StructBodyDeclarations):
[_StructBodyDeclaration_](#StructBodyDeclaration) _{_[_StructBodyDeclaration_](#StructBodyDeclaration)_}_  

## [InterfaceBodyDeclarations](Semantics.md#InterfaceBodyDeclarations):
[_InterfaceBodyDeclaration_](#InterfaceBodyDeclaration) _{_[_InterfaceBodyDeclaration_](#InterfaceBodyDeclaration)_}_  

---

## [PrimitiveType](Semantics.md#PrimitiveType):
[_NumericType_](#NumericType) _[_[_TypeAtomicity_](#TypeAtomicity)_]_  
**bool** _[_[_TypeAtomicity_](#TypeAtomicity)_]_  
**\_char** _[_[_TypeAtomicity_](#TypeAtomicity)_]_  

## [PointerOrArraySuffix](Semantics.md#PointerOrArraySuffix):
[_PointerSuffix_](#PointerSuffix) *[*_PointerOrArraySuffix_*]*  
[_ArrayDim_](#ArrayDim) *[*_PointerOrArraySuffix_*]*  

## [TypeName](Semantics.md#TypeName):
_Identifier_ _{_**.** _Identifier_*}*  

## [VoidPointer](Semantics.md#VoidPointer):
**unsafe** **void** _[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** _[_[_TypeAtomicity_](#TypeAtomicity)_]_  

## [FunctionType](Semantics.md#FunctionType):
**(** _[_[_ParameterTypes_](#ParameterTypes)_]_ **)** **->** [_Result_](#Result)  

## [EnumConstant](Semantics.md#EnumConstant):
_Identifier_ _[_**=** _ConstantExpression_*]*  
_Identifier_ **=** [_Block_](#Block)  

## [BodyDeclaration](Semantics.md#BodyDeclaration):
_[_[_NestedEncapsulation_](#NestedEncapsulation)_]_ [_MemberDeclaration_](#MemberDeclaration)  
_[_[_NestedEncapsulation_](#NestedEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

## [UnionType](Semantics.md#UnionType):
[_TypedefDeclaration_](#TypedefDeclaration)  
[_EnumDeclaration_](#EnumDeclaration)  
[_UnionDeclaration_](#UnionDeclaration)  
[_StructDeclaration_](#StructDeclaration)  

## [StructBodyDeclaration](Semantics.md#StructBodyDeclaration):
_[_[_StructNestedEncapsulation_](#StructNestedEncapsulation)_]_ [_StructMemberDeclaration_](#StructMemberDeclaration)  
_[_[_StructNestedEncapsulation_](#StructNestedEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

## [InterfaceBodyDeclaration](Semantics.md#InterfaceBodyDeclaration):
_[_[_InterfaceNestedEncapsulation_](#InterfaceNestedEncapsulation)_]_ [_InterfaceMemberDeclaration_](#InterfaceMemberDeclaration)  
_[_[_InterfaceNestedEncapsulation_](#InterfaceNestedEncapsulation)_]_ [_TypeDeclaration_](#TypeDeclaration)  

---

## [NumericType](Semantics.md#NumericType):
[_IntegralType_](#IntegralType)  
[_FloatingPointType_](#FloatingPointType)  

## [TypeAtomicity](Semantics.md#TypeAtomicity):
**atomic**  

## [PointerSuffix](Semantics.md#PointerSuffix):
_[_[_ValueMutability_](#ValueMutability)_]_ _[_[_ValueVolatility_](#ValueVolatility)_]_ **&** _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_ _[_[_PointerSize_](#PointerSize)_]_ _[_[_TypeAtomicity_](#TypeAtomicity)_]_  

## [ArrayDim](Semantics.md#ArrayDim):
**[** *[*_NumberLiteral_*]* **]** _[_[_ArrayLayout_](#ArrayLayout)_]_ _[_[_ArrayRawness_](#ArrayRawness)_]_  
**[** _Identifier_ **]** _[_[_ArrayLayout_](#ArrayLayout)_]_ _[_[_ArrayRawness_](#ArrayRawness)_]_  

## [ValueMutability](Semantics.md#ValueMutability):
**var**  

## [ValueVolatility](Semantics.md#ValueVolatility):
**volatile**  

## [ParameterTypes](Semantics.md#ParameterTypes):
[_FixedParameterTypes_](#FixedParameterTypes) _[_**,** [_VariableArityParameterType_](#VariableArityParameterType)_]_  
[_VariableArityParameterType_](#VariableArityParameterType)  

## [Result](Semantics.md#Result):
**noreturn**  
**void**  
[_Type_](#Type)  

## [Block](Semantics.md#Block):
**{** _[_[_BlockStatements_](#BlockStatements)_]_ **}**  

## [NestedEncapsulation](Semantics.md#NestedEncapsulation):
_(one of)_  
**public** **private**  

## [MemberDeclaration](Semantics.md#MemberDeclaration):
[_FieldDeclaration_](#FieldDeclaration)  
[_MethodDeclaration_](#MethodDeclaration)  
[_StaticInitializer_](#StaticInitializer)  

## [StructNestedEncapsulation](Semantics.md#StructNestedEncapsulation):
_(one of)_  
**public** **protected** **private**  

## [StructMemberDeclaration](Semantics.md#StructMemberDeclaration):
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_FieldDeclaration_](#FieldDeclaration)  
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_MethodDeclaration_](#MethodDeclaration)  
[_ConstructorDeclaration_](#ConstructorDeclaration)  
[_StaticInitializer_](#StaticInitializer)  

## [InterfaceNestedEncapsulation](Semantics.md#InterfaceNestedEncapsulation):
**private**  

## [InterfaceMemberDeclaration](Semantics.md#InterfaceMemberDeclaration):
[_FieldDeclaration_](#FieldDeclaration)  
_[_[_MemberStaticity_](#MemberStaticity)_]_ [_MethodDeclaration_](#MethodDeclaration)  
[_StaticInitializer_](#StaticInitializer)  

---

## [IntegralType](Semantics.md#IntegralType):
_(one of)_  
**\_ubyte** **\_byte** **\_ushort** **\_short** **\_uint** **\_int** **\_ulong** **\_long**  

## [FloatingPointType](Semantics.md#FloatingPointType):
_(one of)_  
**\_float** **\_double**  

## [ReferenceAliasability](Semantics.md#ReferenceAliasability):
**aliasable**  

## [PointerSize](Semantics.md#PointerSize):
**wide**  

## [ArrayLayout](Semantics.md#ArrayLayout):
**packed**  

## [ArrayRawness](Semantics.md#ArrayRawness):
**unsafe** **raw**  

## [FixedParameterTypes](Semantics.md#FixedParameterTypes):
[_FixedParameterType_](#FixedParameterType) _{_**,** [_FixedParameterType_](#FixedParameterType)_}_  

## [VariableArityParameterType](Semantics.md#VariableArityParameterType):
**...** **:** [_Type_](#Type)  

## [BlockStatements](Semantics.md#BlockStatements):
_BlockStatement_ *{*_BlockStatement_*}*  

## [FieldDeclaration](Semantics.md#FieldDeclaration):
[_FieldMutability_](#FieldMutability) _[_[_ValueVolatility_](#ValueVolatility)_]_ _Identifier_ **:** [_Type_](#Type) _[_**=** _ConstantExpression_*]* **;**  

## [MethodDeclaration](Semantics.md#MethodDeclaration):
_[_[_MethodExtensibility_](#MethodExtensibility)_]_ _[_[_MethodOverride_](#MethodOverride)_]_ **func** [_MethodHeader_](#MethodHeader) [_MethodBody_](#MethodBody)  

## [StaticInitializer](Semantics.md#StaticInitializer):
[_MemberStaticity_](#MemberStaticity) [_Block_](#Block)  

## [MemberStaticity](Semantics.md#MemberStaticity):
**static**  

## [ConstructorDeclaration](Semantics.md#ConstructorDeclaration):
[_ConstructorHeader_](#ConstructorHeader) [_Block_](#Block)  

---

## [FixedParameterType](Semantics.md#FixedParameterType):
**:** [_Type_](#Type)  

## [FieldMutability](Semantics.md#FieldMutability):
_(one of)_  
**var** **const**  

## [MethodExtensibility](Semantics.md#MethodExtensibility):
_(one of)_  
**open** **abstract**  

## [MethodOverride](Semantics.md#MethodOverride):
**override**  

## [MethodHeader](Semantics.md#MethodHeader):
_Identifier_ **(** _[_[_Parameters_](#Parameters)_]_ **)** **->** [_Result_](#Result)  

## [MethodBody](Semantics.md#MethodBody):
[_Block_](#Block)  
**;**  

## [ConstructorHeader](Semantics.md#ConstructorHeader):
**init** **(** _[_[_Parameters_](#Parameters)_]_ **)** _[_**->** [_Result_](#Result)_]_  

---

## [Parameters](Semantics.md#Parameters):
[_ThisParameter_](#ThisParameter) _[_**,** [_FixedParameters_](#FixedParameters)_]_ _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_FixedParameters_](#FixedParameters) _[_**,** [_VariableArityParameter_](#VariableArityParameter)_]_  
[_VariableArityParameter_](#VariableArityParameter)  

---

## [ThisParameter](Semantics.md#ThisParameter):
**this** _[_**:** [_ValueMutability_](#ValueMutability) _[_[_ValueVolatility_](#ValueVolatility)_]_ _[_**&** _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_ _[_[_PointerSize_](#PointerSize)_]_*]*_]_  
**this** **:** [_ValueVolatility_](#ValueVolatility) _[_**&** _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_ _[_[_PointerSize_](#PointerSize)_]_*]*  
**this** **:** **&** _[_[_ReferenceAliasability_](#ReferenceAliasability)_]_ _[_[_PointerSize_](#PointerSize)_]_  

## [FixedParameters](Semantics.md#FixedParameters):
[_FixedParameter_](#FixedParameter) _{_**,** [_FixedParameter_](#FixedParameter)_}_  

## [VariableArityParameter](Semantics.md#VariableArityParameter):
**...** _Identifier_ **:** [_Type_](#Type)  

---

## [FixedParameter](Semantics.md#FixedParameter):
_Identifier_ **:** [_Type_](#Type)  
