a = float(input("Valor 1: "))
b = float(input("Valor 2: "))
c = input("Operador: ")

def calculadora(numero1, numero2, operacao):
    if operacao == "+": 
        resultado = numero1 + numero2
    
    elif operacao == "-":
        resultado = numero1 - numero2
    
    elif operacao == "*":
        resultado = numero1 * numero2
    
    elif operacao == "/":
        resultado = numero1 / numero2
    
    else:
        print("Informe uma operação válida... ")
        
        if resultado: 
            print(resultado)
        else:
            pass 
        
