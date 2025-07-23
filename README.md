## Savana International Academy Educational Resource Management System

### Project Overview
This project is a command-line application developed as part of the Savana International Academy's internship programme. The goal of this program is to create a simple, in-memory/file-based system for managing the inventory of educational resources, such as books and other materials.

The application allows users to perform basic library management tasks, including adding new resources, viewing the current inventory, and tracking the borrowing and return of items. It serves as a foundational project to practice core Python concepts like data structures (lists and dictionaries), functions, and user input handling.

### Features
1. Add New Resource: Add a new educational resource to the inventory with details like title, author, and quantity.

2. View All Resources: Display a formatted list of all resources currently in the system, including their availability.

3. Search Resources: Find specific resources by searching for a keyword in their title.

4. Borrow Resource: Mark a resource as borrowed by a student, which decrements its available quantity.

5. Return Resource: Mark a resource as returned, which increments its available quantity.

6. Check Availability: Quickly check the current availability status of a specific resource by its unique ID.

7. Persistent Data: All resource data is automatically saved to and loaded from a file (resources.csv), ensuring your inventory is not lost when the program closes.