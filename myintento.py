def raiz_cuadrada (objetivo): 
#= int (input('Escoge un entero: '))
    respuesta = 0

    while respuesta **2 < objetivo:
        print(respuesta)
        respuesta += 1
    
    if respuesta **2 == objetivo:
        print(f'La raiz cuadrada {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
        

#Aproximacion
def aproximacion (objetivo, epsilon):
    #= int(input('Escoge un numero: '))
    #epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs (respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo),respuesta)
        respuesta += paso
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        

#BusquedaBinaria
def busqueda_binaria (objetivo, epsilon):
#objetivo = int (input('Escoge un numero: '))
#epsilon = 0.000000001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


opciones = int(input("""Hola tenemos tres metodos para que averigues cual es la raiz cuadrada de un numero:
-El primer metodo se llama Raiz cuadrada: Si quieres usar este marca el numero 1
-El segundo metodo se llama aproximacion: Si quieres usar este marca el numero 2
-El tercer metodo se llama busqueda binaria: Si quieres usar este marca el numero 3
Asi que escoge un numero: """))
               
               
if opciones == 1: 
    print('Que bien escogiste la opcion de raiz Cuadrada')
    numero = int(input('Dime un numero del que quieras saber la raiz cuadrada: '))
    raiz_cuadrada(numero)
elif opciones == 2:
    print('Que bien escogiste la opcion de aproximacion, este es un poco mas rapido y exacto que el de raiz cuadrada')
    numero = int(input('Dime un numero del que quieras saber la raiz cuadrada: '))
    variable_epsilon = float(input('Dime que porcentaje de error acepta, escoge un numero menor a 0.01'))
    aproximacion(numero, variable_epsilon)
elif opciones == 3:
    print('Que bien escogiste la opcion de busqueda binaria, este es el metodo mas rapido y exacto de todos')
    numero = int(input('Dime un numero del que quieras saber la raiz cuadrada: '))
    variable_epsilon = float(input('Dime que porcentaje de error acepta, escoge un numero menor a 0.01'))
    busqueda_binaria(numero, variable_epsilon)
else:
    print('Algo hiciste mal')