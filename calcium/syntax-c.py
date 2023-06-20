from alchemist.front.parser.generator import repeat, oneof, ProductionTemplate

# External definitions


class TranslationUnit(ProductionTemplate):
    _template = "ExternalDeclaration", repeat("ExternalDeclaration")

###


class ExternalDeclaration(ProductionTemplate):
    _template = oneof("FunctionDefinition", "Declaration")

###


class FunctionDefinition(ProductionTemplate):
    _template = "DeclarationSpecifiers", "Declarator", ["DeclarationList"], "CompoundStatement"

###


class DeclarationList(ProductionTemplate):
    _template = "Declaration", repeat("Declaration")

# Declarations


class Declaration(ProductionTemplate):
    _template = oneof(
        ("DeclarationSpecifiers", ["InitDeclaratorList"], "Semicolon"),
        "Static_AssertDeclaration"
    )

###


class DeclarationSpecifiers(ProductionTemplate):
    _template = oneof("StorageClassSpecifier", "TypeSpecifier", "TypeQualifier", "FunctionSpecifier", "AlignmentSpecifier"), ["DeclarationSpecifiers"]


class InitDeclaratorList(ProductionTemplate):
    _template = "InitDeclarator", repeat("Comma", "InitDeclarator")


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
    _template = "_Alignas", "LeftParenthesis", oneof("TypeName", "ConstantExpression"), "RightParenthesis"


class InitDeclarator(ProductionTemplate):
    _template = "Declarator", ["Equals", "Initializer"]

###


class AtomicTypeSpecifier(ProductionTemplate):
    _template = "_Atomic", "LeftParenthesis", "TypeName", "RightParenthesis"


class StructOrUnionSpecifier(ProductionTemplate):
    _template = oneof(
        ("StructOrUnion", "Identifier", ["LeftCurlyBracket", "StructDeclarationList", "RightCurlyBracket"]),
        ("StructOrUnion", "LeftCurlyBracket", "StructDeclarationList", "RightCurlyBracket")
    )


class EnumSpecifier(ProductionTemplate):
    _template = oneof(
        ("Enum", "Identifier", ["LeftCurlyBracket", "EnumeratorList", ["Comma"], "RightCurlyBracket"]),
        ("Enum", "LeftCurlyBracket", "EnumeratorList", ["Comma"], "RightCurlyBracket")
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
        ("LeftCurlyBracket", "InitializerList", ["Comma"], "RightCurlyBracket")
    )

###


class StructOrUnion(ProductionTemplate):
    _template = oneof("Struct", "Union")


class StructDeclarationList(ProductionTemplate):
    _template = "StructDeclaration", repeat("StructDeclaration")


class EnumeratorList(ProductionTemplate):
    _template = "Enumerator", repeat("Comma", "Enumerator")


class SpecifierQualifierList(ProductionTemplate):
    _template = oneof("TypeSpecifier", "TypeQualifier", "AlignmentSpecifier"), ["SpecifierQualifierList"]


class AbstractDeclarator(ProductionTemplate):
    _template = oneof(
        ("Pointer", ["DirectAbstractDeclarator"]),
        "DirectAbstractDeclarator"
    )


class Pointer(ProductionTemplate):
    _template = "Asterisk", ["TypeQualifierList"], ["Pointer"]


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
    _template = ["Designation"], "Initializer", repeat("Comma", ["Designation"], "Initializer")

###


class StructDeclaration(ProductionTemplate):
    _template = oneof(
        ("SpecifierQualifierList", ["StructDeclaratorList"], "Semicolon"),
        "Static_AssertDeclaration"
    )


class Enumerator(ProductionTemplate):
    _template = "EnumerationConstant", ["Equals", "ConstantExpression"]


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
    _template = "TypeQualifier", repeat("TypeQualifier")


class ParameterTypeList(ProductionTemplate):
    _template = "ParameterList", ["Comma", "TripleFullStop"]


class IdentifierList(ProductionTemplate):
    _template = "Identifier", repeat("Comma", "Identifier")


class Designation(ProductionTemplate):
    _template = "DesignatorList", "Equals"

###


class StructDeclaratorList(ProductionTemplate):
    _template = "StructDeclarator", repeat("Comma", "StructDeclarator")


class ParameterList(ProductionTemplate):
    _template = "ParameterDeclaration", repeat("Comma", "ParameterDeclaration")


class DesignatorList(ProductionTemplate):
    _template = "Designator", repeat("Designator")

###


class StructDeclarator(ProductionTemplate):
    _template = oneof(
        ("Declarator", ["Colon", "ConstantExpression"]),
        ("Colon", "ConstantExpression")
    )


class ParameterDeclaration(ProductionTemplate):
    _template = "DeclarationSpecifiers", [oneof("Declarator", "AbstractDeclarator")]


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
    _template = oneof("Identifier", ("Case", "ConstantExpression"), "Default"), "Colon", "Statement"


class CompoundStatement(ProductionTemplate):
    _template = "LeftCurlyBracket", ["BlockItemList"], "RightCurlyBracket"


class ExpressionStatement(ProductionTemplate):
    _template = ["Expression"], "Semicolon"


class SelectionStatement(ProductionTemplate):
    _template = oneof(
        ("If", "LeftParenthesis", "Expression", "RightParenthesis", "Statement", ["Else", "Statement"]),
        ("Switch", "LeftParenthesis", "Expression", "RightParenthesis", "Statement")
    )


class IterationStatement(ProductionTemplate):
    _template = oneof(
        ("While", "LeftParenthesis", "Expression", "RightParenthesis", "Statement"),
        ("Do", "Statement", "While", "LeftParenthesis", "Expression", "RightParenthesis", "Semicolon"),
        ("For", "LeftParenthesis", oneof((["Expression"], "Semicolon"), "Declaration"), ["Expression"], "Semicolon", ["Expression"], "RightParenthesis", "Statement")
    )


class JumpStatement(ProductionTemplate):
    _template = oneof(("Goto", "Identifier"), "Continue", "Break", ("Return", ["Expression"])), "Semicolon"

###


class BlockItemList(ProductionTemplate):
    _template = "BlockItem", repeat("BlockItem")

###


class BlockItem(ProductionTemplate):
    _template = oneof("Declaration", "Statement")


# Expressions


class Expression(ProductionTemplate):
    _template = "AssignmentExpression", repeat("Comma", "AssignmentExpression")


class ConstantExpression(ProductionTemplate):
    _template = "ConditionalExpression"

###


class AssignmentExpression(ProductionTemplate):
    _template = oneof(
        "ConditionalExpression",
        ("UnaryExpression", "AssignmentOperator", "AssignmentExpression")
    )


class ConditionalExpression(ProductionTemplate):
    _template = "LogicalOrExpression", ["Question", "Expression", "Colon", "ConditionalExpression"]

###


class UnaryExpression(ProductionTemplate):
    _template = oneof(
        "PostfixExpression",
        (oneof("DoublePlus", "DoubleMinus", "Sizeof"), "UnaryExpression"),
        ("UnaryOperator", "CastExpression"),
        (oneof("Sizeof", "_Alignof"), "LeftParenthesis", "TypeName", "RightParenthesis")
    )


class AssignmentOperator(ProductionTemplate):
    _template = oneof("Equals", "AsteriskEquals", "SlashEquals", "PercentEquals", "PlusEquals", "MinusEquals", "DoubleLesserThanEquals", "DoubleGreaterThanEquals", "AmpersandEquals", "CaretEquals", "VerticalBarEquals")


class LogicalOrExpression(ProductionTemplate):
    _template = "LogicalAndExpression", repeat("DoubleVerticalBar", "LogicalAndExpression")

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
        ("LeftParenthesis", "TypeName", "RightParenthesis", "LeftCurlyBracket", "InitializerList", ["Comma"], "RightCurlyBracket")
    )


class UnaryOperator(ProductionTemplate):
    _template = oneof("Ampersand", "Asterisk", "Plus", "Minus", "Tilde", "Exclamation")


class CastExpression(ProductionTemplate):
    _template = oneof(
        "UnaryExpression",
        ("LeftParenthesis", "TypeName", "RightParenthesis", "CastExpression")
    )


class LogicalAndExpression(ProductionTemplate):
    _template = "InclusiveOrExpression", repeat("DoubleAmpersand", "InclusiveOrExpression")

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
    _template = "AssignmentExpression", repeat("Comma", "AssignmentExpression")


class InclusiveOrExpression(ProductionTemplate):
    _template = "ExclusiveOrExpression", repeat("VerticalBar", "ExclusiveOrExpression")

###


class GenericSelection(ProductionTemplate):
    _template = "_Generic", "LeftParenthesis", "AssignmentExpression", "Comma", "GenericAssocList", "RightParenthesis"


class ExclusiveOrExpression(ProductionTemplate):
    _template = "AndExpression", repeat("Caret", "AndExpression")

###


class GenericAssocList(ProductionTemplate):
    _template = "GenericAssociation", repeat("Comma", "GenericAssociation")


class AndExpression(ProductionTemplate):
    _template = "EqualityExpression", repeat("Ampersand", "EqualityExpression")

###


class GenericAssociation(ProductionTemplate):
    _template = oneof("TypeName", "Default"), "Colon", "AssignmentExpression"


class EqualityExpression(ProductionTemplate):
    _template = "RelationalExpression", repeat(oneof("DoubleEquals", "ExclamationEquals"), "RelationalExpression")

###


class RelationalExpression(ProductionTemplate):
    _template = "ShiftExpression", repeat(oneof("LesserThan", "GreaterThan", "LesserThanEquals", "GreaterThanEquals"), "ShiftExpression")

###


class ShiftExpression(ProductionTemplate):
    _template = "AdditiveExpression", repeat(oneof("DoubleLesserThan", "DoubleGreaterThan"), "AdditiveExpression")

###


class AdditiveExpression(ProductionTemplate):
    _template = "MultiplicativeExpression", repeat(oneof("Plus", "Minus"), "MultiplicativeExpression")

###


class MultiplicativeExpression(ProductionTemplate):
    _template = "CastExpression", repeat(oneof("Asterisk", "Slash", "Percent"), "CastExpression")
