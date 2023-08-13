import random
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="QWE098*123asd",
    database="ticket_system"
)
cursor = db.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS tickets (
    ticket_no INT PRIMARY KEY,
    name VARCHAR(100),
    source VARCHAR(100),
    destination VARCHAR(100),
    coach_type VARCHAR(20),
    seat_no INT
)
"""
cursor.execute(create_table_query)
db.commit()

def generate_ticket_number():
    return random.randint(10000, 99999)

def reserve_ticket():
    name = input("Enter your name: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    coach_type = input("Enter coach type: ")
    seat_no = random.randint(1, 100)
    ticket_no = generate_ticket_number()

    insert_query = "INSERT INTO tickets (ticket_no, name, source, destination, coach_type, seat_no) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (ticket_no, name, source, destination, coach_type, seat_no)
    cursor.execute(insert_query, values)
    db.commit()

    print("Ticket reserved successfully!")
    print(f"Your ticket number is: {ticket_no}")

def get_ticket_details(ticket_no):
    select_query = "SELECT * FROM tickets WHERE ticket_no = %s"
    cursor.execute(select_query, (ticket_no,))
    ticket = cursor.fetchone()

    if ticket:
        print("Ticket Details:")
        print(f"Ticket Number: {ticket[0]}")
        print(f"Name: {ticket[1]}")
        print(f"Source: {ticket[2]}")
        print(f"Destination: {ticket[3]}")
        print(f"Coach Type: {ticket[4]}")
        print(f"Seat Number: {ticket[5]}")
    else:
        print("Ticket not found.")
while True:
    print("\n1. Reserve a Ticket")
    print("2. Get Ticket Details")
    print("3. Exit")
    choice = int(input("Select an option: "))

    if choice == 1:
        reserve_ticket()
    elif choice == 2:
        ticket_no = int(input("Enter your ticket number: "))
        get_ticket_details(ticket_no)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
cursor.close()
db.close()
