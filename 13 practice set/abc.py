%{
#include <stdio.h>
%}

%%
[0-9]+\.[0-9]+    printf("%s is a floating point number\n", yytext);
[0-9]+            printf("%s is an integer number\n", yytext);
while|if|else|for printf("%s is a keyword\n", yytext);
int|float|char|double|void    printf("%s is a datatype\n", yytext);
[a-zA-Z_][a-zA-Z0-9_]*    printf("%s is an identifier\n", yytext);
[+=*/-]    printf("%s is an operator\n", yytext);
";"    printf("%s is a delimiter\n", yytext);
","    printf("%s is a separator\n", yytext);
#include[ ]*["<][a-zA-Z0-9_]+\.h[">]    printf("%s is a preprocessor\n", yytext);
%%

int yywrap(void) {
    return 1;
}



int main() {
    FILE *file = freopen("test.c", "r", stdin);
    if (!file) {
        printf("Error opening file: test.c\n");
        return 1;
    }
    yylex();
    return 0;
}
