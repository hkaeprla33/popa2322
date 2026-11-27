"""Простой калькулятор с базовыми арифметическими операциями."""

def add(a: float, b: float) -> float:
    """Сложение."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление. Бросает ValueError при делении на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
