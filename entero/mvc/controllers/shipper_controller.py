from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Shipper, ShipperRepository


class ShipperController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = ShipperRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["ShipperID"] or not values["ShipperName"]:
                messagebox.showwarning("Advertencia", "ShipperID y ShipperName son campos obligatorios")
                return
            
            shipper = Shipper(
                ShipperID=int(values["ShipperID"]),
                ShipperName=values["ShipperName"],
                Phone=values["Phone"],
            )
            if self.repo.insert(shipper):
                messagebox.showinfo("Guardar", "Transportista guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar transportista: {e}")

    def on_update(self, values):
        try:
            if not values["ShipperID"]:
                messagebox.showwarning("Advertencia", "ShipperID es obligatorio para actualizar")
                return
                
            shipper = Shipper(
                ShipperID=int(values["ShipperID"]),
                ShipperName=values["ShipperName"],
                Phone=values["Phone"],
            )
            if self.repo.update(shipper):
                messagebox.showinfo("Actualizar", "Transportista actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar transportista: {e}")

    def on_delete(self, shipper_id_str: str):
        try:
            if not shipper_id_str:
                messagebox.showwarning("Advertencia", "ShipperID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este transportista?"):
                sid = int(shipper_id_str)
                if self.repo.delete(sid):
                    messagebox.showinfo("Eliminar", "Transportista eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar transportista: {e}")
