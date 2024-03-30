def suma(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Tipo de dato no válido.")
        return None
    return num1 + num2

def resta(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Tipo de dato no válido.")
        return None
    return num1 - num2

def producto(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Tipo de dato no válido.")
        return None
    return num1 * num2

def division(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Tipo de dato no válido.")
        return None
    if num2 == 0:
        print("Error: No es posible dividir entre cero.")
        return None
    return num1 / num2