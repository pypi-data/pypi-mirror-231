parser grammar CalculatorParser;

options {
    tokenVocab = CalculatorLexer;
}

prog:   (expr1 expr2 semicolon)+ EOF;
expr2: twoEquals expr1
;
expr1:   expr1 (asterisk|plus|hyphen|slash) expr1
    | digits
    ;

asterisk: ASTERISK;
plus: PLUS;
hyphen: HYPHEN;
slash: SLASH;
semicolon: SEMICOLON;
equals: EQUALS;
digit: DIGIT;
lineFeed: LINE_FEED;
upperAlphabet: UPPER_ALPHABET;
openParenthesis: OPEN_PARENTHESIS;
closeParenthesis: CLOSE_PARENTHESIS;
twoEquals: equals equals;
digits: digit+;