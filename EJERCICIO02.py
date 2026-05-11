from abc import ABC, abstractmethod

# Clase abstracta
class SensorTemperatura(ABC):
    @abstractmethod
    def obtener_temperatura(self):
        pass

# Subclase Celsius
class SensorCelsius(SensorTemperatura):
    def __init__(self, temperatura_c=0):
        self.temperatura_c = temperatura_c

    def obtener_temperatura(self):
        return self.temperatura_c

    def a_fahrenheit(self):
        return (self.temperatura_c * 9/5) + 32

# Subclase Fahrenheit
class SensorFahrenheit(SensorTemperatura):
    def __init__(self, temperatura_f=32):
        self.temperatura_f = temperatura_f

    def obtener_temperatura(self):
        return self.temperatura_f

    def a_celsius(self):
        return (self.temperatura_f - 32) * 5/9

def menu_sensores():
    print("SISTEMA DE MEDICIÓN DE TEMPERATURA")
    print("1. Sensor Celsius")
    print("2. Sensor Fahrenheit")
    print("3. Salir")

while True:
    menu_sensores()
    opcion = input("Elige un sensor (1-3): ")

    if opcion == "1":
        temp_c = float(input("Ingresa la temperatura en Celsius: "))
        sensor = SensorCelsius(temp_c)
        print(f"Temperatura ingresada: {sensor.obtener_temperatura()}°C")
        print(f"Convertida a Fahrenheit: {sensor.a_fahrenheit():.2f}°F\n")
    elif opcion == "2":
        temp_f = float(input("Ingresa la temperatura en Fahrenheit: "))
        sensor = SensorFahrenheit(temp_f)
        print(f"Temperatura ingresada: {sensor.obtener_temperatura()}°F")
        print(f"Convertida a Celsius: {sensor.a_celsius():.2f}°C\n")
    elif opcion == "3":
        print("¡Gracias por usar el sistema de medición!\n")
        break
    else:
        print("Opción inválida. Intenta nuevamente.\n")