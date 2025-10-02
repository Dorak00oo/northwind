import tkinter as tk
from tkinter import ttk

from mvc.utils.validation import validate_int_input


class SupplierView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="GESTIÓN DE SUPPLIERS", font=("Arial", 16, "bold"), fg="brown")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)

        tk.Label(form_frame, text="SupplierID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.SupplierID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="SupplierName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierName.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierContactName.grid(row=3, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierAddress = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierAddress.grid(row=4, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierCity = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierCity.grid(row=5, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierPostalCode = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierPostalCode.grid(row=6, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierCountry = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierCountry.grid(row=7, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Phone:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
        self.SupplierPhone = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.SupplierPhone.grid(row=8, column=1, sticky="w", pady=10)

        button_frame = tk.Frame(parent)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=self._on_save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=self._on_update).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=self._on_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=controller.refresh).pack(side=tk.LEFT, padx=5)

        tree_frame = tk.Frame(parent)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("SupplierID", "SupplierName", "ContactName", "Address", "City", "PostalCode", "Country", "Phone"), show="headings", height=8)
        self.tree.heading("SupplierID", text="ID")
        self.tree.heading("SupplierName", text="Nombre")
        self.tree.heading("ContactName", text="Contacto")
        self.tree.heading("Address", text="Dirección")
        self.tree.heading("City", text="Ciudad")
        self.tree.heading("PostalCode", text="Código Postal")
        self.tree.heading("Country", text="País")
        self.tree.heading("Phone", text="Teléfono")
        self.tree.column("SupplierID", width=60)
        self.tree.column("SupplierName", width=150)
        self.tree.column("ContactName", width=120)
        self.tree.column("Address", width=150)
        self.tree.column("City", width=100)
        self.tree.column("PostalCode", width=100)
        self.tree.column("Country", width=100)
        self.tree.column("Phone", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "SupplierID": self.SupplierID.get(),
            "SupplierName": self.SupplierName.get(),
            "ContactName": self.SupplierContactName.get(),
            "Address": self.SupplierAddress.get(),
            "City": self.SupplierCity.get(),
            "PostalCode": self.SupplierPostalCode.get(),
            "Country": self.SupplierCountry.get(),
            "Phone": self.SupplierPhone.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.SupplierID.get())
        self.clear()

    def clear(self):
        self.SupplierID.delete(0, tk.END)
        self.SupplierName.delete(0, tk.END)
        self.SupplierContactName.delete(0, tk.END)
        self.SupplierAddress.delete(0, tk.END)
        self.SupplierCity.delete(0, tk.END)
        self.SupplierPostalCode.delete(0, tk.END)
        self.SupplierCountry.delete(0, tk.END)
        self.SupplierPhone.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)
