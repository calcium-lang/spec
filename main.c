#include "lexer.h"
#include <stdio.h>

const uint8_t buffer[] = {
    'p', 'a', 'c', 'k', 'a', 'g', 'e', ' ', 'f', 'o', 'o', ';', '\n',
    'i', 'm', 'p', 'o', 'r', 't', ' ', 'f', 'o', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'l', 'a', 'n', 'g', ';', '\n'
};
uint32_t i = 0;

int peekByte() {
    if (i < sizeof(buffer)) {
        return buffer[i];
    } else {
        return EOF;
    }
}

void nextByte() {
    if (i < sizeof(buffer)) {
        i++;
    }
}

int main() {
    LexerPointer ptr = {
        .peekByte = peekByte,
        .nextByte = nextByte,
        .page = 1,
        .line = 1,
        .column = 1
    };
    Token * token;

    while ((token = nextToken(&ptr)) != NULL && token->token != EOFToken) {
        printf("%d (%u:%u:%u)\n", token->token, token->page, token->line, token->column);

        if (token->token == KeywordToken) {
            Keyword * kw = (Keyword *)token;
            printf("    %d\n", kw->keyword);
        } else if (token->token == IdentifierToken) {
            Identifier * id = (Identifier *)token;
            printf("    %s\n", id->value);
        }
    }

    return 0;
}
