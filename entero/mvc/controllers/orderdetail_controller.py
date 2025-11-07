from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import OrderDetail, OrderDetailRepository


class OrderDetailController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = OrderDetailRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["OrderDetailID"]:
                messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio")
                return
            
            order_detail = OrderDetail(
                OrderDetailID=int(values["OrderDetailID"]),
                OrderID=int(values["OrderID"]) if values["OrderID"] else None,
                ProductID=int(values["ProductID"]) if values["ProductID"] else None,
                Quantity=int(values["Quantity"]) if values["Quantity"] else None,
            )
            if self.repo.insert(order_detail):
                messagebox.showinfo("Guardar", "Detalle de pedido guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar detalle de pedido: {e}")

    def on_update(self, values):
        try:
            if not values["OrderDetailID"]:
                messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio para actualizar")
                return
                
            order_detail = OrderDetail(
                OrderDetailID=int(values["OrderDetailID"]),
                OrderID=int(values["OrderID"]) if values["OrderID"] else None,
                ProductID=int(values["ProductID"]) if values["ProductID"] else None,
                Quantity=int(values["Quantity"]) if values["Quantity"] else None,
            )
            if self.repo.update(order_detail):
                messagebox.showinfo("Actualizar", "Detalle de pedido actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar detalle de pedido: {e}")

    def on_delete(self, order_detail_id_str: str):
        try:
            if not order_detail_id_str:
                messagebox.showwarning("Advertencia", "OrderDetailID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este detalle de pedido?"):
                odid = int(order_detail_id_str)
                if self.repo.delete(odid):
                    messagebox.showinfo("Eliminar", "Detalle de pedido eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar detalle de pedido: {e}")
