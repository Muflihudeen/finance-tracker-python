import json
transactions = []


while True:
    print("\n=== Financial Tracker ===")
    print('1. Add Income')
    print('2. Add Expenses')
    print('3. View Records')
    print('4. Show Balance')
    print('5. Delete Transaction')
    print('6. Exit')

    choice = input('Enter your choice: ')
    if choice == "1":
        description = input("Enter income description: ")
        category = input("Enter category: ")
        amount = float(input("Enter income amount: "))

        transactions.append({
            "type": "income",
            "description": description,
            "category": category,
            "amount": amount 
        })
        print('Income added successfully!')

    elif choice == "2":
        description = input("Enter expense description: ")
        category = input("Enter category: ")
        amount = float(input("Enter expense amount: "))

        transactions.append({
            "type": "expense",
            "description": description,
            "category": category,
            "amount": amount
        })

        print('Expense added successfully!')

    elif choice == "3":
        if len(transactions) == 0:
            print('No transactions recorded yet.')  
        else:
            print("\nTYPE | CATEGORY | DESCRIPTION | AMOUNT")
            print("--------------------------------------")
            for t in transactions:
             print(f"{t['type']} | {t['category']} | {t['description']} | ₦{t['amount']}")

    elif choice == "4":
        balance = 0 
        for t in transactions:
            if t['type'] == "income":
                balance += t['amount']
            else: 
                balance -= t['amount']

        print('Your balance is: ₦', balance)

    elif choice == "5":
       if len(transactions) == 0:
        print("No transactions to delete")
       else:
           for i, t in enumerate(transactions):
            print(f"{i + 1}. {t['type']} | {t['description']} | ₦{t['amount']}")

           index = int(input("Enter number to delete: ")) - 1

           if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            print("Deleted:", removed["description"])
           else:
            print("Invalid number")    

    elif choice == "6":
        with open('finance_data.json', 'w') as f:
            json.dump(transactions, f, )
        
        print('Data saved. Exiting...')
        break

    else: 
        print('Invalid choice')                 