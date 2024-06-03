def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número
numero = int(input("Introduce un número: "))
print(f"{numero}! = {factorial(numero)}")
