from collections import deque

# Stack for undoing bookings
undo_stack = []

# Queue for ticket requests
ticket_queue = deque()

# List to manage flight schedules
flight_schedule = []

# Function to add a booking
def booking(booking):
    undo_stack.append(booking)
    print(f"Booking are: {booking}")

# Function to undo a booking
def undo_booking():
    if undo_stack:
        undone_booking = undo_stack.pop()
        
        print(f"Booking undone: {undone_booking}")
    else:
        print("No bookings to undo")

# Function to request a ticket
def request_ticket(request):
    ticket_queue.append(request)
    print(f"Ticket request : {request}")

# Function to process a ticket request
def process_ticket_request():
    if ticket_queue:
        processed_request = ticket_queue.popleft()
        print(f"Ticket request processed: {processed_request}")
    else:
        print("No ticket requests to process")

# Function to add a flight to the schedule
def flights(flight):
    flight_schedule.append(flight)
    print(f"Flight schedule added are: {flight}")

# Function to display flight schedule
def display_flights():
    if flight_schedule:
        print("Flight Schedule:")
        for flight in flight_schedule:
            print(flight)
    else:
        print("No flights scheduled")

# Example usage
booking("Multi-City Flight Ticket")
booking("One-Way Flight Ticket")
booking("Toronto to London")

undo_booking()
undo_booking()

request_ticket("International Flight Ticket")
request_ticket(" Domestic Flight Ticket ")

process_ticket_request()
process_ticket_request()

flights(" International Flight Ticket ")
flights(" Domestic Flight Ticket ")
flights("multi_city flight ticket")
display_flights()
