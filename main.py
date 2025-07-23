# This is a Python program to manage the inventory of
# educational resources

# array -> Data structure for storing some list of values
RESOURCES = [] 


# Program functions

def add_resource():
    """
    Prompts for new resources and adds the resource 
    to the RESOURCES list 
    """
    # Python concepts: Python Dictionaries, Lists
    
    # 1. Prompt the user for:
    # title, category, total quantity
    title = input("Enter title: ")
    category = input("Enter category: ")
    total_quantity = input("Enter total quantity: ")
    
    # 2. Compose the new resource in a dictionary
    new_resource = {
        "id": 1,
        "title": title,
        "category": category,
        "total_quantity": total_quantity,
        "available_quantity": total_quantity,
        "borrowed_by": []
    }
    
    # 3. Insert the newly created resource(the dictionary) into
    # RESOURCES = []
    RESOURCES.append(new_resource)
    print(f"Resource '{title}' added successfully with ID {1}")
    
def view_resources():
   """
   Displays all resources
   """
   print("View resources")
    
def borrow_resource():
    print("Borrow resource")

def return_resource():
    print("Return resource")

def check_availability():
    print("Check resource") 

def load_data():
    pass

def save_inventory(resources_list):
    pass

def search_resources():
    print("Search resource")

def menu():
    """Displays the main menu to the user"""
    print("1. Add New Resource")
    print("2. View All Resources")
    print("3. Search Resources")
    print("4. Borrow Resource")
    print("5. Return Resource")
    print("6. Check Availability")
    print("0. Exit")

def main():
    """
    The main function will act as the entry-point of our program.
    """
    while True:
        # Display menu items
        menu()

        # Get the user's choice
        user_choice = input("Enter an option >> ")
        
        # Process the user's choice
        if user_choice == "1":
            add_resource()
        elif user_choice == "2":
            view_resources()
        elif user_choice == "3":
            search_resources()
        elif user_choice == "4":
            borrow_resource()
        elif user_choice == "5":
            return_resource()
        elif user_choice == "6":
            check_availability()
        elif user_choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Please enter a valid option")
       
   
        
       
if __name__ == "__main__":
    main()