# task1 = Task1()
# task1.checkTicketAvailability()
# task1.calculateTotalCost()
# task1.looping()
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="ticketbookingsystem"
)
venue = "Harmony Hall"
cur = con.cursor()
cur.execute("select venue_id from venue where venue_name= %s", (venue,))
venue_id = cur.fetchone()

print(venue_id[0])

"""
    event = {
        "event_name" : input("What is name of event? "),
        "event_date" : input("What is the date of the event?"),
        "event_time" : input("What is Event timing?"),
        "venue_name" : input("What is name of venue?"),
        "total_seats" : int(input("what are total seats?")),
        "available_seats" : int(input("What are available seats?")),
        "ticket_price" : float(input("What is the ticket price?")),
        "event_type" : input("What is event type?")
    }
    
    booking = Booking(event)
    print(booking.getBookedNoOfTickets())
 #   first_event = Event(event)
  #  first_event.display_event_details()
"""
