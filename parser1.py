##
## Very simple interpreter
##
## Challenge: add a power operator
##
import sys
INT = 1

##
## Tokeniser: converts strings to a list of words
##
def tokens(cs):
    tks = []
    NUM = 0
    NONUM = 1
    state = NONUM
    word = ""
    while len(cs) > 0:
        c = cs[0]
        cs = cs[1:]
        if state == NUM:
            if c.isdigit():
                word = word + c
            elif c in ['+','-','*','/','(',')']:
                tks.append(word)
                tks.append(c)
                word = ""
                state = NONUM
            elif c.isspace():
                tks.append(word)
                word = ""
                state = NONUM
            else:
                print("Illegal character:", c)
                sys.exit()
                
        elif state == NONUM:
            if c.isdigit():
                word = c
                state = NUM
            elif c in ['+','-','*','/','(',')']:
                tks.append(c)
                state = NONUM
            elif c.isspace():
                state = NONUM
            else:
                print("Illegal character:", c)
                sys.exit()
    if state == NUM:
        tks.append(word)
    return tks
            
                
##
## Parser: converts list of word to a parse tree
##

## exp ::= factor (('*' | '/') factor)*
## factor ::= term (('+' | '-') term)*
## term ::= number | '(' exp ')'

def pExp(tks):
    left,rtks = pFactor(tks)
    while len(rtks) > 0 and rtks[0] in ['+', '-']:
        op = rtks[0]
        right,rtks = pFactor(rtks[1:])
        left = (op, [left, right])
    return (left, rtks)
    
def pFactor(tks):
    left,rtks = pTerm(tks)
    while len(rtks) > 0 and rtks[0] in ['*', '/']:
        op = rtks[0]
        right,rtks = pTerm(rtks[1:])
        left = (op, [left, right])
    return (left, rtks)

def pTerm(tks):
    if tks[0] == '(':
        b, rtks = pExp(tks[1:])
        if rtks[0] == ')':
            return (b, rtks[1:])
        else:
            print("Missing bracket")
            sys.exit()
    else:
        return ((INT, tks[0]), tks[1:])

def parse(ts):
    fact, ts1 = pExp(ts)
    if len(ts1) > 0:
        print("Incomplete parse")
        sys.exit()
    return fact

##
## Evaluation: converts a parse tree to a value
##
def evaluate(exp):
    op, exps = exp
    if op == INT:
        return int(exps)
    else:
        a = evaluate(exps[0])
        b = evaluate(exps[1])
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a // b
        else:
            print("Error")

        
while True:
    stg = input("Enter expression: ")
    tks = tokens(stg)
    syntree = parse(tks)
    print(syntree)
    print("The result is:", evaluate(syntree))
    
