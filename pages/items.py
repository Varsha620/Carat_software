import tkinter as tk
from tkinter import ttk, messagebox
from database.db import get_connection

def load_items_table(table):
    for row in table.get_children():
        table.delete(row)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    for row in cur.fetchall():
        table.insert("", tk.END, values=row)
    conn.close()

def items_page(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Manage Items", font=("Segoe UI", 18)).pack(pady=10)

    form = tk.Frame(content_frame)
    form.pack(pady=20)

    name_var = tk.StringVar()
    cat_var = tk.StringVar()
    price_var = tk.StringVar()
    weight_var = tk.StringVar()

    labels = ["Item Name", "Category", "Price", "Weight"]
    vars = [name_var, cat_var, price_var, weight_var]

    for i, text in enumerate(labels):
        tk.Label(form, text=text).grid(row=i, column=0, padx=5, pady=5)
        tk.Entry(form, textvariable=vars[i]).grid(row=i, column=1, padx=5, pady=5)

    def add_item():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO items(name, category, price, weight) VALUES (?, ?, ?, ?)",
            (name_var.get(), cat_var.get(), price_var.get(), weight_var.get())
        )
        conn.commit()
        conn.close()
        load_items_table(table)
        messagebox.showinfo("Success", "Item added!")

    tk.Button(
        form, text="Add Item", command=add_item,
        bg="green", fg="white"
    ).grid(row=4, column=1, pady=10)

    table = ttk.Treeview(content_frame, columns=("ID","Name","Category","Price","Weight"), show="headings")
    table.pack(fill=tk.BOTH, expand=True)

    for col in ("ID","Name","Category","Price","Weight"):
        table.heading(col, text=col)
        table.column(col, width=100)

    load_items_table(table)
