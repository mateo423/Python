def chequear_numero_en_lista(nu_list):

    for numbers in nu_list:
        if numbers % 2 == 0:
            print("True")
            return True

    else:
        pass
    print("False")
    return False


chequear_numero_en_lista([1, 3, 5])
# con esto podemos ver el typo de dato que es  function print(type(chequear_numero_en_lista))
