from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Category, CategoryRepository


class CategoryController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = CategoryRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["CategoryID"] or not values["CategoryName"]:
                messagebox.showwarning("Advertencia", "CategoryID y CategoryName son campos obligatorios")
                return
            
            category = Category(
                CategoryID=int(values["CategoryID"]),
                CategoryName=values["CategoryName"],
                Description=values["Description"],
            )
            if self.repo.insert(category):
                messagebox.showinfo("Guardar", "Categoría guardada correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar categoría: {e}")

    def on_update(self, values):
        try:
            if not values["CategoryID"]:
                messagebox.showwarning("Advertencia", "CategoryID es obligatorio para actualizar")
                return
                
            category = Category(
                CategoryID=int(values["CategoryID"]),
                CategoryName=values["CategoryName"],
                Description=values["Description"],
            )
            if self.repo.update(category):
                messagebox.showinfo("Actualizar", "Categoría actualizada correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar categoría: {e}")

    def on_delete(self, category_id_str: str):
        try:
            if not category_id_str:
                messagebox.showwarning("Advertencia", "CategoryID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar esta categoría?"):
                cid = int(category_id_str)
                if self.repo.delete(cid):
                    messagebox.showinfo("Eliminar", "Categoría eliminada correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar categoría: {e}")
