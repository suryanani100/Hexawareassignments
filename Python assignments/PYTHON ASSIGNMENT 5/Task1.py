
class Task1:
    def __init__(self):
        print("Enter 3 tasks")

    def checkTicketAvailability(self):
        print("What are the available tickets and Number of required tickets")
        availableTickets = int(input())
        noOfTickets = int(input())
        if availableTickets > noOfTickets:
            print("The tickets are available")
        else:
            print("The tickets are not available.Try again later.")

    def calculateTotalCost(self):
        ticketType = input("What is ticket type?")
        noOfTickets = int(input("What are number of tickets?"))
        base = 0
        if ticketType == "Silver":
            base = 50
        elif ticketType == "Gold":
            base = 100
        elif ticketType == "Diamond":
            base = 150
        print(f"Total cost of tickets are {base * noOfTickets}")

    def looping(self):
        ticketType = input("what is ticket type?")
        while ticketType != "Exit":
            noOfTickets = int(input("No of tickets : "))
            base = 0
            if ticketType == "Silver":
                base = 50
            elif ticketType == "Gold":
                base = 100
            elif ticketType == "Diamond":
                base = 150
            print(f"Total cost of tickets will be {base * noOfTickets}")
            ticketType = input("Enter ticket type : ")
