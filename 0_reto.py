### El famoso fizz buzz

"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 """

string1 = "fizz"

string2 = "buzz"

string3 = "fizzbuzz"

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
       print(string3)
    elif i % 3 == 0 :
        print(string1)
    elif i % 5 == 0:
       print(string2)
    else: 
      print(i)

# Prestar atención con el orden de las condiciones.