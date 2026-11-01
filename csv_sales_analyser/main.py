import csv
import os
from datetime import datetime

class SalesAnalyzer:
    def __init__(self):
        self.sales = {}

    def load_sales(self):
        try:
            with open("sales.csv","r")as f:
                data = csv.DictReader(f)
                temp_dict = {}
                csv_header = ['transaction_id','date','product','quantity','unit_price']
                if csv_header == data.fieldnames:
                    for i in data:
                        if None in i or None in i.values():
                            print("Invalid CSV row: missing or extra fields")
                            return
                        try:
                            id = int(i['transaction_id'])
                            if str(id) not in temp_dict:
                                if id > 0:
                                    try:
                                        qty = int(i['quantity'])
                                        if qty > 0:
                                            try:
                                                up = int(i['unit_price'])
                                                if up >= 0:
                                                    if i['product'].strip() != "":
                                                        try:
                                                            date = datetime.strptime(i['date'],"%Y-%m-%d")  
                                                            temp_dict[str(id)] = {
                                                                    "date": i['date'],
                                                                    "product": i['product'],
                                                                    "quantity": qty,
                                                                    "unit_price": up
                                                                }
                                                        except ValueError:
                                                            print("Invalid date")
                                                            return
                                                    else:
                                                        print("product shouldn't be empty")
                                                        return
                                                else:
                                                    print("unit price shouldn't be negative")
                                                    return
                                            except ValueError:
                                                print("unit price must be integer")
                                                return
                                        else:
                                            print("quantity must be positive")
                                            return
                                    except ValueError:
                                        print("Quantity must be integer")
                                        return
                                else:
                                    print("Id must be positive")
                                    return
                            else:
                                print("Duplicate transaction ID")
                                return
                        except ValueError:
                            print("ID must be integer")
                            return
                    self.sales = temp_dict
                else:
                    print("Invalid CSV header")        

        except FileNotFoundError:
            print("FileNotFoundError triggered")
            with open("sales.csv","w")as f:
                header = ["transaction_id","date","product","quantity","unit_price"]
                temp = csv.DictWriter(f,header)
                csv.DictWriter.writeheader(temp)    

    def add_sale(self):
        try:
            transaction_id = int(input("Enter transaction ID: "))
            if transaction_id > 0:
                if str(transaction_id) not in self.sales:
                    date = input("Enter date: ")
                    try:
                        final_date = datetime.strptime(date,"%Y-%m-%d")
                        product = input("Enter product: ")
                        if product.strip() != "":
                            try:
                                quantity = int(input("Enter quantity: "))
                                if quantity > 0:
                                    try:
                                        unit_price = int(input("Enter unit_price: "))
                                        if unit_price >= 0:
                                            self.sales[str(transaction_id)] = {
                                                "date": date,
                                                "product": product,
                                                "quantity": quantity,
                                                "unit_price": unit_price
                                            }
                                            self.save_sales()
                                        else:
                                            print("unit_price can't be negative")
                                    except ValueError:
                                        print("unit_price must be integer")
                                else:
                                    print("quantity must be positive")
                            except ValueError:
                                print("Quantity must be integer")
                        else:
                            print("Product must be non-empty")
                    except ValueError:
                        print("Invalid date")
                else:
                    print("ID already exists")
            else:
                print("Transaction ID must be positive")
        except ValueError:
            print("Transaction id must be int")
        
    def save_sales(self):
        with open("sales.csv","w",newline="")as f:
            data = csv.DictWriter(f,fieldnames=["transaction_id","date","product","quantity","unit_price"])
            data.writeheader()
            for key,value in self.sales.items():
                temp_dict = {
                    "transaction_id": key,
                    "date": value['date'],
                    "product": value['product'],
                    "quantity": value['quantity'],
                    "unit_price": value['unit_price']
                }
                data.writerow(temp_dict)

    def view_all_sales(self):
        if self.sales != {}:
            for key,value in self.sales.items():
                temp = {
                    "transaction_id": key,
                    "date": value['date'],
                    "product": value['product'],
                    "quantity": value['quantity'],
                    "unit_price": value['unit_price']
                }
                print(temp)
        else:
            print("No sales records found")

    def search_sale(self):
        try:
            transaction_id = int(input("Enter transaction id: "))
            if str(transaction_id) in self.sales:
                print(self.sales[str(transaction_id)])
            else:
                print("Sale not found")
        except ValueError:
            print("Transaction id must be integer")

    def summary(self):
        if self.sales != {}:
            total_transactions = 0
            total_quantity = 0
            total_revenue = 0
            product_wise_revenue = {}
            for key,value in self.sales.items():
                total_transactions += 1
                total_quantity += value['quantity']
                total_revenue += value['quantity']*value['unit_price']
                if value['product'] not in product_wise_revenue:
                    product_wise_revenue[value['product']] = value['quantity']*value['unit_price']
                else:
                    product_wise_revenue[value['product']] += value['quantity']*value['unit_price']

            highest = max(
                product_wise_revenue.items(),
                key=lambda x: x[1]
            )
            highest_list = []
            for product,revenue in product_wise_revenue.items():
                if revenue == highest[1]:
                    highest_list.append(product)

            print(f"Total transactions: {total_transactions}")
            print(f"Total units sold: {total_quantity}")
            print(f"Total revenue: {total_revenue}")
            print(f"Revenue by product: {product_wise_revenue}")
            print(f"Highest-revenue products: {highest_list}")
        else:
            print("No sales records found")

sale = SalesAnalyzer()
sale.load_sales()
print("==== CSV SALES ANALYZER ====")
while True:
    print('''
1. Add Sale
2. View All Sales
3. Search Sale
4. Generate Sales summary
5. Exit
''')
    try:
        user_input = int(input("Enter choice: "))
        if user_input == 1:
            sale.add_sale()
        elif user_input == 2:
            sale.view_all_sales()
        elif user_input == 3:
            sale.search_sale()
        elif user_input == 4:
            sale.summary()
        elif user_input == 5:
            break
        else:
            print("Invalid option")
    except ValueError:
        print("Input should be integer")








