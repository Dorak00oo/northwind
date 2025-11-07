"""Utility helpers for exporting Treeview data to Excel files."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox
from typing import Iterable, List

from openpyxl import Workbook


def _resolve_headers(tree) -> List[str]:
    headers: List[str] = []
    for column_id in tree["columns"]:
        heading = tree.heading(column_id).get("text")
        headers.append(heading if heading else column_id)
    return headers


def _resolve_rows(tree) -> Iterable[Iterable]:
    for item_id in tree.get_children():
        yield tree.item(item_id).get("values", [])


def export_treeview_to_excel(tree, default_name: str) -> None:
    """Prompt the user to export the current Treeview rows to an Excel file.

    Args:
        tree: ttk.Treeview instance whose data will be exported.
        default_name: Base filename used in the suggested export file name.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    suggested_filename = f"{default_name}_{timestamp}.xlsx"

    file_path = filedialog.asksaveasfilename(
        title="Exportar a Excel",
        defaultextension=".xlsx",
        filetypes=[("Excel Workbook", "*.xlsx")],
        initialfile=suggested_filename,
    )

    if not file_path:
        return

    try:
        workbook = Workbook()
        worksheet = workbook.active

        headers = _resolve_headers(tree)
        worksheet.append(headers)

        for row in _resolve_rows(tree):
            worksheet.append(list(row))

        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        workbook.save(file_path)
        messagebox.showinfo("Exportar a Excel", f"Datos exportados correctamente a\n{file_path}")
    except Exception as exc:  # pylint: disable=broad-except
        messagebox.showerror(
            "Exportar a Excel",
            f"No se pudo exportar el archivo.\n\nDetalle: {exc}",
        )


