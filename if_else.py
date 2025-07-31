#if condición:
    # código si la condición es verdadera
#elif otra_condición:
    # código si la primera es falsa, pero esta es verdadera
#else:
    # código si ninguna condición fue verdadera

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("puedes votar")
else:
    print("no puedes votar")


#| Operador | Significado              | Ejemplo            |
#| -------- | ------------------------ | ------------------ |
#| `==`     | Igual a                  | `x == 10`          |
#| `!=`     | Distinto de              | `x != 10`          |
#| `>`      | Mayor que                | `x > 10`           |
#| `<`      | Menor que                | `x < 10`           |
#| `>=`     | Mayor o igual            | `x >= 10`          |
#| `<=`     | Menor o igual            | `x <= 10`          |
#| `and`    | Y (ambas condiciones)    | `x > 5 and x < 10` |
#| `or`     | O (una u otra)           | `x < 0 or x > 100` |
#| `not`    | No (niega una condición) | `not x == 10`      |

calificación = int(input("ingresa tu calificación: "))
if calificación >=90:
    print("exelente")
elif calificación >=70:
    print("Bien")
else:
    print("Reprobado")
