"""Hacer un programa que calcule el IVA de una compra  """


def CalcularIVA(compra):
    iva = compra * 0.19
    return iva


precioCompra = float(input("Ingrese el valor de la compra: "))

iva = CalcularIVA(precioCompra)

print("El valor  de su primer compra sin IVA es : ", precioCompra)
print("EL valor de su segunda compra con IVA es : ", precioCompra + iva)
