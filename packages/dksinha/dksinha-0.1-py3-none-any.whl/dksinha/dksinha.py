import ply.lex as lex
import ply.yacc as yacc

class CalculatorLexer:
    # Define the lexer tokens
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    # Regular expressions for lexer tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ignore = ' \t\n'

    def t_error(self, t):
        print(f"Invalid character: {t.value[0]}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

class CalculatorParser:
    def __init__(self):
        self.tokens = CalculatorLexer().tokens

    def p_expression(self, p):
        '''
        expression : expression PLUS term
                  | expression MINUS term
                  | term
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

    def p_term(self, p):
        '''
        term : term TIMES factor
             | term DIVIDE factor
             | factor
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            if p[3] == 0:
                raise ZeroDivisionError("Division by zero")
            p[0] = p[1] / p[3]

    def p_factor(self, p):
        '''
        factor : NUMBER
               | LPAREN expression RPAREN
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_error(self, p):
        print("Syntax error")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
    
def preBuild(user_arg):
    lexer = CalculatorLexer()
    lexer.build()

    parser = CalculatorParser()
    parser.build()

    input_str = user_arg
    expressions = input_str.split(';')

    for expression in expressions:
        if expression.strip():
            lexer.lexer.input(expression)
            result = parser.parser.parse()
            print(f"Result: {result}")