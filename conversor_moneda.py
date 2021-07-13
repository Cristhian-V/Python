moneda = input("""
que moneda combertira a dolares ungrese una de las siguientes opciones:
1 .- bolivianos
2 .- soles
3 .- pesos
ingrese su opcion: 
""")

monto = input("ingresa el monto a convertir: ")
if moneda == "1":
    total = int(monto) * 6.96
elif moneda == "2":
    total = int(monto) * 2
elif moneda == "3":
    total = int(monto) * 3
else:
    total = "el numero no esta dentro de las opciones mostradas"


print (total)