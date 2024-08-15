def operate(operation: str, a: int, b: int) -> int:
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a // b


if __name__ == '__main__':
    a = int(input("Ingrese a:"))
    b = int(input("Ingrese b:"))
    operator = input("Ingrese el operador (+, -, *, /):")
    print(f'El resultado es: {operate(operator, a, b)}')
