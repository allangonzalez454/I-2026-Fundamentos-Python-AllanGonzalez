class Vehiculo:
    def __init__(self, placa, marca, año):
        self.placa = placa
        self.marca = marca
        self.año = año

    def mostrar_informacion(self):
        print(self.placa, self.marca, self.año)

cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos a registrar: "))

vehiculos = []

for i in range(cantidad_vehiculos):
    placa = input("Ingrese la placa del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    año = input("Ingrese el año del vehículo: ")
    vehiculo = Vehiculo(placa, marca, año)
    vehiculos.append(vehiculo)

for vehiculo in vehiculos:
    vehiculo.mostrar_informacion()

