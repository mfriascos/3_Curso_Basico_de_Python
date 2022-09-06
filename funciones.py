#------------------Primer ejemplo ------------------------

# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')

#------------------Solución con funciones--------------------

# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#-------------------Segundo ejemplo---------------------

# opcion = input('Elige una opción (1,2,3): ')

# if opcion == '1':
#     print('Hola')
#     print('Cómo estás')
#     print('elegiste la opción 1')
#     print('adios')
# elif opcion == '2':
#     print('Hola')
#     print('Cómo estás')
#     print('elegiste la opción 2')
#     print('adios')
# elif opcion == '3':
#     print('Hola')
#     print('Cómo estás')
#     print('elegiste la opción 3')
#     print('adios')
# else: 
#     print('elige una opción correcta')

#--------------------Solucion con funciones----------

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('adios')

opcion = int(input('Elige una opción (1,2,3): '))

if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe una opcion correcta')
    



