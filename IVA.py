"""Hacer un programa que calcule el IVA de una compra  """

def CalcularIVA(p):
    IVA = p*0.19
    return IVA

precioCompra= float(input("Ingrese el valor de la compra"))

IVA = CalcularIVA(precioCompra)

print("El valor  de su primer compra sin IVA es : ", precioCompra)
print("EL valor de su segunda compra con IVA es : ", precioCompra + IVA)
