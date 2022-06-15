#pragma once

#include <stdint.h>

typedef enum {
    UnknownToken,
    EOFToken,
    LeftParenthesisToken,
    RightParenthesisToken,
    AsteriskToken,
    CommaToken,
    FullStopToken,
    ColonToken,
    SemicolonToken,
    EqualsToken,
    LeftSquareBracketToken,
    RightSquareBracketToken,
    UnderscoreToken,
    LeftCurlyBracketToken,
    RightCurlyBracketToken,
    ArrowToken,
    EllipsisToken,
    KeywordToken,
    IdentifierToken
} TokenType;

typedef struct {
    TokenType token;
    uint32_t page;
    uint32_t line;
    uint32_t column;
    uint32_t raw_length;
    uint32_t length;
} Token;

typedef enum {
    _BoolKeyword,
    _ByteKeyword,
    _Char1Keyword,
    _Char2Keyword,
    _Char3Keyword,
    _CharKeyword,
    _DoubleKeyword,
    _FloatKeyword,
    _IntKeyword,
    _LongKeyword,
    _ShortKeyword,
    _UbyteKeyword,
    _UintKeyword,
    _UlongKeyword,
    _UshortKeyword,
    AliasKeyword,
    AsKeyword,
    ConstKeyword,
    EnumKeyword,
    FromKeyword,
    FuncKeyword,
    ImportKeyword,
    OpenKeyword,
    PackageKeyword,
    PrivateKeyword,
    ProtectedKeyword,
    PublicKeyword,
    RestrictKeyword,
    StaticKeyword,
    StructKeyword,
    UnsafeKeyword,
    VarKeyword,
    VoidKeyword,
    VolatileKeyword
} KeywordType;

typedef struct {
    TokenType token;
    uint32_t page;
    uint32_t line;
    uint32_t column;
    uint32_t raw_length;
    uint32_t length;
    KeywordType keyword;
} Keyword;

typedef struct {
    TokenType token;
    uint32_t page;
    uint32_t line;
    uint32_t column;
    uint32_t raw_length;
    uint32_t length;
    uint8_t const * value;
} Identifier;

typedef struct {
    int (*peekByte)();
    void (*nextByte)();
    uint32_t page;
    uint32_t line;
    uint32_t column;
} LexerPointer;

Token * nextToken(LexerPointer *);
