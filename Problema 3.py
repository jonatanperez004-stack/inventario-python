# =========================================
# PROBLEMA 3 - AUDITORIA DE INVENTARIO
# Fundamentos de Programación
# =========================================

# Función
def calcular_pedido(stock_actual, stock_minimo):

    # Verificar si el stock es menor al mínimo
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


#inventario

inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Memoria USB", 20, 15],
    ["A105", "Audifonos", 2, 6]
]


print("===================================")
print("   LISTA DE REABASTECIMIENTO")
print("===================================")


for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("-----------------------------------")
    

input("Presiona Enter para salir...")