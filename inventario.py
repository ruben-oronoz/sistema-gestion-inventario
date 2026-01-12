class Inventario:
	def __init__(self):
		self.inventario= []
		self.cargar_archivo()
		
	def agregar_producto(self):
		nombre = input("Nombre: ").title()
		if self.producto_existe(nombre):
    print("ERROR: El producto ya existe")
    return
		if nombre == "":
			print("ERROR: Nombre vacio")
			return
			
		try:
			precio = float(input("Precio: "))
			stock = int(input("Stock: "))
			
			if precio < 0 or stock < 0:
				print("ERROR: Numero invalido")
				return
				
			producto = {
			'nombre': nombre,
			'precio': precio,
			'stock': stock
			}
			self.inventario.append(producto)
			self.guardar_archivo()
			print("Producto agregado con exito")
			
		except ValueError:
			print("ERROR: Debe ingresar valores numericos en Precio y Stock")
				
	def mostrar_productos(self):
		if not self.inventario:
			print("Inventario vacio")
			return
		
		for p in self.inventario:
			print(f"{p['nombre']} | {p['precio']}$ | {p['stock']}")
			
	def buscar_producto(self):
		nombre = input("Nombre del producto a buscar: ").title()
		
		for p in self.inventario:
			if p['nombre'] == nombre:
				print(p)
				return
		print("No encontrado")			
	
	def eliminar_producto(self):
    nombre = input("Nombre del producto a eliminar: ").title()

    for p in self.inventario:
        if p["nombre"] == nombre:
            confirmacion = input("¿Seguro que desea eliminarlo? (s/n): ").lower()
            if confirmacion == "s":
                self.inventario.remove(p)
                self.guardar_archivo()
                print("Producto eliminado con éxito")
            else:
                print("Eliminación cancelada")
            return

    print("No encontrado")
    	
	def guardar_archivo(self):
		with open("inventario.txt", "w") as archivo:
				for p in self.inventario:
					archivo.write(f"{p['nombre']},{p['precio']},{p['stock']}\n")
				
	def cargar_archivo(self):
		self.inventario.clear()
		try:
			with open("inventario.txt", "r") as archivo:
				for linea in archivo:
					nombre, precio, stock = linea.strip().split(",")
					self.inventario.append({
					'nombre': nombre,
					'precio': float(precio),
					'stock': int(stock)
					})
		except FileNotFoundError:
			pass
