moneda = int(input("""
que moneda combertira a dolares ungrese una de las siguientes opciones:
1 .- bolivianos
2 .- soles
3 .- pesos
ingrese su opcion: 
"""))
monto = int(input("ingresa el monto a convertir: "))

def conversor(monto, conver):
    total = monto * conver
    return total

if moneda == 1:
    total = conversor(monto, 6.96)
elif moneda == 2:
    total = conversor(monto, 2)
elif moneda == 3:
    total = conversor(monto, 3)
else:
    total = "el numero no esta dentro de las opciones mostradas"


print (total)


