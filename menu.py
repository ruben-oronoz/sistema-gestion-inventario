from inventario import Inventario

inv = Inventario()

while True:
	print("~~~~MENU~~~~")
	print("1. Agregar Producto")
	print("2. Mostrar Productos")
	print("3. Buscar Producto")
	print("4. Eliminar Producto")
	print("5. Salir")
		
	opcion = input("Elegir: ")
		
	if opcion == "1":
		inv.agregar_producto()
	elif opcion == "2":
		inv.mostrar_productos()
	elif opcion == "3":
		inv.buscar_producto()
	elif opcion == "4":
		inv.eliminar_producto()
	elif opcion == "5":
		print("Inventario guardado, hasta luego...")
		break	
	else:
		print("Opcion invalida")
