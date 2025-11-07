import tkinter as tk
from tkinter import ttk

from mvc.utils.validation import validate_int_input, validate_float_input
from mvc.utils.export import export_treeview_to_excel


class ProductView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="FORMULARIO DE PRODUCTS", font=("Arial", 16, "bold"), fg="blue")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)
        reg_float = root.register(validate_float_input)

        tk.Label(form_frame, text="ProductID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ProductID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.ProductID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ProductName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.ProductName.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="SupplierID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.SupplierID.grid(row=3, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="CategoryID:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
        self.CategoryID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.CategoryID.grid(row=4, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Unit:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
        self.Unit = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.Unit.grid(row=5, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
        self.Price = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_float, "%P"))
        self.Price.grid(row=6, column=1, sticky="w", pady=10)

        button_frame = tk.Frame(parent)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=self._on_save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=self._on_update).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=self._on_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=controller.refresh).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Exportar a Excel", font=("Arial", 12), bg="#607D8B", fg="white", width=15, command=self.export_to_excel).pack(side=tk.LEFT, padx=5)

        tree_frame = tk.Frame(parent)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ProductID", "ProductName", "SupplierID", "CategoryID", "Unit", "Price"), show="headings", height=10)
        self.tree.heading("ProductID", text="ID")
        self.tree.heading("ProductName", text="Nombre")
        self.tree.heading("SupplierID", text="Proveedor ID")
        self.tree.heading("CategoryID", text="Categoría ID")
        self.tree.heading("Unit", text="Unidad")
        self.tree.heading("Price", text="Precio")
        self.tree.column("ProductID", width=60)
        self.tree.column("ProductName", width=200)
        self.tree.column("SupplierID", width=100)
        self.tree.column("CategoryID", width=100)
        self.tree.column("Unit", width=100)
        self.tree.column("Price", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "ProductID": self.ProductID.get(),
            "ProductName": self.ProductName.get(),
            "SupplierID": self.SupplierID.get(),
            "CategoryID": self.CategoryID.get(),
            "Unit": self.Unit.get(),
            "Price": self.Price.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.ProductID.get())
        self.clear()

    def clear(self):
        self.ProductID.delete(0, tk.END)
        self.ProductName.delete(0, tk.END)
        self.SupplierID.delete(0, tk.END)
        self.CategoryID.delete(0, tk.END)
        self.Unit.delete(0, tk.END)
        self.Price.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def export_to_excel(self):
        self.controller.refresh()
        export_treeview_to_excel(self.tree, "products")


