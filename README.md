# Reto-12
# Punto 1
Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
- endswith: Verifican si una cadena termina o empieza con un parametro especifiado
### Ejemplo:
```python
text = "Hola Mundo"
print(text.endswith("Mundo"))  #Verifica si el string termina con Mundo  
print(text.startswith("Hola")) #Verifica si el string comienza con Hola
```
- isalpha: Verifica si los caracteres de la cadena son letras
### Ejemplo: 
```python
texto = "python"
print(texto.isalpha())
texto = "python1"
print(texto.isalpha())
```
- isalnum: Verifica si los caracteres de la cadena son alfanumericos.
### Ejemplo: 
```python
texto = "hola123"
print(texto.isalnum()) #Los caracteres son alfanumericos.
texto = "hola mundo" #Tiene un espacio y por lo tanto es false. 
print(texto.isalnum())
```
- isdigit: Verifica si los caracteres de la cadena son digitos.
### Ejemplo: 
```python
texto = "1234"
print(texto.isdigit()) #Los caracteres son digitos.
texto = "hola123" #Tiene letras y por lo tanto es false. 
print(texto.isdigit())
```
- isspace: Verifica si todos los caracteres de la cadena son espacios en blanco.
### Ejemplo 
```python
texto = "      "
print(texto.isspace()) #Los caracteres son espacios en blanco.
texto = "hola mundo" #Tiene letras y por lo tanto es false. 
print(texto.isspace())
```
- istitle:Verifica si la cadena sigue el formato de titulo (Cada palabra empieza con mayuscula y el resto en minusculas)
### Ejemplo: 
```python
texto = "Hola Mundo"
print(texto.istitle()) 
texto = "hola mundo" #Las palabras no empiezan con mayuscula y por lo tanto es false. 
print(texto.istitle())
```
- islower, issupper : Verifican si los caracteres alfabeticos estan en mayusculas o minusculas
### Ejemplo 
```python
texto = "HOLA MUNDO"
print(texto.isupper()) 
print(texto.islower())
texto = "Hola Mundo" 
print(texto.islower())
print(texto.isupper())
texto = "hola mundo"
print(texto.islower())
print(texto.isupper())
```
# Punto 2 
Procesar el archivo y extraer:
- cantidad de vocales
- cantidad de consonantes
- 50 palabras que mas se repiten
```python
from collections import Counter
import re

# Leer el archivo
with open('mbox.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Contar vocales
vocales = 'aeiou'
numeroVocales = sum(text.lower().count(v) for v in vocales)

# Contar consonantes
consonantes = 'bcdfghjklmnpqrstvwxyz'
numeroConsonantes = sum(text.lower().count(c) for c in consonantes)

# Contar palabras
palabras = re.findall(r'\b\w+\b', text.lower())
cantidadPalabras = Counter(palabras)
palabrasMasComunes = cantidadPalabras.most_common(50)

print(f'Cantidad de vocales: {numeroVocales}')
print(f'Cantidad de consonantes: {numeroConsonantes}')
print('Listado de las 50 palabras que más se repiten:')
for palabra, conteo in palabrasMasComunes:
    print(f'{palabra}: {conteo}')
```
  
