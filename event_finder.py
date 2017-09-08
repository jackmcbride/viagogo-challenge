import random
import itertools

def generate_events():
    #Randomly generate number of events between 1 and 50. The upper bound can be specified as any number (within reason!).
    e_number = random.randint(1, 50)
    #Make 2D array for events
    events = [[0]* e_number for i in range(e_number)]
    for i in range(0, e_number):
        #Randomly generate x,y co-ordinates between -10 and 10
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        #Randomly generate ticket price and number of tickets
        tickets = generate_tickets()
        events[i] = x,y,tickets
    #Sort events and remove duplicates. Each co-ordinate holds a maximum of one event.
    events.sort()
    list(events for events,_ in itertools.groupby(events))
    return events

#Generate tickets
def generate_tickets():
    #Randomly generate number of tickets, between 0 and 1000
    t_number = random.randint(0, 1000)
    #Make 2D array for tickets
    tickets = [[0]* t_number for i in range(t_number)]
    for i in range(0, t_number):
        #Generate a random price between 0 and 100 to 2 d.p.
        t_price = round(random.uniform(1, 100), 2)
        #Add the ticket price and number into the array
        tickets[i] = t_price, t_number
    return tickets

#Compute the Manhattan distance between two pairs of co-ordinates.
def manhattan_distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x2 - x1) + abs(y2 - y1)

#Handle user interface
def find_events():
    #Prompt user for coordinates
    user_coords = input("\nPlease Input Co-ordinates: ")
    #Check for non numerical values. If detected, print an error message and re-prompt user for co-ordinates.
    if not(user_coords.replace(","," ").replace(" ", "").replace("-", "").isdigit()) or (len(user_coords) < 2):
        print("\nCo-ordinates types must be 2 integers, -10 to +10 inclusive.")
        return find_events()

    #Store co-ordinates in an integer list.
    user_coords = list(map(int, user_coords.split(",")))

    #Check if Co-ordinates are outside of 'world' bounds. If detect, print an error message and re-prompt user for co-ordinates.
    if (-10 > user_coords[0] or user_coords[0] > 10) or (-10 > user_coords[1] or user_coords[1] > 10):
        print("\nCo-ordinates out of bounds. Each co-ordinate value must be between -10 and +10 inclusive.")
        return find_events()

    #Closest events message.
    print("\nClosest Events to (%d,%d):" % (user_coords[0], user_coords[1]) + "\n")

    #Return user co-ordinates.
    return user_coords
    

#Randomly seed event data during program startup.
def seed_events(user_coords, events, tickets):
    #Empty list for event information.
    event_info = []
    for i in range(0, len(events)):
        #Populate a list with the event and ticket data.
        event_info.append((str("0" * (3 - len(str(i+1))) + str(i+1)), manhattan_distance(user_coords, events[i][:2]), events[i][2][0][0], events[i][2][1][1]))
    #Sort the events by Manhattan distance value.
    event_info = sorted(event_info, key=lambda x : x[1])  
    #Return the five closest events.
    return event_info[:5]

#Main function.
def main():
    #Generate event data.
    events = generate_events()
    #Generate ticket data.
    tickets = generate_tickets()
    #Allow user to query program with different sets of co-ordinates.
    while True:
        #Get user co-ordinates.
        user_coords = find_events()
        #Get the closest events to user.
        closest_events = seed_events(user_coords, events, tickets)

        #Print list of events to user.
        if closest_events is not None:
            for event in closest_events:
                if event is not None:
                    print("Event " + str(event[0]) + " - " + "$" + str(event[2]) + ", # of tickets: " + str(event[3]) + ", Distance " + str(event[1]) + "\n")


if __name__ == "__main__": main()