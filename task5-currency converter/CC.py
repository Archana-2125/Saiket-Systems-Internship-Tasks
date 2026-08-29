import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_rates(base_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["result"] != "success":
            raise Exception ("Unable to get exchange rates")

        return data["rates"]

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Connection Error",
            "Unable to connect to the exchange rate API."
        )
        return None

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None



def convert_currency():
    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            messagebox.showerror(
                "Invalid Amount",
                "Please enter an amount greater than 0."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )
        return

    from_currency = from_currency_box.get()
    to_currency = to_currency_box.get()

    if not from_currency or not to_currency:
        messagebox.showerror(
            "Missing Information",
            "Please select both currencies."
        )
        return

    rates = get_rates(from_currency)

    if rates is None:
        return

    if to_currency not in rates:
        messagebox.showerror(
            "Error",
            "Exchange rate not available."
        )
        return

    rate = rates[to_currency]
    converted_amount = amount * rate

    result_label.config(
        text=f"{amount:.2f} {from_currency} = "
             f"{converted_amount:.2f} {to_currency}"
    )



def clear_fields():
    amount_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here")



root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.resizable(False, False)



title_label = tk.Label(
    root,
    text="Currency Converter",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)



amount_label = tk.Label(
    root,
    text="Enter Amount:",
    font=("Arial", 12)
)
amount_label.pack()

amount_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
amount_entry.pack(pady=8)

currencies = [
    "USD",
    "INR",
    "EUR",
    "GBP",
    "JPY",
    "AUD",
    "CAD",
    "SGD",
    "AED",
    "CNY"
]

from_label = tk.Label(
    root,
    text="From Currency:",
    font=("Arial", 12)
)
from_label.pack()

from_currency_box = ttk.Combobox(
    root,
    values=currencies,
    state="readonly",
    font=("Arial", 12)
)
from_currency_box.pack(pady=5)
from_currency_box.set("USD")


to_label = tk.Label(
    root,
    text="To Currency:",
    font=("Arial", 12)
)
to_label.pack()

to_currency_box = ttk.Combobox(
    root,
    values=currencies,
    state="readonly",
    font=("Arial", 12)
)
to_currency_box.pack(pady=5)
to_currency_box.set("INR")



convert_button = tk.Button(
    root,
    text="Convert",
    command=convert_currency,
    font=("Arial", 12, "bold"),
    width=15
)
convert_button.pack(pady=15)



clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    font=("Arial", 11),
    width=15
)
clear_button.pack()



result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    wraplength=400
)
result_label.pack(pady=25)



root.mainloop()