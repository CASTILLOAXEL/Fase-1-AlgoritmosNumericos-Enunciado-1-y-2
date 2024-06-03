def generar_tabla_amortizacion(monto, plazo, tasa_interes):
    saldo = monto
    tasa_interes /= 100
    print(f"{'Periodo':<10}{'Saldo':<15}{'Interés':<15}{'Abono':<15}{'Pago':<15}")

    for periodo in range(1, plazo + 1):
        interes = saldo * tasa_interes
        abono = monto / plazo
        pago = interes + abono
        print(f"{periodo:<10}Q{saldo:<14.2f}Q{interes:<14.2f}Q{abono:<14.2f}Q{pago:<14.2f}")
        saldo -= abono

# Solicitar al usuario los valores
try:
    monto = float(input("Introduce el monto del préstamo (en Q): ").replace(",", ""))
    plazo = int(input("Introduce el plazo en meses: "))
    tasa_interes = float(input("Introduce la tasa de interés mensual: ").replace(",", "."))
    
    print(f"Monto del préstamo: Q{monto:.2f}")
    generar_tabla_amortizacion(monto, plazo, tasa_interes)
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")
