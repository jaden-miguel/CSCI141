# Name: Jaden Miguel
# Date: 14 May 2019
# Purpose: Lab 6 - Square Footage program - will prompt a user for number of rooms
# will then ask for parameters for those rooms, then print the total square footage!
# uses an accumulator to hold running values!

def prompt_user(question, input_type):
    """
    Prompts the user with a question and returns the response in the specified type.
    """
    response = input(f"What is the {question}? ")
    return int(response) if input_type == "integer" else response

def room_square_feet(room_number):
    """
    Determines the square footage of a room based on its shape.
    """
    room_shape = prompt_user(f"shape of room {room_number} (square or rectangle)", "string")
    if room_shape == "rectangle":
        length = prompt_user("length of the room", "integer")
        width = prompt_user("width of the room", "integer")
        return length * width
    else: # Assuming the only other shape is square
        side = prompt_user("side length of the square room", "integer")
        return side * side

def main():
    """
    Main function to calculate the total square footage of all rooms.
    """
    num_rooms = prompt_user("number of rooms", "integer")
    total_square_footage = 0
    for room_number in range(1, num_rooms + 1):
        total_square_footage += room_square_feet(room_number)
    print("Total square footage:", total_square_footage)

if __name__ == "__main__":
    main()
