from alchemist.front.parser.generator import oneof, ProductionTemplate

# External definitions


class TranslationUnit(ProductionTemplate):
    _template = oneof(
        "ExternalDeclaration",
        ("TranslationUnit", "ExternalDeclaration")
    )


class ExternalDeclaration(ProductionTemplate):
    _template = oneof("FunctionDefinition", "Declaration")


class FunctionDefinition(ProductionTemplate):
    _template = "DeclarationSpecifiers", "Declarator", ["DeclarationList"], "CompoundStatement"


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


class InitDeclarator(ProductionTemplate):
    _template = oneof(
        "Declarator",
        ("Declarator", "Equals", "Initializer")
    )


class StorageClassSpecifier(ProductionTemplate):
    _template = oneof("Typedef", "Extern", "Static", "_Thread_Local", "Auto", "Register")


class TypeSpecifier(ProductionTemplate):
    _template = oneof("Void", "Char", "Short", "Int", "Long", "Float", "Double", "Signed", "Unsigned", "_Bool", "_Complex", "AtomicTypeSpecifier", "StructOrUnionSpecifier", "EnumSpecifier", "TypedefName")


class StructOrUnionSpecifier(ProductionTemplate):
    _template = oneof(
        ("StructOrUnion", ["Identifier"], "LeftCurlyBracket", "StructDeclarationList", "RightCurlyBracket"),
        ("StructOrUnion", "Identifier")
    )


class StructOrUnion(ProductionTemplate):
    _template = oneof("Struct", "Union")


class StructDeclarationList(ProductionTemplate):
    _template = oneof(
        "StructDeclaration",
        ("StructDeclarationList", "StructDeclaration")
    )


class StructDeclaration(ProductionTemplate):
    _template = oneof(
        ("SpecifierQualifierList", ["StructDeclaratorList"], "Semicolon"),
        "Static_AssertDeclaration"
    )


class SpecifierQualifierList(ProductionTemplate):
    _template = oneof(
        ("TypeSpecifier", ["SpecifierQualifierList"]),
        ("TypeQualifier", ["SpecifierQualifierList"]),
        ("AlignmentSpecifier", ["SpecifierQualifierList"])
    )


class StructDeclaratorList(ProductionTemplate):
    _template = oneof(
        "StructDeclarator",
        ("StructDeclaratorList", "Comma", "StructDeclarator")
    )


class StructDeclarator(ProductionTemplate):
    _template = oneof(
        "Declarator",
        (["Declarator"], "Colon", "ConstantExpression")
    )


class EnumSpecifier(ProductionTemplate):
    _template = oneof(
        ("Enum", ["Identifier"], "LeftCurlyBracket", "EnumeratorList", "RightCurlyBracket"),
        ("Enum", ["Identifier"], "LeftCurlyBracket", "EnumeratorList", "Comma", "RightCurlyBracket"),
        ("Enum", "Identifier")
    )


class EnumeratorList(ProductionTemplate):
    _template = oneof(
        "Enumerator",
        ("EnumeratorList", "Comma", "Enumerator")
    )


class Enumerator(ProductionTemplate):
    _template = oneof(
        "EnumerationConstant",
        ("EnumerationConstant", "Equals", "ConstantExpression")
    )


class AtomicTypeSpecifier(ProductionTemplate):
    _template = "_Atomic", "LeftParenthesis", "TypeName", "RightParenthesis"


class TypeQualifier(ProductionTemplate):
    _template = oneof("Const", "Restrict", "Volatile", "_Atomic")


class FunctionSpecifier(ProductionTemplate):
    _template = oneof("Inline", "_Noreturn")


class AlignmentSpecifier(ProductionTemplate):
    _template = oneof(
        ("_Alignas", "LeftParenthesis", "TypeName", "RightParenthesis"),
        ("_Alignas", "LeftParenthesis", "ConstantExpression", "RightParenthesis")
    )


class Declarator(ProductionTemplate):
    _template = ["Pointer"], "DirectDeclarator"


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


class Pointer(ProductionTemplate):
    _template = oneof(
        ("Asterisk", ["TypeQualifierList"]),
        ("Asterisk", ["TypeQualifierList"], "Pointer")
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


class ParameterList(ProductionTemplate):
    _template = oneof(
        "ParameterDeclaration",
        ("ParameterList", "Comma", "ParameterDeclaration")
    )


class ParameterDeclaration(ProductionTemplate):
    _template = oneof(
        ("DeclarationSpecifiers", "Declarator"),
        ("DeclarationSpecifiers", ["AbstractDeclarator"])
    )


class IdentifierList(ProductionTemplate):
    _template = oneof(
        "Identifier",
        ("IdentifierList", "Comma", "Identifier")
    )


class TypeName(ProductionTemplate):
    _template = "SpecifierQualifierList", ["AbstractDeclarator"]


class AbstractDeclarator(ProductionTemplate):
    _template = oneof(
        "Pointer",
        (["Pointer"], "DirectAbstractDeclarator")
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


class TypedefName(ProductionTemplate):
    _template = "Identifier"


class Initializer(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("LeftCurlyBracket", "InitializerList", "RightCurlyBracket"),
        ("LeftCurlyBracket", "InitializerList", "Comma", "RightCurlyBracket")
    )


class InitializerList(ProductionTemplate):
    _template = oneof(
        (["Designation"], "Initializer"),
        ("InitializerList", "Comma", ["Designation"], "Initializer")
    )


class Designation(ProductionTemplate):
    _template = "DesignatorList", "Equals"


class DesignatorList(ProductionTemplate):
    _template = oneof(
        "Designator",
        ("DesignatorList", "Designator")
    )


class Designator(ProductionTemplate):
    _template = oneof(
        ("LeftSquareBracket", "ConstantExpression", "RightSquareBracket"),
        ("FullStop", "Identifier")
    )


class Static_AssertDeclaration(ProductionTemplate):
    _template = "_Static_assert", "LeftParenthesis", "ConstantExpression", "Comma", "StringLiteral", "RightParenthesis", "Semicolon"

# Statements


class Statement(ProductionTemplate):
    _template = oneof("LabeledStatement", "CompoundStatement", "ExpressionStatement", "SelectionStatement", "IterationStatement", "JumpStatement")


class LabeledStatement(ProductionTemplate):
    _template = oneof(
        ("Identifier", "Colon", "Statement"),
        ("Case", "ConstantExpression", "Colon", "Statement"),
        ("Default", "Colon", "Statement")
    )


class CompoundStatement(ProductionTemplate):
    _template = "LeftCurlyBracket", ["BlockItemList"], "RightCurlyBracket"


class BlockItemList(ProductionTemplate):
    _template = oneof(
        "BlockItem",
        ("BlockItemList", "BlockItem")
    )


class BlockItem(ProductionTemplate):
    _template = oneof("Declaration", "Statement")


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

# Expressions


class PrimaryExpression(ProductionTemplate):
    _template = oneof(
        "Identifier",
        "Constant",
        "StringLiteral",
        ("LeftParenthesis", "Expression", "RightParenthesis"),
        "GenericSelection"
    )


class GenericSelection(ProductionTemplate):
    _template = "_Generic", "LeftParenthesis", "AssignmentExpression", "Comma", "GenericAssocList", "RightParenthesis"


class GenericAssocList(ProductionTemplate):
    _template = oneof(
        "GenericAssociation",
        ("GenericAssocList", ",", "GenericAssociation")
    )


class GenericAssociation(ProductionTemplate):
    _template = oneof(
        ("TypeName", "Colon", "AssignmentExpression"),
        ("Default", "Colon", "AssignmentExpression")
    )


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


class ArgumentExpressionList(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("ArgumentExpressionList", "Comma", "AssignmentExpression")
    )


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


class UnaryOperator(ProductionTemplate):
    _template = oneof("Ampersand", "Asterisk", "Plus", "Minus", "Tilde", "Exclamation")


class CastExpression(ProductionTemplate):
    _template = oneof(
        "UnaryExpression",
        ("LeftParenthesis", "TypeName", "RightParenthesis", "CastExpression")
    )


class MultiplicativeExpression(ProductionTemplate):
    _template = oneof(
        "CastExpression",
        ("MultiplicativeExpression", "Asterisk", "CastExpression"),
        ("MultiplicativeExpression", "Slash", "CastExpression"),
        ("MultiplicativeExpression", "Percent", "CastExpression")
    )


class AdditiveExpression(ProductionTemplate):
    _template = oneof(
        "MultiplicativeExpression",
        ("AdditiveExpression", "Plus", "MultiplicativeExpression"),
        ("AdditiveExpression", "Minus", "MultiplicativeExpression")
    )


class ShiftExpression(ProductionTemplate):
    _template = oneof(
        "AdditiveExpression",
        ("ShiftExpression", "DoubleLesserThan", "AdditiveExpression"),
        ("ShiftExpression", "DoubleGreaterThan", "AdditiveExpression")
    )


class RelationalExpression(ProductionTemplate):
    _template = oneof(
        "ShiftExpression",
        ("RelationalExpression", "LesserThan", "ShiftExpression"),
        ("RelationalExpression", "GreaterThan", "ShiftExpression"),
        ("RelationalExpression", "LesserThanEquals", "ShiftExpression"),
        ("RelationalExpression", "GreaterThanEquals", "ShiftExpression")
    )


class EqualityExpression(ProductionTemplate):
    _template = oneof(
        "RelationalExpression",
        ("EqualityExpression", "DoubleEquals", "RelationalExpression"),
        ("EqualityExpression", "ExclamationEquals", "RelationalExpression")
    )


class AndExpression(ProductionTemplate):
    _template = oneof(
        "EqualityExpression",
        ("AndExpression", "Ampersand", "EqualityExpression")
    )


class ExclusiveOrExpression(ProductionTemplate):
    _template = oneof(
        "AndExpression",
        ("ExclusiveOrExpression", "Caret", "AndExpression")
    )


class InclusiveOrExpression(ProductionTemplate):
    _template = oneof(
        "ExclusiveOrExpression",
        ("InclusiveOrExpression", "VerticalBar", "ExclusiveOrExpression")
    )


class LogicalAndExpression(ProductionTemplate):
    _template = oneof(
        "InclusiveOrExpression",
        ("LogicalAndExpression", "DoubleAmpersand", "InclusiveOrExpression")
    )


class LogicalOrExpression(ProductionTemplate):
    _template = oneof(
        "LogicalAndExpression",
        ("LogicalOrExpression", "DoubleVerticalBar", "LogicalAndExpression")
    )


class ConditionalExpression(ProductionTemplate):
    _template = oneof(
        "LogicalOrExpression",
        ("LogicalOrExpression", "Question", "Expression", "Colon", "ConditionalExpression")
    )


class AssignmentExpression(ProductionTemplate):
    _template = oneof(
        "ConditionalExpression",
        ("UnaryExpression", "AssignmentOperator", "AssignmentExpression")
    )


class AssignmentOperator(ProductionTemplate):
    _template = oneof("Equals", "AsteriskEquals", "SlashEquals", "PercentEquals", "PlusEquals", "MinusEquals", "DoubleLesserThanEquals", "DoubleGreaterThanEquals", "AmpersandEquals", "CaretEquals", "VerticalBarEquals")


class Expression(ProductionTemplate):
    _template = oneof(
        "AssignmentExpression",
        ("Expression", "Comma", "AssignmentExpression")
    )


class ConstantExpression(ProductionTemplate):
    _template = "ConditionalExpression"
