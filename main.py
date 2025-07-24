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
    print("\n---Add Resource---\n")
    title = input("Enter title: ")
    category = input("Enter category: ")
    total_quantity = input("Enter total quantity: ")
    
    new_resource = {
        "id": 1,
        "title": title,
        "category": category,
        "total_quantity": total_quantity,
        "available_quantity": total_quantity,
        "borrowed_by": []
    }
    
    RESOURCES.append(new_resource)
    print(f"Resource '{title}' added successfully with ID {1}")
   
def view_resources():
   """
   Displays all resources
   """
   print("ID    Title       Category        TOTAL QTY   AVAILABLE QTY       BORROWERS")
   # We will have to iterate/loop over the dictionaries in the RESOURCES[]
   for resource in RESOURCES:
   # And on each iteration, we display the dictionary/reource details for that resource item
       print(f"{resource["id"]}   {resource["title"]}       {resource["category"]}      {resource["total_quantity"]}    {resource["available_quantity"]}        {resource["borrowed_by"]}")
   
    
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
    print("\n\n****RESOURCE MANAGEMENT SYSTEM****\n")
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
        user_choice = input("\nEnter an option >> ")
        
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