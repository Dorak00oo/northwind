import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from mvc.utils.validation import validate_int_input
from mvc.utils.export import export_treeview_to_excel


class OrderView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="GESTIÓN DE ORDERS", font=("Arial", 16, "bold"), fg="navy")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)

        tk.Label(form_frame, text="OrderID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="CustomerID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderCustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderCustomerID.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="EmployeeID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderEmployeeID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderEmployeeID.grid(row=3, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="OrderDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderDate = DateEntry(form_frame, width=25, font=("Arial", 12), date_pattern="yyyy-mm-dd", background="darkblue", foreground="white", borderwidth=2)
        self.OrderDate.grid(row=4, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ShipperID:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
        self.OrderShipperID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.OrderShipperID.grid(row=5, column=1, sticky="w", pady=10)

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

        self.tree = ttk.Treeview(tree_frame, columns=("OrderID", "CustomerID", "EmployeeID", "OrderDate", "ShipperID"), show="headings", height=8)
        self.tree.heading("OrderID", text="ID Pedido")
        self.tree.heading("CustomerID", text="ID Cliente")
        self.tree.heading("EmployeeID", text="ID Empleado")
        self.tree.heading("OrderDate", text="Fecha Pedido")
        self.tree.heading("ShipperID", text="ID Transportista")
        self.tree.column("OrderID", width=100)
        self.tree.column("CustomerID", width=100)
        self.tree.column("EmployeeID", width=100)
        self.tree.column("OrderDate", width=150)
        self.tree.column("ShipperID", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "OrderID": self.OrderID.get(),
            "CustomerID": self.OrderCustomerID.get(),
            "EmployeeID": self.OrderEmployeeID.get(),
            "OrderDate": self.OrderDate.get_date() if self.OrderDate.get_date() else None,
            "ShipperID": self.OrderShipperID.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.OrderID.get())
        self.clear()

    def clear(self):
        self.OrderID.delete(0, tk.END)
        self.OrderCustomerID.delete(0, tk.END)
        self.OrderEmployeeID.delete(0, tk.END)
        self.OrderShipperID.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def export_to_excel(self):
        self.controller.refresh()
        export_treeview_to_excel(self.tree, "orders")
