import tkinter as tk
from scrapy_handler import start_scrapy_process

vars = []


def update_price_label(prices):
    price_ranges = [(i * 50, (i + 1) * 50)
                    for i in range(int(max(prices)) // 50 + 1)]

    # Her fiyatı uygun aralığa yerleştirin
    price_counts = {price_range[0]: 0 for price_range in price_ranges}
    for price in prices:
        for price_range in price_ranges:
            if price >= price_range[0] and price < price_range[1]:
                price_counts[price_range[0]] += 1
                break

    # En çok tercih edilen fiyat aralığını bulun
    most_common_price_range = max(price_counts, key=price_counts.get)
    min_price = most_common_price_range
    max_price = most_common_price_range + 50

    price_label.config(text=f"Most common price range: {
                       min_price} TL - {max_price} TL")


def show_selection():
    category = vars[0].get()
    brand = vars[1].get()

    start_scrapy_process(category, brand, update_price_label)


def createFilter(title, rowNum, options):
    label = tk.Label(a_frame, text=title + ":", bg="#112233", fg="white")
    label.grid(row=rowNum, column=0, padx=10, pady=5, sticky="w")

    var = tk.StringVar(value=options[0])
    vars.append(var)
    dropdown = tk.OptionMenu(a_frame, var, *options)
    dropdown.grid(row=rowNum, column=1, padx=10, pady=5, sticky="ew")


root = tk.Tk()
root.title("Panel Application")
root.configure(background="#112233")
root.geometry("900x400")

# A Panel
a_frame = tk.Frame(root, bg="#112233")
a_frame.pack(pady=20)

categories = ["tişört", "pantolon", "elbise", "etek", "gömlek"]
createFilter("Category", 1, categories)

brands = ["Pull&Bear", "Defacto", "Twist",
          "Calvin Klein", "LC Waikiki", "Network"]
createFilter("Brand", 2, brands)

# B Panel
b_frame = tk.Frame(root, bg="#112233")
b_frame.pack(pady=20)

b_button = tk.Button(b_frame, text="Seçimleri Göster", command=show_selection)
b_button.pack(padx=10, pady=10)

b_label = tk.Label(b_frame, text="", bg="#112233", fg="white")
b_label.pack(padx=10, pady=10)

price_label = tk.Label(b_frame, text="", bg="#112233", fg="white")
price_label.pack(padx=10, pady=10)

root.mainloop()
