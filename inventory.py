class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
     return f"{self.name} | {self.quantity} | ${self.price:.2f}"
    
                    
class Inventory:
    def __init__(self):
        self.store = []
        
    def menu(self):
        print("=== Inventory Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Show Inventory")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Search Item")
        print("8. Exit")        

    def add_item(self, item):
        self.store.append(item)
        
    def remove_item(self, name):
        for index, item in enumerate(self.store):
            if item.name == name:
                del self.store[index]
                break
            
    def update_item(self, name, quantity=None, price=None):
        for index, item in enumerate(self.store):
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                break
    
    def show_inventory(self):
        if not self.store:
            print("Inventory is empty.")
        else:
            print("current Inventory:")
            for item in self.store:
                print(item)
                
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for item in self.store:
                file.write(f"{item.name},{item.price},{item.quantity}\n")
        
                                
    def load_from_file(self, filename):
        self.store.clear()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.add_item(Item(name, float(price), int(quantity)))
        except FileNotFoundError:
            print(f"File {filename} not found.")
            
# Inventory Management System
inv = Inventory()
if __name__ == "__main__":    
    while True: 
        inv.menu()
        user_input = input("Choose an option (1-8) 🦋: ")
    
        match user_input:
            case "1":
                name = input("Enter item name: ")
                prc_input = input("price (or blank to skip): ")
                price = float(prc_input) if prc_input else None
                qty_input = input("quantity (or blank to skip): ")
                quantity = int(qty_input) if qty_input else None
                inv.add_item(Item(name, price, quantity))
                input("\nPress Enter to return to the menu...")
                
            case "2":
                name = input("Enter item name to remove: ")
                inv.remove_item(name)
                input("\nPress Enter to return to the menu...")
                
            case "3":
                name = input("Enter item name to update: ")
                prc_input = input("price (or blank to skip): ")
                price = float(prc_input) if prc_input else None
                qty_input = input("quantity (or blank to skip): ")
                quantity = int(qty_input) if qty_input else None
                inv.update_item(name, quantity if quantity else None, price if price else None)
                input("\nPress Enter to return to the menu...")
                
            case "4":
                inv.show_inventory()
                input("\nPress Enter to return to the menu...")
                
            case "5":
                filename = input("Enter filename to save inventory: ")
                inv.save_to_file(filename)
                
            case "6":
                filename = input("Enter filename to load inventory: ")
                inv.load_from_file(filename)
                
            case "7":
                name = input("Enter item name to search: ")
                for item in inv.store:
                    if item.name == name:
                        print(item)
                        break
                else:
                    print(f"Item {name} not found.")
            case "8":
                print("Exiting the program.")
                exit()
        print("\n")
            
            
            
# inv.add_item(Item("Apple", 2.5, 10))    
# inv.add_item(Item("Banana", 1.0, 5))
# # inv.update_item("Banana", quantity=8)
# # inv.update_item("Apple", price=3.99)
# # 

# # Create new inventory
# inv.add_item(Item("Eggs", 2.5, 12))
# inv.add_item(Item("Juice", 3.75, 4))

# 
# 

# # New inventory
# 
# 





# inv.remove_item("Banana")
            