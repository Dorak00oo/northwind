# FUNCIONES DE VALIDACIÓN
def validate_int_input(P):
    """Valida que solo se ingresen números enteros"""
    if P == "" or P == "-":
        return True
    try:
        int(P)
        return True
    except ValueError:
        return False

def validate_float_input(P):
    """Valida que solo se ingresen números decimales"""
    if P == "" or P == "-" or P == ".":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
