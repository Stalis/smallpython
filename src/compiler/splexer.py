from sly import Lexer

r_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
r_KW = r_ID + r':'

r_CHAR = r'\S'
r_OPCHAR = r'[\!\@\#\$\%\^\&\*\-\+\=\~\/\?\<\>\,\;\|\‘\\]'

r_SQ_STRING = r"\'(\\\'|[^\'])*\'"
r_DQ_STRING = r'\"(\\\"|[^\"])*\"'
r_BQ_STRING = r'\`(\\\`|[^\`])*\`'

r_BIN_DIGIT = r'[0-1]'
r_OCT_DIGIT = r'[0-7]'
r_DEC_DIGIT = r'[0-9]'
r_HEX_DIGIT = r'[0-9A-Za-z]'

r_HEX_NUMBER = r'0[xX]' + r_HEX_DIGIT + r'+'
r_OCT_NUMBER = r'0[oO]' + r_OCT_DIGIT + r'+'
r_BIN_NUMBER = r'0[bB]' + r_BIN_DIGIT + r'+'
r_INTEGER = r'\-?' + r_DEC_DIGIT + r'+'
r_FLOAT = r'\-?' + r_DEC_DIGIT + r'*\.' + r_INTEGER


class SPLexer(Lexer):
    tokens = {
        # Literals
        LITERAL_HEX, LITERAL_OCT, LITERAL_OCT, LITERAL_BIN, LITERAL_DEC, LITERAL_FLOAT,
        LITERAL_STRING, LITERAL_COMMENT, LITERAL_CHAR,
        # SYMBOLS
        SYMBOL_KW_SELECTOR, SYMBOL_OP_SELECTOR, SYMBOL_UN_SELECTOR,
        # IDs
        ID_KEYWORD, ID_INPUT_ARG, ID_NAME,
        # Keywords
        KW_SELF, KW_SUPER, KW_THIS_CONTEXT, KW_NIL, KW_TRUE, KW_FALSE,
        # OPs
        OP_RETURN, OP_ASSIGN, OP_CASCADE, OP_CUSTOM,
        # Delimiters
        NEWLINE, COMMA
    }
    ignore = ' \t\r'
    literals = {'[', ']', '(', ')', '{', '}', '|', '#{', '<', '>'}

    def __init__(self):
        self.nesting_level = 0
    # Literals
    LITERAL_HEX = r'0[xX]' + r_HEX_DIGIT + r'+'
    LITERAL_OCT = r'0[oO]' + r_OCT_DIGIT + r'+'
    LITERAL_BIN = r'0[bB]' + r_BIN_DIGIT + r'+'
    LITERAL_DEC = r_INTEGER
    LITERAL_FLOAT = r_FLOAT
    LITERAL_STRING = r_SQ_STRING
    LITERAL_COMMENT = r_DQ_STRING
    LITERAL_CHAR = r'\$' + r_CHAR

    # IDs
    SYMBOL_KW_SELECTOR = r'#(' + r_KW + r')+'
    SYMBOL_OP_SELECTOR = r'#(' + r_OPCHAR + r')+'
    SYMBOL_UN_SELECTOR = r'#' + r_ID
    ID_KEYWORD = r_ID + r':'
    ID_INPUT_ARG = r':' + r_ID
    ID_NAME = r_ID

    # Keywords
    ID_NAME['self'] = KW_SELF
    ID_NAME['super'] = KW_SUPER
    ID_NAME['thisContext'] = KW_THIS_CONTEXT
    ID_NAME['nil'] = KW_NIL
    ID_NAME['True'] = KW_TRUE
    ID_NAME['False'] = KW_FALSE

    # Reserved OPs
    OP_RETURN = r'\^'
    OP_ASSIGN = r':='
    OP_CASCADE = r'\;'
    OP_CUSTOM = r_OPCHAR + r'+'

    @_(r'\[')
    def context_open(self, t):
        t.type = 'CONTEXT_OPEN'
        self.nesting_level += 1
        return t

    @_(r'\]')
    def context_close(self, t):
        t.type = 'CONTEXT_CLOSE'
        self.nesting_level -= 1
        return t

    COMMA = r'\.'

    @_(r'\n+')
    def NEWLINE(self, t):
        self.lineno += len(t.value)
        return t

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
