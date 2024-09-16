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
