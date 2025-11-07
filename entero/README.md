# Northwind Management System

Sistema de gestión de base de datos Northwind desarrollado con Python y Tkinter, implementando el patrón arquitectónico MVC (Model-View-Controller).

## 📋 Descripción

Este proyecto es una aplicación de escritorio que permite gestionar la base de datos Northwind a través de una interfaz gráfica intuitiva. El sistema incluye funcionalidades CRUD (Create, Read, Update, Delete) para todas las entidades principales de la base de datos.

## 🏗️ Arquitectura

El proyecto está estructurado siguiendo el patrón MVC:

```
db-tarea/
├── app.py                 # Punto de entrada principal
├── northwind.py          # Versión monolítica (legacy)
├── mvc/                  # Estructura MVC
│   ├── controllers/      # Controladores
│   ├── models/          # Modelos de datos
│   ├── views/           # Vistas (interfaz)
│   ├── db/             # Conexión a base de datos
│   └── utils/          # Utilidades
└── README.md
```

## 🚀 Características

- **Interfaz de pestañas**: Organización clara por entidades
- **Operaciones CRUD**: Crear, leer, actualizar y eliminar registros
- **Validación de datos**: Validación en tiempo real de entrada
- **Conexión a MySQL**: Integración con base de datos Northwind
- **Arquitectura MVC**: Código bien estructurado y mantenible

## 📊 Entidades Gestionadas

1. **Products** - Gestión de productos
2. **Customers** - Gestión de clientes
3. **Employees** - Gestión de empleados
4. **Categories** - Gestión de categorías
5. **Suppliers** - Gestión de proveedores
6. **Shippers** - Gestión de transportistas
7. **Orders** - Gestión de pedidos
8. **OrderDetails** - Detalles de pedidos

## 🛠️ Requisitos del Sistema

- Python 3.7+
- MySQL Server
- Base de datos Northwind

## 📦 Dependencias

```
tkinter
mysql-connector-python
tkcalendar
```

## 🔧 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Dorak00oo/northwind.git
   cd northwind
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar base de datos:**
   - Asegúrate de tener MySQL Server ejecutándose
   - Crea la base de datos 'northwind'
   - Modifica la configuración en `mvc/db/connection.py` si es necesario

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

## ⚙️ Configuración de Base de Datos

El archivo de configuración se encuentra en `mvc/db/connection.py`:

```python
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'northwind'
}
```

## 🎯 Uso

1. **Ejecutar la aplicación**: `python app.py`
2. **Probar conexión**: Usar el botón "Probar Conexión DB"
3. **Navegar por pestañas**: Cada pestaña corresponde a una entidad
4. **Operaciones CRUD**: Usar los botones Guardar, Actualizar, Eliminar, Limpiar
5. **Visualizar datos**: Usar "Mostrar Todos" para ver todos los registros

## 📁 Estructura del Proyecto

### Controllers
- `product_controller.py` - Lógica de negocio para productos
- `customer_controller.py` - Lógica de negocio para clientes
- `employee_controller.py` - Lógica de negocio para empleados
- `category_controller.py` - Lógica de negocio para categorías
- `supplier_controller.py` - Lógica de negocio para proveedores
- `shipper_controller.py` - Lógica de negocio para transportistas
- `order_controller.py` - Lógica de negocio para pedidos
- `orderdetail_controller.py` - Lógica de negocio para detalles de pedidos

### Views
- `product_view.py` - Interfaz de usuario para productos
- `customer_view.py` - Interfaz de usuario para clientes
- `employee_view.py` - Interfaz de usuario para empleados
- `category_view.py` - Interfaz de usuario para categorías
- `supplier_view.py` - Interfaz de usuario para proveedores
- `shipper_view.py` - Interfaz de usuario para transportistas
- `order_view.py` - Interfaz de usuario para pedidos
- `orderdetail_view.py` - Interfaz de usuario para detalles de pedidos

### Models
- `product.py` - Modelo de datos para productos

### Database
- `connection.py` - Configuración y conexión a la base de datos

### Utils
- `validation.py` - Funciones de validación

## 🐛 Solución de Problemas

### Error de Conexión a Base de Datos
1. Verificar que MySQL Server esté ejecutándose
2. Verificar credenciales en `mvc/db/connection.py`
3. Verificar que la base de datos 'northwind' existe
4. Verificar permisos de usuario

### Dependencias Faltantes
```bash
pip install mysql-connector-python
pip install tkcalendar
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Dorak00oo**
- GitHub: [@Dorak00oo](https://github.com/Dorak00oo)

## 📞 Soporte

Si tienes preguntas o necesitas ayuda, por favor abre un issue en el repositorio.

---

**Nota**: Este proyecto es parte de un curso de programación orientada a objetos con GUI en Python.
