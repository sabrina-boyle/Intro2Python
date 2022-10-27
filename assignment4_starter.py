# sabsing
# October 22, 2021
#
# This is my Programming Assignment 4 where I used a while loop and dictionaries to analyze orders of parts from Midwest Widget Co


supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'


# Your code goes here
import json
supplier_data = json.loads(supplier_data)

print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity")
print(" ")

print("Parts for order are:")
for data in supplier_data['parts']:
    print(data)
print(" ")

selected_part = ""
available_quantity = 0
available_parts = supplier_data['parts']
not_available_parts = []
order = {}
while 'quit' not in selected_part:## loop until quit
    selected_part = input("Please enter in a part name, or quit to exit: ") ## user inputs part
    if selected_part in supplier_data['parts']:
        selected_quantity = int(input("Please enter in a quantity to order: ")) ## user inputs quantity
        available_quantity = supplier_data[selected_part]['quantity']
        if available_quantity != 0: ## varify if available
            if selected_quantity <= available_quantity: ## varify if quantity available
                supplier_data[selected_part]['quantity'] -= selected_quantity
                if selected_part in order:
                    order[selected_part] += selected_quantity
                else:
                    order[selected_part] = selected_quantity
            else:
                print("Error, only", available_quantity, "of", selected_part, "are available!")
        else:
            available_parts.remove(selected_part) 
            not_available_parts += [selected_part]
            print("Error, only", available_quantity, "of", selected_part, "are available!")
            continue
    elif selected_part in not_available_parts:
        print("Error, only", available_quantity, "of", selected_part, "are available!")
    elif 'quit' not in selected_part:
        print("Error, part does not exist, try again")
    else:
        break

print(" ")
print("Your order")
total_cost = 0
for data in order:
    part_cost = order[data]*supplier_data[data]['price']
    print(f"{data} - {order[data]} @ {supplier_data[data]['price']} = ${part_cost}")
    total_cost += part_cost

print(f"Total: ${total_cost}")
print("Thank you for using the parts ordering system!")
    
##print order
        
