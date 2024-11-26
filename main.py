from antlr4 import *
from PytoJavaLexer import PytoJavaLexer
from PytoJavaParser import PytoJavaParser
from TraduceJavaCode import TraduceJavaCode

# Autor Rusell Emmanuel Canche Ciau
# Numero de Control: 21390320
# Fecha: 26/11/2024
# I7A

def main():
    try:
        # Solicitar y abrir el archivo
        in_code = input("File Name> ")
        with open(in_code, 'r') as fileope:
            input_text = fileope.read()

        # Crear lexer y parser
        lexer = PytoJavaLexer(InputStream(input_text))
        stream = CommonTokenStream(lexer)
        parser = PytoJavaParser(stream)
        tree = parser.pyton_line()

        # Crear el traductor y ejecutar la traducción
        traductor = TraduceJavaCode()
        walker = ParseTreeWalker()
        walker.walk(traductor, tree)

        # Obtener y guardar el código Java traducido
        java_code = traductor.get_java_code()
        output_file = "Multiplicacion.java"  # Nombre fijo para la clase
        
        with open(output_file, 'w') as f:
            f.write(java_code)

        # Mostrar resultados
        print("\nCódigo Java generado:")
        print(java_code)
        print(f"\nCódigo Java guardado en: {output_file}")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{in_code}'")
    except Exception as e:
        print(f"Error durante la traducción: {str(e)}")

if __name__ == '__main__':
    main()