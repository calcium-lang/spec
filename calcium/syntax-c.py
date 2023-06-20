from alchemist.front.parser.generator import oneof, ProductionTemplate

# External definitions


class TranslationUnit(ProductionTemplate):
    _template = oneof(
        "ExternalDeclaration",
        ("TranslationUnit", "ExternalDeclaration")
    )

###


class ExternalDeclaration(ProductionTemplate):
    _template = oneof("FunctionDefinition", "Declaration")

###


class FunctionDefinition(ProductionTemplate):
    _template = "DeclarationSpecifiers", "Declarator", ["DeclarationList"], "CompoundStatement"

###


class DeclarationList(ProductionTemplate):
    _template = oneof(
        "Declaration",
        ("DeclarationList", "Declaration")
    )

# Declarations


class Declaration(ProductionTemplate):
    _template = oneof(
        ("DeclarationSpecifiers", ["InitDeclaratorList"], "Semicolon"),
        "Static_AssertDeclaration"
    )

###


class DeclarationSpecifiers(ProductionTemplate):
    _template = oneof(
        ("StorageClassSpecifier", ["DeclarationSpecifiers"]),
        ("TypeSpecifier", ["DeclarationSpecifiers"]),
        ("TypeQualifier", ["DeclarationSpecifiers"]),
        ("FunctionSpecifier", ["DeclarationSpecifiers"]),
        ("AlignmentSpecifier", ["DeclarationSpecifiers"])
    )


class InitDeclaratorList(ProductionTemplate):
    _template = oneof(
        "InitDeclarator",
        ("InitDeclaratorList", "Comma", "InitDeclarator")
    )


class Static_AssertDeclaration(ProductionTemplate):
    _template = "_Static_Assert", "LeftParenthesis", "ConstantExpression", "Comma", "StringLiteral", "RightParenthesis", "Semicolon"

###


class StorageClassSpecifier(ProductionTemplate):
    _template = oneof("Typedef", "Extern", "Static", "_Thread_Local", "Auto", "Register")


class TypeSpecifier(ProductionTemplate):
    _template = oneof("Void", "Char", "Short", "Int", "Long", "Float", "Double", "Signed", "Unsigned", "_Bool", "_Complex", "AtomicTypeSpecifier", "StructOrUnionSpecifier", "EnumSpecifier", "TypedefName")


class TypeQualifier(ProductionTemplate):
    _template = oneof("Const", "Restrict", "Volatile", "_Atomic")


class FunctionSpecifier(ProductionTemplate):
    _template = oneof("Inline", "_Noreturn")


class AlignmentSpecifier(ProductionTemplate):
    _template = oneof(
        ("_Alignas", "LeftParenthesis", "TypeName", "RightParenthesis"),
        ("_Alignas", "LeftParenthesis", "ConstantExpression", "RightParenthesis")
    )


class InitDeclarator(ProductionTemplate):
    _template = oneof(
        "Declarator",
        ("Declarator", "Equals", "Initializer")
    )

###


class AtomicTypeSpecifier(ProductionTemplate):
    _template = "_Atomic", "LeftParenthesis", "TypeName", "RightParenthesis"


class StructOrUnionSpecifier(ProductionTemplate):
    _template = oneof(
        ("StructOrUnion", ["Identifier"], "LeftCurlyBracket", "StructDeclarationList", "RightCurlyBracket"),
        ("StructOrUnion", "Identifier")
    )


class EnumSpecifier(ProductionTemplate):
    _template = oneof(
        ("Enum", ["Identifier"], "LeftCurlyBracket", "EnumeratorList", "RightCurlyBracket"),
        ("Enum", ["Identifier"], "LeftCurlyBracket", "EnumeratorList", "Comma", "RightCurlyBracket"),
        ("Enum", "Identifier")
    )


class TypedefName(ProductionTemplate):
    _template = "Identifier"


class TypeName(ProductionTemplate):
    _template = "SpecifierQualifierList", ["AbstractDeclarator"]


class Declarator(ProductionTemplate):
    _template = ["Pointer"], "DirectDeclarator"


class Initializer(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("LeftCurlyBracket", "InitializerList", "RightCurlyBracket"),
        ("LeftCurlyBracket", "InitializerList", "Comma", "RightCurlyBracket")
    )

###


class StructOrUnion(ProductionTemplate):
    _template = oneof("Struct", "Union")


class StructDeclarationList(ProductionTemplate):
    _template = oneof(
        "StructDeclaration",
        ("StructDeclarationList", "StructDeclaration")
    )


class EnumeratorList(ProductionTemplate):
    _template = oneof(
        "Enumerator",
        ("EnumeratorList", "Comma", "Enumerator")
    )


class SpecifierQualifierList(ProductionTemplate):
    _template = oneof(
        ("TypeSpecifier", ["SpecifierQualifierList"]),
        ("TypeQualifier", ["SpecifierQualifierList"]),
        ("AlignmentSpecifier", ["SpecifierQualifierList"])
    )


class AbstractDeclarator(ProductionTemplate):
    _template = oneof(
        "Pointer",
        (["Pointer"], "DirectAbstractDeclarator")
    )


class Pointer(ProductionTemplate):
    _template = oneof(
        ("Asterisk", ["TypeQualifierList"]),
        ("Asterisk", ["TypeQualifierList"], "Pointer")
    )


class DirectDeclarator(ProductionTemplate):
    _template = oneof(
        "Identifier",
        ("LeftParenthesis", "Declarator", "RightParenthesis"),
        ("DirectDeclarator", "LeftSquareBracket", ["TypeQualifierList"], ["AssignmentExpression"], "RightSquareBracket"),
        ("DirectDeclarator", "LeftSquareBracket", "Static", ["TypeQualifierList"], "AssignmentExpression", "RightSquareBracket"),
        ("DirectDeclarator", "LeftSquareBracket", "TypeQualifierList", "Static", "AssignmentExpression", "RightSquareBracket"),
        ("DirectDeclarator", "LeftSquareBracket", ["TypeQualifierList"], "Asterisk", "RightSquareBracket"),
        ("DirectDeclarator", "LeftParenthesis", "ParameterTypeList", "RightParenthesis"),
        ("DirectDeclarator", "LeftParenthesis", ["IdentifierList"], "RightParenthesis")
    )


class InitializerList(ProductionTemplate):
    _template = oneof(
        (["Designation"], "Initializer"),
        ("InitializerList", "Comma", ["Designation"], "Initializer")
    )

###


class StructDeclaration(ProductionTemplate):
    _template = oneof(
        ("SpecifierQualifierList", ["StructDeclaratorList"], "Semicolon"),
        "Static_AssertDeclaration"
    )


class Enumerator(ProductionTemplate):
    _template = oneof(
        "EnumerationConstant",
        ("EnumerationConstant", "Equals", "ConstantExpression")
    )


class DirectAbstractDeclarator(ProductionTemplate):
    _template = oneof(
        ("LeftParenthesis", "AbstractDeclarator", "RightParenthesis"),
        (["DirectAbstractDeclarator"], "LeftSquareBracket", ["TypeQualifierList"], ["AssignmentExpression"], "RightSquareBracket"),
        (["DirectAbstractDeclarator"], "LeftSquareBracket", "Static", ["TypeQualifierList"], "AssignmentExpression", "RightSquareBracket"),
        (["DirectAbstractDeclarator"], "LeftSquareBracket", "TypeQualifierList", "Static", "AssignmentExpression", "RightSquareBracket"),
        (["DirectAbstractDeclarator"], "LeftSquareBracket", "Asterisk", "RightSquareBracket"),
        (["DirectAbstractDeclarator"], "LeftParenthesis", ["ParameterTypeList"], "RightParenthesis")
    )


class TypeQualifierList(ProductionTemplate):
    _template = oneof(
        "TypeQualifier",
        ("TypeQualifierList", "TypeQualifier")
    )


class ParameterTypeList(ProductionTemplate):
    _template = oneof(
        "ParameterList",
        ("ParameterList", "Comma", "TripleFullStop")
    )


class IdentifierList(ProductionTemplate):
    _template = oneof(
        "Identifier",
        ("IdentifierList", "Comma", "Identifier")
    )


class Designation(ProductionTemplate):
    _template = "DesignatorList", "Equals"

###


class StructDeclaratorList(ProductionTemplate):
    _template = oneof(
        "StructDeclarator",
        ("StructDeclaratorList", "Comma", "StructDeclarator")
    )


class ParameterList(ProductionTemplate):
    _template = oneof(
        "ParameterDeclaration",
        ("ParameterList", "Comma", "ParameterDeclaration")
    )


class DesignatorList(ProductionTemplate):
    _template = oneof(
        "Designator",
        ("DesignatorList", "Designator")
    )

###


class StructDeclarator(ProductionTemplate):
    _template = oneof(
        "Declarator",
        (["Declarator"], "Colon", "ConstantExpression")
    )


class ParameterDeclaration(ProductionTemplate):
    _template = oneof(
        ("DeclarationSpecifiers", "Declarator"),
        ("DeclarationSpecifiers", ["AbstractDeclarator"])
    )


class Designator(ProductionTemplate):
    _template = oneof(
        ("LeftSquareBracket", "ConstantExpression", "RightSquareBracket"),
        ("FullStop", "Identifier")
    )


# Statements


class Statement(ProductionTemplate):
    _template = oneof("LabeledStatement", "CompoundStatement", "ExpressionStatement", "SelectionStatement", "IterationStatement", "JumpStatement")

###


class LabeledStatement(ProductionTemplate):
    _template = oneof(
        ("Identifier", "Colon", "Statement"),
        ("Case", "ConstantExpression", "Colon", "Statement"),
        ("Default", "Colon", "Statement")
    )


class CompoundStatement(ProductionTemplate):
    _template = "LeftCurlyBracket", ["BlockItemList"], "RightCurlyBracket"


class ExpressionStatement(ProductionTemplate):
    _template = ["Expression"], "Semicolon"


class SelectionStatement(ProductionTemplate):
    _template = oneof(
        ("If", "LeftParenthesis", "Expression", "RightParenthesis", "Statement"),
        ("If", "LeftParenthesis", "Expression", "RightParenthesis", "Statement", "Else", "Statement"),
        ("Switch", "LeftParenthesis", "Expression", "RightParenthesis", "Statement")
    )


class IterationStatement(ProductionTemplate):
    _template = oneof(
        ("While", "LeftParenthesis", "Expression", "RightParenthesis", "Statement"),
        ("Do", "Statement", "While", "LeftParenthesis", "Expression", "RightParenthesis", "Semicolon"),
        ("For", "LeftParenthesis", ["Expression"], "Semicolon", ["Expression"], "Semicolon", ["Expression"], "RightParenthesis", "Statement"),
        ("For", "LeftParenthesis", "Declaration", ["Expression"], "Semicolon", ["Expression"], "RightParenthesis", "Statement")
    )


class JumpStatement(ProductionTemplate):
    _template = oneof(
        ("Goto", "Identifier", "Semicolon"),
        ("Continue", "Semicolon"),
        ("Break", "Semicolon"),
        ("Return", ["Expression"], "Semicolon")
    )

###


class BlockItemList(ProductionTemplate):
    _template = oneof(
        "BlockItem",
        ("BlockItemList", "BlockItem")
    )

###


class BlockItem(ProductionTemplate):
    _template = oneof("Declaration", "Statement")


# Expressions


class Expression(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("Expression", "Comma", "AssignmentExpression")
    )


class ConstantExpression(ProductionTemplate):
    _template = "ConditionalExpression"

###


class AssignmentExpression(ProductionTemplate):
    _template = oneof(
        "ConditionalExpression",
        ("UnaryExpression", "AssignmentOperator", "AssignmentExpression")
    )


class ConditionalExpression(ProductionTemplate):
    _template = oneof(
        "LogicalOrExpression",
        ("LogicalOrExpression", "Question", "Expression", "Colon", "ConditionalExpression")
    )

###


class UnaryExpression(ProductionTemplate):
    _template = oneof(
        "PostfixExpression",
        ("DoublePlus", "UnaryExpression"),
        ("DoubleMinus", "UnaryExpression"),
        ("UnaryOperator", "CastExpression"),
        ("Sizeof", "UnaryExpression"),
        ("Sizeof", "LeftParenthesis", "TypeName", "RightParenthesis"),
        ("_Alignof", "LeftParenthesis", "TypeName", "RightParenthesis")
    )


class AssignmentOperator(ProductionTemplate):
    _template = oneof("Equals", "AsteriskEquals", "SlashEquals", "PercentEquals", "PlusEquals", "MinusEquals", "DoubleLesserThanEquals", "DoubleGreaterThanEquals", "AmpersandEquals", "CaretEquals", "VerticalBarEquals")


class LogicalOrExpression(ProductionTemplate):
    _template = oneof(
        "LogicalAndExpression",
        ("LogicalOrExpression", "DoubleVerticalBar", "LogicalAndExpression")
    )

###


class PostfixExpression(ProductionTemplate):
    _template = oneof(
        "PrimaryExpression",
        ("PostfixExpression", "LeftSquareBracket", "Expression", "RightSquareBracket"),
        ("PostfixExpression", "LeftParenthesis", ["ArgumentExpressionList"], "RightParenthesis"),
        ("PostfixExpression", "FullStop", "Identifier"),
        ("PostfixExpression", "HyphenGreaterThan", "Identifier"),
        ("PostfixExpression", "DoublePlus"),
        ("PostfixExpression", "DoubleMinus"),
        ("LeftParenthesis", "TypeName", "RightParenthesis", "LeftCurlyBracket", "InitializerList", "RightCurlyBracket"),
        ("LeftParenthesis", "TypeName", "RightParenthesis", "LeftCurlyBracket", "InitializerList", "Comma", "RightCurlyBracket")
    )


class UnaryOperator(ProductionTemplate):
    _template = oneof("Ampersand", "Asterisk", "Plus", "Minus", "Tilde", "Exclamation")


class CastExpression(ProductionTemplate):
    _template = oneof(
        "UnaryExpression",
        ("LeftParenthesis", "TypeName", "RightParenthesis", "CastExpression")
    )


class LogicalAndExpression(ProductionTemplate):
    _template = oneof(
        "InclusiveOrExpression",
        ("LogicalAndExpression", "DoubleAmpersand", "InclusiveOrExpression")
    )

###


class PrimaryExpression(ProductionTemplate):
    _template = oneof(
        "Identifier",
        "Constant",
        "StringLiteral",
        ("LeftParenthesis", "Expression", "RightParenthesis"),
        "GenericSelection"
    )


class ArgumentExpressionList(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("ArgumentExpressionList", "Comma", "AssignmentExpression")
    )


class InclusiveOrExpression(ProductionTemplate):
    _template = oneof(
        "ExclusiveOrExpression",
        ("InclusiveOrExpression", "VerticalBar", "ExclusiveOrExpression")
    )

###


class GenericSelection(ProductionTemplate):
    _template = "_Generic", "LeftParenthesis", "AssignmentExpression", "Comma", "GenericAssocList", "RightParenthesis"


class ExclusiveOrExpression(ProductionTemplate):
    _template = oneof(
        "AndExpression",
        ("ExclusiveOrExpression", "Caret", "AndExpression")
    )

###


class GenericAssocList(ProductionTemplate):
    _template = oneof(
        "GenericAssociation",
        ("GenericAssocList", "Comma", "GenericAssociation")
    )


class AndExpression(ProductionTemplate):
    _template = oneof(
        "EqualityExpression",
        ("AndExpression", "Ampersand", "EqualityExpression")
    )

###


class GenericAssociation(ProductionTemplate):
    _template = oneof(
        ("TypeName", "Colon", "AssignmentExpression"),
        ("Default", "Colon", "AssignmentExpression")
    )


class EqualityExpression(ProductionTemplate):
    _template = oneof(
        "RelationalExpression",
        ("EqualityExpression", "DoubleEquals", "RelationalExpression"),
        ("EqualityExpression", "ExclamationEquals", "RelationalExpression")
    )

###


class RelationalExpression(ProductionTemplate):
    _template = oneof(
        "ShiftExpression",
        ("RelationalExpression", "LesserThan", "ShiftExpression"),
        ("RelationalExpression", "GreaterThan", "ShiftExpression"),
        ("RelationalExpression", "LesserThanEquals", "ShiftExpression"),
        ("RelationalExpression", "GreaterThanEquals", "ShiftExpression")
    )

###


class ShiftExpression(ProductionTemplate):
    _template = oneof(
        "AdditiveExpression",
        ("ShiftExpression", "DoubleLesserThan", "AdditiveExpression"),
        ("ShiftExpression", "DoubleGreaterThan", "AdditiveExpression")
    )

###


class AdditiveExpression(ProductionTemplate):
    _template = oneof(
        "MultiplicativeExpression",
        ("AdditiveExpression", "Plus", "MultiplicativeExpression"),
        ("AdditiveExpression", "Minus", "MultiplicativeExpression")
    )

###


class MultiplicativeExpression(ProductionTemplate):
    _template = oneof(
        "CastExpression",
        ("MultiplicativeExpression", "Asterisk", "CastExpression"),
        ("MultiplicativeExpression", "Slash", "CastExpression"),
        ("MultiplicativeExpression", "Percent", "CastExpression")
    )
