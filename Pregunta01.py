def get_fraction():
    while True:
        try:
            x, y = map(int, input("Ingresa una fracción (X/Y): ").split('/'))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return x, y
        except ValueError:
            print("Error: X debe ser menor o igual a Y, y Y no debe ser 0.")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0.")

def calculate_percentage(x, y, total):
    percentage = (x / y) * 100
    if percentage < 1:
        return 'E'
    elif percentage > 99:
        return 'F'
    return round(percentage)

def main():
    while True:
        try:
            x, y = get_fraction()
            fuel_percentage = calculate_percentage(x, y, 100)
            print(f"Nivel de combustible: {str(fuel_percentage)}%")
            break
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == '__main__':
    main()
