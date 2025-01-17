import tkinter as tk
from tkinter import messagebox
import numpy as np
import os

matrices_created = False  # Global flag to track matrix creation

def create_matrix_entry(rows, cols, frame):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

def get_matrix_from_entries(entries):
    matrix = []
    for row_entries in entries:
        row = []
        for entry in row_entries:
            value = entry.get()
            if value == "":
                raise ValueError("Все поля должны быть заполнены.")
            try:
                row.append(float(value))
            except ValueError:
                raise ValueError("Введены некорректные данные. Пожалуйста, введите числа.")
        matrix.append(row)
    return np.array(matrix)

def add_matrices():
    global matrices_created
    if not matrices_created:
        messagebox.showwarning("Ошибка", "Сначала создайте матрицы.")
        return
    try:
        matrix1 = get_matrix_from_entries(entries1)
        matrix2 = get_matrix_from_entries(entries2)
        if matrix1.shape != matrix2.shape:
            raise ValueError("Матрицы должны быть одинакового размера.")
        result = matrix1 + matrix2
        result_label.config(text=str(result))
    except ValueError as e:
        messagebox.showwarning("Ошибка", str(e))

def subtract_matrices():
    global matrices_created
    if not matrices_created:
        messagebox.showwarning("Ошибка", "Сначала создайте матрицы.")
        return
    try:
        matrix1 = get_matrix_from_entries(entries1)
        matrix2 = get_matrix_from_entries(entries2)
        if matrix1.shape != matrix2.shape:
            raise ValueError("Матрицы должны быть одинакового размера.")
        result = matrix1 - matrix2
        result_label.config(text=str(result))
    except ValueError as e:
        messagebox.showwarning("Ошибка", str(e))

def multiply_matrices():
    global matrices_created
    if not matrices_created:
        messagebox.showwarning("Ошибка", "Сначала создайте матрицы.")
        return
    try:
        matrix1 = get_matrix_from_entries(entries1)
        matrix2 = get_matrix_from_entries(entries2)
        if matrix1.shape[1] != matrix2.shape[0]:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        result = np.dot(matrix1, matrix2)
        result_label.config(text=str(result))
    except ValueError as e:
        messagebox.showwarning("Ошибка", str(e))

def transpose_matrix():
    global matrices_created
    if not matrices_created:
        messagebox.showwarning("Ошибка", "Сначала создайте матрицы.")
        return
    try:
        matrix = get_matrix_from_entries(entries1)
        result = np.transpose(matrix)
        result_label.config(text=str(result))
    except ValueError as e:
        messagebox.showwarning("Ошибка", str(e))

def create_matrices():
    global entries1, entries2, matrices_created
    try:
        # Проверка на пустые поля
        if rows_entry.get() == "" or cols_entry.get() == "":
            raise ValueError("Поля количества строк и столбцов должны быть заполнены.")

        # Попытка преобразовать введённые значения в целые числа
        try:
            rows = int(rows_entry.get())
            cols = int(cols_entry.get())
        except ValueError:
            raise ValueError("Введены некорректные данные. Пожалуйста, введите целые числа.")

        # Проверка на положительные размеры матрицы
        if rows <= 0 or cols <= 0:
            raise ValueError("Размеры матрицы должны быть положительными числами.")

        # Проверка на максимальный размер матрицы
        if rows > 15 or cols > 15:
            raise ValueError("Максимальный размер матрицы не должен превышать 15x15.")

        # Очистка старых матриц
        for widget in frame1.winfo_children():
            widget.destroy()
        for widget in frame2.winfo_children():
            widget.destroy()

        # Создание новых матриц
        entries1 = create_matrix_entry(rows, cols, frame1)
        entries2 = create_matrix_entry(rows, cols, frame2)

        matrices_created = True  # Matrices have been created successfully

    except ValueError as e:
        matrices_created = False  # Reset the flag in case of error
        messagebox.showwarning("Ошибка", str(e))

root = tk.Tk()
root.title("Матрицы")
root.resizable(width=False, height=False)

# Проверка наличия иконки
icon_path = os.path.abspath("icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    messagebox.showwarning("Предупреждение",
                           f"Предупреждение: Файл иконки '{icon_path}' не найден. Приложение будет запущено без иконки.")
# Поля для ввода размеров матрицы
tk.Label(root, text="Количество строк:").grid(row=0, column=0, padx=10, pady=10)
rows_entry = tk.Entry(root, width=5)
rows_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Количество столбцов:").grid(row=0, column=2, padx=10, pady=10)
cols_entry = tk.Entry(root, width=5)
cols_entry.grid(row=0, column=3, padx=10, pady=10)

# Кнопка для создания матриц
create_button = tk.Button(root, text="Создать матрицы", command=create_matrices)
create_button.grid(row=0, column=4, padx=10, pady=10)

# Создание рамок для матриц
frame1 = tk.Frame(root)
frame1.grid(row=1, column=0, padx=10, pady=10)

frame2 = tk.Frame(root)
frame2.grid(row=1, column=1, padx=10, pady=10)

# Создание кнопок для операций
add_button = tk.Button(root, text="Сложить\nматрицы №1 и №2", command=add_matrices)
add_button.grid(row=2, column=0, pady=10)

subtract_button = tk.Button(root, text="Вычесть\nматрицы №1 и №2", command=subtract_matrices)
subtract_button.grid(row=2, column=1, pady=10)

multiply_button = tk.Button(root, text="Умножить\nматрицы №1 и №2", command=multiply_matrices)
multiply_button.grid(row=3, column=0, pady=10)

transpose_button = tk.Button(root, text="Транспонировать\nматрицу №1", command=transpose_matrix)
transpose_button.grid(row=3, column=1, pady=10)

# Создание метки для вывода результата
result_label = tk.Label(root, text="Результат будет здесь", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()