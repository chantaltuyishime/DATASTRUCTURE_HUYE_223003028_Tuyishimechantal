
attendees = [input("Enter the name of an attendee: ") 
for _ in range(int(input("Enter the number of attendees: ")))]


print("\nPeople who attended the meeting:", attendees)


attendees.append(input("\nEnter the name of the new attendee: "))


print("Updated list of attendees:", attendees)
