from datetime import datetime

class SistemaComidasRapidas:
    def __init__(self):
        # Datos almacenados en memoria con ejemplos
        self.comidas = [
            {"id": 1, "nombre": "Hamburguesa Clásica", "precio": 8.50, "descripcion": "Carne, lechuga, tomate, queso", "categoria": "Hamburguesas", "disponible": True},
            {"id": 2, "nombre": "Pizza Margarita", "precio": 12.00, "descripcion": "Salsa de tomate, mozzarella, albahaca", "categoria": "Pizzas", "disponible": True},
            {"id": 3, "nombre": "Coca Cola", "precio": 2.50, "descripcion": "Bebida gaseosa 500ml", "categoria": "Bebidas", "disponible": True}
        ]
        self.ordenes = []
        self.registros = []
        
        # Usuario actual
        self.usuario_actual = None
        self.rol_actual = None
    
    def login(self):
        """Sistema de login por selección de rol"""
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN - COMIDAS RÁPIDAS")
        print("="*50)
        print("\nSelecciona tu rol:")
        print("1. Jefe")
        print("2. Mesero")
        print("3. Cocinero")
        print("4. Salir")
        
        while True:
            try:
                opcion = input("\nIngresa tu opción (1-4): ").strip()
                
                if opcion == "1":
                    self.rol_actual = "Jefe"
                    self.usuario_actual = "Jefe"
                    print(f"\n¡Bienvenido, {self.rol_actual}!")
                    self.registrar_entrada()
                    self.menu_jefe()
                    break
                elif opcion == "2":
                    self.rol_actual = "Mesero"
                    self.usuario_actual = "Mesero"
                    print(f"\n¡Bienvenido, {self.rol_actual}!")
                    self.registrar_entrada()
                    self.menu_mesero()
                    break
                elif opcion == "3":
                    self.rol_actual = "Cocinero"
                    self.usuario_actual = "Cocinero"
                    print(f"\n¡Bienvenido, {self.rol_actual}!")
                    self.registrar_entrada()
                    self.menu_cocinero()
                    break
                elif opcion == "4":
                    print("\n¡Hasta luego!")
                    return False
                else:
                    print("Opción inválida. Por favor, selecciona 1, 2, 3 o 4.")
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                return False
        
        return True
    
    def registrar_entrada(self):
        """Registra la hora de entrada del usuario"""
        registro = {
            "usuario": self.usuario_actual,
            "rol": self.rol_actual,
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "hora_entrada": datetime.now().strftime("%H:%M:%S"),
            "hora_salida": None
        }
        self.registros.append(registro)
    
    def registrar_salida(self):
        """Registra la hora de salida del usuario"""
        for registro in reversed(self.registros):
            if (registro["usuario"] == self.usuario_actual and 
                registro["hora_salida"] is None):
                registro["hora_salida"] = datetime.now().strftime("%H:%M:%S")
                print(f"Salida registrada: {registro['hora_salida']}")
                break
    
    # ==================== GESTIÓN DE COMIDAS ====================
    
    def agregar_comida(self):
        """Agrega una nueva comida al menú"""
        print("\n" + "-"*30)
        print("AGREGAR NUEVA COMIDA")
        print("-"*30)
        
        nombre = input("Nombre de la comida: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        
        try:
            precio = float(input("Precio: $"))
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
                return
        except ValueError:
            print("Precio inválido.")
            return
        
        descripcion = input("Descripción (opcional): ").strip()
        categoria = input("Categoría: ").strip()
        
        comida = {
            "id": self.generar_id_comida(),
            "nombre": nombre,
            "precio": precio,
            "descripcion": descripcion,
            "categoria": categoria,
            "disponible": True
        }
        
        self.comidas.append(comida)
        print(f"\n✅ Comida '{nombre}' agregada exitosamente.")
    
    def generar_id_comida(self) -> int:
        """Genera un ID único para una comida"""
        if not self.comidas:
            return 1
        return max(comida["id"] for comida in self.comidas) + 1
    
    def ver_comidas(self):
        """Muestra todas las comidas disponibles"""
        if not self.comidas:
            print("\nNo hay comidas registradas.")
            return
        
        print("\n" + "="*80)
        print("MENÚ DE COMIDAS")
        print("="*80)
        print(f"{'ID':<5} {'Nombre':<25} {'Precio':<10} {'Categoría':<15} {'Estado':<10}")
        print("-"*80)
        
        for comida in self.comidas:
            estado = "✅" if comida["disponible"] else "❌"
            print(f"{comida['id']:<5} {comida['nombre']:<25} ${comida['precio']:<9} {comida['categoria']:<15} {estado:<10}")
        
        print("="*80)
    
    def modificar_comida(self):
        """Modifica una comida existente"""
        self.ver_comidas()
        
        try:
            id_comida = int(input("\nIngresa el ID de la comida a modificar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        comida = next((c for c in self.comidas if c["id"] == id_comida), None)
        
        if not comida:
            print("Comida no encontrada.")
            return
        
        print(f"\nModificando: {comida['nombre']}")
        print("(Presiona Enter para mantener el valor actual)")
        
        nombre = input(f"Nuevo nombre [{comida['nombre']}]: ").strip()
        if nombre:
            comida['nombre'] = nombre
        
        precio_str = input(f"Nuevo precio [${comida['precio']}]: ").strip()
        if precio_str:
            try:
                precio = float(precio_str)
                if precio > 0:
                    comida['precio'] = precio
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Precio inválido.")
        
        descripcion = input(f"Nueva descripción [{comida['descripcion']}]: ").strip()
        if descripcion:
            comida['descripcion'] = descripcion
        
        categoria = input(f"Nueva categoría [{comida['categoria']}]: ").strip()
        if categoria:
            comida['categoria'] = categoria
        
        disponible = input(f"¿Disponible? (s/n) [{'s' if comida['disponible'] else 'n'}]: ").strip().lower()
        if disponible in ['s', 'n']:
            comida['disponible'] = disponible == 's'
        
        print(f"\n✅ Comida '{comida['nombre']}' modificada exitosamente.")
    
    def eliminar_comida(self):
        """Elimina una comida del menú"""
        self.ver_comidas()
        
        try:
            id_comida = int(input("\nIngresa el ID de la comida a eliminar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        comida = next((c for c in self.comidas if c["id"] == id_comida), None)
        
        if not comida:
            print("Comida no encontrada.")
            return
        
        confirmacion = input(f"\n¿Estás seguro de eliminar '{comida['nombre']}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.comidas.remove(comida)
            print(f"\n✅ Comida '{comida['nombre']}' eliminada exitosamente.")
        else:
            print("Operación cancelada.")
    
    # ==================== GESTIÓN DE ÓRDENES ====================
    
    def agregar_orden(self):
        """Agrega una nueva orden"""
        print("\n" + "-"*30)
        print("NUEVA ORDEN")
        print("-"*30)
        
        # Mostrar comidas disponibles
        comidas_disponibles = [c for c in self.comidas if c["disponible"]]
        
        if not comidas_disponibles:
            print("No hay comidas disponibles para ordenar.")
            return
        
        print("\nComidas disponibles:")
        for comida in comidas_disponibles:
            print(f"{comida['id']}. {comida['nombre']} - ${comida['precio']}")
        
        # Recopilar items de la orden
        items = []
        total = 0
        
        while True:
            try:
                id_comida = input("\nIngresa el ID de la comida (o 'fin' para terminar): ").strip()
                
                if id_comida.lower() == 'fin':
                    break
                
                id_comida = int(id_comida)
                comida = next((c for c in comidas_disponibles if c["id"] == id_comida), None)
                
                if not comida:
                    print("ID de comida no válido.")
                    continue
                
                cantidad = int(input(f"Cantidad de '{comida['nombre']}': "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue
                
                subtotal = comida['precio'] * cantidad
                items.append({
                    "id_comida": comida['id'],
                    "nombre": comida['nombre'],
                    "precio_unitario": comida['precio'],
                    "cantidad": cantidad,
                    "subtotal": subtotal
                })
                
                total += subtotal
                print(f"Agregado: {cantidad}x {comida['nombre']} - ${subtotal}")
                
            except ValueError:
                print("Valor inválido.")
                continue
        
        if not items:
            print("La orden debe tener al menos un item.")
            return
        
        # Información adicional de la orden
        cliente = input("Nombre del cliente: ").strip()
        mesa = input("Número de mesa (opcional): ").strip()
        notas = input("Notas especiales (opcional): ").strip()
        
        orden = {
            "id": self.generar_id_orden(),
            "cliente": cliente,
            "mesa": mesa,
            "items": items,
            "total": total,
            "notas": notas,
            "estado": "Pendiente",
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mesero": self.usuario_actual
        }
        
        self.ordenes.append(orden)
        print(f"\n✅ Orden #{orden['id']} creada exitosamente.")
        print(f"Total: ${total:.2f}")
    
    def generar_id_orden(self) -> int:
        """Genera un ID único para una orden"""
        if not self.ordenes:
            return 1
        return max(orden["id"] for orden in self.ordenes) + 1
    
    def ver_ordenes(self):
        """Muestra todas las órdenes"""
        if not self.ordenes:
            print("\nNo hay órdenes registradas.")
            return
        
        print("\n" + "="*100)
        print("ÓRDENES")
        print("="*100)
        
        for orden in self.ordenes:
            print(f"\nOrden #{orden['id']} - {orden['fecha']}")
            print(f"Cliente: {orden['cliente']} | Mesa: {orden['mesa']} | Estado: {orden['estado']}")
            print(f"Mesero: {orden['mesero']}")
            if orden['notas']:
                print(f"Notas: {orden['notas']}")
            
            print("Items:")
            for item in orden['items']:
                print(f"  • {item['cantidad']}x {item['nombre']} - ${item['subtotal']:.2f}")
            
            print(f"Total: ${orden['total']:.2f}")
            print("-" * 50)
    
    def modificar_orden(self):
        """Modifica una orden existente"""
        self.ver_ordenes()
        
        try:
            id_orden = int(input("\nIngresa el ID de la orden a modificar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        orden = next((o for o in self.ordenes if o["id"] == id_orden), None)
        
        if not orden:
            print("Orden no encontrada.")
            return
        
        print(f"\nModificando Orden #{orden['id']}")
        print("1. Cambiar estado")
        print("2. Agregar notas")
        print("3. Cancelar")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            print("\nEstados disponibles:")
            print("1. Pendiente")
            print("2. En preparación")
            print("3. Lista")
            print("4. Entregada")
            print("5. Cancelada")
            
            try:
                estado_opcion = int(input("Nuevo estado (1-5): "))
                estados = ["Pendiente", "En preparación", "Lista", "Entregada", "Cancelada"]
                if 1 <= estado_opcion <= 5:
                    orden['estado'] = estados[estado_opcion - 1]
                    print(f"✅ Estado cambiado a: {orden['estado']}")
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Opción inválida.")
        
        elif opcion == "2":
            notas = input("Nuevas notas: ").strip()
            if notas:
                orden['notas'] = notas
                print("✅ Notas actualizadas.")
    
    def eliminar_orden(self):
        """Elimina una orden"""
        self.ver_ordenes()
        
        try:
            id_orden = int(input("\nIngresa el ID de la orden a eliminar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        orden = next((o for o in self.ordenes if o["id"] == id_orden), None)
        
        if not orden:
            print("Orden no encontrada.")
            return
        
        confirmacion = input(f"\n¿Estás seguro de eliminar la Orden #{orden['id']}? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.ordenes.remove(orden)
            print(f"\n✅ Orden #{orden['id']} eliminada exitosamente.")
        else:
            print("Operación cancelada.")
    
    # ==================== MENÚS POR ROL ====================
    
    def menu_jefe(self):
        """Menú principal para el Jefe"""
        while True:
            print("\n" + "="*50)
            print("MENÚ JEFE")
            print("="*50)
            print("1. Gestión de Comidas")
            print("2. Gestión de Órdenes")
            print("3. Ver Registros")
            print("4. Cerrar Sesión")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.submenu_comidas()
            elif opcion == "2":
                self.submenu_ordenes()
            elif opcion == "3":
                self.ver_registros()
            elif opcion == "4":
                self.registrar_salida()
                break
            else:
                print("Opción inválida.")
    
    def menu_mesero(self):
        """Menú principal para el Mesero"""
        while True:
            print("\n" + "="*50)
            print("MENÚ MESERO")
            print("="*50)
            print("1. Ver Comidas")
            print("2. Gestión de Órdenes")
            print("3. Ver Registros")
            print("4. Cerrar Sesión")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.ver_comidas()
            elif opcion == "2":
                self.submenu_ordenes()
            elif opcion == "3":
                self.ver_registros()
            elif opcion == "4":
                self.registrar_salida()
                break
            else:
                print("Opción inválida.")
    
    def menu_cocinero(self):
        """Menú principal para el Cocinero"""
        while True:
            print("\n" + "="*50)
            print("MENÚ COCINERO")
            print("="*50)
            print("1. Ver Comidas")
            print("2. Ver Órdenes")
            print("3. Ver Registros")
            print("4. Cerrar Sesión")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.ver_comidas()
            elif opcion == "2":
                self.ver_ordenes()
            elif opcion == "3":
                self.ver_registros()
            elif opcion == "4":
                self.registrar_salida()
                break
            else:
                print("Opción inválida.")
    
    def submenu_comidas(self):
        """Submenú para gestión de comidas"""
        while True:
            print("\n" + "-"*30)
            print("GESTIÓN DE COMIDAS")
            print("-"*30)
            print("1. Agregar comida")
            print("2. Ver comidas")
            print("3. Modificar comida")
            print("4. Eliminar comida")
            print("5. Volver")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.agregar_comida()
            elif opcion == "2":
                self.ver_comidas()
            elif opcion == "3":
                self.modificar_comida()
            elif opcion == "4":
                self.eliminar_comida()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
    
    def submenu_ordenes(self):
        """Submenú para gestión de órdenes"""
        while True:
            print("\n" + "-"*30)
            print("GESTIÓN DE ÓRDENES")
            print("-"*30)
            print("1. Agregar orden")
            print("2. Ver órdenes")
            print("3. Modificar orden")
            print("4. Eliminar orden")
            print("5. Volver")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.agregar_orden()
            elif opcion == "2":
                self.ver_ordenes()
            elif opcion == "3":
                self.modificar_orden()
            elif opcion == "4":
                self.eliminar_orden()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
    
    def ver_registros(self):
        """Muestra los registros de entrada y salida"""
        if not self.registros:
            print("\nNo hay registros de entrada/salida.")
            return
        
        print("\n" + "="*80)
        print("REGISTROS DE ENTRADA Y SALIDA")
        print("="*80)
        print(f"{'Usuario':<15} {'Rol':<12} {'Fecha':<12} {'Entrada':<10} {'Salida':<10}")
        print("-"*80)
        
        for registro in self.registros:
            salida = registro['hora_salida'] if registro['hora_salida'] else "En sesión"
            print(f"{registro['usuario']:<15} {registro['rol']:<12} {registro['fecha']:<12} {registro['hora_entrada']:<10} {salida:<10}")
        
        print("="*80)

def main():
    """Función principal del programa"""
    sistema = SistemaComidasRapidas()
    
    print("¡Bienvenido al Sistema de Gestión de Comidas Rápidas!")
    print("El sistema ya tiene 3 comidas de ejemplo cargadas.")
    
    while True:
        if not sistema.login():
            break

if __name__ == "__main__":
    main()
