# verificar_as.py
def es_as_privado(asn):
    if (64512 <= asn <= 65534) or (4200000000 <= asn <= 4294967294):
        return True
    return False

asn = int(input("Introduce el número de AS de BGP: "))

if es_as_privado(asn):
    print(f"El AS {asn} es privado.")
else:
    print(f"El AS {asn} es público.")
