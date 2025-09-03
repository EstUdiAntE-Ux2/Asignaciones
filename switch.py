bolsa = []

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Insertar elementos (cantidad definida por el usuario)")
    print("2. Contar elementos en el array")
    print("3. Verificar si el array está vacío")
    print("4. Añadir un elemento")
    print("5. Remover un elemento")
    print("6. Remover todos los elementos")
    print("7. Contar cuántas veces se repite un elemento")
    print("8. Verificar si el array contiene un elemento")
    print("9. Mostrar todos los elementos")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            n = int(input("¿Cuántos elementos quieres insertar? "))
            for i in range(n):
                valor = input(f"Elemento {i+1}: ")
                bolsa.append(valor)
            print("Elementos insertados correctamente.")

        case "2":
            print(f"El array tiene {len(bolsa)} elementos.")

        case "3":
            if len(bolsa) == 0:
                print("El array está vacío.")
            else:
                print("El array NO está vacío.")

        case "4":
            valor = input("Introduce el elemento a añadir: ")
            bolsa.append(valor)
            print("Elemento añadido.")

        case "5":
            valor = input("Introduce el elemento a remover: ")
            if valor in bolsa:
                bolsa.remove(valor)
                print("Elemento removido.")
            else:
                print("Ese elemento no está en el array.")

        case "6":
            bolsa.clear()
            print("Todos los elementos fueron eliminados.")

        case "7":
            valor = input("Introduce el elemento a contar: ")
            print(f"El elemento '{valor}' aparece {bolsa.count(valor)} veces.")

        case "8":
            valor = input("Introduce el elemento a buscar: ")
            if valor in bolsa:
                print(f"El elemento '{valor}' SÍ está en el array.")
            else:
                print(f"El elemento '{valor}' NO está en el array.")

        case "9":
            print("Elementos en el array:", bolsa)

        case "0":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida, intenta de nuevo.")
