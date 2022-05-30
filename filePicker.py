import tkinter as tk
from tkinter import filedialog


def pickFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    # print(file_path)
    return file_path
