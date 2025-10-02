from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Supplier, SupplierRepository


class SupplierController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = SupplierRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["SupplierID"] or not values["SupplierName"]:
                messagebox.showwarning("Advertencia", "SupplierID y SupplierName son campos obligatorios")
                return
            
            supplier = Supplier(
                SupplierID=int(values["SupplierID"]),
                SupplierName=values["SupplierName"],
                ContactName=values["ContactName"],
                Address=values["Address"],
                City=values["City"],
                PostalCode=values["PostalCode"],
                Country=values["Country"],
                Phone=values["Phone"],
            )
            if self.repo.insert(supplier):
                messagebox.showinfo("Guardar", "Proveedor guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar proveedor: {e}")

    def on_update(self, values):
        try:
            if not values["SupplierID"]:
                messagebox.showwarning("Advertencia", "SupplierID es obligatorio para actualizar")
                return
                
            supplier = Supplier(
                SupplierID=int(values["SupplierID"]),
                SupplierName=values["SupplierName"],
                ContactName=values["ContactName"],
                Address=values["Address"],
                City=values["City"],
                PostalCode=values["PostalCode"],
                Country=values["Country"],
                Phone=values["Phone"],
            )
            if self.repo.update(supplier):
                messagebox.showinfo("Actualizar", "Proveedor actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar proveedor: {e}")

    def on_delete(self, supplier_id_str: str):
        try:
            if not supplier_id_str:
                messagebox.showwarning("Advertencia", "SupplierID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este proveedor?"):
                sid = int(supplier_id_str)
                if self.repo.delete(sid):
                    messagebox.showinfo("Eliminar", "Proveedor eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar proveedor: {e}")
