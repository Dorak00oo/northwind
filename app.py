import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.controllers.product_controller import ProductController
from mvc.controllers.customer_controller import CustomerController
from mvc.controllers.employee_controller import EmployeeController
from mvc.controllers.category_controller import CategoryController
from mvc.controllers.supplier_controller import SupplierController
from mvc.controllers.shipper_controller import ShipperController
from mvc.controllers.order_controller import OrderController
from mvc.controllers.orderdetail_controller import OrderDetailController

from mvc.views.product_view import ProductView
from mvc.views.customer_view import CustomerView
from mvc.views.employee_view import EmployeeView
from mvc.views.category_view import CategoryView
from mvc.views.supplier_view import SupplierView
from mvc.views.shipper_view import ShipperView
from mvc.views.order_view import OrderView
from mvc.views.orderdetail_view import OrderDetailView


# FUNCIÓN PARA PROBAR LA CONEXIÓN
def test_connection():
    """Prueba la conexión a la base de datos"""
    try:
        db = DatabaseConnection()
        if db.connect():
            messagebox.showinfo("Conexión", "Conexión exitosa a la base de datos Northwind")
        else:
            messagebox.showerror("Error de Conexión", 
                               "No se pudo conectar a la base de datos.\n\n"
                               "Verifique:\n"
                               "1. MySQL Server está ejecutándose\n"
                               "2. Usuario y contraseña son correctos\n"
                               "3. La base de datos 'northwind' existe\n"
                               "4. La configuración en el código es correcta")
    except Exception as e:
        messagebox.showerror("Error de Conexión", f"Error inesperado: {e}")


def main():
    root = tk.Tk()
    root.geometry('1200x700')
    root.title("Northwind Management System")

    # Crear el widget Notebook (pestañas)
    notebook = ttk.Notebook(root)

    # Crear los frames que irán dentro de las pestañas
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    tab4 = ttk.Frame(notebook)
    tab5 = ttk.Frame(notebook)
    tab6 = ttk.Frame(notebook)
    tab7 = ttk.Frame(notebook)
    tab8 = ttk.Frame(notebook)

    # Añadir las pestañas al Notebook
    notebook.add(tab1, text="Products")
    notebook.add(tab2, text="Customers")
    notebook.add(tab3, text="Employees")
    notebook.add(tab4, text="Categories")
    notebook.add(tab5, text="Suppliers")
    notebook.add(tab6, text="Shippers")
    notebook.add(tab7, text="Orders")
    notebook.add(tab8, text="OrderDetails")

    # Empaquetar el Notebook para que se muestre en la ventana
    notebook.pack(expand=True, fill="both")

    # Botón de prueba de conexión
    connection_frame = tk.Frame(root)
    connection_frame.pack(pady=10)

    btn_test_connection = tk.Button(connection_frame, text="Probar Conexión DB", font=("Arial", 10), bg="#607D8B", fg="white", width=15, command=test_connection)
    btn_test_connection.pack(side=tk.LEFT, padx=5)

    # Crear instancias de controladores y vistas para cada pestaña
    db = DatabaseConnection()
    
    # Products
    product_controller = ProductController(db)
    product_view = ProductView(root, tab1, product_controller)
    
    # Customers
    customer_controller = CustomerController(db)
    customer_view = CustomerView(root, tab2, customer_controller)
    
    # Employees
    employee_controller = EmployeeController(db)
    employee_view = EmployeeView(root, tab3, employee_controller)
    
    # Categories
    category_controller = CategoryController(db)
    category_view = CategoryView(root, tab4, category_controller)
    
    # Suppliers
    supplier_controller = SupplierController(db)
    supplier_view = SupplierView(root, tab5, supplier_controller)
    
    # Shippers
    shipper_controller = ShipperController(db)
    shipper_view = ShipperView(root, tab6, shipper_controller)
    
    # Orders
    order_controller = OrderController(db)
    order_view = OrderView(root, tab7, order_controller)
    
    # OrderDetails
    orderdetail_controller = OrderDetailController(db)
    orderdetail_view = OrderDetailView(root, tab8, orderdetail_controller)

    root.mainloop()


if __name__ == "__main__":
    main()