from datetime import datetime
import json
class ExpenseTracker:

    def add_expense(self,amount,category,description,unique_id):
        today = datetime.today().strftime("%Y-%m-%d")
        if isinstance(amount, int) and not isinstance(amount, bool):
            if amount > 0:
                self.amount = amount
                if isinstance(category,str):
                  if category.strip() != "":
                    self.category = category
                    if isinstance(description,str):
                      if description.strip() != "":
                        self.description = description
                        self.unique_id = unique_id
                        try:
                            with open("expense.json","r")as f1:
                                data = json.load(f1)
                                if data != "":
                                    id_exists_checker = 0
                                    read_existing_data = []
                                    for i in data:
                                        read_existing_data.append(i)
                                        if i['id'] == self.unique_id:
                                            id_exists_checker += 1
                                    if id_exists_checker == 0:
                                        temp1 = {
                                            "id": self.unique_id,
                                            "date": today,
                                            "amount": self.amount,
                                            "category": self.category,
                                            "description": self.description
                                        }
                                        read_existing_data.append(temp1)
                                        with open("expense.json","w")as f2:
                                            json.dump(read_existing_data,f2,indent=4)
                                    else:
                                        print("expense ID already exists")
                                else:
                                    temp2 = [{
                                                "id": self.unique_id,
                                                "date": today,
                                                "amount": self.amount,
                                                "category": self.category,
                                                "description": self.description
                                            }]
                                    with open("expense.json","w")as f2:
                                        json.dump(temp2,f2,indent=4)

                        except FileNotFoundError:
                            temp2 = [{
                                    "id": self.unique_id,
                                    "date": today,
                                    "amount": self.amount,
                                    "category": self.category,
                                    "description": self.description
                                }]
                            with open("expense.json","w")as f2:
                                json.dump(temp2,f2,indent=4)

                        except json.JSONDecodeError:
                            temp2 = [{
                                    "id": self.unique_id,
                                    "date": today,
                                    "amount": self.amount,
                                    "category": self.category,
                                    "description": self.description
                                }]
                            with open("expense.json","w")as f2:
                                json.dump(temp2,f2,indent=4)


                    else:
                        print("Description can't be empty")
                        return
                else:
                    print("Category can't be empty")   
                    return        
            else:
                print("Amount must be greater than 0")  
                return  
        else:
            print("Amount must be an integer")   
            return
         
    def view_expense(self):
        try:
            with open("expense.json","r")as f:
                data = json.load(f)
                for i in data:
                    print(i)
                
        except FileNotFoundError:
            print("File doesn't exists")

        except json.JSONDecodeError:
            print("Invalid json")

    def delete_expense(self,unique_id):
        self.unique_id = unique_id
        try:
            with open("expense.json","r")as f:
                data = json.load(f)
                temp = []
                exist = 0
                for i in data:
                    if i['id'] != self.unique_id:
                        temp.append(i)
                    else:
                        exist += 1
            if exist >= 1:
                with open("expense.json","w")as f:
                    json.dump(temp,f,indent=4)
            else:
                print("No matching id exists")

        except FileNotFoundError:
            print("File doesn't exists")
        except json.JSONDecodeError:
            print("Invalid json")

    def summary(self):
        try:
            with open("expense.json","r")as f:
                data = json.load(f)
                total_spending = 0
                spending_by_category = {}
                highest_value_expense = None
                for i in data:
                    total_spending += i['amount']
                    if i['category'] not in spending_by_category:
                        spending_by_category[i['category']] = i['amount']
                    else:
                        spending_by_category[i['category']] += i['amount']
                    if highest_value_expense is None:
                        highest_value_expense = i
                    else:
                        if highest_value_expense['amount'] < i['amount']:
                            highest_value_expense = i
            summary = {
                "total_spending": total_spending,
                "spending_by_category": spending_by_category,
                "highest_value_expense": highest_value_expense
            }
            return summary
        except FileNotFoundError:
            print("File doesn't exists")
        except json.JSONDecodeError:
            return {
                "total_spending": 0,
                "spending_by_category": {},
                "highest_value_expense": None
            }

test = ExpenseTracker()
while True:
    print('''
1. Add expense
2. View expense
3. Delete expense
4. Summary
5. Exit
''')
    try:
        user_input = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    if user_input == 1:
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        unique_id = int(input("Enter id: "))
        test.add_expense(amount,category,description,unique_id)
    elif user_input == 2:
        test.view_expense()
    elif user_input == 3:
        unique_id = int(input("Enter id: "))
        test.delete_expense(unique_id)
    elif user_input == 4:
        print(test.summary())
    elif user_input == 5:
        break
    else:
        print("Invalid Input")



