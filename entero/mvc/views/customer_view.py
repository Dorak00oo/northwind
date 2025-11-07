import tkinter as tk
from tkinter import ttk

from mvc.utils.validation import validate_int_input
from mvc.utils.export import export_treeview_to_excel


class CustomerView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="GESTIÓN DE CUSTOMERS", font=("Arial", 16, "bold"), fg="green")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)

        tk.Label(form_frame, text="CustomerID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.CustomerID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="CustomerName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.CustomerName.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.ContactName.grid(row=3, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
        self.Address = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.Address.grid(row=4, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
        self.City = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.City.grid(row=5, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
        self.PostalCode = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.PostalCode.grid(row=6, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
        self.Country = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.Country.grid(row=7, column=1, sticky="w", pady=10)

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

        self.tree = ttk.Treeview(tree_frame, columns=("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country"), show="headings", height=10)
        self.tree.heading("CustomerID", text="ID")
        self.tree.heading("CustomerName", text="Nombre Cliente")
        self.tree.heading("ContactName", text="Contacto")
        self.tree.heading("Address", text="Dirección")
        self.tree.heading("City", text="Ciudad")
        self.tree.heading("PostalCode", text="Código Postal")
        self.tree.heading("Country", text="País")
        self.tree.column("CustomerID", width=60)
        self.tree.column("CustomerName", width=150)
        self.tree.column("ContactName", width=120)
        self.tree.column("Address", width=150)
        self.tree.column("City", width=100)
        self.tree.column("PostalCode", width=100)
        self.tree.column("Country", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "CustomerID": self.CustomerID.get(),
            "CustomerName": self.CustomerName.get(),
            "ContactName": self.ContactName.get(),
            "Address": self.Address.get(),
            "City": self.City.get(),
            "PostalCode": self.PostalCode.get(),
            "Country": self.Country.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.CustomerID.get())
        self.clear()

    def clear(self):
        self.CustomerID.delete(0, tk.END)
        self.CustomerName.delete(0, tk.END)
        self.ContactName.delete(0, tk.END)
        self.Address.delete(0, tk.END)
        self.City.delete(0, tk.END)
        self.PostalCode.delete(0, tk.END)
        self.Country.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def export_to_excel(self):
        self.controller.refresh()
        export_treeview_to_excel(self.tree, "customers")
