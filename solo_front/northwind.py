from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from tkcalendar import DateEntry


# Datos de demostración


DEMO_MESSAGE = "Esta acción solo está disponible en el backend."


SAMPLE_PRODUCTS = [
    (1, "Chai", 1, 1, "10 boxes", 18.0),
    (2, "Chang", 1, 1, "24 - 12 oz bottles", 19.0),
]

SAMPLE_CUSTOMERS = [
    (1, "Alfreds Futterkiste", "Maria Anders", "Obere Str. 57", "Berlin", "12209", "Germany"),
    (2, "Ana Trujillo Emparedados", "Ana Trujillo", "Avda. de la Constitución 2222", "México D.F.", "05021", "Mexico"),
]

SAMPLE_EMPLOYEES = [
    (1, "Davolio", "Nancy", "1968-12-08", "", "Inside sales coordinator"),
    (2, "Fuller", "Andrew", "1952-02-19", "", "Vice President"),
]

SAMPLE_CATEGORIES = [
    (1, "Beverages", "Soft drinks, coffees, teas"),
    (2, "Condiments", "Sweet and savory sauces"),
]

SAMPLE_SUPPLIERS = [
    (1, "Exotic Liquids", "Charlotte Cooper", "49 Gilbert St.", "London", "EC1 4SD", "UK", "(171) 555-2222"),
    (2, "New Orleans Cajun Delights", "Shelley Burke", "P.O. Box 78934", "New Orleans", "70117", "USA", "(100) 555-4822"),
]

SAMPLE_SHIPPERS = [
    (1, "Speedy Express", "(503) 555-9831"),
    (2, "United Package", "(503) 555-3199"),
]

SAMPLE_ORDERS = [
    (10248, 1, 5, "1996-07-04", 3),
    (10249, 2, 6, "1996-07-05", 1),
]

SAMPLE_ORDERDETAILS = [
    (10248, 10248, 11, 12),
    (10249, 10249, 42, 10),
]



# Acciones de demostración (sin conexión a base de datos)


def save_product():
    messagebox.showinfo("Solo Front", f"Guardar producto\n\n{DEMO_MESSAGE}")


def update_product():
    messagebox.showinfo("Solo Front", f"Actualizar producto\n\n{DEMO_MESSAGE}")


def delete_product():
    messagebox.showinfo("Solo Front", f"Eliminar producto\n\n{DEMO_MESSAGE}")


def show_all_products():
    tree_products.delete(*tree_products.get_children())
    for row in SAMPLE_PRODUCTS:
        tree_products.insert("", "end", values=row)


def save_customer():
    messagebox.showinfo("Solo Front", f"Guardar cliente\n\n{DEMO_MESSAGE}")


def update_customer():
    messagebox.showinfo("Solo Front", f"Actualizar cliente\n\n{DEMO_MESSAGE}")


def delete_customer():
    messagebox.showinfo("Solo Front", f"Eliminar cliente\n\n{DEMO_MESSAGE}")


def show_all_customers():
    tree_customers.delete(*tree_customers.get_children())
    for row in SAMPLE_CUSTOMERS:
        tree_customers.insert("", "end", values=row)


def save_employee():
    messagebox.showinfo("Solo Front", f"Guardar empleado\n\n{DEMO_MESSAGE}")


def update_employee():
    messagebox.showinfo("Solo Front", f"Actualizar empleado\n\n{DEMO_MESSAGE}")


def delete_employee():
    messagebox.showinfo("Solo Front", f"Eliminar empleado\n\n{DEMO_MESSAGE}")


def show_all_employees():
    tree_employees.delete(*tree_employees.get_children())
    for row in SAMPLE_EMPLOYEES:
        tree_employees.insert("", "end", values=row)


def save_category():
    messagebox.showinfo("Solo Front", f"Guardar categoría\n\n{DEMO_MESSAGE}")


def update_category():
    messagebox.showinfo("Solo Front", f"Actualizar categoría\n\n{DEMO_MESSAGE}")


def delete_category():
    messagebox.showinfo("Solo Front", f"Eliminar categoría\n\n{DEMO_MESSAGE}")


def show_all_categories():
    tree_categories.delete(*tree_categories.get_children())
    for row in SAMPLE_CATEGORIES:
        tree_categories.insert("", "end", values=row)


def save_supplier():
    messagebox.showinfo("Solo Front", f"Guardar proveedor\n\n{DEMO_MESSAGE}")


def update_supplier():
    messagebox.showinfo("Solo Front", f"Actualizar proveedor\n\n{DEMO_MESSAGE}")


def delete_supplier():
    messagebox.showinfo("Solo Front", f"Eliminar proveedor\n\n{DEMO_MESSAGE}")


def show_all_suppliers():
    tree_suppliers.delete(*tree_suppliers.get_children())
    for row in SAMPLE_SUPPLIERS:
        tree_suppliers.insert("", "end", values=row)


def save_shipper():
    messagebox.showinfo("Solo Front", f"Guardar transportista\n\n{DEMO_MESSAGE}")


def update_shipper():
    messagebox.showinfo("Solo Front", f"Actualizar transportista\n\n{DEMO_MESSAGE}")


def delete_shipper():
    messagebox.showinfo("Solo Front", f"Eliminar transportista\n\n{DEMO_MESSAGE}")


def show_all_shippers():
    tree_shippers.delete(*tree_shippers.get_children())
    for row in SAMPLE_SHIPPERS:
        tree_shippers.insert("", "end", values=row)


def save_order():
    messagebox.showinfo("Solo Front", f"Guardar pedido\n\n{DEMO_MESSAGE}")


def update_order():
    messagebox.showinfo("Solo Front", f"Actualizar pedido\n\n{DEMO_MESSAGE}")


def delete_order():
    messagebox.showinfo("Solo Front", f"Eliminar pedido\n\n{DEMO_MESSAGE}")


def show_all_orders():
    tree_orders.delete(*tree_orders.get_children())
    for row in SAMPLE_ORDERS:
        tree_orders.insert("", "end", values=row)


def save_orderdetail():
    messagebox.showinfo("Solo Front", f"Guardar detalle de pedido\n\n{DEMO_MESSAGE}")


def update_orderdetail():
    messagebox.showinfo("Solo Front", f"Actualizar detalle de pedido\n\n{DEMO_MESSAGE}")


def delete_orderdetail():
    messagebox.showinfo("Solo Front", f"Eliminar detalle de pedido\n\n{DEMO_MESSAGE}")


def show_all_orderdetails():
    tree_orderdetails.delete(*tree_orderdetails.get_children())
    for row in SAMPLE_ORDERDETAILS:
        tree_orderdetails.insert("", "end", values=row)


def test_connection():
    messagebox.showinfo(
        "Solo Front",
        "Esta es la versión de demostración sin conexión real a la base de datos.",
    )



# Funciones utilitarias de limpieza


def clear_product_form():
    ProductID.delete(0, tk.END)
    ProductName.delete(0, tk.END)
    SupplierID.delete(0, tk.END)
    CategoryID.delete(0, tk.END)
    Unit.delete(0, tk.END)
    Price.delete(0, tk.END)


def clear_customer_form():
    CustomerID.delete(0, tk.END)
    CustomerName.delete(0, tk.END)
    ContactName.delete(0, tk.END)
    Address.delete(0, tk.END)
    City.delete(0, tk.END)
    PostalCode.delete(0, tk.END)
    Country.delete(0, tk.END)


def clear_employee_form():
    EmployeeID.delete(0, tk.END)
    LastName.delete(0, tk.END)
    FirstName.delete(0, tk.END)
    Notes.delete("1.0", tk.END)


def clear_category_form():
    CategoryID.delete(0, tk.END)
    CategoryName.delete(0, tk.END)
    Description.delete("1.0", tk.END)


def clear_supplier_form():
    SupplierID.delete(0, tk.END)
    SupplierName.delete(0, tk.END)
    SupplierContactName.delete(0, tk.END)
    SupplierAddress.delete(0, tk.END)
    SupplierCity.delete(0, tk.END)
    SupplierPostalCode.delete(0, tk.END)
    SupplierCountry.delete(0, tk.END)
    SupplierPhone.delete(0, tk.END)


def clear_shipper_form():
    ShipperID.delete(0, tk.END)
    ShipperName.delete(0, tk.END)
    ShipperPhone.delete(0, tk.END)


def clear_order_form():
    OrderID.delete(0, tk.END)
    OrderCustomerID.delete(0, tk.END)
    OrderEmployeeID.delete(0, tk.END)
    OrderShipperID.delete(0, tk.END)


def clear_orderdetail_form():
    OrderDetailID.delete(0, tk.END)
    OrderDetailOrderID.delete(0, tk.END)
    OrderDetailProductID.delete(0, tk.END)
    Quantity.delete(0, tk.END)


# Construcción de la interfaz (idéntica al archivo original)

root = tk.Tk()
root.geometry("1200x700")
root.title("Northwind Management System (Front-End Demo)")

notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)
tab8 = ttk.Frame(notebook)

notebook.add(tab1, text="Products")
notebook.add(tab2, text="Customers")
notebook.add(tab3, text="Employees")
notebook.add(tab4, text="Categories")
notebook.add(tab5, text="Suppliers")
notebook.add(tab6, text="Shippers")
notebook.add(tab7, text="Orders")
notebook.add(tab8, text="OrderDetails")

notebook.pack(expand=True, fill="both")

connection_frame = tk.Frame(root)
connection_frame.pack(pady=10)

btn_test_connection = tk.Button(
    connection_frame,
    text="Probar Conexión DB",
    font=("Arial", 10),
    bg="#607D8B",
    fg="white",
    width=15,
    command=test_connection,
)
btn_test_connection.pack(side=tk.LEFT, padx=5)


# ----------------------------- Tab 1: Products -----------------------------

titulo = tk.Label(tab1, text="FORMULARIO DE PRODUCTS", font=("Arial", 16, "bold"), fg="blue")
titulo.pack(pady=20)

form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

ProductID = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
tk.Label(form_frame, text="ProductID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ProductID.grid(row=1, column=1, sticky="w", pady=10)

ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
tk.Label(form_frame, text="ProductName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

SupplierID = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
tk.Label(form_frame, text="SupplierID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

CategoryID = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
tk.Label(form_frame, text="CategoryID:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID.grid(row=4, column=1, sticky="w", pady=10)

Unit = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
tk.Label(form_frame, text="Unit:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Unit.grid(row=5, column=1, sticky="w", pady=10)

Price = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price.grid(row=6, column=1, sticky="w", pady=10)

button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_product).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_product).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_product).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_product_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_products).pack(side=tk.LEFT, padx=5)

tree_frame = tk.Frame(tab1)
tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

tree_products = ttk.Treeview(
    tree_frame,
    columns=("ProductID", "ProductName", "SupplierID", "CategoryID", "Unit", "Price"),
    show="headings",
    height=10,
)
tree_products.heading("ProductID", text="ID")
tree_products.heading("ProductName", text="Nombre")
tree_products.heading("SupplierID", text="Proveedor ID")
tree_products.heading("CategoryID", text="Categoría ID")
tree_products.heading("Unit", text="Unidad")
tree_products.heading("Price", text="Precio")
tree_products.column("ProductID", width=60)
tree_products.column("ProductName", width=200)
tree_products.column("SupplierID", width=100)
tree_products.column("CategoryID", width=100)
tree_products.column("Unit", width=100)
tree_products.column("Price", width=100)

scrollbar_products = ttk.Scrollbar(tree_frame, orient="vertical", command=tree_products.yview)
tree_products.configure(yscrollcommand=scrollbar_products.set)
tree_products.pack(side="left", fill="both", expand=True)
scrollbar_products.pack(side="right", fill="y")


# ---------------------------- Tab 2: Customers -----------------------------

titulo2 = tk.Label(tab2, text="GESTIÓN DE CUSTOMERS", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame, text="CustomerID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="CustomerName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Address = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Address.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
City = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
City.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
PostalCode = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PostalCode.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Country = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Country.grid(row=7, column=1, sticky="w", pady=10)

button_frame2 = tk.Frame(tab2)
button_frame2.pack(pady=20)

tk.Button(button_frame2, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_customer).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_customer).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_customer).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_customer_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_customers).pack(side=tk.LEFT, padx=5)

tree_frame2 = tk.Frame(tab2)
tree_frame2.pack(fill="both", expand=True, padx=20, pady=10)

tree_customers = ttk.Treeview(
    tree_frame2,
    columns=("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country"),
    show="headings",
    height=10,
)
for column, title in [
    ("CustomerID", "ID"),
    ("CustomerName", "Nombre Cliente"),
    ("ContactName", "Contacto"),
    ("Address", "Dirección"),
    ("City", "Ciudad"),
    ("PostalCode", "Código Postal"),
    ("Country", "País"),
]:
    tree_customers.heading(column, text=title)

tree_customers.column("CustomerID", width=60)
tree_customers.column("CustomerName", width=150)
tree_customers.column("ContactName", width=120)
tree_customers.column("Address", width=150)
tree_customers.column("City", width=100)
tree_customers.column("PostalCode", width=100)
tree_customers.column("Country", width=100)

scrollbar_customers = ttk.Scrollbar(tree_frame2, orient="vertical", command=tree_customers.yview)
tree_customers.configure(yscrollcommand=scrollbar_customers.set)
tree_customers.pack(side="left", fill="both", expand=True)
scrollbar_customers.pack(side="right", fill="y")


# ----------------------------- Tab 3: Employees ----------------------------

titulo3 = tk.Label(tab3, text="GESTIÓN DE EMPLOYEES", font=("Arial", 16, "bold"), fg="purple")
titulo3.pack(pady=20)

form_frame = tk.Frame(tab3)
form_frame.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame, text="EmployeeID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeID = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
EmployeeID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="LastName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
LastName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
LastName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="FirstName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
FirstName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
FirstName.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="BirthDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
BirthDate = DateEntry(form_frame, width=25, font=("Arial", 12), date_pattern="yyyy-mm-dd", background="darkblue", foreground="white", borderwidth=2)
BirthDate.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="Notes:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Notes = tk.Text(form_frame, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
Notes.grid(row=5, column=1, sticky="w", pady=10)

button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

tk.Button(button_frame3, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_employee).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_employee).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_employee).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_employee_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_employees).pack(side=tk.LEFT, padx=5)

tree_frame3 = tk.Frame(tab3)
tree_frame3.pack(fill="both", expand=True, padx=20, pady=10)

tree_employees = ttk.Treeview(
    tree_frame3,
    columns=("EmployeeID", "LastName", "FirstName", "BirthDate", "Photo", "Notes"),
    show="headings",
    height=8,
)
for column, title in [
    ("EmployeeID", "ID"),
    ("LastName", "Apellido"),
    ("FirstName", "Nombre"),
    ("BirthDate", "Fecha Nacimiento"),
    ("Photo", "Foto"),
    ("Notes", "Notas"),
]:
    tree_employees.heading(column, text=title)

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


# ----------------------------- Tab 4: Categories ---------------------------

titulo4 = tk.Label(tab4, text="GESTIÓN DE CATEGORIES", font=("Arial", 16, "bold"), fg="orange")
titulo4.pack(pady=20)

form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame4, text="CategoryID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(
    form_frame4,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
CategoryID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text="CategoryName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryName = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
CategoryName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text="Description:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Description = tk.Text(form_frame4, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
Description.grid(row=3, column=1, sticky="w", pady=10)

button_frame4 = tk.Frame(tab4)
button_frame4.pack(pady=20)

tk.Button(button_frame4, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_category).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_category).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_category).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_category_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_categories).pack(side=tk.LEFT, padx=5)

tree_frame4 = tk.Frame(tab4)
tree_frame4.pack(fill="both", expand=True, padx=20, pady=10)

tree_categories = ttk.Treeview(
    tree_frame4,
    columns=("CategoryID", "CategoryName", "Description"),
    show="headings",
    height=8,
)
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


# ----------------------------- Tab 5: Suppliers ----------------------------

titulo5 = tk.Label(tab5, text="GESTIÓN DE SUPPLIERS", font=("Arial", 16, "bold"), fg="brown")
titulo5.pack(pady=20)

form_frame5 = tk.Frame(tab5)
form_frame5.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame5, text="SupplierID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(
    form_frame5,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
SupplierID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="SupplierName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierName = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierContactName = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierContactName.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierAddress = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierAddress.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierCity = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierCity.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierPostalCode = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierPostalCode.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierCountry = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierCountry.grid(row=7, column=1, sticky="w", pady=10)

tk.Label(form_frame5, text="Phone:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierPhone = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierPhone.grid(row=8, column=1, sticky="w", pady=10)

button_frame5 = tk.Frame(tab5)
button_frame5.pack(pady=20)

tk.Button(button_frame5, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_supplier).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame5, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_supplier).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame5, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_supplier).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame5, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_supplier_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame5, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_suppliers).pack(side=tk.LEFT, padx=5)

tree_frame5 = tk.Frame(tab5)
tree_frame5.pack(fill="both", expand=True, padx=20, pady=10)

tree_suppliers = ttk.Treeview(
    tree_frame5,
    columns=("SupplierID", "SupplierName", "ContactName", "Address", "City", "PostalCode", "Country", "Phone"),
    show="headings",
    height=8,
)
for column, title in [
    ("SupplierID", "ID"),
    ("SupplierName", "Nombre"),
    ("ContactName", "Contacto"),
    ("Address", "Dirección"),
    ("City", "Ciudad"),
    ("PostalCode", "Código Postal"),
    ("Country", "País"),
    ("Phone", "Teléfono"),
]:
    tree_suppliers.heading(column, text=title)

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


# ----------------------------- Tab 6: Shippers -----------------------------

titulo6 = tk.Label(tab6, text="GESTIÓN DE SHIPPERS", font=("Arial", 16, "bold"), fg="teal")
titulo6.pack(pady=20)

form_frame6 = tk.Frame(tab6)
form_frame6.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame6, text="ShipperID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperID = tk.Entry(
    form_frame6,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
ShipperID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame6, text="ShipperName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperName = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
ShipperName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame6, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ShipperPhone = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
ShipperPhone.grid(row=3, column=1, sticky="w", pady=10)

button_frame6 = tk.Frame(tab6)
button_frame6.pack(pady=20)

tk.Button(button_frame6, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_shipper).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame6, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_shipper).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame6, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_shipper).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame6, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_shipper_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame6, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_shippers).pack(side=tk.LEFT, padx=5)

tree_frame6 = tk.Frame(tab6)
tree_frame6.pack(fill="both", expand=True, padx=20, pady=10)

tree_shippers = ttk.Treeview(
    tree_frame6,
    columns=("ShipperID", "ShipperName", "Phone"),
    show="headings",
    height=8,
)
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


# ------------------------------ Tab 7: Orders ------------------------------

titulo7 = tk.Label(tab7, text="GESTIÓN DE ORDERS", font=("Arial", 16, "bold"), fg="navy")
titulo7.pack(pady=20)

form_frame7 = tk.Frame(tab7)
form_frame7.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame7, text="OrderID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
OrderID = tk.Entry(
    form_frame7,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame7, text="CustomerID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
OrderCustomerID = tk.Entry(
    form_frame7,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderCustomerID.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame7, text="EmployeeID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
OrderEmployeeID = tk.Entry(
    form_frame7,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderEmployeeID.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame7, text="OrderDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDate = DateEntry(form_frame7, width=25, font=("Arial", 12), date_pattern="yyyy-mm-dd", background="darkblue", foreground="white", borderwidth=2)
OrderDate.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame7, text="ShipperID:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
OrderShipperID = tk.Entry(
    form_frame7,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderShipperID.grid(row=5, column=1, sticky="w", pady=10)

button_frame7 = tk.Frame(tab7)
button_frame7.pack(pady=20)

tk.Button(button_frame7, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_order).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame7, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_order).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame7, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_order).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame7, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_order_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame7, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_orders).pack(side=tk.LEFT, padx=5)

tree_frame7 = tk.Frame(tab7)
tree_frame7.pack(fill="both", expand=True, padx=20, pady=10)

tree_orders = ttk.Treeview(
    tree_frame7,
    columns=("OrderID", "CustomerID", "EmployeeID", "OrderDate", "ShipperID"),
    show="headings",
    height=8,
)
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


# --------------------------- Tab 8: OrderDetails ---------------------------

titulo8 = tk.Label(tab8, text="GESTIÓN DE ORDERDETAILS", font=("Arial", 16, "bold"), fg="maroon")
titulo8.pack(pady=20)

form_frame8 = tk.Frame(tab8)
form_frame8.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame8, text="OrderDetailID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailID = tk.Entry(
    form_frame8,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderDetailID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame8, text="OrderID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailOrderID = tk.Entry(
    form_frame8,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderDetailOrderID.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame8, text="ProductID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
OrderDetailProductID = tk.Entry(
    form_frame8,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
OrderDetailProductID.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame8, text="Quantity:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Quantity = tk.Entry(
    form_frame8,
    width=25,
    font=("Arial", 12),
    relief="solid",
    bd=1,
)
Quantity.grid(row=4, column=1, sticky="w", pady=10)

button_frame8 = tk.Frame(tab8)
button_frame8.pack(pady=20)

tk.Button(button_frame8, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_orderdetail).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame8, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_orderdetail).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame8, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_orderdetail).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame8, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_orderdetail_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame8, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=show_all_orderdetails).pack(side=tk.LEFT, padx=5)

tree_frame8 = tk.Frame(tab8)
tree_frame8.pack(fill="both", expand=True, padx=20, pady=10)

tree_orderdetails = ttk.Treeview(
    tree_frame8,
    columns=("OrderDetailID", "OrderID", "ProductID", "Quantity"),
    show="headings",
    height=8,
)
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


# ---------------------------------------------------------------------------
# Inicialización con datos de ejemplo
# ---------------------------------------------------------------------------

show_all_products()
show_all_customers()
show_all_employees()
show_all_categories()
show_all_suppliers()
show_all_shippers()
show_all_orders()
show_all_orderdetails()


if __name__ == "__main__":
    root.mainloop()


