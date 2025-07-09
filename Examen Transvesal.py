
productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "UWU131HD": ["Dell", 15.6, "8GB", "SSD", "1TB", "AMD Ryzen 3", "Nvidia GTX1660Ti"],
    "0324UHD": ["Acer", 14, "16GB", "DD", "512GB", "Intel Core i5 9400f", "Nvidia RTX2080Ti"],
    "678FHD": ["Lenovo", 14, "8GB", "DD", "2T", "AMD Ryzen 7", "Integrada"],
    "FS5361HD": ["Acer", 15.6, "8GB", "DD", '1TGB',"Intel Core i9", 'Integrada'],
}
stock = {"8475HD": [387990, 10], # [precio, stock]
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "UWU131HD": [299990, 1],
    "0324UHD": [399990, 2],
    "678FHD": [499990, 3],
    "5598FHD": [387990, 5],
    "FS5361HD": [599990, 0], # Este modelo no tiene stock 
}

def Marca_En_Stock(marca):
    try:
        total = 0
        marca_lower = marca.lower()
        for modelo, detalles in productos.items():
            if detalles[0].lower() == marca_lower:
                if modelo in stock and len(stock[modelo]) > 1:
                    total += stock[modelo][1]
        print(f"El stock total para {marca.capitalize()} es: {total}")
    except Exception as e:
        print(f"¡Ocurrió un error inesperado!: {e}")

def Buscar_Precios(precio_minimo, precio_maximo):
    while True:
        try:
            resultados = []
            for modelo, detalles in productos.items():
                if modelo in stock and len(stock[modelo]) > 1:
                    precio, cantidad_stock=stock[modelo]
                    if precio_minimo<= precio <= precio_maximo and cantidad_stock > 0:
                
                        resultados.append(f"{detalles[0]}--{modelo}")

            if resultados:
                resultados.sort()
                print_titulo("Resultados de la Búsqueda")
                print("\nLos modelos en el rango de precios son:", resultados)
            else:
                print("\nNo hay notebooks en ese rango de precios.")
            
        except ValueError:
            print("¡Error! Debe ingresar valores enteros para los precios.")
def actualizar_precio(modelo, preciosNuevo):
    try:
        if modelo in stock:
            stock[modelo][0] = preciosNuevo
            return True
        return False
    except Exception as e:
        print(f"¡Ocurrio un error inesperado!: {e}")
        return False

def print_titulo(titulo):
    print("╔" + "═"*48 + "╗")
    print("║" + titulo.center(48) + "║")
    print("╚" + "═"*48 + "╝")


def main():
    while True:
        print_titulo("Menu Principal")
        print("╔" + "═"*48 + "╗")
        print("║1. Stock por marca.".ljust(49) + "║")
        print("║2. Búsqueda por precio.".ljust(49) + "║")
        print("║3. Actualizar precio.".ljust(49) + "║")
        print("║4. Salir.".ljust(49) + "║")
        print("╚" + "═"*48 + "╝")
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            if not marca:
                print("¡Error! El campo no puede estar vacío.")
                continue
            if not marca in stock:
                print("¡Error! La marca ingresada no existe.")
                continue
            print_titulo("Marca en Stock")
            Marca_En_Stock(marca)

        elif opcion == "2":
            while True:
                try:
                    precio_minimo = int(input("Ingrese precio mínimo: "))
                    precio_maximo = int(input("Ingrese precio máximo: "))
                    Buscar_Precios(precio_minimo, precio_maximo)
                    continuar = input("¿Desea buscar Notebook? (S/N): ").strip().lower()
                    if continuar != "N":
                        break

                except ValueError:
                    print("¡Error! Debe ingresar valores enteros!!")
                except Exception as e:
                    print(f"¡Error! Ocurrió un error inesperado: {e}")
        elif opcion == "3":
            while True:
                try:
                    print_titulo("Actualizar precios de Notebooks")
                    modelo = input("Ingrese modelo a actualizar: ").strip().upper()
                    if not modelo:
                        raise ValueError("El campo no puede estar vacio.") 
                    
                    Precio_Nuevo = int(input("Ingrese un nuevo precio para el producto seleccionado: "))
                    if actualizar_precio(modelo, Precio_Nuevo):
                        print_titulo("Precio actualizado con exito!.")
                    else:
                        print("El modelo seleccionado no existe.")
                    continuar = input("¿Actualizar otro precio? (S/N): ").strip().lower()
                    if continuar != "N":
                        break
                except ValueError:
                    print("¡Error! El precio debe ser un número entero!.")
                    
                
        elif opcion == "4":
            print("Muchas gracias por utilizar nuestro sistema. Hasta la proxima!")
            break
        else:
            print("Debe seleccionar una opción válida (1-4).")

if __name__ == "__main__":
    main()