from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Customer, CustomerRepository


class CustomerController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = CustomerRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["CustomerID"] or not values["CustomerName"]:
                messagebox.showwarning("Advertencia", "CustomerID y CustomerName son campos obligatorios")
                return
            
            customer = Customer(
                CustomerID=int(values["CustomerID"]),
                CustomerName=values["CustomerName"],
                ContactName=values["ContactName"],
                Address=values["Address"],
                City=values["City"],
                PostalCode=values["PostalCode"],
                Country=values["Country"],
            )
            if self.repo.insert(customer):
                messagebox.showinfo("Guardar", "Cliente guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar cliente: {e}")

    def on_update(self, values):
        try:
            if not values["CustomerID"]:
                messagebox.showwarning("Advertencia", "CustomerID es obligatorio para actualizar")
                return
                
            customer = Customer(
                CustomerID=int(values["CustomerID"]),
                CustomerName=values["CustomerName"],
                ContactName=values["ContactName"],
                Address=values["Address"],
                City=values["City"],
                PostalCode=values["PostalCode"],
                Country=values["Country"],
            )
            if self.repo.update(customer):
                messagebox.showinfo("Actualizar", "Cliente actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar cliente: {e}")

    def on_delete(self, customer_id_str: str):
        try:
            if not customer_id_str:
                messagebox.showwarning("Advertencia", "CustomerID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este cliente?"):
                cid = int(customer_id_str)
                if self.repo.delete(cid):
                    messagebox.showinfo("Eliminar", "Cliente eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar cliente: {e}")
