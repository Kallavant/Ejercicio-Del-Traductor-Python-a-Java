from PytoJavaListener import PytoJavaListener
from PytoJavaParser import *

class TraduceJavaCode(PytoJavaListener):
    def __init__(self):
        self.java_code = []
        self.current_expression = ""
        self.function_body = []
        self.in_function = False
        
    def enterPyton_line(self, ctx:PytoJavaParser.Pyton_lineContext):
        self.java_code.append("public class Multiplicacion {")
        
    def exitPyton_line(self, ctx:PytoJavaParser.Pyton_lineContext):
        self.java_code.append("}")
        
    def enterFuncion(self, ctx:PytoJavaParser.FuncionContext):
        self.in_function = True
        self.function_name = ctx.IDENT().getText()
        
    def exitFuncion(self, ctx:PytoJavaParser.FuncionContext):
        self.in_function = False
        # Añadir la función completa al código
        self.java_code.extend(self.function_body)
        self.function_body = []

    # Sirve para leer los parametros     
    def enterParametros(self, ctx:PytoJavaParser.ParametrosContext):
        params = []
        for ident in ctx.IDENT():
            params.append(f"int {ident.getText()}")
        param_str = ", ".join(params)
        self.function_body.append(f"    public static int {self.function_name}({param_str}) {{")
        
    def exitParametros(self, ctx:PytoJavaParser.ParametrosContext):
        pass
        
    def enterStatement(self, ctx:PytoJavaParser.StatementContext):
        if ctx.RETURN():
            self.current_expression = "        return "
        elif ctx.IDENT():
            self.current_expression = f"        int {ctx.IDENT().getText()} = "
            
    def exitStatement(self, ctx:PytoJavaParser.StatementContext):
        if self.current_expression:
            if self.in_function:
                self.function_body.append(self.current_expression + ";")
            else:
                self.java_code.append(self.current_expression + ";")
            self.current_expression = ""
            
    def enterExpresion(self, ctx:PytoJavaParser.ExpresionContext):
        pass

    # Aqui lo unico que hace es guardar las experesiones    
    def exitExpresion(self, ctx:PytoJavaParser.ExpresionContext):
        if len(ctx.term()) == 2:  # Si hay una operación de resta
            term1 = self.get_term_text(ctx.term(0))
            term2 = self.get_term_text(ctx.term(1))
            self.current_expression += f"{term1} - {term2}"
        else:
            self.current_expression += self.get_term_text(ctx.term(0))
            
    def get_term_text(self, term_ctx):
        if len(term_ctx.factor()) == 2:
            return f"{term_ctx.factor(0).getText()} * {term_ctx.factor(1).getText()}"
        return term_ctx.factor(0).getText()
            
    def enterPrint_java(self, ctx:PytoJavaParser.Print_javaContext):
        self.function_body.append("    }")  # Cerrar la función anterior
        self.java_code.extend(self.function_body)
        self.java_code.append("\n    public static void main(String[] args) {")
        
    def exitPrint_java(self, ctx:PytoJavaParser.Print_javaContext):
        self.java_code.append("        System.out.println(multiplica(5, 6));")
        self.java_code.append("    }")
    
    #Sirve para guardar el codigo en un archivo .Java
    def get_java_code(self):
        return "\n".join(self.java_code)