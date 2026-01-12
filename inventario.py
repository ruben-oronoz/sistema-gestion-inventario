class Inventario:
    def __init__(self):
        self.inventario = []
        self.cargar_archivo()

    def agregar_producto(self):
        nombre = input("Nombre: ").title()

        if nombre == "":
            print("ERROR: Nombre vacío")
            return

        if self.producto_existe(nombre):
            print("ERROR: El producto ya existe")
            return

        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))

            if precio < 0 or stock < 0:
                print("ERROR: Número inválido")
                return

            producto = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }

            self.inventario.append(producto)
            self.guardar_archivo()
            print("Producto agregado con éxito")

        except ValueError:
            print("ERROR: Debe ingresar valores numéricos en Precio y Stock")

    def mostrar_productos(self):
        if not self.inventario:
            print("Inventario vacío")
            return

        for p in self.inventario:
            self.mostrar_producto(p)

    def buscar_producto(self):
        nombre = input("Nombre del producto a buscar: ").title()

        for p in self.inventario:
            if p["nombre"] == nombre:
                self.mostrar_producto(p)
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

    def mostrar_producto(self, producto):
        print(
            f"Nombre: {producto['nombre']} | "
            f"Precio: {producto['precio']}$ | "
            f"Stock: {producto['stock']}"
        )

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
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock)
                    })
        except FileNotFoundError:
            pass

    def producto_existe(self, nombre):
        for p in self.inventario:
            if p["nombre"] == nombre:
                return True
        return False
