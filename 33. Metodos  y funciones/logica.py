def chequear_numero_en_lista(nu_list):
    
    for number in nu_list:
        if number % 2 == 0:
            return True
        print("True")
    
    else:
            pass
    return False
print("False")

chequear_numero_en_lista([2,3,5])