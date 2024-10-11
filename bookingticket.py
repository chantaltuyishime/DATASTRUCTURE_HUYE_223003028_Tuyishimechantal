from collections import deque

# Stack for undoing bookings
class BookingStack:
    def __init__(self):
        self.stack = []

    def book_flight(self, booking):
        self.stack.append(booking)
        print(f"Booking confirmed: {booking}")

    def undo_booking(self):
        if self.stack:
            canceled_booking = self.stack.pop()
            print(f"Booking undone: {canceled_booking}")
        else:
            print("No bookings to undo.")


# Queue for processing ticket requests
class TicketQueue:
    def __init__(self):
        self.queue = deque()

    def request_ticket(self, request):
        self.queue.append(request)
        print(f"Ticket request added: {request}")

    def process_ticket(self):
        if self.queue:
            ticket = self.queue.popleft()
            print(f"Processing ticket request: {ticket}")
        else:
            print("No ticket requests to process.")


# List to manage flight schedules
class FlightSchedule:
    def __init__(self):
        self.schedule = []

    def add_flight(self, flight):
        self.schedule.append(flight)
        print(f"Flight added to schedule: {flight}")

    def show_schedule(self):
        if self.schedule:
            print("\nAvailable Flights:")
            for idx, flight in enumerate(self.schedule, 1):
                print(f"{idx}. {flight}")
        else:
            print("No flights available.")


# Main function to demonstrate the system
def main():
    booking_stack = BookingStack()
    ticket_queue = TicketQueue()
    flight_schedule = FlightSchedule()

    while True:
        print("\n--- Flight Booking System ---")
        print("1. Add Flight to Schedule")
        print("2. Show Available Flights")
        print("3. Request Ticket")
        print("4. Process Ticket Request")
        print("5. Book a Flight")
        print("6. Undo Last Booking")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            flight = input("Enter flight details : ")
            flight_schedule.add_flight(flight)

        elif choice == "2":
            flight_schedule.show_schedule()

        elif choice == "3":
            passenger_name = input("Enter your name: ")
            flight_choice = input("Enter flight details for ticket request: ")
            ticket_queue.request_ticket(f"{passenger_name} - {flight_choice}")

        elif choice == "4":
            ticket_queue.process_ticket()

        elif choice == "5":
            passenger_name = input("Enter your name: ")
            flight_choice = input("Enter flight details to book: ")
            booking_stack.book_flight(f"{passenger_name} - {flight_choice}")

        elif choice == "6":
            booking_stack.undo_booking()

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
