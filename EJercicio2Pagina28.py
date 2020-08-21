
class Vendedor:
    nombre = ''
    suelto = 0

    def calcular_comision(self , venta1,venta2,venta3):
        comision = (venta1 + venta2 + venta3) * 0.10
        return comision


vendedor1 = Vendedor()
vendedor1.nombre = input("Ingrese el nombre: ")
vendedor1.sueldo = float(input("Ingrese el sueldo base:"))

venta1 = float(input("Ingrese el valor de la venta 1: "))
venta2 = float(input("Ingrese el valor de la venta 2: "))
venta3 = float(input("Ingrese el valor de la venta 3: "))

valor_comision = vendedor1.calcular_comision(venta1,venta2,venta3)
total_pagar = vendedor1.sueldo + valor_comision

print(f"\n El vendedor {vendedor1.nombre}, obtuvo una comision de $ {valor_comision} y un sueldo total de $ {total_pagar}")