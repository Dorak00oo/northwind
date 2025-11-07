from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Order, OrderRepository


class OrderController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = OrderRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["OrderID"]:
                messagebox.showwarning("Advertencia", "OrderID es obligatorio")
                return
            
            order = Order(
                OrderID=int(values["OrderID"]),
                CustomerID=int(values["CustomerID"]) if values["CustomerID"] else None,
                EmployeeID=int(values["EmployeeID"]) if values["EmployeeID"] else None,
                OrderDate=values["OrderDate"],
                ShipperID=int(values["ShipperID"]) if values["ShipperID"] else None,
            )
            if self.repo.insert(order):
                messagebox.showinfo("Guardar", "Pedido guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar pedido: {e}")

    def on_update(self, values):
        try:
            if not values["OrderID"]:
                messagebox.showwarning("Advertencia", "OrderID es obligatorio para actualizar")
                return
                
            order = Order(
                OrderID=int(values["OrderID"]),
                CustomerID=int(values["CustomerID"]) if values["CustomerID"] else None,
                EmployeeID=int(values["EmployeeID"]) if values["EmployeeID"] else None,
                OrderDate=values["OrderDate"],
                ShipperID=int(values["ShipperID"]) if values["ShipperID"] else None,
            )
            if self.repo.update(order):
                messagebox.showinfo("Actualizar", "Pedido actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar pedido: {e}")

    def on_delete(self, order_id_str: str):
        try:
            if not order_id_str:
                messagebox.showwarning("Advertencia", "OrderID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este pedido?"):
                oid = int(order_id_str)
                if self.repo.delete(oid):
                    messagebox.showinfo("Eliminar", "Pedido eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar pedido: {e}")
