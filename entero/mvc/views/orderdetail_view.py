import tkinter as tk
from tkinter import ttk

from mvc.utils.validation import validate_int_input
from mvc.utils.export import export_treeview_to_excel


class OrderDetailView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="GESTIÓN DE ORDERDETAILS", font=("Arial", 16, "bold"), fg="maroon")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)

        tk.Label(form_frame, text="OrderDetailID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderDetailID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderDetailID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="OrderID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderDetailOrderID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderDetailOrderID.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ProductID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderDetailProductID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderDetailProductID.grid(row=3, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Quantity:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
        self.Quantity = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.Quantity.grid(row=4, column=1, sticky="w", pady=10)

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

        self.tree = ttk.Treeview(tree_frame, columns=("OrderDetailID", "OrderID", "ProductID", "Quantity"), show="headings", height=8)
        self.tree.heading("OrderDetailID", text="ID Detalle")
        self.tree.heading("OrderID", text="ID Pedido")
        self.tree.heading("ProductID", text="ID Producto")
        self.tree.heading("Quantity", text="Cantidad")
        self.tree.column("OrderDetailID", width=100)
        self.tree.column("OrderID", width=100)
        self.tree.column("ProductID", width=100)
        self.tree.column("Quantity", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "OrderDetailID": self.OrderDetailID.get(),
            "OrderID": self.OrderDetailOrderID.get(),
            "ProductID": self.OrderDetailProductID.get(),
            "Quantity": self.Quantity.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.OrderDetailID.get())
        self.clear()

    def clear(self):
        self.OrderDetailID.delete(0, tk.END)
        self.OrderDetailOrderID.delete(0, tk.END)
        self.OrderDetailProductID.delete(0, tk.END)
        self.Quantity.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def export_to_excel(self):
        self.controller.refresh()
        export_treeview_to_excel(self.tree, "orderdetails")
