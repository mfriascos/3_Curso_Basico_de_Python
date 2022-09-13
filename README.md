# 3_Curso_Basico_de_Python

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

**Curso básico de Python otorgado por Platzi, todos los derechos a Platzi y a Facundo García Martoni**

**Table of Contents**

- [El arte de la programación](#el-arte-de-la-programación)
- [¿Por qué aprender Python?](#por-qué-aprender-python)
  - [Campos de uso de Python:](#campos-de-uso-de-python)
- [El núcleo de un programa: Los algoritmos](#el-núcleo-de-un-programa-los-algoritmos)
  - [Definiciones de algoritmo](#definiciones-de-algoritmo)
  - [¿Cómo se Diseña un Algoritmo?](#¿cómo-se-diseña-un-algoritmo)
  - [Características de los Algoritmos](#características-de-los-algoritmos)
- [Instalación de herramientas](#instalación-de-herramientas)
  - [Editor de código](#editor-de-código)
  - [Ejemplos de editor de código](#ejemplos-de-editor-de-código)
  - [consola](#consola)
  - [Lenguaje de programación](#lenguaje-de-programación)
- [Tu mejor herramienta: La consola](#tu-mejor-herramienta-la-consola)
  - [Comandos básicos para usar en la consola](#comandos-básicos-para-usar-en-la-consola)
- [Explorando Python: Operadores Aritméticos](#explorando-python-operadores-aritméticos)
  -[Python Keywords](#python-keywords)
- [¿Qué es una variable?](#¿qué-es-una-variable)
  - [Asignación de variables](#asignación-de-variables)
  - [Reasignación de variables](#reasignación-de-variables)
  - [Reglas en el uso de identificadores de variable](#reglas-en-el-uso-de-identificadores-de-variable)
  - [Tipos de variables en Python](#tipos-de-variables-en-python)
- [Los primitivos: Tipos de Datos Sencillos](#los-primitivos-tipos-de-datos-sencillos)
  - [Tipos de datos primitivos en Python](#tipos-de-datos-primitivos-en-python)
  - [Tipos de dato adicionales](#tipos-de-dato-adicionales)
  - [¿Cómo saber el tipo de dato que estoy usando?](#¿cómo-saber-el-tipo-de-dato-que-estoy-usando)
- [Convertir un datos a un tipo diferente](#convertir-un-datos-a-un-tipo-diferente)
  -[Ejemplo de conversión de datos en Python](#ejemplo-de-conversión-de-datos-en-python)
- [Operadores Lógicos y de Comparación en Python](#operadores-lógicos-y-de-comparación-en-python)
  - [Operadores lógicos](#operadores-lógicos)
  - [Operadores de comparación](#operadores-de-comparación)
- [Conversor de Monedas](#conversor-de-monedas)
- [Construyendo el Camino de un Programa con Condicionales](#construyendo-el-camino-de-un-programa-con-condicionales)
  - [En lenguaje natural (español)](#en-lenguaje-natural-español)
  - [Ejemplo de condicionales en Python](#ejemplo-de-condicionales-en-python)
- [Varios Paises en mi Conversor de Monedas](#varios-paises-en-mi-conversor-de-monedas)
  - [if:](#if)
  - [else:](#else)
  - [elif:](#elif)
  - [Añadir comentarios en Python](#añadir-comentarios-en-python)
- [Aprendiendo a no Repetir Código con Funciones](#aprendiendo-a-no-repetir-código-con-funciones)
  - [Cómo usar def en Python](#cómo-usar-def-en-python)
  - [Ejemplo de funciones con def en Python](#ejemplo-de-funciones-con-def-en-python)
- [Modularizando Nuestro Conversor de Monedas](#modularizando-nuestro-conversor-de-monedas)
- [Trabajando con Texto: Cadenas de Caracteres](#trabajando-con-texto-cadenas-de-caracteres)
  - [Métodos para trabajar con texto en Python](#métodos-para-trabajar-con-texto-en-python)
  - [Índices:](#índices)
- [Trabajando con Texto: Slices](#trabajando-con-texto-slices)
  - [Cómo usar slices en Python](#cómo-usar-slices-en-python)
- [Proyecto: Palindromo](#proyecto-palindromo)
- [Aprendiendo Bucles](#aprendiendo-bucles)
  - [Ejemplo de bucle en Python](#ejemplo-de-bucle-en-python)
  - [Ejemplo de bucle en la vida real](#ejemplo-de-bucle-en-la-vida-real)
- [El Ciclo While](#el-ciclo-while)
  - [Ejemplo de while en Python](#ejemplo-de-while-en-python)
- [Explorando un Bucle Diferente: El Ciclo For](#explorando-un-bucle-diferente-el-ciclo-for)
  - [Ejemplo del bucle for en Python](#ejemplo-del-bucle-for-en-python)
- [Recorriendo un string con for](#recorriendo-un-string-con-for)
- [Interrumpiendo ciclos con Break y Continue](#interrumpiendo-ciclos-con-break-y-continue)
- [Proyecto: Prueba de Primalidad](#proyecto-prueba-de-primalidad)
- [Proyecto: Videojuego](#proyecto-videojuego)












## El arte de la programación

Los lenguajes de programación están por todos lados. Python un lenguaje que podemos aprender para iniciarnos en la ingeniería de software. Es utilizado en Drones, autos autónomos y hasta cohetes, nosrodea por todos lados.

Razones por iniciarse con Python

* El lenguaje con mayor crecimiento
* Es el curso ideal si no tienes ningún contacto con la programación o ya dominas algún lenguaje y quieres aprender más.
* Su forma de escribir es elegante y simple
* La programación está en todos lados
* Programar es darle instrucciones a la computadora para que resuelva un problema.
* La industria de tecnología es una de las que tienen mayor crecimiento.

## ¿Por qué aprender Python?

Python es lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Python es muy elogiado por su elegante sintaxis y su código legible, si estás comenzando tu carrera de programación, Python se adapta a tus necesidades.

Python tienen una amplia gama de usos. Desde procesamiento de datos, al aprendizaje de máquina. Por ello, Python es elegido como el lenguaje de programación de muchas empresas y organizaciones.

### Campos de uso de Python:

* Frontend: Se encarga de llevar el diseño de una aplicación o sitio web a código
* IoT: Se encarga de darle la capacidad de conectarse a internet a elementos que pueden estar a nuestro alrededor.
* IA: Se encarga de enseñarle a la computadora a resolver un determinado problema sin la necesidad de estar involucrados constantemente.
* Backend: Se encarga de crear la lógica con la cual va a funcionar una determinada aplicación y que va a ser almacenada en un servidor.
* DevOps: Se encarga de manejar la información almacenada en la nube de una determinada aplicación.
* Data Science: Se encarga de tomar la información relevante de un determinado ambiente y poder sacar conclusiones al respecto.
* Videojuegos: Se encarga de combinar la programación, el diseño y la música para generar grandes experiencias a los usuarios.
* Desarrollo móvil: Se encarga de crear aplicaciones que serán almacenadas en la PlayStore o AppStore, y que podremos hacer uso de ellas desde nuestros smartphones.

## El núcleo de un programa: Los algoritmos

Dentro de todo lenguaje de programación existe un núcleo llamado algoritmo. Un algoritmo es una serie de pasos ordenados para resolver un problema. Este es finito, ordenado, y no ambiguo.

### Definiciones de algoritmo

* Algoritmo: Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la solución de un tipo de problema.
* Algoritmo: Se denomina algoritmo a un grupo finito de operaciones organizadas de manera lógica y ordenada que permite solucionar un determinado problema.
* Algoritmo: una serie de instrucciones o reglas establecidas que, por medio de una sucesión de pasos, permiten arribar a un resultado o solución.
* Algoritmo: una secuencia de instrucciones que representan un modelo de solución para determinado tipo de problemas. O bien como un conjunto de instrucciones que realizadas en orden conducen a obtener la solución de un problema.

### ¿Cómo se Diseña un Algoritmo?

En programación, un algoritmo establece, de manera genérica e informal, la secuencia de pasos o acciones que resuelve un determinado problema y, para representarlo, se utiliza, fundamentalmente, dos tipos de notación: pseudocódigo y diagramas de flujo.

**Partes de un Algoritmo**

Todo algoritmo debe obedecer a la estructura básica de un sistema, es decir: entrada, proceso y salida.

### Características de los Algoritmos

Las características fundamentales que debe cumplir todo algoritmo son:

* Un algoritmo debe ser preciso e indicar el orden de realización de cada paso.
* Un algoritmo debe estar definido. Si se sigue un algoritmo dos veces, se debe obtener el mismo resultado cada vez.
* Un algoritmo debe ser finito. el algoritmo se debe terminar en algún momento; o sea, debe tener un número finito de pasos.
* Un algoritmo debe ser legible: El texto que lo describe debe ser claro, tal que permita entenderlo y leerlo fácilmente.

## Instalación de herramientas 

Para empezar a programar con Python, necesitaremos las siguientes herramientas:

### Editor de código

Facilita la escritura del código, ya que da ciertas ayudas o resalta palabras claves del lenguaje de programación.

### Ejemplos de editor de código

* Visual Studio Code
* Sublime text
* Atom
* Pycharm

El que recomienda y el que se va a utilizar es Visual Studio Code, porque es el más popular en la industria de tecnología y varios desarrolladores lo utilizan.

### Consola

Programa que sirve para manejar la computadora sin necesidad de emplear la interfaz gráfica.

Ejemplos de consola

CMD
Power Shell
Cmder.

Se utilizará cmder, porque tiene comandos compatibles con sistemas operativos del tipo Unix y Windows.

### Lenguaje de programación

Python, que es el lenguaje más usado en el mundo y es ampliamente considerado el más fácil de aprender.

## Tu mejor herramienta: La consola 

No necesitamos la interfaz gráfica de nuestra computadora para poder usarla. Para esto, nuestra mejor herramienta es la consola. La consola nos permite comunicarnos con el computador por medio de comandos y así realizar tareas sin la necesidad de utilizar el mouse en una interfaz, sino solamente a través del código.

### Comandos básicos para usar en la consola:

* Ctrl + L = Limpiar pantalla
* cd = Change Directory
* … = Carpeta padre
* cd… = Cambiar de directorio a la carpeta padre
* Alt + 92 =
* ls = list
* mkdir = Make directory
* touch = para crear archivos

## Explorando Python: Operadores Aritméticos

Primero, para iniciar la consola interactiva de Python debemos escribir el comando **py **en Windows, pero en otros sistemas el comando es python3.
Ahora, podemos comenzar.

En la consola nos permite escribir operaciones matemáticas como 5 + 5 sin escribir nada más, pero en el editor de código debemos “imprimir” el resultado, de la siguiente manera:

print(5 + 5). Con esto obtendremos el resultado.

Ahora veamos como se realiza cada operación aritmética:

Operadores aritméticos en Python

* Suma: 5 + 5
* Resta: 5 - 5
* Multiplicación: 5 * 5
* División (con decimales): 5 / 5
* División (sin decimales): 21 // 5
* Resto de la división: 21 % 5
* Potencia: 2 ** 2
* Raíz cuadrada:

```Python
math.sqrt(9)     
 3.0
math.sqrt(11.11)   
 3.3331666624997918
math.sqrt(Decimal('6.25'))     
 2.5
 ```
Python respeta la separación de términos, por lo que si escribimos 5 + 5 * 2 multiplicará primero 5 x 2. En el caso de que quisiéramos que primero sume 5 + 5 ponemos paréntesis:
(5 + 5) * 2.

Para recordar el orden de las operaciones en álgebra y en Python, es recomendable utilizar el orden PEMDAS:

* Paréntesis
* Exponentes o raíces
* Multiplicaciones
* Divisiones
* Adiciones y sustracciones

### Python Keywords

Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

Keyword | Description
------------- | -------------
and | A logical operator
as | To create an alias
assert | For debugging
break | To break out of a loop
class | To define a class
continue | To continue to the next iteration of a loop
def | To define a function
del | To delete an object
elif | Used in conditional statements, same as else if
else | Used in conditional statements
except | Used with exceptions, what to do when an exception occurs
False | Boolean value, result of comparison operations
finally | Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for | To create a for loop
from | To import specific parts of a module
global | To declare a global variable
if | To make a conditional statement
import | To import a module
in | To check if a value is present in a list, tuple, etc.
is | To test if two variables are equal
lambda | To create an anonymous function
None | Represents a null value
nonlocal | To declare a non-local variable
not | A logical operator
or | A logical operator
pass | A null statement, a statement that will do nothing
raise | To raise an exception
return | To exit a function and return a value
True | Boolean value, result of comparison operations
try | To make a try...except statement
while | To create a while loop
with | Used to simplify exception handling
yield | To end a function, returns a generator

## ¿Qué es una variable? 

Una variable es un lugar en memoria (una especie de caja) en el que podemos guardar objetos (números, texto, etc). Esta variable posee un identificador o nombre con el cual podemos llamarla más tarde cuando la necesitemos.

### Asignación de variables

En Python, creamos las variables asignándoles un valor de la siguiente manera:

```Python
<identificador> = <valor>
```

en este caso el signo = se lee como “asignar”

### Reasignación de variables

Podemos en cualquier momento cambiar el valor de nuestra variable volviendo a asignar un valor al mismo identificador:

```Python
<identificador> = <nuevo_valor>
```

### Reglas en el uso de identificadores de variable

* No pueden empezar con un número.
* Deben estar en minúsculas
* Para separar las palabras usamos el guion bajo: _
* Estas reglas son aplicadas al lenguaje Python, en otros lenguajes puede haber otras reglas.

### Tipos de variables en Python

* a = 28 → int (entero)
* b = 1.5 → float (decimales)
* c = “Hello” → str (string o cadena de texto)
* d = True → boolean (verdadero o falso)
* e = None → NoneType (Sin valor)
* 33f = “5” → str (5 y “5” no son lo mismo. La primera es un entero y la segunda una cadena de texto)

## Los primitivos: Tipos de Datos Sencillos

Un objeto es una forma de modelar el mundo en programación. En los lenguajes de programación se caracterizan por tener métodos y atributos. En Python todo es un objeto.

Podemos encontrar cuatro tipos de datos que vienen definidos por defecto en Python, a estos tipos de datos los conocemos como primitivos.

### Tipos de datos primitivos en Python

* Integers: números Enteros
* Floats: números de punto flotante (decimales)
* Strings: cadena de caracteres (texto)
* Boolean: boolenaos (Verdadero o Falso)

Algunos operadores aritméticos pueden funcionar para operar con otros tipos de datos. Por ejemplo: podemos sumar strings, lo que concatena el texto o multiplicar un entero por un string, lo que repetirá el _string _las veces que indique el entero.

### Tipos de dato adicionales

* Datos en texto: str
* Datos numéricos: int, float, complex
* Datos en secuencia: list, tuple, range
* Datos de mapeo: dict
* Set Types: set, frozenset
* Datos booleanos: bool
* Datos binarios: bytes, bytearray, memoryview

### ¿Cómo saber el tipo de dato que estoy usando?

Usamos el comando type()

**Ejemplo:**
```Python
x = 5
print(type(x))
```

## Convertir un datos a un tipo diferente

Cómo convertir un tipo de dato a otro en Python:

Sintaxis | Descripción
-----------|------------
int(var) | variable a entero
float(var) | variable a flotante
str(var) | variable a texto
bool(var) | variable a booleano
abs(var) | variable a valor absoluto


### Ejemplo de conversión de datos en Python
```Python 
>>> number1 = input("Escribe un número: ")
Escribe un número: 4
>>> number2 = input("Escribe otro número: ")
Escribe un número: 5
>>> numero1 + numero 2
=> '45' <== Se concatenan
```

Solución:
```Python
>>> number1 = int(input("Escribe un numero: "))
Escribe un numero: 100
>>> number2 = int(input("Escribe otro numero: "))
Escribe otro numero: 300
>>> number1 + number2
=> 400
```

Ejemplo 2:
```Python
>>> numero1 = 4.5
int(numero1)
=> 4 <== Trunca el flotante
```

Ejemplo 3:
```Python
>>> numero1 = 4.5
str(numero1)
=> '4.5' <== Lo convierte a texto
```

## Operadores Lógicos y de Comparación en Python

Conoce los operadores lógicos que tiene Python y cómo utilizarlos de manera adecuada:

### Operadores lógicos

* and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
* or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se cumplen.
* not ( no): invierte el valor de una variable, dando el valor contrario al de la variable evaluada.

### Operadores de comparación

* == ( igual qué ): determina si dos valores son iguales o no.
* != (diferente de): determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
* "> (mayor que): compara dos valores, y determina si es mayor que el otro".
* < (menor que): compara dos valores y determina si es menor que el otro.
* ">= (mayor o igual): compara dos valores y determinas si es mayor o igual que el otro."
* <= (menor o igual): compara dos valores y determinas si es menor o igual que el otro.

## Conversor de Monedas

Verificar archivos conversor.py conversor_inverso.py

## Construyendo el Camino de un Programa con Condicionales

Los condicionales son decisiones que se establecen desacuerdo a los parámetros que indiquemos, para obtener un tipo de resultado deseado.

**Ejemplo:** si un número es mayor o igual que otro, los números deberán sumarse, de lo contrario deberán restarse. Debe cumplirse una condición para saber cuál será el camino a seguir.

A continuación veremos cómo funcionan los condicionales en Python.

**if**
(Si) se usa para la condición principal.

**elif**
(Si no) en caso de que la condición principal o anterior no se cumpla, se puede utilizar para agregar otra condición.

**else**
(Sino) en caso de que la(s) condición(es) anterior(es) no se cumplan, se ejecuta como alternativa sin condicional.

### En lenguaje natural (español)

‘Si’ introduce una oración en la que se indica una condición real o hipotética que se ha de cumplir necesariamente para que sea cierto o se produzca lo que se expresa: Si corres, lo alcanzarás.

‘Sino’ es una conjunción adversativa que se escribe en una sola palabra y se usa, principalmente, para contraponer un concepto a otro: No estudia, sino que trabaja.

‘Si no’** introduce una oración condicional: Si no estudias, no aprobarás.

### Ejemplo de condicionales en Python

```Python
edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Usted es mayor de edad")

else:
    print("Usted es menor de edad")
```
```Python
numero =int(input("Escribe un número: "))

if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")
```
## Varios Paises en mi Conversor de Monedas

Un detalle muy importante en cualquier lenguaje de programación es conocer las diferencias entre los condicionales. En Python en particular, es crucial mencionar la diferencia entre if, elif y else.

Diferencias entre if, else y elif

### if:
if se encarga de iniciar el condicional y solicitar un requisito para ejecutar todo el código por debajo, que conocemos como bloque de código.

### else:
Si se desea ejecutar otro código en caso de que no se cumpla el if. Por ejemplo: el usuario no elige la opción 1, entonces (else)…

### elif:
Se utiliza cuando utilizamos múltiples condiciones, lo que en el código de esta clase son la opción 2 y 3. En esta clase, teníamos la opción 1, pero debemos también evaluar qué pasa si el usuario elige la opción 2 o 3, por lo que decimos “que estamos evaluando múltiples condiciones”.

### Añadir comentarios en Python
Para realizar un comentario (de una sola línea), empleamos el “#”. Un comentario es simplemente texto, el cual no es ejecutado y no afecta en absoluto en el código. Se utiliza para explicar las líneas de código que hemos creado y hacerlas más fáciles de entender.

## Aprendiendo a no Repetir Código con Funciones 

Las funciones ayudan a optimizar el código. Es decir, utilizar la menor cantidad de líneas dentro del código y evitar escribir acciones repetitivas.

Esto nos sirve para entregar un código más limpio y con buenas prácticas, que no desperdicia recursos innecesariamente. En Python, para definir funciones empleamos def.

Gracias a def, podemos “definir” funciones que emplearemos más tarde. Una función, en programación, es un grupo de instrucciones con un objetivo en particular y que se ejecuta cuando es “invocada”.

Cuando la definimos, estamos dándole un conjunto de instrucciones o un algoritmo. Al ahorrar líneas de código con funciones logramos también que la legibilidad de este sea más fácil.

### Cómo usar def en Python
```Python
def nombredelafuncion():
    # instrucciones de la función
```

### Ejemplo de funciones con def en Python
```Python
def conversacion(opcion):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opcion: ' + str(opcion))
    print('Adiós')

opcion = int(input('Ingrese una opción (1, 2, 3): '))

if opcion == 1:
    conversacion(opcion)

elif opcion == 2:
    conversacion(opcion)

elif opcion == 3:
    conversacion(opcion)

else:
    print('Escribe una opción correcta.')
```

## Modularizando Nuestro Conversor de Monedas

Para el siguiente ejemplo, crearemos el código para un conversor de monedas.

En la primera parte se define la función que resumirá muchos procesos del programa. Usando def, se agrega la función “conversor” con los parámetros que varían dependiendo de las respuestas, que son: tipo de pesos y valor del dólar. Es decir, dentro del programa se definirá el valor de cada parámetro.
```Python
def conversor(tipo_pesos, valor_dolar):
```
En la variable pesos se plantea que el usuario introduzca con input la cantidad de pesos que tiene, encontrando el primer parámetro, que es el tipo de pesos, que se establece más adelante por fuera de la función, ya que es un protocolo.
```Python
pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
```
Ese dato ingresado en la variable pesos se convierte de un string a un número con float.
```Python
pesos = float(pesos)
```
En este punto, la variable dólares aparece para definir cuánto cuesta, con base en los pesos ingresados anteriormente y el valor dólar que se definirá más tarde por fuera de la función, ya que es un protocolo.
```Python
dolares = pesos / valor_dolar
```
El valor, que probablemente sea decimal, se reduce con el atributo round dependiento de la variable dolares a solo 2 decimales.
```Python
dolares = round(dolares, 2)
```
Debido a que los dólares son obtenidos como números, se traducen a strings por medio del operador str
```Python
dolares = str(dolares)
```
Una vez obtenido el valor de los dolares en string, se imprime el resultado entre cadenas de texto.
```Python
print (“Tienes $ " + dolares + " dolares”)
```
Luego de establecer la función, se crea la variable menu que no se imprime y contiene texto de referencia.
```Python
menu = “”“
Tienes dinero 💲
Nosotros la convertimos 💰
1 - cop
2 - eur
3 - arg
Elige una opción: “””
```
Ya definida la variable menu, se crea la variable opción que dependerá de lo ingresado en input por el usuario en relación con la variable menu. Es decir, que se imprime menu y se deja el espacio para obtener un dato digitado por el usuario, que luego es traducido en número usando int.

```Python
opción = int(input(menu))
``` 
Dependiendo de lo que este usuario ingrese en el input de la variable opción: Usando if, si es igual a 1, entonces se ejecuta la función anterior de conversor. Dentro de esta se establece el protocolo de tipo de peso para este caso y en relación con menu que es Colombianos. El protocolo de valor del dólar se define con base en el tipo de peso
```Python
if opción == 1:
conversor(“colombianos”, 3875)
```
Empleando elif, si se selecciona otra opción de la variable menu ingresado en el input de opción, se ajusta el protocolo en función a lo mostrado en menu.
```Python
elif opción == 2:
conversor(“euros”, 0.8)
elif opción == 3:
conversor(“argentinos”, 65)
```
Si no se ingresa ningún dato relacionado dentro de las 3 opción de menu, se imprime que ingrese una opción correcta.
```Python
else:
print(“ingresa una opción correcta”)
```
## Trabajando con Texto: Cadenas de Caracteres

Para trabajar con cadenas de texto en Python, vamos a aplicar una serie de métodos a las variables que hayamos creado anteriormente.
Método: es una función especial, que existe para un tipo de dato en particular. Por ejemplo, si queremos que el texto ingresado se transforme en mayúsculas.

### Métodos para trabajar con texto en Python

En python se puede hacer más que concatenar cadenas

* **variable.strip():** El método strip eliminará todos los caracteres vacíos que pueda contener la variable

* **variable.lower():** El método lower convertirá a las letras en minúsculas.

* **variable.upper():** El método upper convertirá a las letras en mayúsculas.

* **variable.capitalize():** El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

* **variable.replace (‘o’, ‘a’):** El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.

* **len(variable):** Te indica la longitud de la cadena de texto dentro de la variable en ese momento.

### Índices:
Se escriben entre corchetes al lado de la variable y son apuntadores numéricos a cada caracter. Por ejemplo, para el nombre Facundo, cuando utilizamos la variable **nombre[1]**, aparece la letra ‘a’, dado que dicha variable tiene almacenada en ese momento la cadena de caracteres ‘Facundo’ donde la ‘a’ es el segundo caracterer.

**Aclaración:** se comienza a contar caracteres desde el 0 (que es el primer número en informática). Siguiendo el ejemplo, la letra ‘F’ de ‘Facundo’ es el caracter número 0. Por ende, nombre[0], nos devolvería una F.

## Trabajando con Texto: Slices

En Python, los slices, traducidos al español como “rebanadas”, nos permiten dividir los caracteres de un string de múltiples formas. A continuación, realizaremos un ejemplo cómo utilizarlos:

### Cómo usar slices en Python
```Python
nombre = "Francisco"
nombre
"Francisco"
nombre[0 : 3]
```
Arranca desde el primer índice hasta llegar antes del 3° índice.
El resultado sería
"Fra"
```Python
nombre[:3]
```
Va desde el principio hasta antes de llegar del 3° índice. Como no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio. Recordemos que empezamos a contar desde cero como primer dígito.
El resultado sería
"Fra"
```Python
nombre[1:7]
```
Arranca desde el índice 1 hasta llegar antes del 7.
El resultado sería
"rancis"
```Python
nombre[1:7:2]
```
Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3er parámetro, el cual es 2.
El resultado sería
"rni"
```Python
nombre[1::3]
```
Arranca desde el índice 1 hasta el final del string (al no haber ningún 2° parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
El resultado sería
"rcc"
```Python
nombre[::-1]
```
Al no haber parámetro en las 2 primeras posiciones, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
El resultado sería
"ocsicnarF"

## Proyecto: Palindromo 

En este ejemplo, aprenderemos a detectar si una palabra es palíndromo en Python. Para el ejemplo utilizaremos “Luz azul”.

Vamos a definir la función utilizando def:
```Python
def esPalindromo(palabra):
	palabra = str(palabra).strip().lower()
	palabra and print(palabra == palabra[::-1])
esPalindromo(luzazul) # va a imprimir True.
```

**¿Qué acaba de ocurrir?**

En la primera línea de la función, convertimos el valor recibido a string, eliminamos los espacios indeseados aplicando strip y formateamos a minúscula con lower.

¿Por qué? Porque si ejecutamos esPalindromo(True) nuestro programa mostraría un error, ya que no se pueden ejecutar métodos strip y lower sobre datos de tipo booleano.

En la segunda línea, ejecutando palabra and, lo que le decimos al programa es que si la variable palabra es Truty, ejecute el código después del and.

Esta es una forma mucho más corta de correr el siguiente código:
```Python
if palabra == True:
	#ejecutar.....
```
**Pero, ¿qué es un valor truty?**

En programación, un valor truty es cualquier valor que, sin ser explícitamente un booleano True, la computadora lo interpreta como un true. Por ejemplo: cualquier número mayor a 0 o cualquier string que no este vacío.

Luego, dentro del print() no es necesario hacer un if que retorne true o false, al hacer la comparación.
```Python
# if palabra == palabra[::-1]:
#	return True
# else:
#	return False

palabra == palabra[::-1]
```
Si la comparación es correcta, va a imprimir True, de lo contrario devolvera False.

## Aprendiendo Bucles 

Un bucle es un ciclo continuo en todos los lenguajes de programación que nos permite iterar sobre nuestros pasos: magina un contador cíclico (1,2,3,4,5,6…) donde puedes agregar un paso más sobre tu programa principal.

### Ejemplo de bucle en Python
Para este ejemplo, utilizaremos las potencias hasta llegar a un número determinado:
```Python
def potencia(numero):
    
    potencia = 1

    while (potencia <= 10):
        
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1
        

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(numero)


if __name__ == "__main__":
    run()
```
### Ejemplo de bucle en la vida real

* Despertar
* Estudiar en Platzi
* Comer
* Dormir

Cuando repetimos estas acciones en ese orden, durante un tiempo determinado o infinito estamos hablando de un bucle.

## El Ciclo While

Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).

La sintaxis del bucle while es la siguiente:
```Python
while condicion:
    cuerpo del bucle
```
Python evalúa la condición:

* Si el resultado es True, se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
* Si el resultado es False, el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.

### Ejemplo de while en Python
```Python
def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) +
              ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == "__main__":
    run()
```
## Explorando un Bucle Diferente: El Ciclo For

El ciclo for es un tipo de bucle usado cuando se conozcan la cantidad de veces a iterar.

Un contador es una variable que se encarga de contener valores que irán incrementando o decrementando cada vez que se ejecuta una acción que lo contenga. El incremento o decremento es llamado paso del contador y es siempre constante.

**Ejemplo:** El marcador de un partido de fútbol, cada vez que un equipo anote un gol, aumenta su marcador en una unidad.

**Ejemplo 2:** En las carreras de autos, cuando un vehículo pasa por la línea de meta, se incrementa en una unidad el número de vueltas dadas al circuito, o bien se decrementa el número de vueltas que faltan por realizar.

Entonces, el incremento es siempre constante, el paso del contador no necesariamente puede ser una unidad, también puede incrementarse o decrementarse de a dos, tres, cuatro, hasta n. Es decir, puede ser cualquier número que conserve siempre el mismo valor durante todo el programa.

Su sintaxis es:
```Python
variable = variable + constante(al incrementar)
variable = variable - constante(al decrementar)
```
o de manera resumida:
```Python
variable += constante
variable -= constante
```
Ejemplo:
```Python
gol_local = 0 #si anotan gol: gol_local = gol_local +1
```
Consejo: Es importante inicializar en cero a la variable cuando aparezca a ambos lados del símbolo de asignación

### Ejemplo del bucle for en Python
```Python
def imprimir_numero(inicio, fin):
    for inicio in range(fin+1):
        print(f'Numero: {inicio}')


def imprimir_numero_while(inicio, fin):
    while inicio <= fin:
        print(f'Numero: {inicio}')
        inicio += 1

def run():


    while True:
        print('')
        print('*********************************************************')
        print('*******************N U M E R O S**********************')
        print('')
        inicio = int(input('Digite el número inicial para la secuencial:  '))
        print('')
        fin = int(input('Digite el número final para la secuencial: '))
        print('')

        if inicio < fin:
            imprimir_numero(inicio,fin)
        else:
            print(f'El numero inicial {inicio} debe ser ser menor al numero final {fin}.')



if __name__ == "__main__":
    run()
```

## Recorriendo un string con for

Recorrer un string con el ciclo For es tomar la cadena de caracteres y separarlas una a una. De este modo, quedaría el comando:
```Python
def run():
    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())
 
if __name__ == "__main__":
    run()
```

Donde usaremos la variable frase para recorrer la frase que se escriba en el input. Cuando se escriba una frase, se recorrerá cambiando todas las letras a mayúsculas.

Ejemplo del ciclo For para recorrer strings en Python

**Ejemplo 1**
```Python
def run():
    ## Este ejemplo imprime cada caracter de tu nombre
    nombre = input("Escribe tu nombre :")
    for letra in nombre:
        print(letra)

if __name__ == "__main__":
    run()
```
**Ejemplo 2**
```Python
def run():
    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()
```
## Interrumpiendo ciclos con Break y Continue

La instrucción continue en Python devuelve el control al comienzo del ciclo while o ciclo for. Esta instrucción rechaza todas las declaraciones restantes en la iteración actual del ciclo y mueve el control de regreso a la parte superior del mismo.

La instrucción break en Python termina el ciclo actual y reanuda la ejecución en la siguiente instrucción. En otras palabras, break rompe el ciclo entero mientras que continue solo rompe la vuelta actual.

Ejemplos de interrupción de ciclos con break y continue en Python

**Ejemplo1**
```Python
def run():
    for i in range(10000):
        print(i)
        if i == 5678:
            break

if __name__ == '__main__':
    run()
```
**Ejemplo 2**
```Python
def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

if __name__ == '__main__':
    run()
```
**Ejemplo 3**
```Python
def run():
    texto= input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()
```

## Proyecto: Prueba de Primalidad 

En este ejemplo, aprenderemos cómo detectar si un número es primo en Python. Esto se conoce como prueba de primalidad. Un número primo es todo número que puede dividirse únicamente por sí mismo y por 1. Todos los números primos, excepto el 2, son impares.

En la matemática aplicada, los números primos son utilizados para generar códigos criptográficos seguros. Esto se logra empleando los números primos de Mersenne (números muy grandes).

Ejemplo: cómo averiguar si un número es primo en Python
```Python
def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0
    for i in range(1 , numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(str(numero) + " es primo")
    else:
        print(str(numero) +  " NO es primo")


if __name__ == "__main__":
    run()
```

## Proyecto: Videojuego

Para el siguiente ejemplo, utilizaremos módulos en Python para crear la funcionalidad de nuestro código. Un módulo es un archivo con funciones ya predefinidas, que tenemos disponibles para ejecutarlas. Para traer o invocar un módulo, debemos escribir lo siguiente:
```Python
import random
```
En este caso, “importamos” la función random, que trae un conjunto de funciones que nos permiten trabajar con la aleatoridad.
```Python
numero_aleatorio = random. 
```
Gracias al punto ., accedemos a las funciones que trae el módulo. En este caso, generamos una variable y le asignamos random.randint(1, 100), lo cual nos genera un número aleatorio entero desde un número hasta otro (en este caso del 1 al 100).

Ejemplo de juego de aleatoriedad con módulos en Python
```Python
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un numero del 1 al 100 :"))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_elegido = int(input("Elije otro numero  :"))
    print("Ganaste!")


if __name__ == "__main__":
    run()
```

## Almacrnar Varios Valores en una variable: Listas

Las listas nos permiten guardar múltiples valores en una sola variable. Estas listas en Python nos permiten guardar elementos del mismo tipo o diferentes, por lo que podemos tener strings, números enteros y decimales juntos en una misma variable. Las listas también son conocidas como arrays en otros lenguajes programación.

Cómo trabajar con listas en Python

### Declarar lista
my_lista = []
my_lista = list()

### Unir listas
my_lista = [1]
my_lista2 = [2,3,4]
my_lista3 = my_lista + my_lista2
my_lista3 # [1,2,3,4]

### Partir listas como slices
my_lista = [1,2,3]
my_lista[1:] = [2,3]

### Extender una lista
my_lista = [1]
my_lista2 = [2,3,4]
my_lista.extend(my_lista2) # [1,2,3,4]

### Multiplicar listas
my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']

### Eliminar el último elemento de la lista
my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]

### Ordenar lista
my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]

### Eliminar un elemento
my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

### Eliminar si conocemos su valor
my_lista = [1,2,3,4,5]
my_lista.remove(3)
my_lista #[1,2,4,5]

### saber qué métodos hay dentro de un elemento
my_lista = [1,2,3,4,5]
dir(my_lista) # ['__add__', '__class__', '__contains__', ...

### Modificar un elemento
my_lista = [1,2,3,4,5]
my_lista[0] = 100
my_lista # [100,2,3,4,5]

### Añadir un elemento al final
my_lista = [1,2,3,4,5]
my_lista.append(6)
my_lista # [1,2,3,4,5,6]

### Organizar una lista
my_lista = [2,5,1,3,4]
my_lista.sort() #[1,2,3,4,5]

### Métodos adicionales para listas
.sorted()
También ordena como sort() pero modifica la lista inicial
.clear()
Vacía la lista
.count()
Cuenta las veces que esta un elemento en lista
.index()
Indica la posición donde esta un elemento de la lista
.insert()
Inserta un elemento en una posición dada ej: lista.insert(posición,item)
.reverse()
Le da la vuelta a una lista
