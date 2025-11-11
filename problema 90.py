import re

prohibidas = ["tonto", "feo"]  
texto = input("Introduce el texto: ")

patron = r'\b(' + '|'.join(re.escape(p) for p in prohibidas) + r')\b'
regex = re.compile(patron, flags=re.IGNORECASE)

censurado = regex.sub(lambda m: '*' * len(m.group(0)), texto)

print("\nTexto censurado:")
print(censurado)
```import re

prohibidas = ["tonto", "feo"] 
texto = input("Introduce el texto: ")

patron = r'\b(' + '|'.join(re.escape(p) for p in prohibidas) + r')\b'
regex = re.compile(patron, flags=re.IGNORECASE)

censurado = regex.sub(lambda m: '*' * len(m.group(0)), texto)

print("\nTexto censurado:")
print(censurado)