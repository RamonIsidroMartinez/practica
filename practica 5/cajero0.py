class CajeroAutomatico:
    def __init__(self):
        self.saldo = 1000  # Saldo inicial

    def mostrar_menu(self):
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

    def consultar_saldo(self):
        print(f"Su saldo actual es: ${self.saldo}")

    def retirar_dinero(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Su nuevo saldo es: ${self.saldo}")
        else:
            print("Error: Fondos insuficientes")

    def depositar_dinero(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Su nuevo saldo es: ${self.saldo}")
        else:
            print("Error: Monto de depósito no válido")

# Programa principal
cajero = CajeroAutomatico()

while True:
    cajero.mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        cajero.consultar_saldo()
    elif opcion == '2':
        monto = float(input("Ingrese el monto a retirar: "))
        cajero.retirar_dinero(monto)
    elif opcion == '3':
        monto = float(input("Ingrese el monto a depositar: "))
        cajero.depositar_dinero(monto)
    elif opcion == '4':
        print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
