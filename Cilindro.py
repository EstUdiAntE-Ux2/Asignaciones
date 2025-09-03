radio = int(input("ingrese el radio del cilindro: "));
altura = float(input("ingrese la altura del cilindro: "));
pi = 3.1416;
Area = 2 * pi * radio * altura;
volumen = pi * pow(radio, 2) * altura;

print("El area del cilindro es de: " + str(Area));
print("El volumen del cilindro es de: " + str(volumen));

