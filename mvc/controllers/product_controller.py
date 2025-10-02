from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Product, ProductRepository


class ProductController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = ProductRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["ProductID"] or not values["ProductName"]:
                messagebox.showwarning("Advertencia", "ProductID y ProductName son campos obligatorios")
                return
            
            product = Product(
                ProductID=int(values["ProductID"]),
                ProductName=values["ProductName"],
                SupplierID=int(values["SupplierID"]) if values["SupplierID"] else None,
                CategoryID=int(values["CategoryID"]) if values["CategoryID"] else None,
                Unit=values["Unit"],
                Price=float(values["Price"]) if values["Price"] else None,
            )
            if self.repo.insert(product):
                messagebox.showinfo("Guardar", "Producto guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar producto: {e}")

    def on_update(self, values):
        try:
            if not values["ProductID"]:
                messagebox.showwarning("Advertencia", "ProductID es obligatorio para actualizar")
                return
                
            product = Product(
                ProductID=int(values["ProductID"]),
                ProductName=values["ProductName"],
                SupplierID=int(values["SupplierID"]) if values["SupplierID"] else None,
                CategoryID=int(values["CategoryID"]) if values["CategoryID"] else None,
                Unit=values["Unit"],
                Price=float(values["Price"]) if values["Price"] else None,
            )
            if self.repo.update(product):
                messagebox.showinfo("Actualizar", "Producto actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar producto: {e}")

    def on_delete(self, product_id_str: str):
        try:
            if not product_id_str:
                messagebox.showwarning("Advertencia", "ProductID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este producto?"):
                pid = int(product_id_str)
                if self.repo.delete(pid):
                    messagebox.showinfo("Eliminar", "Producto eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar producto: {e}")


