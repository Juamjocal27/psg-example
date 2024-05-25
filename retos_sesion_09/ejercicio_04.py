# Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes y otra con los precios
abarrotes = ["Leche", "Pan", "Huevo", "Azucar", "Arroz"]
print(abarrotes)
precio = [6, 0.5, 1, 4, 10]

# 1. Agregar 5 productos, nuevos al final de las listas
abarrotes.append("Fideo")
precio.append(6)
abarrotes.append("Avena")
precio.append(7)
abarrotes.append("Harina")
precio.append(5.5)
abarrotes.append("Sal")
precio.append(2)
abarrotes.append("Cereales")
precio.append(3)
print(abarrotes)

# 2. Eliminar el producto con el nombre "Leche" de las listas
eliminar = abarrotes.index("Leche")
abarrotes.pop(eliminar)
precio.pop(eliminar)
print(abarrotes)

# 3. ¿Cúanto cuesta el producto "Pan" y "Huevo"
pan = abarrotes.index("Pan")
huevo = abarrotes.index("Huevo")
print("Precio pan: ", precio[pan])
print("precio huevo:", precio[huevo])

# 4. ¿Cual es el producto más caro y más barato?
print(precio)
caro = precio.index(max(precio))
barato = precio.index(min(precio))
producto_caro = abarrotes[caro]
producto_barato = abarrotes[barato]
print("Caro: ", producto_caro)
print("Barato:", producto_barato)

# 5. ¿Cuantos productos tienes en total?
Total_productos = len(abarrotes)
print("Total de productos:", Total_productos)

# 6. ¿Cuanto cuesta el total de los productos?
total_precios = sum(precio)
print(total_precios)

# 7. Ordena los productos alfabéticamente y precios si es posible
abarrotes.sort()
precio.sort()
print(abarrotes)
print(precio)

# 8. Eliminar todos los productos de las listas
abarrotes.clear()
precio.clear()
print(abarrotes)
print(precio)