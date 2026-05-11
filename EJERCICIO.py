from abc import ABC, abstractmethod

# Clase abstracta
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# Subclase Email
class EmailNotificacion(Notificacion):
    def __init__(self, asunto, cuerpo):
        self.asunto = asunto
        self.cuerpo = cuerpo

    def enviar(self, mensaje):
        print("\n=== Enviando Email ===")
        print(f"Asunto: {self.asunto}")
        print(f"Cuerpo: {self.cuerpo} - Mensaje extra: {mensaje}\n")

# Subclase SMS
class SMSNotificacion(Notificacion):
    def __init__(self, limite_caracteres=160):
        self.limite_caracteres = limite_caracteres

    def enviar(self, mensaje):
        mensaje_final = mensaje[:self.limite_caracteres]
        print(f"\n=== Enviando SMS ===")
        print(f"Mensaje: {mensaje_final}\n")

def menu_notificaciones():
    print("SISTEMA DE NOTIFICACIONES")
    print("1. Enviar Email")
    print("2. Enviar SMS")
    print("3. Salir")

while True:
    menu_notificaciones()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        asunto = input("Asunto del email: ")
        cuerpo = input("Cuerpo del email: ")
        mensaje = input("Mensaje adicional: ")
        email = EmailNotificacion(asunto, cuerpo)
        email.enviar(mensaje)
    elif opcion == "2":
        limite = input("Limite de caracteres para SMS (enter=160): ")
        limite = int(limite) if limite else 160
        mensaje = input("Mensaje SMS: ")
        sms = SMSNotificacion(limite_caracteres=limite)
        sms.enviar(mensaje)
    elif opcion == "3":
        print("¡Gracias por usar el sistema de notificaciones!\n")
        break
    else:
        print("Opción inválida. Intenta nuevamente.\n")