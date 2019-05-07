#Larry Liu
#Create a parser for simple functionality with the ability to do numerical calculations, use if else statements and the ability to print to console. Uses ply.
varDic = {}

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class basicNode: #Node that is at top of the tree.
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        return self.value

    def execute(self):
        # print(type(self.value.evaluate()))
        if type(self.value) == str:
            print('\'' + self.value + '\'')
        elif type(self.value) == int or type(self.value) == float:
            print(self.value)
        elif type(self.value.evaluate()) == str:
            # print('This is a string.')
            print('\'' + self.value.evaluate() + '\'')
        else:
            print(self.value.evaluate())
        return

class whateverNode(Node): #Recursive Node
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return self.value

class ListNode(Node): #Node that processes list objects with constraints.
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        List = []
        for items in self.value:
            if type(items) in [str, int, float, list]:
                List.append(items)
            else:
                List.append(items.evaluate())
        return List

class changeNode(Node): #changes the variable of the node
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        if type(v2) in [str,int,list,float]:
            varDic[self.v1] = self.v2
        else:
            varDic[self.v1] = self.v2.evaluate()
    def execute(self):
        varDic[self.v1]  = self.v2.evaluate()
    def evaluate(self):
        return varDic[self.v1]

class listVarNode(Node): #Node that process a single node in List
    def __init__(self,v1,v2,v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def execute(self):
        currList = varDic[self.v1.v1]
        for i in range(0, len(self.v3)):
            if i == len(self.v3) - 1:
                currList[self.v3[i].evaluate()] = self.v2.evaluate()
            else:
                currList = currList[self.v3[i].evaluate()]

class NumberNode(Node): #Node that processes Numbers, whether they have decimal or not.
    def __init__(self, v):
        if type(v) == int:
            self.value = v
        elif ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value


class BoolNode(Node): #Node that processes true and false.
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return self.value

class ifNode(Node): #Node that processes if statements.
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def execute(self):
        if self.v1.evaluate() == True:
            self.v2.execute()

class ifElseNode(Node): #Node that processes if and else statements.
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def execute(self):
        if self.v1.evaluate() == True:
            self.v2.execute()
        else:
            self.v3.execute()
class whileNode(Node): #Node that processes while loops.
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def execute(self):
        while self.v1.evaluate() == True:
            self.v2.execute()

class StringNode(Node): #Node that processes strings.
    def __init__(self, v):
        v = v.replace("\"", "")
        v = v.replace("\'", "")
        self.value = str(v)
    def evaluate(self):
        return self.value

class notNode(Node):# Node that processes the not keyword.
    def __init__(self, v1):
        self.v1 = v1
    def evaluate(self):
        if not self.v1.evaluate():
            return True
        else:
            return False
class variableNode(Node): #Node that processes all variables.
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value

class BopNode(Node): #Node that processes symbols, all of them.
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op



    def evaluate(self):
        # if type(self.v1) == variableNode:
        #     self.v1 = varDic[self.v1.evaluate()]
        # if type(self.v2) == variableNode:
        #     self.v2 = varDic[self.v2.evaluate()]
        # if type(self.v1) == str:
        #     self.v1 = stringNode(self.v1)
        # elif type(self.v1) == int:
        #     self.v1 = NumberNode(self.v1)
        # elif type(self.v1) == float:
        #     self.v1 = NumberNode(self.v1)
        # elif type(self.v1) == list:
        #     self.v1 = ListNode(self.v1)
        # if type(self.v2) == str:
        #     self.v2 = stringNode(self.v2)
        # elif type(self.v2) == int:
        #     self.v2 = NumberNode(self.v2)
        # elif type(self.v2) == float:
        #     self.v2 = NumberNode(self.v2)
        # elif type(self.v2) == list:
        #     self.v2  = ListNode(self.v2)
        # if type(self.v1) == variableNode:
        #     self.v1 = changeNode[self.v1.evaluate()]
        # if type(self.v2) == variableNode:
        #     self.v2 = changeNode[self.v2.evaluate()]
        if self.op == '+':
            return self.v1.evaluate() + self.v2.evaluate()
        elif self.op == '[':
            return self.v1.evaluate()[self.v2.evaluate()]
        elif self.op == '-':
            return self.v1.evaluate() - self.v2.evaluate()
        elif self.op == '*':
            return self.v1.evaluate() * self.v2.evaluate()
        elif self.op == '/':
            return self.v1.evaluate() / self.v2.evaluate()
        elif self.op == '**':
            return self.v1.evaluate() ** self.v2.evaluate()
        elif self.op == '%':
            return self.v1.evaluate() % self.v2.evaluate()
        elif self.op == '//':
            return self.v1.evaluate() // self.v2.evaluate()
        elif self.op == '>':
            if self.v1.evaluate() > self.v2.evaluate():
                return True
            elif self.v1.evaluate() <= self.v2.evaluate():
                return False
        elif self.op == '<':
            # print(varDic)
            if self.v1.evaluate() < self.v2.evaluate():
                return True
            elif self.v1.evaluate() >= self.v2.evaluate():
                return False
        elif self.op == '>=':
            if self.v1.evaluate() >= self.v2.evaluate():
                return True
            elif self.v1.evaluate() < self.v2.evaluate():
                return False
        elif self.op == '<=':
            if self.v1.evaluate() <= self.v2.evaluate():
                return True
            elif self.v1.evaluate() > self.v2.evaluate():
                return False
        elif self.op == '==':
            if self.v1.evaluate() == self.v2.evaluate():
                return True
            elif self.v1.evaluate() != self.v2.evaluate():
                return False
        elif self.op == '<>':
            if self.v1.evaluate() != self.v2.evaluate():
                return True
            elif self.v1.evaluate() == self.v2.evaluate():
                return False
        elif self.op == 'and':
            if self.v1.evaluate() and self.v2.evaluate():
                return True
            else:
                return False
        elif self.op == 'or':
            if self.v1.evaluate() or self.v2.evaluate():
                return True
            else:
                return False
        elif self.op == 'in':
            if self.v1.evaluate() in self.v2.evaluate():
                return True
            else:
                return False


class NegNode(Node): #Node that processes negative numbers
    def __init__(self, v1):
        self.v1 = v1

    def evaluate(self):
        return -self.v1.evaluate()

#
#
# class BopNode0(Node):
#     def __init__(self, op, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
#         self.op = op
#
#     def evaluate(self):
#         if (self.op == '+'):
#             return -self.v1.evaluate() + -self.v2.evaluate()
#         elif (self.op == '-'):
#             return -self.v1.evaluate() - -self.v2.evaluate()
#         elif (self.op == '*'):
#             return -self.v1.evaluate() * -self.v2.evaluate()
#         elif (self.op == '/'):
#             return -self.v1.evaluate() / -self.v2.evaluate()
#         elif (self.op == '**'):
#             return -self.v1.evaluate() ** -self.v2.evaluate()
#         elif (self.op == '%'):
#             return -self.v1.evaluate() % -self.v2.evaluate()
#         elif (self.op == '//'):
#             return -self.v1.evaluate() // -self.v2.evaluate()
#         elif (self.op == '>'):
#             if(-self.v1.evaluate() > -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() < -self.v2.evaluate()):
#                 return False
#         elif (self.op == '<'):
#             if(-self.v1.evaluate() < -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() > -self.v2.evaluate()):
#                 return False
#         elif (self.op == '>='):
#             if(-self.v1.evaluate() >= -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() <= -self.v2.evaluate()):
#                 return False
#         elif (self.op == '<='):
#             if(-self.v1.evaluate() <= -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() >= -self.v2.evaluate()):
#                 return False
#         elif (self.op == '=='):
#             if(-self.v1.evaluate() == -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() != -self.v2.evaluate()):
#                 return False
#         elif (self.op == '><'):
#             if(-self.v1.evaluate() != -self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() == -self.v2.evaluate()):
#                 return False
#
# class BopNode1half(Node):
#     def __init__(self, op, op1, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
#         self.op = op
#         self.op1 = op1
#
#
#     def evaluate(self):
#         if (self.op == '+'):
#             return self.v1.evaluate() + -self.v2.evaluate()
#         elif (self.op == '-'):
#             return self.v1.evaluate() - -self.v2.evaluate()
#         elif (self.op == '*'):
#             return self.v1.evaluate() * -self.v2.evaluate()
#         elif (self.op == '/'):
#             return self.v1.evaluate() / -self.v2.evaluate()
#         elif (self.op == '**'):
#             return self.v1.evaluate() ** -self.v2.evaluate()
#         elif (self.op == '%'):
#             return self.v1.evaluate() % -self.v2.evaluate()
#         elif (self.op == '//'):
#             return self.v1.evaluate() // -self.v2.evaluate()
#         elif (self.op == '>'):
#             if(self.v1.evaluate() > -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() < -self.v2.evaluate()):
#                 return False
#         elif (self.op == '<'):
#             if(self.v1.evaluate() < -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() > -self.v2.evaluate()):
#                 return False
#         elif (self.op == '>='):
#             if(self.v1.evaluate() >= -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() <= -self.v2.evaluate()):
#                 return False
#         elif (self.op == '<='):
#             if(self.v1.evaluate() <= -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() >= -self.v2.evaluate()):
#                 return False
#         elif (self.op == '=='):
#             if(self.v1.evaluate() == -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() != -self.v2.evaluate()):
#                 return False
#         elif (self.op == '><'):
#             if(self.v1.evaluate() != -self.v2.evaluate()):
#                 return True
#             elif(self.v1.evaluate() == -self.v2.evaluate()):
#                 return False
#
#
# class BopNode2(Node):
#     def __init__(self, op, op1, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
#         self.op1 = op1
#         self.op = op
#
#
#     def evaluate(self):
#         if (self.op == '+'):
#             return -self.v1.evaluate() + self.v2.evaluate()
#         elif (self.op == '-'):
#             return -self.v1.evaluate() - self.v2.evaluate()
#         elif (self.op == '*'):
#             return -self.v1.evaluate() * self.v2.evaluate()
#         elif (self.op == '/'):
#             return -self.v1.evaluate() / self.v2.evaluate()
#         elif (self.op == '**'):
#             return -self.v1.evaluate() ** self.v2.evaluate()
#         elif (self.op == '%'):
#             return -self.v1.evaluate() % self.v2.evaluate()
#         elif (self.op == '//'):
#             return -self.v1.evaluate() // self.v2.evaluate()
#         elif (self.op == '>'):
#             if(-self.v1.evaluate() > self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() < self.v2.evaluate()):
#                 return False
#         elif (self.op == '<'):
#             if(-self.v1.evaluate() < self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() > self.v2.evaluate()):
#                 return False
#         elif (self.op == '>='):
#             if(-self.v1.evaluate() >= self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() <= self.v2.evaluate()):
#                 return False
#         elif (self.op == '<='):
#             if(-self.v1.evaluate() <= self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() >= self.v2.evaluate()):
#                 return False
#         elif (self.op == '=='):
#             if(-self.v1.evaluate() == self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() != self.v2.evaluate()):
#                 return False
#         elif (self.op == '><'):
#             if(-self.v1.evaluate() != self.v2.evaluate()):
#                 return True
#             elif(-self.v1.evaluate() == self.v2.evaluate()):
#                 return False

class PrintNode(Node): #Node that evaluates the print statement.
    def __init__(self, v):
        self.value = v

    def execute(self):
        print(self.value.evaluate())


class BlockNode(Node): #Node that processes the entire block statment.
    def __init__(self, s):
        self.sl = [s]

    def execute(self):
        for statement in self.sl:
            statement.execute()

class EmptyNode(Node): #Edge case node that evaluates an empty block.
    def __init__(self):
        self.s1 = 0
    def execute(self):
        self.s1 = self.s1

#The following section determines how the blocks should be read and covers all the cases that are included in the above nodes.
tokens = [
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMI',
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EXPONENT', 'MOD', 'FLOOR', 'GREATER', 'GREATE', 'LESS', 'LESSE', 'ASSERTEQUAL',
    'NOTE', 'LBRACK', 'RBRACK', 'STRING', 'COMMA','EQUALS', 'NAME']

reserved = {'while' : 'WHILE', 'else' : 'ELSE', 'if': 'IF', 'print' : 'PRINT', 'True' : 'TRUE', 'False' : 'FALSE', 'in' : 'IN', 'not' : 'NOT', 'and' : 'AND', 'or' : 'OR' }
tokens += reserved.values()

# Tokens
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_MOD = r'\%'
t_FLOOR = r'\/\/'
t_GREATER = r'>'
t_GREATE = r'>='
t_LESS = r'<'
t_LESSE = r'<='
t_ASSERTEQUAL = r'=='
t_NOTE = r'<>'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COMMA = r'\,'
t_EQUALS = r'='

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'"[^"]*"|\'[^\']*\''
    t.value = StringNode(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t


# Ignored characters
t_ignore = "\t \n "


def t_error(t):
    print("Syntax error at '%s'" % t.value)


# Build the lexer
import ply.lex as lex

lex.lex()

# Parsing rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'GREATER', 'GREATE', 'LESS', 'LESSE', 'ASSERTEQUAL', 'NOTE'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FLOOR'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'EXPONENT'),
    ('left', 'LBRACK'),
    ('left', 'IF'),
    ('left', 'ELSE')
)

def p_block3(t): #Empty Node
    """
        block : LBRACE RBRACE
    """
    t[0] = EmptyNode()

def p_block(t): #Node with something in it that is recusively parsed
    """
    block : LBRACE inblock RBRACE
    """
    t[0] = t[2]



def p_inblock(t): #inblock can be both a statement and another block
    """
    inblock : smt inblock
    """
    t[0] = t[2]
    t[0].sl.insert(0, t[1])

def p_inblock3(t): #inblock can be just a block with another block
    """inblock : block inblock"""
    t[0] = t[2]
    t[0].sl.insert(0, t[1])

def p_block2(t): #inblock can be just one block ending the recursion for inblock
    """ inblock : block"""
    t[0] = BlockNode(t[1])

def p_inblock2(t): #inblock can just be one statement ending the recursivion for in block
    """
    inblock : smt
    """
    t[0] = BlockNode(t[1])

# def p_if_else_stmt(t):
#     """smt : IF LPAREN expression RPAREN block ELSE block smt
#             | IF LPAREN expression RPAREN block ELSE block"""
#     t[0] = ifElseNode(t[3], t[5], t[7])

def p_if_stmt(t): #if or if else statement recursion
    """smt :  IF LPAREN expression RPAREN block ELSE block
            | IF LPAREN expression RPAREN block
            """
    if len(t) > 6 and t[6] == "else":
        t[0] = ifElseNode(t[3], t[5], t[7])
    else:
        t[0] = ifNode(t[3], t[5])


def p_while_stmt(t): #while recurision
    """smt : WHILE LPAREN expression RPAREN block"""
    t[0] = whileNode(t[3], t[5])

def p_smt(t): #printing
    """
    smt : print_smt
    """
    t[0] = t[1]

def p_print_smt(t): #print statement, prints the statement inside expression
    """
    print_smt : PRINT LPAREN expression RPAREN SEMI
    """
    t[0] = PrintNode(t[3])

def p_assign2(t): # assigns the value to a variable
    """smt : expression EQUALS expression SEMI
            | expression listBrack EQUALS expression SEMI"""
    # print("t1" + str(t[1].v1))
    # if type(t[1].v1) == changeNode:
    #     print(t[1].v1.v1)
    if len(t) > 5:
        t[0] = listVarNode(t[1],t[4],t[2])
    else:
        t[0] = changeNode(t[1].v1, t[3])

def p_listbrack(t): #creates a list object
    """listBrack : LBRACK expression RBRACK followBrack
                | LBRACK expression RBRACK nextBrack"""
    t[4].insert(0, t[2])
    t[0] = t[4]

def p_next_brack(t): #for multi-dimensional arrays
    """nextBrack : LBRACK expression RBRACK followBrack"""
    t[0] = t[4]

def p_fol_brack(t):
    """followBrack :  """
    List = []
    t[0] = List


def p_expression_binop(t):#math operations
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPONENT expression
                  | expression MOD expression
                  | expression GREATER expression
                  | expression GREATE expression
                  | expression LESS expression
                  | expression LESSE expression
                  | expression ASSERTEQUAL expression
                  | expression NOTE expression
                  | expression AND expression
                  | expression OR expression
                  | expression IN expression
                  | expression FLOOR expression
                  | expression LBRACK expression RBRACK'''

    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_notop(t): #no operation
    '''expression : NOT expression'''
    t[0] = notNode(t[2])


def p_expression_negop(t): #negative numbers
    '''expression : MINUS expression'''
    t[0] = NegNode(t[2])

def p_expression_true(t): #boolean true
    'expression : TRUE'
    t[0] = BoolNode(True)

def p_expression_false(t): #boolean false
    'expression : FALSE'
    t[0] = BoolNode(False)



def p_list(t): #list parsing
    'expression : LIST'
    t[0] = t[1]

def p_listafter(t): #bracket listing
    'LIST : LBRACK listin RBRACK'
    t[0] = ListNode(t[2])

def p_listempty(t): #empty list
    'LIST : LBRACK RBRACK'
    t[0] = []


def p_list_internal(t): #objects in array
    'listin : expression tail'
    t[2].insert(0,t[1])
    t[0] = t[2]

def p_tail(t):  #recursion for listin
    'tail : COMMA expression tail'
    # print(t[3])
    # print(t[2])
    t[3].insert(0, t[2])
    t[0] = t[3]

def p_tail_none(t): #ends recursion for listin
    'tail : '
    List = []
    t[0] = List


# def p_expression_binop0(t):
#     '''expression :   MINUS expression PLUS MINUS expression
#                     | MINUS expression MINUS MINUS expression
#                     | MINUS expression TIMES MINUS expression
#                     | MINUS expression DIVIDE MINUS expression
#                     | MINUS expression EXPONENT MINUS expression
#                     | MINUS expression MOD MINUS expression
#                     | MINUS expression GREATER MINUS expression
#                     | MINUS expression GREATE MINUS expression
#                     | MINUS expression LESS MINUS expression
#                     | MINUS expression LESSE MINUS expression
#                     | MINUS expression ASSERTEQUAL MINUS expression
#                     | MINUS expression NOTE MINUS expression'''
#
#     t[0] = BopNode0(t[3], t[2], t[5])
#
# def p_expression_binop1half(t):
#     '''expression :   expression PLUS MINUS expression
#                     | expression MINUS MINUS expression
#                     | expression TIMES MINUS expression
#                     | expression DIVIDE MINUS expression
#                     | expression EXPONENT MINUS expression
#                     | expression MOD MINUS expression
#                     | expression GREATER MINUS expression
#                     | expression GREATE MINUS expression
#                     | expression LESS MINUS expression
#                     | expression LESSE MINUS expression
#                     | expression ASSERTEQUAL MINUS expression
#                     | expression NOTE MINUS expression'''
#     t[0] = BopNode1half(t[2], t[3], t[1], t[4])

# def p_expression_binop2(t):
#     '''expression :   MINUS expression PLUS expression
#                     | MINUS expression MINUS expression
#                     | MINUS expression TIMES expression
#                     | MINUS expression DIVIDE expression
#                     | MINUS expression EXPONENT expression
#                     | MINUS expression MOD expression
#                     | MINUS expression GREATER expression
#                     | MINUS expression GREATE expression
#                     | MINUS expression LESS expression
#                     | MINUS expression LESSE expression
#                     | MINUS expression ASSERTEQUAL expression
#                     | MINUS expression NOTE expression'''
#
#     t[0] = BopNode2(t[3], t[1], t[2], t[4])


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_str(t): #string parsing
    'expression : STRING'
    t[0] = t[1]


def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]


def p_factor_number(t): #number parsing
    'factor : NUMBER'
    t[0] = t[1]

def p_factor_name(t):
    'expression : NAME'
    if t[1] not in varDic:
        t[0] = changeNode(t[1], NumberNode(0))
    else:
        t[0] = changeNode(t[1], varDic.get(t[1]))

def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc

yacc.yacc()

import sys

# if (len(sys.argv) != 2):
#    sys.exit("invalid arguments")
# fd = open(sys.argv[1], 'r')
# code = ""
# for line in fd:
#    code += line.strip()

# code = "{print("hello");}"

# try:
    # while True:
    #    token = lex.token()
    #    if not token: break
    #    print(token)
def test(): #opens file to parse
    code = ""
    List = open(sys.argv[1], 'r')
    for line in List:
        code += line.strip()
    ast = yacc.parse(code, debug = 0)
    ast.execute()
# except Exception:
#     print("ERROR")

test()