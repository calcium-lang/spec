#include "lexer.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define controlChar(c) ((c >= 0x00 && c <= 0x1F) || c == 0x7F)

#define printableChar(c) (c >= 0x20 && c <= 0x7E)

#define spaceChar(c) ((c >= 0x08 && c <= 0x0D) || c == 0x20)

#define symbolChar(c) ((c >= 0x21 && c <= 0x2F) || (c >= 0x3A && c <= 0x40) || (c >= 0x5B && c <= 0x60) || (c >= 0x7B && c <= 0x7E))

#define digitChar(c) (c >= 0x30 && c <= 0x39)

#define letterChar(c) ((c >= 0x41 && c <= 0x5A) || (c >= 0x61 && c <= 0x7A))

#define lowerLetterChar(c) (c >= 0x61 && c <= 0x7A)

#define upperLetterChar(c) (c >= 0x41 && c <= 0x5A)

#define UTF8Char1Start(c) (c >= 0x00 && c <= 0x7F)

#define UTF8Char2Start(c) (c >= 0xC0 && c <= 0xDF)

#define UTF8Char3Start(c) (c >= 0xE0 && c <= 0xEF)

#define UTF8Char4Start(c) (c >= 0xF0 && c <= 0xF7)

#define UTF8CharCont(c) (c >= 0x80 && c <= 0xBF)

#define UTF8CharInvalidStart(c) ((c >= 0x80 && c <= 0xBF) || (c >= 0xF8 && c <= 0xFF))

static Token * simpleToken(LexerPointer * ptr, TokenType type, uint32_t length) {
    Token * token = malloc(sizeof(Token));

    if (token != NULL) {
        token->token = type;
        token->page = ptr->page;
        token->line = ptr->line;
        token->column = ptr->column;
        token->raw_length = length;
        token->length = length;
    }

    ptr->column += length;
    return token;
}

static Token * keyword(LexerPointer * ptr, KeywordType type, uint32_t length) {
    Keyword * kw = malloc(sizeof(Keyword));

    if (kw != NULL) {
        kw->token = KeywordToken;
        kw->page = ptr->page;
        kw->line = ptr->line;
        kw->column = ptr->column;
        kw->raw_length = length;
        kw->length = length;
        kw->keyword = type;
    }

    ptr->column += length;
    return (Token *)kw;
}

static int8_t nextUTF8(LexerPointer * ptr, uint8_t buffer[4]) {
    int next = ptr->peekByte();

    if (UTF8Char1Start(next)) {
        buffer[0] = next;
        ptr->nextByte();
        return 1;
    } else if (UTF8Char2Start(next)) {
        buffer[0] = next;
        ptr->nextByte();
        next = ptr->peekByte();

        if (UTF8CharCont(next)) {
            buffer[1] = next;
            ptr->nextByte();
            return 2;
        } else {
            return -1;
        }
    } else if (UTF8Char3Start(next)) {
        buffer[0] = next;
        ptr->nextByte();
        next = ptr->peekByte();

        if (UTF8CharCont(next)) {
            buffer[1] = next;
            ptr->nextByte();
            next = ptr->peekByte();

            if (UTF8CharCont(next)) {
                buffer[2] = next;
                ptr->nextByte();
                return 3;
            } else {
                return -2;
            }
        } else {
            return -1;
        }
    } else if (UTF8Char4Start(next)) {
        buffer[0] = next;
        ptr->nextByte();
        next = ptr->peekByte();

        if (UTF8CharCont(next)) {
            buffer[1] = next;
            ptr->nextByte();
            next = ptr->peekByte();

            if (UTF8CharCont(next)) {
                buffer[2] = next;
                ptr->nextByte();
                next = ptr->peekByte();

                if (UTF8CharCont(next)) {
                    buffer[3] = next;
                    ptr->nextByte();
                    return 4;
                } else {
                    return -3;
                }
            } else {
                return -2;
            }
        } else {
            return -1;
        }
    } else {
        buffer[0] = next;
        ptr->nextByte();
        return -1;
    }
}

static uint8_t space(LexerPointer * ptr, int next) {
    if (next == '\b') {
        ptr->nextByte();

        if (ptr->column > 1) {
            ptr->column--;
        }
    } else if (next == '\t') {
        ptr->nextByte();
        ptr->column += 8 - (ptr->column - 1) % 8;
    } else if (next == '\n') {
        ptr->nextByte();
        ptr->line++;
        ptr->column = 1;
    } else if (next == '\v') {
        ptr->nextByte();
        ptr->line++;
    } else if (next == '\f') {
        ptr->nextByte();
        ptr->page++;
        ptr->line = 1;
        ptr->column = 1;
    } else if (next == '\r') {
        ptr->nextByte();
        ptr->column = 1;
    } else if (next == ' ') {
        ptr->nextByte();
        ptr->column++;
    } else {
        return 0;
    }

    return 1;
}

typedef struct {
    uint32_t increment;
    uint32_t length;
    uint32_t max_length;
    uint8_t * ptr;
} VarStr;

static uint8_t addByte(VarStr * buffer, uint8_t b) {
    if (buffer != NULL) {
        if (buffer->ptr == NULL || buffer->length >= buffer->max_length) {
            buffer->length = buffer->max_length;
            uint8_t * aux = realloc(buffer->ptr, buffer->max_length + buffer->increment + 1);

            if (aux != NULL) {
                buffer->ptr = aux;
            } else {
                return 0;
            }

            memset(&(buffer->ptr[buffer->max_length + 1]), '\0', buffer->increment);

            buffer->max_length += buffer->increment;
        }

        buffer->ptr[buffer->length] = b;
        buffer->length++;
        return 1;
    } else {
        return 0;
    }
}

Token * nextToken(LexerPointer * ptr) {
    if (ptr != NULL) {
        while (1) {
            int next = ptr->peekByte();

            if (next != EOF) {
                if (space(ptr, next)) {
                    //
                } else if (next == '(') {
                    ptr->nextByte();
                    return simpleToken(ptr, LeftParenthesisToken, 1);
                } else if (next == ')') {
                    ptr->nextByte();
                    return simpleToken(ptr, RightParenthesisToken, 1);
                } else if (next == '*') {
                    ptr->nextByte();
                    return simpleToken(ptr, AsteriskToken, 1);
                } else if (next == ',') {
                    ptr->nextByte();
                    return simpleToken(ptr, CommaToken, 1);
                } else if (next == '-') {
                    ptr->nextByte();
                    next = ptr->peekByte();

                    if (next == '>') {
                        ptr->nextByte();
                        return simpleToken(ptr, ArrowToken, 2);
                    } else {
                        fprintf(stderr, "Lexical error: Unknown token '-' found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                        return simpleToken(ptr, UnknownToken, 1);
                    }
                } else if (next == '.') {
                    ptr->nextByte();
                    next = ptr->peekByte();

                    if (next == '.') {
                        ptr->nextByte();
                        next = ptr->peekByte();

                        if (next == '.') {
                            ptr->nextByte();
                            return simpleToken(ptr, EllipsisToken, 3);
                        } else {
                            fprintf(stderr, "Lexical error: Unknown token '..' found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 2);
                            return simpleToken(ptr, UnknownToken, 2);
                        }
                    } else {
                        return simpleToken(ptr, FullStopToken, 1);
                    }
                } else if (next == '/') {
                    ptr->nextByte();
                    next = ptr->peekByte();

                    if (next == '*') {
                        ptr->column++;

                        while (1) {
                            do {
                                if (!space(ptr, next)) {
                                    uint8_t buffer[4];
                                    int8_t length = nextUTF8(ptr, buffer);

                                    if (length < 0) {
                                        fprintf(stderr, "Lexical warning: UTF-8 error 0x");

                                        for (int i = 0; i < -length; i++) {
                                            fprintf(stderr, "%02hhx", buffer[i]);
                                        }

                                        fprintf(stderr, " found in comment at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                                    }

                                    ptr->column++;
                                }
                            } while ((next = ptr->peekByte()) != EOF && next != '*');

                            if (next == EOF) {
                                break;
                            } else {
                                do {
                                    ptr->nextByte();
                                    ptr->column++;
                                } while ((next = ptr->peekByte()) == '*');

                                if (next == EOF) {
                                    break;
                                } else if (next == '/') {
                                    ptr->nextByte();
                                    ptr->column++;
                                    break;
                                }
                            }
                        }
                    } else if (next == '/') {
                        ptr->column++;

                        do {
                            if (!space(ptr, next)) {
                                uint8_t buffer[4];
                                int8_t length = nextUTF8(ptr, buffer);

                                if (length < 0) {
                                    fprintf(stderr, "Lexical warning: UTF-8 error 0x");

                                    for (int i = 0; i < -length; i++) {
                                        fprintf(stderr, "%02hhx", buffer[i]);
                                    }

                                    fprintf(stderr, " found in comment at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                                }

                                ptr->column++;
                            }
                        } while ((next = ptr->peekByte()) != EOF && next != '\n' && next != '\v' && next != '\f');
                    } else {
                        fprintf(stderr, "Lexical error: Unknown token '/' found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                        return simpleToken(ptr, UnknownToken, 1);
                    }
                } else if (next == ':') {
                    ptr->nextByte();
                    return simpleToken(ptr, ColonToken, 1);
                } else if (next == ';') {
                    ptr->nextByte();
                    return simpleToken(ptr, SemicolonToken, 1);
                } else if (next == '=') {
                    ptr->nextByte();
                    return simpleToken(ptr, EqualsToken, 1);
                } else if (next == '[') {
                    ptr->nextByte();
                    return simpleToken(ptr, LeftSquareBracketToken, 1);
                } else if (next == ']') {
                    ptr->nextByte();
                    return simpleToken(ptr, RightSquareBracketToken, 1);
                } else if (next == '_') {
                    ptr->nextByte();
                    next = ptr->peekByte();

                    if (next == '_' || letterChar(next) || digitChar(next) || UTF8Char2Start(next) || UTF8Char3Start(next) || UTF8Char4Start(next)) {
                        VarStr str = {
                            .increment = 7
                        };
                        uint32_t raw_length = 1;
                        uint32_t length = 1;

                        if (!addByte(&str, '_')) {
                            free(str.ptr);
                            return NULL;
                        }

                        do {
                            uint8_t buffer[4];
                            int8_t l = nextUTF8(ptr, buffer);

                            if (l > 0) {
                                for (int i = 0; i < l; i++) {
                                    if (!addByte(&str, buffer[i])) {
                                        free(str.ptr);
                                        return NULL;
                                    }
                                }

                                raw_length += l;
                                length++;
                            } else {
                                fprintf(stderr, "Lexical error: Unknown token '%s' with UTF-8 error 0x", str.ptr);
                                free(str.ptr);

                                for (int i = 0; i < -l; i++) {
                                    fprintf(stderr, "%02hhx", buffer[i]);
                                }

                                fprintf(stderr, " found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + length + 1);

                                raw_length += -l;
                                length++;
                                Token * unk = malloc(sizeof(Token));

                                if (unk != NULL) {
                                    unk->token = UnknownToken;
                                    unk->page = ptr->page;
                                    unk->line = ptr->line;
                                    unk->column = ptr->column;
                                    unk->raw_length = raw_length;
                                    unk->length = length;
                                }

                                ptr->column += length;
                                return unk;
                            }
                        } while ((next = ptr->peekByte()) == '_' || letterChar(next) || digitChar(next) || UTF8Char2Start(next) || UTF8Char3Start(next) || UTF8Char4Start(next));

                        if (raw_length == length && length >= 4 && length <= 7) {
                            if (strcmp((char *)str.ptr, "_bool") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _BoolKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_byte") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _ByteKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_char1") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _Char1Keyword, length);
                            } else if (strcmp((char *)str.ptr, "_char2") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _Char2Keyword, length);
                            } else if (strcmp((char *)str.ptr, "_char3") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _Char3Keyword, length);
                            } else if (strcmp((char *)str.ptr, "_char") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _CharKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_double") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _DoubleKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_float") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _FloatKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_int") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _IntKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_long") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _LongKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_short") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _ShortKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_ubyte") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _UbyteKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_uint") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _UintKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_ulong") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _UlongKeyword, length);
                            } else if (strcmp((char *)str.ptr, "_ushort") == 0) {
                                free(str.ptr);
                                return keyword(ptr, _UshortKeyword, length);
                            }
                        }

                        Identifier * id = malloc(sizeof(Identifier));

                        if (id != NULL) {
                            id->token = IdentifierToken;
                            id->page = ptr->page;
                            id->line = ptr->line;
                            id->column = ptr->column;
                            id->raw_length = raw_length;
                            id->length = length;
                            id->value = str.ptr;
                        } else {
                            free(str.ptr);
                        }

                        ptr->column += length;
                        return (Token *)id;
                    } else {
                        return simpleToken(ptr, UnderscoreToken, 1);
                    }
                } else if (next == '{') {
                    ptr->nextByte();
                    return simpleToken(ptr, LeftCurlyBracketToken, 1);
                } else if (next == '}') {
                    ptr->nextByte();
                    return simpleToken(ptr, RightCurlyBracketToken, 1);
                } else if (letterChar(next)) {
                    VarStr str = {
                        .increment = 8
                    };
                    uint32_t raw_length = 0;
                    uint32_t length = 0;

                    do {
                        uint8_t buffer[4];
                        int8_t l = nextUTF8(ptr, buffer);

                        if (l > 0) {
                            for (int i = 0; i < l; i++) {
                                if (!addByte(&str, buffer[i])) {
                                    free(str.ptr);
                                    return NULL;
                                }
                            }

                            raw_length += l;
                            length++;
                        } else {
                            fprintf(stderr, "Lexical error: Unknown token '%s' with UTF-8 error 0x", str.ptr);
                            free(str.ptr);

                            for (int i = 0; i < -l; i++) {
                                fprintf(stderr, "%02hhx", buffer[i]);
                            }

                            fprintf(stderr, " found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + length + 1);

                            raw_length += -l;
                            length++;
                            Token * unk = malloc(sizeof(Token));

                            if (unk != NULL) {
                                unk->token = UnknownToken;
                                unk->page = ptr->page;
                                unk->line = ptr->line;
                                unk->column = ptr->column;
                                unk->raw_length = raw_length;
                                unk->length = length;
                            }

                            ptr->column += length;
                            return unk;
                        }
                    } while ((next = ptr->peekByte()) == '_' || letterChar(next) || digitChar(next) || UTF8Char2Start(next) || UTF8Char3Start(next) || UTF8Char4Start(next));

                    if (raw_length == length && length >= 2 && length <= 8) {
                        if (strcmp((char *)str.ptr, "alias") == 0) {
                            free(str.ptr);
                            return keyword(ptr, AliasKeyword, length);
                        } else if (strcmp((char *)str.ptr, "as") == 0) {
                            free(str.ptr);
                            return keyword(ptr, AsKeyword, length);
                        } else if (strcmp((char *)str.ptr, "const") == 0) {
                            free(str.ptr);
                            return keyword(ptr, ConstKeyword, length);
                        } else if (strcmp((char *)str.ptr, "enum") == 0) {
                            free(str.ptr);
                            return keyword(ptr, EnumKeyword, length);
                        } else if (strcmp((char *)str.ptr, "from") == 0) {
                            free(str.ptr);
                            return keyword(ptr, FromKeyword, length);
                        } else if (strcmp((char *)str.ptr, "func") == 0) {
                            free(str.ptr);
                            return keyword(ptr, FuncKeyword, length);
                        } else if (strcmp((char *)str.ptr, "import") == 0) {
                            free(str.ptr);
                            return keyword(ptr, ImportKeyword, length);
                        } else if (strcmp((char *)str.ptr, "open") == 0) {
                            free(str.ptr);
                            return keyword(ptr, OpenKeyword, length);
                        } else if (strcmp((char *)str.ptr, "package") == 0) {
                            free(str.ptr);
                            return keyword(ptr, PackageKeyword, length);
                        } else if (strcmp((char *)str.ptr, "private") == 0) {
                            free(str.ptr);
                            return keyword(ptr, PrivateKeyword, length);
                        } else if (strcmp((char *)str.ptr, "protected") == 0) {
                            free(str.ptr);
                            return keyword(ptr, ProtectedKeyword, length);
                        } else if (strcmp((char *)str.ptr, "public") == 0) {
                            free(str.ptr);
                            return keyword(ptr, PublicKeyword, length);
                        } else if (strcmp((char *)str.ptr, "restrict") == 0) {
                            free(str.ptr);
                            return keyword(ptr, RestrictKeyword, length);
                        } else if (strcmp((char *)str.ptr, "static") == 0) {
                            free(str.ptr);
                            return keyword(ptr, StaticKeyword, length);
                        } else if (strcmp((char *)str.ptr, "struct") == 0) {
                            free(str.ptr);
                            return keyword(ptr, StructKeyword, length);
                        } else if (strcmp((char *)str.ptr, "unsafe") == 0) {
                            free(str.ptr);
                            return keyword(ptr, UnsafeKeyword, length);
                        } else if (strcmp((char *)str.ptr, "var") == 0) {
                            free(str.ptr);
                            return keyword(ptr, VarKeyword, length);
                        } else if (strcmp((char *)str.ptr, "void") == 0) {
                            free(str.ptr);
                            return keyword(ptr, VoidKeyword, length);
                        } else if (strcmp((char *)str.ptr, "volatile") == 0) {
                            free(str.ptr);
                            return keyword(ptr, VolatileKeyword, length);
                        }
                    }

                    Identifier * id = malloc(sizeof(Identifier));

                    if (id != NULL) {
                        id->token = IdentifierToken;
                        id->page = ptr->page;
                        id->line = ptr->line;
                        id->column = ptr->column;
                        id->raw_length = raw_length;
                        id->length = length;
                        id->value = str.ptr;
                    } else {
                        free(str.ptr);
                    }

                    ptr->column += length;
                    return (Token *)id;
                } else if (UTF8Char1Start(next)) {
                    fprintf(stderr, "Lexical error: Unknown token '%c' found at %u:%u:%u-%u:%u:%u\n", next, ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                    ptr->nextByte();
                    return simpleToken(ptr, UnknownToken, 1);
                } else if (!UTF8CharInvalidStart(next)) {
                    VarStr str = {
                        .increment = 8
                    };
                    uint32_t raw_length = 0;
                    uint32_t length = 0;

                    do {
                        uint8_t buffer[4];
                        int8_t l = nextUTF8(ptr, buffer);

                        if (l > 0) {
                            for (int i = 0; i < l; i++) {
                                if (!addByte(&str, buffer[i])) {
                                    free(str.ptr);
                                    return NULL;
                                }
                            }

                            raw_length += l;
                            length++;
                        } else {
                            fprintf(stderr, "Lexical error: Unknown token '%s' with UTF-8 error 0x", str.ptr);
                            free(str.ptr);

                            for (int i = 0; i < -l; i++) {
                                fprintf(stderr, "%02hhx", buffer[i]);
                            }

                            fprintf(stderr, " found at %u:%u:%u-%u:%u:%u\n", ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + length + 1);

                            raw_length += -l;
                            length++;
                            Token * unk = malloc(sizeof(Token));

                            if (unk != NULL) {
                                unk->token = UnknownToken;
                                unk->page = ptr->page;
                                unk->line = ptr->line;
                                unk->column = ptr->column;
                                unk->raw_length = raw_length;
                                unk->length = length;
                            }

                            ptr->column += length;
                            return unk;
                        }
                    } while ((next = ptr->peekByte()) == '_' || letterChar(next) || digitChar(next) || UTF8Char2Start(next) || UTF8Char3Start(next) || UTF8Char4Start(next));

                    Identifier * id = malloc(sizeof(Identifier));

                    if (id != NULL) {
                        id->token = IdentifierToken;
                        id->page = ptr->page;
                        id->line = ptr->line;
                        id->column = ptr->column;
                        id->raw_length = raw_length;
                        id->length = length;
                        id->value = str.ptr;
                    } else {
                        free(str.ptr);
                    }

                    return (Token *)id;
                } else {
                    fprintf(stderr, "Lexical error: UTF-8 error 0x%02hhx found at %u:%u:%u-%u:%u:%u\n", next, ptr->page, ptr->line, ptr->column, ptr->page, ptr->line, ptr->column + 1);
                    ptr->nextByte();
                    return simpleToken(ptr, UnknownToken, 1);
                }
            } else {
                return simpleToken(ptr, EOFToken, 0);
            }
        }
    } else {
        return NULL;
    }
}
