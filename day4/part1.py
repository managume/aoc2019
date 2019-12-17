"""
Cond. 1: Tiene que tener seis dígitos
Cond. 2: Tiene que estar dentro del rango dado
Cond. 3: Al menos dos dígitos adyacentes tienen que ser iguales
Cond. 4: Las cifras tienen que incrementar su valor, nunca disminuir.
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
        #print(f"Checking candidate: {candidate}")
        if not check_size(candidate):
            #print("Error: Less than 6 digits")
            pass
        elif not check_doubles(candidate):
            #print("Error: There are no adjacent digits")
            pass
        elif not check_increasing(candidate):
            #print("Error: Does not meet increasing criteria")
            pass
        else:
            candidates.append(candidate)
    return candidates


example = [122345,111123,135679,111111,223450,123789]
dictionary = [x for x in range(307237,769059,1)]

passwords = cracker(dictionary)
number_of_passwords = len(passwords)

print(passwords)
print(number_of_passwords)