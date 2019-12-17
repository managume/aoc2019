"""
Cond. 1: Tiene que tener seis dígitos
Cond. 2: Tiene que estar dentro del rango dado
Cond. 3: Al menos dos dígitos adyacentes tienen que ser iguales
Cond. 4: Las cifras tienen que incrementar su valor, nunca disminuir.
Cond. 5: Tiene que tener dos dígitos adyacentes que no formen parte de otro grupo de números adyancentes superior.
"""

def check_size(number):
    chars = [int(c) for c in str(number)]
    return len(chars) == 6

def check_doubles(number):
    chars = [int(c) for c in str(number)]
    i = 0
    while i < (len(chars)-1):
        if chars[i] == chars[i+1]:
            return True
        i += 1

def check_exact_doubles(number):
    state = False
    chars = [int(c) for c in str(number)]
    d = {chars.count(x):x for x in chars}
    print(d)
    for key in d.keys():
        if key == 2:
            state = True
    return state

def check_increasing(number):
    chars = [int(c) for c in str(number)]
    i = 0
    state = True
    while i < (len(chars)-1):
        if chars[i] > chars[i+1]:
            state = False
        i += 1
    return state

def cracker(dictionary):
    candidates = []
    for candidate in dictionary:
        #print(f"Verificando contraseña candidata: {candidate}")
        if not check_size(candidate):
            #print("Error: La contraseña candidata no tiene 6 dígitos")
            pass
        elif not check_doubles(candidate):
            #print("Error: La contraseña candidata no tiene dígitos adyacentes")
            pass
        elif not check_increasing(candidate):
            #print("Error: La contraseña candidata no cumple el criterio ascendente")
            pass
        elif not check_exact_doubles(candidate):
            #print("Error: La contraseña candidata no tiene dobles exactos")
            pass
        else:
            candidates.append(candidate)
    return candidates


example1 = [122345,111123,135679,111111,223450,123789]
example2 = [112233,123444,111122]
dictionary = [x for x in range(307237,769059,1)]

passwords = cracker(dictionary)
number_of_passwords = len(passwords)

print(passwords)
print(number_of_passwords)