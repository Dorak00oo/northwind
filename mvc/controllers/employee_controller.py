from __future__ import annotations

from typing import Optional
from tkinter import messagebox

from mvc.db.connection import DatabaseConnection
from mvc.models.product import Employee, EmployeeRepository


class EmployeeController:
    def __init__(self, db: Optional[DatabaseConnection] = None):
        self.db = db or DatabaseConnection()
        self.repo = EmployeeRepository(self.db)
        self.view = None

    def attach_view(self, view):
        self.view = view

    def refresh(self):
        items = self.repo.list_all()
        if self.view:
            self.view.render_rows(items)

    def on_save(self, values):
        try:
            if not values["EmployeeID"] or not values["LastName"] or not values["FirstName"]:
                messagebox.showwarning("Advertencia", "EmployeeID, LastName y FirstName son campos obligatorios")
                return
            
            employee = Employee(
                EmployeeID=int(values["EmployeeID"]),
                LastName=values["LastName"],
                FirstName=values["FirstName"],
                BirthDate=values["BirthDate"],
                Photo="",
                Notes=values["Notes"],
            )
            if self.repo.insert(employee):
                messagebox.showinfo("Guardar", "Empleado guardado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar empleado: {e}")

    def on_update(self, values):
        try:
            if not values["EmployeeID"]:
                messagebox.showwarning("Advertencia", "EmployeeID es obligatorio para actualizar")
                return
                
            employee = Employee(
                EmployeeID=int(values["EmployeeID"]),
                LastName=values["LastName"],
                FirstName=values["FirstName"],
                BirthDate=values["BirthDate"],
                Photo="",
                Notes=values["Notes"],
            )
            if self.repo.update(employee):
                messagebox.showinfo("Actualizar", "Empleado actualizado correctamente")
                self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar empleado: {e}")

    def on_delete(self, employee_id_str: str):
        try:
            if not employee_id_str:
                messagebox.showwarning("Advertencia", "EmployeeID es obligatorio para eliminar")
                return
                
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este empleado?"):
                eid = int(employee_id_str)
                if self.repo.delete(eid):
                    messagebox.showinfo("Eliminar", "Empleado eliminado correctamente")
                    self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar empleado: {e}")
