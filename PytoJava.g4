grammar PytoJava;

// Lexer rules
DEF      : 'def' ;
RETURN   : 'return' ;
PRINT    : 'print' ;
NUMBER   : [0-9]+ ;
IDENT    : [a-zA-Z][a-zA-Z0-9]* ;
MINUS    : '-' ;
MULTIPLY : '*' ;
ASSIGN   : '=' ;
LPAREN   : '(' ;
RPAREN   : ')' ;
COLON    : ':' ;
COMMA    : ',' ;
WS       : [ \t\r\n]+ -> skip ;

// Parser rules
pyton_line: (funcion | print_java | WS)*;

// Rule for a function definition
funcion: DEF IDENT LPAREN parametros RPAREN COLON cuerpo;

// Funcion de los parametros
parametros: IDENT (COMMA IDENT)*;  // Permite uno o más parámetros

// Funcion del cuerpo
cuerpo: statement+;

//Los elementos que contendra el cuerpo
statement: RETURN expresion 
        | IDENT ASSIGN expresion
        | print_java ;

// Expresion para leer el menos y la multiplicacion
expresion: term (MINUS term)*;

// Terminos de la multiplicacion
term: factor (MULTIPLY factor)*;

// Factores para el identificador , los numeros , las expresiones con los parentesis de abre y cierre
factor: IDENT | NUMBER | LPAREN expresion RPAREN;

// el contenido del print que lee del archivo .txt
print_java: PRINT LPAREN expresion RPAREN;