class Moto:
    def __init__(self, marca, CC, año):
        self.marca = marca
        self.CC = CC
        self.año = año
    
    def mostrar(self):
        print(f"Marca: {self.marca}, CC: {self.CC}, Año: {self.año}")

        
Motos = []

Cantidad = int(input("ingrese la cantidad de motos que desea registrar:"))

for i in range(Cantidad):
    print("\nMoto", i + 1)

    nombre = input("Ingrese la marca de la moto: ")
    CC = float(input("Ingrese la cilindrada de la moto: "))
    año = int(input("Ingrese el año de la moto: "))

    moto = Moto(nombre, CC, año)
    Motos.append(moto)

for i in range(len(Motos)):
    print("Motos", i + 1)
    Motos[i].mostrar()

