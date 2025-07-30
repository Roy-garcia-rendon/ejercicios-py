#| Método           | Descripción                                    | Ejemplo                                   |
#| ---------------- | ---------------------------------------------- | ----------------------------------------- |
#| `.lower()`       | Convierte a minúsculas                         | `"Hola".lower()` → `"hola"`               |
#| `.upper()`       | Convierte a mayúsculas                         | `"hola".upper()` → `"HOLA"`               |
#| `.capitalize()`  | Primera letra en mayúscula                     | `"maria".capitalize()` → `"Maria"`        |
#| `.title()`       | Primera letra de cada palabra en mayúscula     | `"juan perez".title()` → `"Juan Perez"`   |
#| `.strip()`       | Quita espacios y saltos de línea               | `" Ana \n".strip()` → `"Ana"`             |
#| `.replace(a, b)` | Reemplaza `a` por `b`                          | `"Carlos".replace("C", "K")` → `"Karlos"` |
#| `.find(txt)`     | Devuelve la posición de `txt`, o -1 si no está | `"Ana".find("n")` → `1`                   |
#| `in`             | Verifica si hay una subcadena                  | `"jo" in "Jose"` → `True`                 |

nombre = "   María José\n"

# Limpieza básica
nombre = nombre.strip()
print(nombre)  # "María José"

# Estilo
print(nombre.lower())       # "maría josé"
print(nombre.upper())       # "MARÍA JOSÉ"
print(nombre.capitalize())  # "María josé"
print(nombre.title())       # "María José"

# Reemplazo
print(nombre.replace("í", "i"))  # "Maria José"

# Búsqueda
print(nombre.find("José"))  # 6
print("José" in nombre)     # True

nombre = "Rodrigo Aner Garcia "
print(nombre.strip())
print(nombre.title())
print(nombre.replace("o", "0"))
print("Aner" in nombre)