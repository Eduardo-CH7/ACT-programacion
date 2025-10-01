def es_email_valido(email):
    return "@" in email

email = input("Introduce tu dirección email: ")
if es_email_valido(email):
    print("La dirección es válida.")
else:
    print("La dirección no es válida.")