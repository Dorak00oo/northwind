from tkinter import ttk

from mvc.controllers.product_controller import ProductController
from mvc.views.product_view import ProductView


class MainView:
    def __init__(self, root, notebook: ttk.Notebook, controller):
        self.root = root
        self.notebook = notebook
        self.controller = controller

        # Tabs placeholders to be populated incrementally
        self.tab_products = ttk.Frame(self.notebook)
        self.tab_customers = ttk.Frame(self.notebook)
        self.tab_employees = ttk.Frame(self.notebook)
        self.tab_categories = ttk.Frame(self.notebook)
        self.tab_suppliers = ttk.Frame(self.notebook)
        self.tab_shippers = ttk.Frame(self.notebook)
        self.tab_orders = ttk.Frame(self.notebook)
        self.tab_orderdetails = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_products, text="Products")
        self.notebook.add(self.tab_customers, text="Customers")
        self.notebook.add(self.tab_employees, text="Employees")
        self.notebook.add(self.tab_categories, text="Categories")
        self.notebook.add(self.tab_suppliers, text="Suppliers")
        self.notebook.add(self.tab_shippers, text="Shippers")
        self.notebook.add(self.tab_orders, text="Orders")
        self.notebook.add(self.tab_orderdetails, text="OrderDetails")

        # Initialize Products MVC slice
        self.product_controller = ProductController()
        self.product_view = ProductView(self.root, self.tab_products, self.product_controller)
        self.product_controller.refresh()


