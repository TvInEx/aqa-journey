def is_even(n: int) -> bool:
    """Возвращает True, если число чётное."""
    return n % 2 == 0

def to_int(value: str) -> int:
    """Преобразовать строку в целое число. Если не получается (например, строка "abc") — вернуть None."""
    try:
        return int(value)
    except(ValueError, TypeError):
        return None
    
def format_price(amount: float) -> str:
    """Вернуть строку вида "1234.50" — ровно 2 знака после точки."""
    return f"{float(amount):.2f}"

def describe_type(value) -> str:
    """Вернуть название типа значения: "int", "str", "list" и т.д."""
    return type(value).__name__

def safe_divide(a: float, b: float):
    """Вернуть a / b. Если b == 0 — вернуть None (без падения программы)."""
    if b == 0:
        return None
    return a/b

def to_bool(value: str) -> bool:
    """Строки "true", "1", "yes" (без учёта регистра и пробелов) -> True, остальные -> False."""
    if not isinstance(value, str):
        return False
    return value.lower().strip() in ("yes", "1", "true")

def clean_text(text: str) -> str:
    """Если text - не строка, вернуть None. Если строка - вернуть её без пробелов по краям и в нижнем регистре."""
    if not isinstance(text, str):
        return None
    return text.strip().lower()

def calculate_percentage(part: float, total: float) -> float:
    """Считает процент: (part / total) * 100. Если total == 0, вернуть None. Если part больше total, вернуть None."""
    if total == 0 or part > total:
        return None
    return part/total*100

def sum_valid_ints(items: list) -> int:
    """Принимает список любых значений. Пытается преобразовать каждое в int и сложить.
    Если элемент нельзя преобразовать (например "abc"), пропускает его. Если на вход пришло не список, вернуть 0."""
    summ = 0
    if not isinstance(items, list):
        return 0
    for item in items:
        try: 
            summ += int(item)
        except(ValueError, TypeError): pass
    return summ