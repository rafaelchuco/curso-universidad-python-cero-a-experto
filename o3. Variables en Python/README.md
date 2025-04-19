# 🧠 Variables en Python

¡Hola y bienvenidos! 👋 En esta sección comenzamos a trabajar con uno de los conceptos más fundamentales en cualquier lenguaje de programación: **las variables**.

---

## 📌 ¿Qué es una variable en Python?

Una **variable** es un nombre simbólico que se utiliza para guardar un valor dentro de la memoria temporal (RAM) de la computadora. Este valor puede cambiar durante la ejecución del programa, de ahí el nombre "variable".

En Python, las variables **son dinámicas**, lo que significa que no necesitas declarar su tipo. Pueden almacenar diferentes tipos de datos en distintos momentos.

```python
# Ejemplos de variables
nombre = "María"       # Cadena de texto
edad = 30              # Número entero
peso = 65.5            # Número decimal (float)
es_casado = False      # Valor booleano (True/False)
```

---

## 🧾 Sintaxis de una variable

Para declarar una variable en Python:

```
nombre_variable = valor
```

- El **nombre de la variable** debe comenzar con una letra o guion bajo (`_`) y no debe contener espacios.
- El **símbolo igual `=`** es el operador de asignación.
- El **valor** puede ser de cualquier tipo: string, número, booleano, lista, etc.

📌 Importante: una variable **debe tener un valor asignado** al momento de ser creada. No se puede declarar una variable vacía sin valor asignado.

---

## 🔢 Tipos de datos comunes en variables

- **`str`** (cadenas de texto): `'hola'`, `"Python"`
- **`int`** (números enteros): `10`, `-3`
- **`float`** (números decimales): `3.14`, `-2.5`
- **`bool`** (booleanos): `True`, `False`
- **`None`** (ausencia de valor): `None`

Los valores booleanos se escriben **con la primera letra en mayúscula**.

---

## 🧠 Variables y memoria RAM: funcionamiento interno

Cuando se declara una variable en Python, esta no almacena directamente el valor asignado, sino que **apunta a un objeto** que contiene ese valor en otra parte de la memoria.

### Tipos de memoria en juego:
- **Stack**: almacena referencias de variables
- **Heap**: almacena los objetos (como números, cadenas, etc.)

```python
edad = 30  # Se crea una variable que apunta a un objeto de tipo int con valor 30
```

Este objeto de tipo entero se almacena en el heap, mientras que el nombre de la variable `edad` reside en el stack apuntando a esa dirección.

Si luego cambiamos el valor:
```python
edad = 32
```
Ya no se modifica el objeto anterior, sino que se **crea un nuevo objeto** en una dirección distinta, y la variable ahora apunta a esta nueva dirección.

🔁 Este comportamiento es el que permite que las variables cambien su valor durante la ejecución.

---

## 📏 Reglas y buenas prácticas para nombres de variables

### ✅ Reglas básicas:
- Pueden contener letras (mayúsculas/minúsculas), dígitos (0-9) y guiones bajos `_`
- **No pueden comenzar con dígitos**
- **No pueden usar palabras reservadas** del lenguaje (`if`, `class`, `for`, `try`, etc.)
- Python es **case sensitive**: `mi_variable` y `Mi_variable` son distintas

### 🤝 Buenas prácticas (convenciones):
- Usar **snake_case**: minúsculas y guiones bajos entre palabras (`nombre_usuario`, `edad_actual`)
- Nombres **descriptivos**: evitar letras sueltas como `x` o `n` a menos que sean temporales o en bucles

---

## 🔍 Constantes en Python

Python no tiene una sintaxis especial para declarar constantes, pero existe una **convención** para indicar que una variable no debe cambiar:

- Se escribe el nombre de la constante en **mayúsculas** y usando guiones bajos (`_`) para separar palabras

```python
PI = 3.14159
MENSAJE_ERROR = "Ha ocurrido un error."
NOMBRE_USUARIO_VALIDO = "admin"
```

Aunque técnicamente puedes modificar el valor de una constante, **no deberías hacerlo**. Esta convención es una guía para que tú (y otros programadores) respeten su inmutabilidad.

También puedes acceder a constantes definidas en módulos estándar como `math`:

```python
import math
print(math.pi)  # 3.141592653589793
```

---

## 🧪 Práctica y Ejercicios

En los siguientes ejemplos comenzaremos a crear variables, observar cómo cambian sus valores, y cómo usar distintos tipos de datos.

```python
nombre = "Juan"
print("Hola", nombre)

nombre = "Lucía"
print("Ahora el nombre es:", nombre)
```

Este tipo de práctica te permitirá entender cómo se comportan las variables y cómo manipular la información durante la ejecución de tus programas.

---

## 🚀 Próximo paso

En el siguiente módulo comenzaremos a realizar ejercicios prácticos para afianzar estos conceptos. ¡Prepárate para escribir tu primer programa dinámico en Python! 

