import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from typing import Optional


# CONFIGURACIÓN DE BASE DE DATOS 
DATABASE_CONFIG = {
    'host': 'localhost',      
    'user': 'root',           
    'password': '',           
    'database': 'northwind'   
}


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="", database="northwind"):
        self.host = host
        self.user = user
        self.password = ""
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return True
        except Error as e:
            messagebox.showerror("Error de Conexión", f"Error al conectar con la base de datos: {e}")
            return False
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        try:
            if self.connection is None or not self.connection.is_connected():
                if not self.connect():
                    return False
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al ejecutar consulta: {e}")
            return False
    
    def fetch_all(self, query, params=None):
        try:
            if self.connection is None or not self.connection.is_connected():
                if not self.connect():
                    return []
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al obtener datos: {e}")
            return []

    # Métodos compatibles con el código existente
    def execute(self, query: str, params: Optional[list] = None) -> bool:
        return self.execute_query(query, params)

    def fetch_one(self, query: str, params: Optional[list] = None) -> Optional[tuple]:
        try:
            if self.connection is None or not self.connection.is_connected():
                if not self.connect():
                    return None
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al obtener dato: {e}")
            return None


# Conexión usando la configuración importada
db = DatabaseConnection(**DATABASE_CONFIG)