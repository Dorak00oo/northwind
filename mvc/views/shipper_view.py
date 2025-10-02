import tkinter as tk
from tkinter import ttk

from mvc.utils.validation import validate_int_input


class ShipperView:
    def __init__(self, root, parent, controller):
        self.root = root
        self.controller = controller
        controller.attach_view(self)

        titulo = tk.Label(parent, text="GESTIÓN DE SHIPPERS", font=("Arial", 16, "bold"), fg="teal")
        titulo.pack(pady=20)

        form_frame = tk.Frame(parent)
        form_frame.pack(pady=20, anchor="w", padx=50)

        reg_int = root.register(validate_int_input)

        tk.Label(form_frame, text="ShipperID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ShipperID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, validate="key", validatecommand=(reg_int, "%P"))
        self.ShipperID.grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="ShipperName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ShipperName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.ShipperName.grid(row=2, column=1, sticky="w", pady=10)

        tk.Label(form_frame, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
        self.ShipperPhone = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.ShipperPhone.grid(row=3, column=1, sticky="w", pady=10)

        button_frame = tk.Frame(parent)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=self._on_save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=self._on_update).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=self._on_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mostrar Todos", font=("Arial", 12), bg="#9C27B0", fg="white", width=12, command=controller.refresh).pack(side=tk.LEFT, padx=5)

        tree_frame = tk.Frame(parent)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ShipperID", "ShipperName", "Phone"), show="headings", height=8)
        self.tree.heading("ShipperID", text="ID")
        self.tree.heading("ShipperName", text="Nombre")
        self.tree.heading("Phone", text="Teléfono")
        self.tree.column("ShipperID", width=60)
        self.tree.column("ShipperName", width=300)
        self.tree.column("Phone", width=200)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _collect_values(self):
        return {
            "ShipperID": self.ShipperID.get(),
            "ShipperName": self.ShipperName.get(),
            "Phone": self.ShipperPhone.get(),
        }

    def _on_save(self):
        self.controller.on_save(self._collect_values())
        self.clear()

    def _on_update(self):
        self.controller.on_update(self._collect_values())
        self.clear()

    def _on_delete(self):
        self.controller.on_delete(self.ShipperID.get())
        self.clear()

    def clear(self):
        self.ShipperID.delete(0, tk.END)
        self.ShipperName.delete(0, tk.END)
        self.ShipperPhone.delete(0, tk.END)

    def render_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)
