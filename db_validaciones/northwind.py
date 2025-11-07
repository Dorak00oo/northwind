import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from mysql.connector import Error

# CONFIGURACIÓN DE BASE DE DATOS 
DATABASE_CONFIG = {
    'host': 'localhost',      
    'user': 'root',           
    'password': '',           
    'database': 'northwind'   
}


# FUNCIONES DE VALIDACIÓN
def validate_int_input(P):
    """Valida que solo se ingresen números enteros"""
    if P == "" or P == "-":
        return True
    try:
        int(P)
        return True
    except ValueError:
        return False

def validate_float_input(P):
    """Valida que solo se ingresen números decimales"""
    if P == "" or P == "-" or P == ".":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False


# CLASE DE CONEXIÓN A BASE DE DATOS
class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = ""
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return True
        except Error as e:
            messagebox.showerror("Error de Conexión", f"Error al conectar con la base de datos: {e}")
            return False
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        try:
            if self.connection is None or not self.connection.is_connected():
                if not self.connect():
                    return False
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al ejecutar consulta: {e}")
            return False
    
    def fetch_all(self, query, params=None):
        try:
            if self.connection is None or not self.connection.is_connected():
                if not self.connect():
                    return []
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al obtener datos: {e}")
            return []


# Conexión usando la configuración importada
db = DatabaseConnection(**DATABASE_CONFIG)


# FUNCIONES CRUD PARA PRODUCTS
def save_product():
    """Guarda un nuevo producto en la base de datos"""
    try:
        if not ProductID.get() or not ProductName.get():
            messagebox.showwarning("Advertencia", "ProductID y ProductName son campos obligatorios")
            return
        
        query = "INSERT INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            int(ProductID.get()) if ProductID.get() else None,
            ProductName.get(),
            int(SupplierID.get()) if SupplierID.get() else None,
            int(CategoryID.get()) if CategoryID.get() else None,
            Unit.get(),
            float(Price.get()) if Price.get() else None
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Producto guardado correctamente")
            clear_product_form()
            show_all_products()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar producto: {e}")

def update_product():
    """Actualiza un producto existente"""
    try:
        if not ProductID.get():
            messagebox.showwarning("Advertencia", "ProductID es obligatorio para actualizar")
            return
        
        query = "UPDATE products SET ProductName=%s, SupplierID=%s, CategoryID=%s, Unit=%s, Price=%s WHERE ProductID=%s"
        params = (
            ProductName.get(),
            int(SupplierID.get()) if SupplierID.get() else None,
            int(CategoryID.get()) if CategoryID.get() else None,
            Unit.get(),
            float(Price.get()) if Price.get() else None,
            int(ProductID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Producto actualizado correctamente")
            clear_product_form()
            show_all_products()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar producto: {e}")

def delete_product():
    """Elimina un producto de la base de datos"""
    try:
        if not ProductID.get():
            messagebox.showwarning("Advertencia", "ProductID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este producto?"):
            query = "DELETE FROM products WHERE ProductID = %s"
            params = (int(ProductID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Producto eliminado correctamente")
                clear_product_form()
                show_all_products()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar producto: {e}")

def clear_product_form():
    """Limpia todos los campos del formulario de productos"""
    ProductID.delete(0, tk.END)
    ProductName.delete(0, tk.END)
    SupplierID.delete(0, tk.END)
    CategoryID.delete(0, tk.END)
    Unit.delete(0, tk.END)
    Price.delete(0, tk.END)

def show_all_products():
    """Muestra todos los productos en el TreeView"""
    try:
        # Limpiar TreeView existente
        for item in tree_products.get_children():
            tree_products.delete(item)
        
        query = "SELECT ProductID, ProductName, SupplierID, CategoryID, Unit, Price FROM products"
        products = db.fetch_all(query)
        
        for product in products:
            tree_products.insert('', 'end', values=product)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar productos: {e}")


# FUNCIONES CRUD PARA CUSTOMERS
def save_customer():
    """Guarda un nuevo cliente en la base de datos"""
    try:
        if not CustomerID.get() or not CustomerName.get():
            messagebox.showwarning("Advertencia", "CustomerID y CustomerName son campos obligatorios")
            return
        
        query = "INSERT INTO customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (
            int(CustomerID.get()) if CustomerID.get() else None,
            CustomerName.get(),
            ContactName.get(),
            Address.get(),
            City.get(),
            PostalCode.get(),
            Country.get()
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Cliente guardado correctamente")
            clear_customer_form()
            show_all_customers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar cliente: {e}")

def update_customer():
    """Actualiza un cliente existente"""
    try:
        if not CustomerID.get():
            messagebox.showwarning("Advertencia", "CustomerID es obligatorio para actualizar")
            return
        
        query = "UPDATE customers SET CustomerName=%s, ContactName=%s, Address=%s, City=%s, PostalCode=%s, Country=%s WHERE CustomerID=%s"
        params = (
            CustomerName.get(),
            ContactName.get(),
            Address.get(),
            City.get(),
            PostalCode.get(),
            Country.get(),
            int(CustomerID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Cliente actualizado correctamente")
            clear_customer_form()
            show_all_customers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar cliente: {e}")

def delete_customer():
    """Elimina un cliente de la base de datos"""
    try:
        if not CustomerID.get():
            messagebox.showwarning("Advertencia", "CustomerID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este cliente?"):
            query = "DELETE FROM customers WHERE CustomerID = %s"
            params = (int(CustomerID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Cliente eliminado correctamente")
                clear_customer_form()
                show_all_customers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar cliente: {e}")

def clear_customer_form():
    """Limpia todos los campos del formulario de clientes"""
    CustomerID.delete(0, tk.END)
    CustomerName.delete(0, tk.END)
    ContactName.delete(0, tk.END)
    Address.delete(0, tk.END)
    City.delete(0, tk.END)
    PostalCode.delete(0, tk.END)
    Country.delete(0, tk.END)

def show_all_customers():
    """Muestra todos los clientes en el TreeView"""
    try:
        # Limpiar TreeView existente
        for item in tree_customers.get_children():
            tree_customers.delete(item)
        
        query = "SELECT CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country FROM customers"
        customers = db.fetch_all(query)
        
        for customer in customers:
            tree_customers.insert('', 'end', values=customer)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar clientes: {e}")


# FUNCIONES CRUD PARA EMPLOYEES
def save_employee():
    try:
        if not EmployeeID.get() or not LastName.get() or not FirstName.get():
            messagebox.showwarning("Advertencia", "EmployeeID, LastName y FirstName son campos obligatorios")
            return
        
        query = "INSERT INTO employees (EmployeeID, LastName, FirstName, BirthDate, Photo, Notes) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            int(EmployeeID.get()) if EmployeeID.get() else None,
            LastName.get(),
            FirstName.get(),
            BirthDate.get_date() if BirthDate.get_date() else None,
            "", 
            Notes.get("1.0", tk.END).strip()
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Empleado guardado correctamente")
            clear_employee_form()
            show_all_employees()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar empleado: {e}")

def update_employee():
    try:
        if not EmployeeID.get():
            messagebox.showwarning("Advertencia", "EmployeeID es obligatorio para actualizar")
            return
        
        query = "UPDATE employees SET LastName=%s, FirstName=%s, BirthDate=%s, Photo=%s, Notes=%s WHERE EmployeeID=%s"
        params = (
            LastName.get(),
            FirstName.get(),
            BirthDate.get_date() if BirthDate.get_date() else None,
            "", 
            Notes.get("1.0", tk.END).strip(),
            int(EmployeeID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Empleado actualizado correctamente")
            clear_employee_form()
            show_all_employees()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar empleado: {e}")

def delete_employee():
    try:
        if not EmployeeID.get():
            messagebox.showwarning("Advertencia", "EmployeeID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este empleado?"):
            query = "DELETE FROM employees WHERE EmployeeID = %s"
            params = (int(EmployeeID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Empleado eliminado correctamente")
                clear_employee_form()
                show_all_employees()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar empleado: {e}")

def clear_employee_form():
    EmployeeID.delete(0, tk.END)
    LastName.delete(0, tk.END)
    FirstName.delete(0, tk.END)
    Notes.delete("1.0", tk.END)

def show_all_employees():
    try:
        for item in tree_employees.get_children():
            tree_employees.delete(item)
        
        query = "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM employees"
        employees = db.fetch_all(query)
        
        for employee in employees:
            tree_employees.insert('', 'end', values=employee)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar empleados: {e}")


# FUNCIONES CRUD PARA CATEGORIES
def save_category():
    try:
        if not CategoryID.get() or not CategoryName.get():
            messagebox.showwarning("Advertencia", "CategoryID y CategoryName son campos obligatorios")
            return
        
        query = "INSERT INTO categories (CategoryID, CategoryName, Description) VALUES (%s, %s, %s)"
        params = (
            int(CategoryID.get()) if CategoryID.get() else None,
            CategoryName.get(),
            Description.get("1.0", tk.END).strip()
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Categoría guardada correctamente")
            clear_category_form()
            show_all_categories()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar categoría: {e}")

def update_category():
    try:
        if not CategoryID.get():
            messagebox.showwarning("Advertencia", "CategoryID es obligatorio para actualizar")
            return
        
        query = "UPDATE categories SET CategoryName=%s, Description=%s WHERE CategoryID=%s"
        params = (
            CategoryName.get(),
            Description.get("1.0", tk.END).strip(),
            int(CategoryID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Categoría actualizada correctamente")
            clear_category_form()
            show_all_categories()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar categoría: {e}")

def delete_category():
    try:
        if not CategoryID.get():
            messagebox.showwarning("Advertencia", "CategoryID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar esta categoría?"):
            query = "DELETE FROM categories WHERE CategoryID = %s"
            params = (int(CategoryID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Categoría eliminada correctamente")
                clear_category_form()
                show_all_categories()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar categoría: {e}")

def clear_category_form():
    CategoryID.delete(0, tk.END)
    CategoryName.delete(0, tk.END)
    Description.delete("1.0", tk.END)

def show_all_categories():
    try:
        for item in tree_categories.get_children():
            tree_categories.delete(item)
        
        query = "SELECT CategoryID, CategoryName, Description FROM categories"
        categories = db.fetch_all(query)
        
        for category in categories:
            tree_categories.insert('', 'end', values=category)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar categorías: {e}")


# FUNCIONES CRUD PARA SUPPLIERS
def save_supplier():
    try:
        if not SupplierID.get() or not SupplierName.get():
            messagebox.showwarning("Advertencia", "SupplierID y SupplierName son campos obligatorios")
            return
        
        query = "INSERT INTO suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (
            int(SupplierID.get()) if SupplierID.get() else None,
            SupplierName.get(),
            SupplierContactName.get(),
            SupplierAddress.get(),
            SupplierCity.get(),
            SupplierPostalCode.get(),
            SupplierCountry.get(),
            SupplierPhone.get()
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Proveedor guardado correctamente")
            clear_supplier_form()
            show_all_suppliers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar proveedor: {e}")

def update_supplier():
    try:
        if not SupplierID.get():
            messagebox.showwarning("Advertencia", "SupplierID es obligatorio para actualizar")
            return
        
        query = "UPDATE suppliers SET SupplierName=%s, ContactName=%s, Address=%s, City=%s, PostalCode=%s, Country=%s, Phone=%s WHERE SupplierID=%s"
        params = (
            SupplierName.get(),
            SupplierContactName.get(),
            SupplierAddress.get(),
            SupplierCity.get(),
            SupplierPostalCode.get(),
            SupplierCountry.get(),
            SupplierPhone.get(),
            int(SupplierID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Proveedor actualizado correctamente")
            clear_supplier_form()
            show_all_suppliers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar proveedor: {e}")

def delete_supplier():
    try:
        if not SupplierID.get():
            messagebox.showwarning("Advertencia", "SupplierID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este proveedor?"):
            query = "DELETE FROM suppliers WHERE SupplierID = %s"
            params = (int(SupplierID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Proveedor eliminado correctamente")
                clear_supplier_form()
                show_all_suppliers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar proveedor: {e}")

def clear_supplier_form():
    SupplierID.delete(0, tk.END)
    SupplierName.delete(0, tk.END)
    SupplierContactName.delete(0, tk.END)
    SupplierAddress.delete(0, tk.END)
    SupplierCity.delete(0, tk.END)
    SupplierPostalCode.delete(0, tk.END)
    SupplierCountry.delete(0, tk.END)
    SupplierPhone.delete(0, tk.END)

def show_all_suppliers():
    try:
        for item in tree_suppliers.get_children():
            tree_suppliers.delete(item)
        
        query = "SELECT SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone FROM suppliers"
        suppliers = db.fetch_all(query)
        
        for supplier in suppliers:
            tree_suppliers.insert('', 'end', values=supplier)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar proveedores: {e}")


# FUNCIONES CRUD PARA SHIPPERS
def save_shipper():
    try:
        if not ShipperID.get() or not ShipperName.get():
            messagebox.showwarning("Advertencia", "ShipperID y ShipperName son campos obligatorios")
            return
        
        query = "INSERT INTO shippers (ShipperID, ShipperName, Phone) VALUES (%s, %s, %s)"
        params = (
            int(ShipperID.get()) if ShipperID.get() else None,
            ShipperName.get(),
            ShipperPhone.get()
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Transportista guardado correctamente")
            clear_shipper_form()
            show_all_shippers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar transportista: {e}")

def update_shipper():
    try:
        if not ShipperID.get():
            messagebox.showwarning("Advertencia", "ShipperID es obligatorio para actualizar")
            return
        
        query = "UPDATE shippers SET ShipperName=%s, Phone=%s WHERE ShipperID=%s"
        params = (
            ShipperName.get(),
            ShipperPhone.get(),
            int(ShipperID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Transportista actualizado correctamente")
            clear_shipper_form()
            show_all_shippers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar transportista: {e}")

def delete_shipper():
    try:
        if not ShipperID.get():
            messagebox.showwarning("Advertencia", "ShipperID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este transportista?"):
            query = "DELETE FROM shippers WHERE ShipperID = %s"
            params = (int(ShipperID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Transportista eliminado correctamente")
                clear_shipper_form()
                show_all_shippers()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar transportista: {e}")

def clear_shipper_form():
    ShipperID.delete(0, tk.END)
    ShipperName.delete(0, tk.END)
    ShipperPhone.delete(0, tk.END)

def show_all_shippers():
    try:
        for item in tree_shippers.get_children():
            tree_shippers.delete(item)
        
        query = "SELECT ShipperID, ShipperName, Phone FROM shippers"
        shippers = db.fetch_all(query)
        
        for shipper in shippers:
            tree_shippers.insert('', 'end', values=shipper)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar transportistas: {e}")


# FUNCIONES CRUD PARA ORDERS
def save_order():
    try:
        if not OrderID.get():
            messagebox.showwarning("Advertencia", "OrderID es obligatorio")
            return
        
        query = "INSERT INTO orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s, %s)"
        params = (
            int(OrderID.get()) if OrderID.get() else None,
            int(OrderCustomerID.get()) if OrderCustomerID.get() else None,
            int(OrderEmployeeID.get()) if OrderEmployeeID.get() else None,
            OrderDate.get_date() if OrderDate.get_date() else None,
            int(OrderShipperID.get()) if OrderShipperID.get() else None
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Pedido guardado correctamente")
            clear_order_form()
            show_all_orders()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar pedido: {e}")

def update_order():
    try:
        if not OrderID.get():
            messagebox.showwarning("Advertencia", "OrderID es obligatorio para actualizar")
            return
        
        query = "UPDATE orders SET CustomerID=%s, EmployeeID=%s, OrderDate=%s, ShipperID=%s WHERE OrderID=%s"
        params = (
            int(OrderCustomerID.get()) if OrderCustomerID.get() else None,
            int(OrderEmployeeID.get()) if OrderEmployeeID.get() else None,
            OrderDate.get_date() if OrderDate.get_date() else None,
            int(OrderShipperID.get()) if OrderShipperID.get() else None,
            int(OrderID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Pedido actualizado correctamente")
            clear_order_form()
            show_all_orders()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar pedido: {e}")

def delete_order():
    try:
        if not OrderID.get():
            messagebox.showwarning("Advertencia", "OrderID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este pedido?"):
            query = "DELETE FROM orders WHERE OrderID = %s"
            params = (int(OrderID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Pedido eliminado correctamente")
                clear_order_form()
                show_all_orders()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar pedido: {e}")

def clear_order_form():
    OrderID.delete(0, tk.END)
    OrderCustomerID.delete(0, tk.END)
    OrderEmployeeID.delete(0, tk.END)
    OrderShipperID.delete(0, tk.END)

def show_all_orders():
    try:
        for item in tree_orders.get_children():
            tree_orders.delete(item)
        
        query = "SELECT OrderID, CustomerID, EmployeeID, OrderDate, ShipperID FROM orders"
        orders = db.fetch_all(query)
        
        for order in orders:
            tree_orders.insert('', 'end', values=order)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar pedidos: {e}")


# FUNCIONES CRUD PARA ORDERDETAILS
def save_orderdetail():
    try:
        if not OrderDetailID.get():
            messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio")
            return
        
        query = "INSERT INTO orderdetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)"
        params = (
            int(OrderDetailID.get()) if OrderDetailID.get() else None,
            int(OrderDetailOrderID.get()) if OrderDetailOrderID.get() else None,
            int(OrderDetailProductID.get()) if OrderDetailProductID.get() else None,
            int(Quantity.get()) if Quantity.get() else None
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Guardar", "Detalle de pedido guardado correctamente")
            clear_orderdetail_form()
            show_all_orderdetails()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar detalle de pedido: {e}")

def update_orderdetail():
    try:
        if not OrderDetailID.get():
            messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio para actualizar")
            return
        
        query = "UPDATE orderdetails SET OrderID=%s, ProductID=%s, Quantity=%s WHERE OrderDetailID=%s"
        params = (
            int(OrderDetailOrderID.get()) if OrderDetailOrderID.get() else None,
            int(OrderDetailProductID.get()) if OrderDetailProductID.get() else None,
            int(Quantity.get()) if Quantity.get() else None,
            int(OrderDetailID.get())
        )
        
        if db.execute_query(query, params):
            messagebox.showinfo("Actualizar", "Detalle de pedido actualizado correctamente")
            clear_orderdetail_form()
            show_all_orderdetails()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar detalle de pedido: {e}")

def delete_orderdetail():
    try:
        if not OrderDetailID.get():
            messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio para eliminar")
            return
        
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este detalle de pedido?"):
            query = "DELETE FROM orderdetails WHERE OrderDetailID = %s"
            params = (int(OrderDetailID.get()),)
            
            if db.execute_query(query, params):
                messagebox.showinfo("Eliminar", "Detalle de pedido eliminado correctamente")
                clear_orderdetail_form()
                show_all_orderdetails()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar detalle de pedido: {e}")

def clear_orderdetail_form():
    OrderDetailID.delete(0, tk.END)
    OrderDetailOrderID.delete(0, tk.END)
    OrderDetailProductID.delete(0, tk.END)
    Quantity.delete(0, tk.END)

def show_all_orderdetails():
    try:
        for item in tree_orderdetails.get_children():
            tree_orderdetails.delete(item)
        
        query = "SELECT OrderDetailID, OrderID, ProductID, Quantity FROM orderdetails"
        orderdetails = db.fetch_all(query)
        
        for orderdetail in orderdetails:
            tree_orderdetails.insert('', 'end', values=orderdetail)
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar detalles de pedido: {e}")



# FUNCIÓN PARA PROBAR LA CONEXIÓN
def test_connection():
    """Prueba la conexión a la base de datos"""
    try:
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


# Crear la ventana principal
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

# CONTENIDO DE LA PESTAÑA 1 (PRODUCTS)
# Título
titulo = tk.Label(tab1,
                  text="FORMULARIO DE PRODUCTS",
                  font=("Arial", 16, "bold"),
                  fg="blue")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: ProductID
tk.Label(form_frame, text="ProductID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ProductID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
ProductID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ProductName
tk.Label(form_frame, text="ProductName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: SupplierID
tk.Label(form_frame, text="SupplierID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: CategoryID
tk.Label(form_frame, text="CategoryID:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
CategoryID.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Unit
tk.Label(form_frame, text="Unit:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Unit = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Unit.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Price
tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_float_input), "%P"))
Price.grid(row=6, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_product)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_product)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_product)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_product_form)
btn_clear.pack(side=tk.LEFT, padx=5)

btn_show_all = tk.Button(button_frame, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_products)
btn_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar productos
tree_frame = tk.Frame(tab1)
tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Crear TreeView con scrollbar
tree_products = ttk.Treeview(tree_frame, columns=("ProductID", "ProductName", "SupplierID", "CategoryID", "Unit", "Price"), show="headings", height=10)

# Configurar columnas
tree_products.heading("ProductID", text="ID")
tree_products.heading("ProductName", text="Nombre")
tree_products.heading("SupplierID", text="Proveedor ID")
tree_products.heading("CategoryID", text="Categoría ID")
tree_products.heading("Unit", text="Unidad")
tree_products.heading("Price", text="Precio")

# Configurar ancho de columnas
tree_products.column("ProductID", width=60)
tree_products.column("ProductName", width=200)
tree_products.column("SupplierID", width=100)
tree_products.column("CategoryID", width=100)
tree_products.column("Unit", width=100)
tree_products.column("Price", width=100)

# Scrollbar para TreeView
scrollbar_products = ttk.Scrollbar(tree_frame, orient="vertical", command=tree_products.yview)
tree_products.configure(yscrollcommand=scrollbar_products.set)

# Empaquetar TreeView y scrollbar
tree_products.pack(side="left", fill="both", expand=True)
scrollbar_products.pack(side="right", fill="y")

# CONTENIDO DE LA PESTAÑA 2 (CUSTOMERS)
titulo2 = tk.Label(tab2, text="GESTIÓN DE CUSTOMERS", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: CustomerID
tk.Label(form_frame, text="CustomerID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CustomerName
tk.Label(form_frame, text="CustomerName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ContactName
tk.Label(form_frame, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Address
tk.Label(form_frame, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Address = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Address.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: City
tk.Label(form_frame, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
City = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
City.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: PostalCode
tk.Label(form_frame, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
PostalCode = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PostalCode.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Country
tk.Label(form_frame, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Country = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Country.grid(row=7, column=1, sticky="w", pady=10)

# Frame para botones de Customers
button_frame2 = tk.Frame(tab2)
button_frame2.pack(pady=20)

# Botones de acción para Customers
btn_cust_save = tk.Button(button_frame2, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_customer)
btn_cust_save.pack(side=tk.LEFT, padx=5)

btn_cust_update = tk.Button(button_frame2, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_customer)
btn_cust_update.pack(side=tk.LEFT, padx=5)

btn_cust_delete = tk.Button(button_frame2, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_customer)
btn_cust_delete.pack(side=tk.LEFT, padx=5)

btn_cust_clear = tk.Button(button_frame2, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_customer_form)
btn_cust_clear.pack(side=tk.LEFT, padx=5)

btn_cust_show_all = tk.Button(button_frame2, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_customers)
btn_cust_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar clientes
tree_frame2 = tk.Frame(tab2)
tree_frame2.pack(fill="both", expand=True, padx=20, pady=10)

# Crear TreeView con scrollbar
tree_customers = ttk.Treeview(tree_frame2, columns=("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country"), show="headings", height=10)

# Configurar columnas
tree_customers.heading("CustomerID", text="ID")
tree_customers.heading("CustomerName", text="Nombre Cliente")
tree_customers.heading("ContactName", text="Contacto")
tree_customers.heading("Address", text="Dirección")
tree_customers.heading("City", text="Ciudad")
tree_customers.heading("PostalCode", text="Código Postal")
tree_customers.heading("Country", text="País")

# Configurar ancho de columnas
tree_customers.column("CustomerID", width=60)
tree_customers.column("CustomerName", width=150)
tree_customers.column("ContactName", width=120)
tree_customers.column("Address", width=150)
tree_customers.column("City", width=100)
tree_customers.column("PostalCode", width=100)
tree_customers.column("Country", width=100)

# Scrollbar para TreeView
scrollbar_customers = ttk.Scrollbar(tree_frame2, orient="vertical", command=tree_customers.yview)
tree_customers.configure(yscrollcommand=scrollbar_customers.set)

# Empaquetar TreeView y scrollbar
tree_customers.pack(side="left", fill="both", expand=True)
scrollbar_customers.pack(side="right", fill="y")



# PESTAÑA 3 (EMPLOYEES)

# Título
titulo3 = tk.Label(tab3,
                  text="GESTIÓN DE EMPLOYEES",
                  font=("Arial", 16, "bold"),
                  fg="purple")
titulo3.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab3)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: EmployeeID
tk.Label(form_frame, text="EmployeeID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
EmployeeID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: LastName
tk.Label(form_frame, text="LastName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
LastName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
LastName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: FirstName
tk.Label(form_frame, text="FirstName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
FirstName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
FirstName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: BirthDate
tk.Label(form_frame, text="BirthDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
BirthDate = DateEntry(form_frame, width=25, font=("Arial", 12), date_pattern="yyyy-mm-dd", background="darkblue", foreground="white", borderwidth=2)
BirthDate.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Notes
tk.Label(form_frame, text="Notes:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Notes = tk.Text(form_frame, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
Notes.grid(row=5, column=1, sticky="w", pady=10)

# Frame para botones
button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

# Botones de acción
btn_emp_save = tk.Button(button_frame3, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_employee)
btn_emp_save.pack(side=tk.LEFT, padx=5)

btn_emp_update = tk.Button(button_frame3, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_employee)
btn_emp_update.pack(side=tk.LEFT, padx=5)

btn_emp_delete = tk.Button(button_frame3, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_employee)
btn_emp_delete.pack(side=tk.LEFT, padx=5)

btn_emp_clear = tk.Button(button_frame3, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_employee_form)
btn_emp_clear.pack(side=tk.LEFT, padx=5)

btn_emp_show_all = tk.Button(button_frame3, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_employees)
btn_emp_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar empleados
tree_frame3 = tk.Frame(tab3)
tree_frame3.pack(fill="both", expand=True, padx=20, pady=10)

tree_employees = ttk.Treeview(tree_frame3, columns=("EmployeeID", "LastName", "FirstName", "BirthDate", "Photo", "Notes"), show="headings", height=8)
tree_employees.heading("EmployeeID", text="ID")
tree_employees.heading("LastName", text="Apellido")
tree_employees.heading("FirstName", text="Nombre")
tree_employees.heading("BirthDate", text="Fecha Nacimiento")
tree_employees.heading("Photo", text="Foto")
tree_employees.heading("Notes", text="Notas")

tree_employees.column("EmployeeID", width=60)
tree_employees.column("LastName", width=120)
tree_employees.column("FirstName", width=120)
tree_employees.column("BirthDate", width=120)
tree_employees.column("Photo", width=100)
tree_employees.column("Notes", width=200)

scrollbar_employees = ttk.Scrollbar(tree_frame3, orient="vertical", command=tree_employees.yview)
tree_employees.configure(yscrollcommand=scrollbar_employees.set)
tree_employees.pack(side="left", fill="both", expand=True)
scrollbar_employees.pack(side="right", fill="y")

# PESTAÑA 4 (CATEGORIES)
titulo4 = tk.Label(tab4, text="GESTIÓN DE CATEGORIES", font=("Arial", 16, "bold"), fg="orange")
titulo4.pack(pady=20)

form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)

# Fila 1: CategoryID
tk.Label(form_frame4, text="CategoryID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
CategoryID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CategoryName
tk.Label(form_frame4, text="CategoryName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryName = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
CategoryName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Description
tk.Label(form_frame4, text="Description:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Description = tk.Text(form_frame4, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
Description.grid(row=3, column=1, sticky="w", pady=10)

# Frame para botones de Categories
button_frame4 = tk.Frame(tab4)
button_frame4.pack(pady=20)

# Botones de acción para Categories
btn_cat_save = tk.Button(button_frame4, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_category)
btn_cat_save.pack(side=tk.LEFT, padx=5)

btn_cat_update = tk.Button(button_frame4, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_category)
btn_cat_update.pack(side=tk.LEFT, padx=5)

btn_cat_delete = tk.Button(button_frame4, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_category)
btn_cat_delete.pack(side=tk.LEFT, padx=5)

btn_cat_clear = tk.Button(button_frame4, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_category_form)
btn_cat_clear.pack(side=tk.LEFT, padx=5)

btn_cat_show_all = tk.Button(button_frame4, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_categories)
btn_cat_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar categorías
tree_frame4 = tk.Frame(tab4)
tree_frame4.pack(fill="both", expand=True, padx=20, pady=10)

tree_categories = ttk.Treeview(tree_frame4, columns=("CategoryID", "CategoryName", "Description"), show="headings", height=8)
tree_categories.heading("CategoryID", text="ID")
tree_categories.heading("CategoryName", text="Nombre")
tree_categories.heading("Description", text="Descripción")

tree_categories.column("CategoryID", width=60)
tree_categories.column("CategoryName", width=200)
tree_categories.column("Description", width=400)

scrollbar_categories = ttk.Scrollbar(tree_frame4, orient="vertical", command=tree_categories.yview)
tree_categories.configure(yscrollcommand=scrollbar_categories.set)
tree_categories.pack(side="left", fill="both", expand=True)
scrollbar_categories.pack(side="right", fill="y")

# PESTAÑA 5 (SUPPLIERS)
titulo5 = tk.Label(tab5, text="GESTIÓN DE SUPPLIERS", font=("Arial", 16, "bold"), fg="brown")
titulo5.pack(pady=20)

form_frame5 = tk.Frame(tab5)
form_frame5.pack(pady=20, anchor="w", padx=50)

# Fila 1: SupplierID
tk.Label(form_frame5, text="SupplierID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
SupplierID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: SupplierName
tk.Label(form_frame5, text="SupplierName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierName = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ContactName
tk.Label(form_frame5, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierContactName = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierContactName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Address
tk.Label(form_frame5, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierAddress = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierAddress.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: City
tk.Label(form_frame5, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierCity = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierCity.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: PostalCode
tk.Label(form_frame5, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierPostalCode = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierPostalCode.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Country
tk.Label(form_frame5, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierCountry = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierCountry.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Phone
tk.Label(form_frame5, text="Phone:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierPhone = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierPhone.grid(row=8, column=1, sticky="w", pady=10)

# Frame para botones de Suppliers
button_frame5 = tk.Frame(tab5)
button_frame5.pack(pady=20)

# Botones de acción para Suppliers
btn_sup_save = tk.Button(button_frame5, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_supplier)
btn_sup_save.pack(side=tk.LEFT, padx=5)

btn_sup_update = tk.Button(button_frame5, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_supplier)
btn_sup_update.pack(side=tk.LEFT, padx=5)

btn_sup_delete = tk.Button(button_frame5, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_supplier)
btn_sup_delete.pack(side=tk.LEFT, padx=5)

btn_sup_clear = tk.Button(button_frame5, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_supplier_form)
btn_sup_clear.pack(side=tk.LEFT, padx=5)

btn_sup_show_all = tk.Button(button_frame5, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_suppliers)
btn_sup_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar proveedores
tree_frame5 = tk.Frame(tab5)
tree_frame5.pack(fill="both", expand=True, padx=20, pady=10)

tree_suppliers = ttk.Treeview(tree_frame5, columns=("SupplierID", "SupplierName", "ContactName", "Address", "City", "PostalCode", "Country", "Phone"), show="headings", height=8)
tree_suppliers.heading("SupplierID", text="ID")
tree_suppliers.heading("SupplierName", text="Nombre")
tree_suppliers.heading("ContactName", text="Contacto")
tree_suppliers.heading("Address", text="Dirección")
tree_suppliers.heading("City", text="Ciudad")
tree_suppliers.heading("PostalCode", text="Código Postal")
tree_suppliers.heading("Country", text="País")
tree_suppliers.heading("Phone", text="Teléfono")

tree_suppliers.column("SupplierID", width=60)
tree_suppliers.column("SupplierName", width=150)
tree_suppliers.column("ContactName", width=120)
tree_suppliers.column("Address", width=150)
tree_suppliers.column("City", width=100)
tree_suppliers.column("PostalCode", width=100)
tree_suppliers.column("Country", width=100)
tree_suppliers.column("Phone", width=100)

scrollbar_suppliers = ttk.Scrollbar(tree_frame5, orient="vertical", command=tree_suppliers.yview)
tree_suppliers.configure(yscrollcommand=scrollbar_suppliers.set)
tree_suppliers.pack(side="left", fill="both", expand=True)
scrollbar_suppliers.pack(side="right", fill="y")

# PESTAÑA 6 (SHIPPERS)
titulo6 = tk.Label(tab6, text="GESTIÓN DE SHIPPERS", font=("Arial", 16, "bold"), fg="teal")
titulo6.pack(pady=20)

form_frame6 = tk.Frame(tab6)
form_frame6.pack(pady=20, anchor="w", padx=50)

# Fila 1: ShipperID
tk.Label(form_frame6, text="ShipperID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperID = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
ShipperID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ShipperName
tk.Label(form_frame6, text="ShipperName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperName = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
ShipperName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Phone
tk.Label(form_frame6, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperPhone = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
ShipperPhone.grid(row=3, column=1, sticky="w", pady=10)

# Frame para botones de Shippers
button_frame6 = tk.Frame(tab6)
button_frame6.pack(pady=20)

# Botones de acción para Shippers
btn_shi_save = tk.Button(button_frame6, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_shipper)
btn_shi_save.pack(side=tk.LEFT, padx=5)

btn_shi_update = tk.Button(button_frame6, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_shipper)
btn_shi_update.pack(side=tk.LEFT, padx=5)

btn_shi_delete = tk.Button(button_frame6, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_shipper)
btn_shi_delete.pack(side=tk.LEFT, padx=5)

btn_shi_clear = tk.Button(button_frame6, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_shipper_form)
btn_shi_clear.pack(side=tk.LEFT, padx=5)

btn_shi_show_all = tk.Button(button_frame6, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_shippers)
btn_shi_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar transportistas
tree_frame6 = tk.Frame(tab6)
tree_frame6.pack(fill="both", expand=True, padx=20, pady=10)

tree_shippers = ttk.Treeview(tree_frame6, columns=("ShipperID", "ShipperName", "Phone"), show="headings", height=8)
tree_shippers.heading("ShipperID", text="ID")
tree_shippers.heading("ShipperName", text="Nombre")
tree_shippers.heading("Phone", text="Teléfono")

tree_shippers.column("ShipperID", width=60)
tree_shippers.column("ShipperName", width=300)
tree_shippers.column("Phone", width=200)

scrollbar_shippers = ttk.Scrollbar(tree_frame6, orient="vertical", command=tree_shippers.yview)
tree_shippers.configure(yscrollcommand=scrollbar_shippers.set)
tree_shippers.pack(side="left", fill="both", expand=True)
scrollbar_shippers.pack(side="right", fill="y")

# PESTAÑA 7 (ORDERS)
titulo7 = tk.Label(tab7, text="GESTIÓN DE ORDERS", font=("Arial", 16, "bold"), fg="navy")
titulo7.pack(pady=20)

form_frame7 = tk.Frame(tab7)
form_frame7.pack(pady=20, anchor="w", padx=50)

# Fila 1: OrderID
tk.Label(form_frame7, text="OrderID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
OrderID = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CustomerID
tk.Label(form_frame7, text="CustomerID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
OrderCustomerID = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderCustomerID.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: EmployeeID
tk.Label(form_frame7, text="EmployeeID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
OrderEmployeeID = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderEmployeeID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: OrderDate
tk.Label(form_frame7, text="OrderDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDate = DateEntry(form_frame7, width=25, font=("Arial", 12), date_pattern="yyyy-mm-dd", background="darkblue", foreground="white", borderwidth=2)
OrderDate.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: ShipperID
tk.Label(form_frame7, text="ShipperID:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
OrderShipperID = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderShipperID.grid(row=5, column=1, sticky="w", pady=10)

# Frame para botones de Orders
button_frame7 = tk.Frame(tab7)
button_frame7.pack(pady=20)

# Botones de acción para Orders
btn_ord_save = tk.Button(button_frame7, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_order)
btn_ord_save.pack(side=tk.LEFT, padx=5)

btn_ord_update = tk.Button(button_frame7, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_order)
btn_ord_update.pack(side=tk.LEFT, padx=5)

btn_ord_delete = tk.Button(button_frame7, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_order)
btn_ord_delete.pack(side=tk.LEFT, padx=5)

btn_ord_clear = tk.Button(button_frame7, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_order_form)
btn_ord_clear.pack(side=tk.LEFT, padx=5)

btn_ord_show_all = tk.Button(button_frame7, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_orders)
btn_ord_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar pedidos
tree_frame7 = tk.Frame(tab7)
tree_frame7.pack(fill="both", expand=True, padx=20, pady=10)

tree_orders = ttk.Treeview(tree_frame7, columns=("OrderID", "CustomerID", "EmployeeID", "OrderDate", "ShipperID"), show="headings", height=8)
tree_orders.heading("OrderID", text="ID Pedido")
tree_orders.heading("CustomerID", text="ID Cliente")
tree_orders.heading("EmployeeID", text="ID Empleado")
tree_orders.heading("OrderDate", text="Fecha Pedido")
tree_orders.heading("ShipperID", text="ID Transportista")

tree_orders.column("OrderID", width=100)
tree_orders.column("CustomerID", width=100)
tree_orders.column("EmployeeID", width=100)
tree_orders.column("OrderDate", width=150)
tree_orders.column("ShipperID", width=100)

scrollbar_orders = ttk.Scrollbar(tree_frame7, orient="vertical", command=tree_orders.yview)
tree_orders.configure(yscrollcommand=scrollbar_orders.set)
tree_orders.pack(side="left", fill="both", expand=True)
scrollbar_orders.pack(side="right", fill="y")

# PESTAÑA 8 (ORDERDETAILS)
titulo8 = tk.Label(tab8, text="GESTIÓN DE ORDERDETAILS", font=("Arial", 16, "bold"), fg="maroon")
titulo8.pack(pady=20)

form_frame8 = tk.Frame(tab8)
form_frame8.pack(pady=20, anchor="w", padx=50)

# Fila 1: OrderDetailID
tk.Label(form_frame8, text="OrderDetailID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailID = tk.Entry(form_frame8, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderDetailID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: OrderID
tk.Label(form_frame8, text="OrderID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailOrderID = tk.Entry(form_frame8, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderDetailOrderID.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ProductID
tk.Label(form_frame8, text="ProductID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailProductID = tk.Entry(form_frame8, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
OrderDetailProductID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Quantity
tk.Label(form_frame8, text="Quantity:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Quantity = tk.Entry(form_frame8, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(root.register(validate_int_input), "%P"))
Quantity.grid(row=4, column=1, sticky="w", pady=10)

# Frame para botones de OrderDetails
button_frame8 = tk.Frame(tab8)
button_frame8.pack(pady=20)

# Botones de acción para OrderDetails
btn_od_save = tk.Button(button_frame8, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_orderdetail)
btn_od_save.pack(side=tk.LEFT, padx=5)

btn_od_update = tk.Button(button_frame8, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_orderdetail)
btn_od_update.pack(side=tk.LEFT, padx=5)

btn_od_delete = tk.Button(button_frame8, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_orderdetail)
btn_od_delete.pack(side=tk.LEFT, padx=5)

btn_od_clear = tk.Button(button_frame8, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_orderdetail_form)
btn_od_clear.pack(side=tk.LEFT, padx=5)

btn_od_show_all = tk.Button(button_frame8, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_orderdetails)
btn_od_show_all.pack(side=tk.LEFT, padx=5)

# TreeView para mostrar detalles de pedidos
tree_frame8 = tk.Frame(tab8)
tree_frame8.pack(fill="both", expand=True, padx=20, pady=10)

tree_orderdetails = ttk.Treeview(tree_frame8, columns=("OrderDetailID", "OrderID", "ProductID", "Quantity"), show="headings", height=8)
tree_orderdetails.heading("OrderDetailID", text="ID Detalle")
tree_orderdetails.heading("OrderID", text="ID Pedido")
tree_orderdetails.heading("ProductID", text="ID Producto")
tree_orderdetails.heading("Quantity", text="Cantidad")

tree_orderdetails.column("OrderDetailID", width=100)
tree_orderdetails.column("OrderID", width=100)
tree_orderdetails.column("ProductID", width=100)
tree_orderdetails.column("Quantity", width=100)

scrollbar_orderdetails = ttk.Scrollbar(tree_frame8, orient="vertical", command=tree_orderdetails.yview)
tree_orderdetails.configure(yscrollcommand=scrollbar_orderdetails.set)
tree_orderdetails.pack(side="left", fill="both", expand=True)
scrollbar_orderdetails.pack(side="right", fill="y")

# Iniciar el bucle principal de la aplicación
root.mainloop()