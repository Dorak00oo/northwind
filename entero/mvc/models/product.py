from dataclasses import dataclass
from typing import List, Tuple, Optional
from datetime import date

from mvc.db.connection import DatabaseConnection


@dataclass
class Product:
    ProductID: int
    ProductName: str
    SupplierID: Optional[int]
    CategoryID: Optional[int]
    Unit: Optional[str]
    Price: Optional[float]


@dataclass
class Customer:
    CustomerID: int
    CustomerName: str
    ContactName: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    PostalCode: Optional[str]
    Country: Optional[str]


@dataclass
class Employee:
    EmployeeID: int
    LastName: str
    FirstName: str
    BirthDate: Optional[date]
    Photo: Optional[str]
    Notes: Optional[str]


@dataclass
class Category:
    CategoryID: int
    CategoryName: str
    Description: Optional[str]


@dataclass
class Supplier:
    SupplierID: int
    SupplierName: str
    ContactName: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    PostalCode: Optional[str]
    Country: Optional[str]
    Phone: Optional[str]


@dataclass
class Shipper:
    ShipperID: int
    ShipperName: str
    Phone: Optional[str]


@dataclass
class Order:
    OrderID: int
    CustomerID: Optional[int]
    EmployeeID: Optional[int]
    OrderDate: Optional[date]
    ShipperID: Optional[int]


@dataclass
class OrderDetail:
    OrderDetailID: int
    OrderID: Optional[int]
    ProductID: Optional[int]
    Quantity: Optional[int]


class ProductRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT ProductID, ProductName, SupplierID, CategoryID, Unit, Price FROM products"
        )

    def insert(self, p: Product) -> bool:
        return self.db.execute_query(
            "INSERT INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s, %s)",
            (p.ProductID, p.ProductName, p.SupplierID, p.CategoryID, p.Unit, p.Price)
        )

    def update(self, p: Product) -> bool:
        return self.db.execute_query(
            "UPDATE products SET ProductName=%s, SupplierID=%s, CategoryID=%s, Unit=%s, Price=%s WHERE ProductID=%s",
            (p.ProductName, p.SupplierID, p.CategoryID, p.Unit, p.Price, p.ProductID)
        )

    def delete(self, product_id: int) -> bool:
        return self.db.execute_query("DELETE FROM products WHERE ProductID = %s", (product_id,))


class CustomerRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country FROM customers"
        )

    def insert(self, c: Customer) -> bool:
        return self.db.execute_query(
            "INSERT INTO customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (c.CustomerID, c.CustomerName, c.ContactName, c.Address, c.City, c.PostalCode, c.Country)
        )

    def update(self, c: Customer) -> bool:
        return self.db.execute_query(
            "UPDATE customers SET CustomerName=%s, ContactName=%s, Address=%s, City=%s, PostalCode=%s, Country=%s WHERE CustomerID=%s",
            (c.CustomerName, c.ContactName, c.Address, c.City, c.PostalCode, c.Country, c.CustomerID)
        )

    def delete(self, customer_id: int) -> bool:
        return self.db.execute_query("DELETE FROM customers WHERE CustomerID = %s", (customer_id,))


class EmployeeRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM employees"
        )

    def insert(self, e: Employee) -> bool:
        return self.db.execute_query(
            "INSERT INTO employees (EmployeeID, LastName, FirstName, BirthDate, Photo, Notes) VALUES (%s, %s, %s, %s, %s, %s)",
            (e.EmployeeID, e.LastName, e.FirstName, e.BirthDate, e.Photo, e.Notes)
        )

    def update(self, e: Employee) -> bool:
        return self.db.execute_query(
            "UPDATE employees SET LastName=%s, FirstName=%s, BirthDate=%s, Photo=%s, Notes=%s WHERE EmployeeID=%s",
            (e.LastName, e.FirstName, e.BirthDate, e.Photo, e.Notes, e.EmployeeID)
        )

    def delete(self, employee_id: int) -> bool:
        return self.db.execute_query("DELETE FROM employees WHERE EmployeeID = %s", (employee_id,))


class CategoryRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT CategoryID, CategoryName, Description FROM categories"
        )

    def insert(self, c: Category) -> bool:
        return self.db.execute_query(
            "INSERT INTO categories (CategoryID, CategoryName, Description) VALUES (%s, %s, %s)",
            (c.CategoryID, c.CategoryName, c.Description)
        )

    def update(self, c: Category) -> bool:
        return self.db.execute_query(
            "UPDATE categories SET CategoryName=%s, Description=%s WHERE CategoryID=%s",
            (c.CategoryName, c.Description, c.CategoryID)
        )

    def delete(self, category_id: int) -> bool:
        return self.db.execute_query("DELETE FROM categories WHERE CategoryID = %s", (category_id,))


class SupplierRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone FROM suppliers"
        )

    def insert(self, s: Supplier) -> bool:
        return self.db.execute_query(
            "INSERT INTO suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (s.SupplierID, s.SupplierName, s.ContactName, s.Address, s.City, s.PostalCode, s.Country, s.Phone)
        )

    def update(self, s: Supplier) -> bool:
        return self.db.execute_query(
            "UPDATE suppliers SET SupplierName=%s, ContactName=%s, Address=%s, City=%s, PostalCode=%s, Country=%s, Phone=%s WHERE SupplierID=%s",
            (s.SupplierName, s.ContactName, s.Address, s.City, s.PostalCode, s.Country, s.Phone, s.SupplierID)
        )

    def delete(self, supplier_id: int) -> bool:
        return self.db.execute_query("DELETE FROM suppliers WHERE SupplierID = %s", (supplier_id,))


class ShipperRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT ShipperID, ShipperName, Phone FROM shippers"
        )

    def insert(self, s: Shipper) -> bool:
        return self.db.execute_query(
            "INSERT INTO shippers (ShipperID, ShipperName, Phone) VALUES (%s, %s, %s)",
            (s.ShipperID, s.ShipperName, s.Phone)
        )

    def update(self, s: Shipper) -> bool:
        return self.db.execute_query(
            "UPDATE shippers SET ShipperName=%s, Phone=%s WHERE ShipperID=%s",
            (s.ShipperName, s.Phone, s.ShipperID)
        )

    def delete(self, shipper_id: int) -> bool:
        return self.db.execute_query("DELETE FROM shippers WHERE ShipperID = %s", (shipper_id,))


class OrderRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT OrderID, CustomerID, EmployeeID, OrderDate, ShipperID FROM orders"
        )

    def insert(self, o: Order) -> bool:
        return self.db.execute_query(
            "INSERT INTO orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s, %s)",
            (o.OrderID, o.CustomerID, o.EmployeeID, o.OrderDate, o.ShipperID)
        )

    def update(self, o: Order) -> bool:
        return self.db.execute_query(
            "UPDATE orders SET CustomerID=%s, EmployeeID=%s, OrderDate=%s, ShipperID=%s WHERE OrderID=%s",
            (o.CustomerID, o.EmployeeID, o.OrderDate, o.ShipperID, o.OrderID)
        )

    def delete(self, order_id: int) -> bool:
        return self.db.execute_query("DELETE FROM orders WHERE OrderID = %s", (order_id,))


class OrderDetailRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def list_all(self) -> List[Tuple]:
        return self.db.fetch_all(
            "SELECT OrderDetailID, OrderID, ProductID, Quantity FROM orderdetails"
        )

    def insert(self, od: OrderDetail) -> bool:
        return self.db.execute_query(
            "INSERT INTO orderdetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)",
            (od.OrderDetailID, od.OrderID, od.ProductID, od.Quantity)
        )

    def update(self, od: OrderDetail) -> bool:
        return self.db.execute_query(
            "UPDATE orderdetails SET OrderID=%s, ProductID=%s, Quantity=%s WHERE OrderDetailID=%s",
            (od.OrderID, od.ProductID, od.Quantity, od.OrderDetailID)
        )

    def delete(self, order_detail_id: int) -> bool:
        return self.db.execute_query("DELETE FROM orderdetails WHERE OrderDetailID = %s", (order_detail_id,))


