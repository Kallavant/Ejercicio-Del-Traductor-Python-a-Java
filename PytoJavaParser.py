# Generated from PytoJava.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\7\2\30\n\2\f\2\16\2\33")
        buf.write("\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4")
        buf.write("(\n\4\f\4\16\4+\13\4\3\5\6\5.\n\5\r\5\16\5/\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\7\7=\n\7\f\7\16\7")
        buf.write("@\13\7\3\b\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\tP\n\t\3\n\3\n\3\n\3\n\3\n\3\n\2\2\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\2\2X\2\31\3\2\2\2\4\34\3\2\2\2\6")
        buf.write("$\3\2\2\2\b-\3\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16A\3\2\2")
        buf.write("\2\20O\3\2\2\2\22Q\3\2\2\2\24\30\5\4\3\2\25\30\5\22\n")
        buf.write("\2\26\30\7\17\2\2\27\24\3\2\2\2\27\25\3\2\2\2\27\26\3")
        buf.write("\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\3")
        buf.write("\3\2\2\2\33\31\3\2\2\2\34\35\7\3\2\2\35\36\7\7\2\2\36")
        buf.write("\37\7\13\2\2\37 \5\6\4\2 !\7\f\2\2!\"\7\r\2\2\"#\5\b\5")
        buf.write("\2#\5\3\2\2\2$)\7\7\2\2%&\7\16\2\2&(\7\7\2\2\'%\3\2\2")
        buf.write("\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+)\3\2\2\2")
        buf.write(",.\5\n\6\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\t\3\2\2\2\61\62\7\4\2\2\628\5\f\7\2\63\64\7\7\2\2\64")
        buf.write("\65\7\n\2\2\658\5\f\7\2\668\5\22\n\2\67\61\3\2\2\2\67")
        buf.write("\63\3\2\2\2\67\66\3\2\2\28\13\3\2\2\29>\5\16\b\2:;\7\b")
        buf.write("\2\2;=\5\16\b\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2")
        buf.write("\2?\r\3\2\2\2@>\3\2\2\2AF\5\20\t\2BC\7\t\2\2CE\5\20\t")
        buf.write("\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\17\3\2\2\2")
        buf.write("HF\3\2\2\2IP\7\7\2\2JP\7\6\2\2KL\7\13\2\2LM\5\f\7\2MN")
        buf.write("\7\f\2\2NP\3\2\2\2OI\3\2\2\2OJ\3\2\2\2OK\3\2\2\2P\21\3")
        buf.write("\2\2\2QR\7\5\2\2RS\7\13\2\2ST\5\f\7\2TU\7\f\2\2U\23\3")
        buf.write("\2\2\2\n\27\31)/\67>FO")
        return buf.getvalue()


class PytoJavaParser ( Parser ):

    grammarFileName = "PytoJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "<INVALID>", "'-'", "'*'", "'='", "'('", "')'", "':'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "NUMBER", "IDENT", 
                      "MINUS", "MULTIPLY", "ASSIGN", "LPAREN", "RPAREN", 
                      "COLON", "COMMA", "WS" ]

    RULE_pyton_line = 0
    RULE_funcion = 1
    RULE_parametros = 2
    RULE_cuerpo = 3
    RULE_statement = 4
    RULE_expresion = 5
    RULE_term = 6
    RULE_factor = 7
    RULE_print_java = 8

    ruleNames =  [ "pyton_line", "funcion", "parametros", "cuerpo", "statement", 
                   "expresion", "term", "factor", "print_java" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    NUMBER=4
    IDENT=5
    MINUS=6
    MULTIPLY=7
    ASSIGN=8
    LPAREN=9
    RPAREN=10
    COLON=11
    COMMA=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Pyton_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.FuncionContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.FuncionContext,i)


        def print_java(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.Print_javaContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.Print_javaContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.WS)
            else:
                return self.getToken(PytoJavaParser.WS, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_pyton_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPyton_line" ):
                listener.enterPyton_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPyton_line" ):
                listener.exitPyton_line(self)




    def pyton_line(self):

        localctx = PytoJavaParser.Pyton_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pyton_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PytoJavaParser.DEF) | (1 << PytoJavaParser.PRINT) | (1 << PytoJavaParser.WS))) != 0):
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PytoJavaParser.DEF]:
                    self.state = 18
                    self.funcion()
                    pass
                elif token in [PytoJavaParser.PRINT]:
                    self.state = 19
                    self.print_java()
                    pass
                elif token in [PytoJavaParser.WS]:
                    self.state = 20
                    self.match(PytoJavaParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(PytoJavaParser.DEF, 0)

        def IDENT(self):
            return self.getToken(PytoJavaParser.IDENT, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def parametros(self):
            return self.getTypedRuleContext(PytoJavaParser.ParametrosContext,0)


        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(PytoJavaParser.COLON, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(PytoJavaParser.CuerpoContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = PytoJavaParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(PytoJavaParser.DEF)
            self.state = 27
            self.match(PytoJavaParser.IDENT)
            self.state = 28
            self.match(PytoJavaParser.LPAREN)
            self.state = 29
            self.parametros()
            self.state = 30
            self.match(PytoJavaParser.RPAREN)
            self.state = 31
            self.match(PytoJavaParser.COLON)
            self.state = 32
            self.cuerpo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.IDENT)
            else:
                return self.getToken(PytoJavaParser.IDENT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.COMMA)
            else:
                return self.getToken(PytoJavaParser.COMMA, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = PytoJavaParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PytoJavaParser.IDENT)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.COMMA:
                self.state = 35
                self.match(PytoJavaParser.COMMA)
                self.state = 36
                self.match(PytoJavaParser.IDENT)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = PytoJavaParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 42
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 45 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PytoJavaParser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpresionContext,0)


        def IDENT(self):
            return self.getToken(PytoJavaParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(PytoJavaParser.ASSIGN, 0)

        def print_java(self):
            return self.getTypedRuleContext(PytoJavaParser.Print_javaContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PytoJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PytoJavaParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(PytoJavaParser.RETURN)
                self.state = 48
                self.expresion()
                pass
            elif token in [PytoJavaParser.IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(PytoJavaParser.IDENT)
                self.state = 50
                self.match(PytoJavaParser.ASSIGN)
                self.state = 51
                self.expresion()
                pass
            elif token in [PytoJavaParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.print_java()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.TermContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.TermContext,i)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.MINUS)
            else:
                return self.getToken(PytoJavaParser.MINUS, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = PytoJavaParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.term()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.MINUS:
                self.state = 56
                self.match(PytoJavaParser.MINUS)
                self.state = 57
                self.term()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.FactorContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.MULTIPLY)
            else:
                return self.getToken(PytoJavaParser.MULTIPLY, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = PytoJavaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.factor()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.MULTIPLY:
                self.state = 64
                self.match(PytoJavaParser.MULTIPLY)
                self.state = 65
                self.factor()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PytoJavaParser.IDENT, 0)

        def NUMBER(self):
            return self.getToken(PytoJavaParser.NUMBER, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = PytoJavaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PytoJavaParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(PytoJavaParser.IDENT)
                pass
            elif token in [PytoJavaParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(PytoJavaParser.NUMBER)
                pass
            elif token in [PytoJavaParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(PytoJavaParser.LPAREN)
                self.state = 74
                self.expresion()
                self.state = 75
                self.match(PytoJavaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_javaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PytoJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_print_java

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_java" ):
                listener.enterPrint_java(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_java" ):
                listener.exitPrint_java(self)




    def print_java(self):

        localctx = PytoJavaParser.Print_javaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print_java)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PytoJavaParser.PRINT)
            self.state = 80
            self.match(PytoJavaParser.LPAREN)
            self.state = 81
            self.expresion()
            self.state = 82
            self.match(PytoJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





