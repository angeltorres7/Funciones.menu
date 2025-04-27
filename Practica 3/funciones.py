#Se le piden los datos de la operacion al usuario
nume1 = int(input("Dame el primer valor: "))
nume2 = int(input("Dame el segundo valor: "))


#Aqui se hacen las funciones para poder hacer las operaciones
def suma(num1,num2):
    suma = num1 + num2
    print(f"El resultado de la suma es: {suma}")
    
def resta(num1,num2):
    resta = num1 - num2
    print(f"El resultado de la resta es: {resta}")
    
def division(num1,num2):
    division = num1 / num2
    print(f"El resultado de la division es: {division}")
    
def mult(num1,num2):
    mult = num1 * num2
    print(f"El resultado de la multiplicacion es: {mult}")
#despues desarrollamos el menú de opciones para que solo se complete una función.
if __name__ == "__main__":
    letrero = """ MENU DE OPCIONES
    1. Suma
    2. Resta
    3. Division
    4. Multiplicacion """
    print(letrero)
    opc = int(input("Elige el numero de la opcion que deseas: "))
    if opc == 1:
        suma(nume1, nume2)
    elif opc == 2:
        resta(nume1, nume2)
    elif opc == 3:
        division(nume1,nume2)
    elif opc == 4:
        mult(nume1, nume2)
    elif opc == 5:
        print("Adios")
    else:
        print("Error. Ingrese una opcion valida")
#Eso es todo, Soy Torres Pérez Roberto Angel.