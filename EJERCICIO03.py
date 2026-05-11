from abc import ABC, abstractmethod

# Clase abstracta
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Subclase Tarjeta de Crédito
class TarjetaCredito(MetodoPago):
    def __init__(self, numero_tarjeta, fecha_expiracion, cvv, saldo=1000):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv
        self.saldo = saldo

    def validar_tarjeta(self):
        if len(str(self.numero_tarjeta)) != 16:
            raise ValueError("Número de tarjeta debe tener 16 dígitos")
        if self.fecha_expiracion < "2026-01":
            raise ValueError("Tarjeta expirada")
        if len(str(self.cvv)) != 3:
            raise ValueError("CVV inválido")
        return True

    def procesar_pago(self, monto):
        try:
            self.validar_tarjeta()
            if monto > self.saldo:
                raise ValueError("Saldo insuficiente en la tarjeta")
            self.saldo -= monto
            print(f"Pago de ${monto} con tarjeta realizado. Saldo restante: ${self.saldo}\n")
        except ValueError as e:
            print(f"Error en el pago con tarjeta: {e}\n")

# Subclase PayPal
class Paypal(MetodoPago):
    def __init__(self, correo, saldo=500):
        self.correo = correo
        self.saldo = saldo

    def procesar_pago(self, monto):
        try:
            if "@" not in self.correo:
                raise ValueError("Correo inválido")
            if monto > self.saldo:
                raise ValueError("Saldo insuficiente en PayPal")
            self.saldo -= monto
            print(f"Pago de ${monto} con PayPal realizado. Saldo restante: ${self.saldo}\n")
        except ValueError as e:
            print(f"Error en el pago con PayPal: {e}\n")


def menu_pago():
    print("SISTEMA DE PAGO")
    print("1. Pagar con Tarjeta de Crédito")
    print("2. Pagar con PayPal")
    print("3. Salir")

while True:
    menu_pago()
    opcion = input("Elige un método de pago (1-3): ")

    if opcion == "1":
        numero = input("Número de tarjeta (16 dígitos): ")
        fecha = input("Fecha expiración (YYYY-MM): ")
        cvv = input("CVV (3 dígitos): ")
        monto = float(input("Monto a pagar: "))
        tarjeta = TarjetaCredito(numero_tarjeta=int(numero), fecha_expiracion=fecha, cvv=int(cvv))
        tarjeta.procesar_pago(monto)

    elif opcion == "2":
        correo = input("Correo de PayPal: ")
        monto = float(input("Monto a pagar: "))
        paypal = Paypal(correo=correo)
        paypal.procesar_pago(monto)

    elif opcion == "3":
        print("¡Gracias por usar el sistema de pago!\n")
        break

    else:
        print("Opción inválida. Intenta nuevamente.\n")