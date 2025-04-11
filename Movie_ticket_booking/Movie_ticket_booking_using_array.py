import numpy as np
from string import ascii_uppercase
from typing import Final
from array import*

ROW:Final = 13
COLUMN:Final = 12
screen_size:Final = 10
# Create a proper 2D array filled with zeros
Movie_1_2D = np.zeros((ROW, COLUMN), dtype=str)
Movie_2_3D = np.zeros((ROW, COLUMN), dtype=str)
Movie_3_2D = np.zeros((ROW, COLUMN), dtype=str)
Movie_4_3D = np.zeros((ROW, COLUMN), dtype=str)
"""screen = np.zeros((screen_size), dtype=str)

for i in range(len(screen)):
    screen[i] = '='"""


def print_line(r):
    for i in range(COLUMN):
        print(f'_ ',end='')

    print()
    if(r == 0):    
        print("       210 Classic")
    elif(r == 3):
        print("      230 Classic Plus")
    elif(r == 7):
        print("        240 Prime")

def initialize_movie_halls():
    """Initialize seating arrangements for all movies"""
    for r in range(ROW):
        for c in range(COLUMN):
            if r < ROW and c == 0:
                # Set row letters in first column
                Movie_1_2D[r,c] = ascii_uppercase[r]
                Movie_2_3D[r,c] = ascii_uppercase[r]
                Movie_3_2D[r,c] = ascii_uppercase[r]
                Movie_4_3D[r,c] = ascii_uppercase[r]
            elif c == 7 or c == 1:
                # Set empty spaces for aisles
                Movie_1_2D[r,c] = ' '
                Movie_2_3D[r,c] = ' '
                Movie_3_2D[r,c] = ' '
                Movie_4_3D[r,c] = ' '
            elif c not in [0,1,7]:
                # Set seat numbers
                seat_number = str((c-2) if c > 7 else (c-1))
                Movie_1_2D[r,c] = seat_number
                Movie_2_3D[r,c] = seat_number
                Movie_3_2D[r,c] = seat_number
                Movie_4_3D[r,c] = seat_number

def show_seats(movie):
    """Display seating arrangement for selected movie"""
    print("\nS C R E E N")
    
    # Select correct movie array based on movie choice
    movie_array = {
        11: Movie_1_2D,
        12: Movie_2_3D,
        2: Movie_3_2D,
        3: Movie_4_3D
    }.get(movie, Movie_1_2D)  # Default to Movie_1_2D if invalid choice
    
    for r in range(ROW):
        # Print section dividers and titles
            
        # Print seats
        for c in range(COLUMN):
            if r in [0, 3, 7] and c == 0:
                print_line(r)
            print(movie_array[r,c], end=' ')
        print()  # New line after each row

def show_movies():
    while True:
        try:
            movie = int(input("select movie:\n1. Movie 'A'[(2D,Hindi)(3D,English)]\n2.Movie 'B'(2D,English)\n3. Movie 'c'(3D,English)\n4. Go Back\nEnter the movie number: "))
            print()
            
            if movie == 1:
                movie *= 10
                choice = int(input("Movie 'A'\n1. 2D, hindi\n2. 3D, English\n3. Go back\nEnter your choice: "))
                print()
                movie += choice
                
                if movie == 13:  # Go back option
                    continue
                elif movie not in [11, 12]:  # Invalid sub-choice
                    print("Invalid choice for Movie A!")
                    continue
                break
            
            elif movie in [2, 3, 4]:  # Valid direct choices
                break
            
            else:
                print("Invalid choice!! Please enter 1-4")
                continue
                
        except ValueError:
            print("Please enter a valid number")
            continue
            
    return movie

def get_seat_numbers(number_of_seats, movie):
    seats = []
    print("\nEnter seat numbers in format 'A5' (Row Letter + Seat Number)")
    print("Example: For first row seat 5, enter 'A5'")
    
    while len(seats) < number_of_seats:
        try:
            seat = input(f"Enter seat {len(seats) + 1}: ").strip().upper()
            
            # Validate format
            if len(seat) < 2:
                print("Invalid format! Use format like 'A5'")
                continue
                
            row = seat[0]
            number = seat[1:]
            
            # Validate row letter
            if not row.isalpha() or row not in ascii_uppercase[:ROW]:
                print(f"Invalid row! Please use letters A-{ascii_uppercase[ROW-1]}")
                continue
                
            # Modified seat number validation
            if not number.isdigit() or int(number) > 9:  # Changed from COLUMN-3 to 9
                print(f"Invalid seat number! Please use numbers 0-9")
                continue
                
            # Check if seat is already taken
            
            row_idx = ascii_uppercase.index(row)
            col_idx = int(number)
            if col_idx < 6:
                col_idx+= 1
            else:
                col_idx+=2

            # Check and append seats for all movie types
            if movie == 11:
                if Movie_1_2D[row_idx, col_idx] == 'X':
                    print("This seat is already booked!")
                    continue
            elif movie == 12:
                if Movie_2_3D[row_idx, col_idx] == 'X':
                    print("This seat is already booked!")
                    continue
            elif movie == 2:
                if Movie_3_2D[row_idx, col_idx] == 'X':
                    print("This seat is already booked!")
                    continue
            elif movie == 3:
                if Movie_4_3D[row_idx, col_idx] == 'X':
                    print("This seat is already booked!")
                    continue
            else:
                print("error!")
                continue
                
            # Append seat if it passed all validations
            seats.append((row_idx, col_idx))
           
        except ValueError:
            print("Invalid input! Please use format like 'A5'")
            
    return seats

def book_ticket():
    movie = show_movies()
    if movie == 4:
        return
        
    number_of_seats = int(input("Enter the number of seats to book: "))
    show_seats(movie)  # Show initial seating
    
    seats = get_seat_numbers(number_of_seats, movie)
  
    # Mark seats as booked
    movie_array = {
        11: Movie_1_2D,
        12: Movie_2_3D,
        2: Movie_3_2D,
        3: Movie_4_3D
    }.get(movie)
    
    for row_idx, col_idx in seats:
        movie_array[row_idx, col_idx] = 'X'
    
    print("\nBooking confirmed! Your seats:")
    for row_idx, col_idx in seats:
        if col_idx > 6:
            print(f"{ascii_uppercase[row_idx]}{col_idx-2}")
        else:
            print(f"{ascii_uppercase[row_idx]}{col_idx-1}")
    
    print("\nUpdated seating arrangement:")
    show_seats(movie)  # Show updated seating

def get_seat_number_to_cancle(number_of_seats, movie):
    seats = []
    while len(seats) < number_of_seats:
        try:
            seat = input(f"Enter seat {len(seats) + 1}: ").strip().upper()
            
            # Validate format
            if len(seat) < 2:
                print("Invalid format! Use format like 'A5'")
                continue
                
            row = seat[0]
            number = seat[1:]
            
            # Validate row letter
            if not row.isalpha() or row not in ascii_uppercase[:ROW]:
                print(f"Invalid row! Please use letters A-{ascii_uppercase[ROW-1]}")
                continue
                
            # Validate seat number
            if not number.isdigit() or int(number) > 9:  # Changed from COLUMN-3 to 9
                print(f"Invalid seat number! Please use numbers 0-9")
                continue
                
            # Check if seat is already taken
            
            row_idx = ascii_uppercase.index(row)
            col_idx = int(number)
            if col_idx < 6:
                col_idx+= 1
            else:
                col_idx+=2

            # Check and append seats for all movie types
            if movie == 11:
                if Movie_1_2D[row_idx, col_idx] != 'X':
                    print("This seat is not booked!")
                    continue
            elif movie == 12:
                if Movie_2_3D[row_idx, col_idx] != 'X':
                    print("This seat is not booked!")
                    continue
            elif movie == 2:
                if Movie_3_2D[row_idx, col_idx] != 'X':
                    print("This seat is not booked!")
                    continue
            elif movie == 3:
                if Movie_4_3D[row_idx, col_idx] != 'X':
                    print("This seat is not booked!")
                    continue
            else:
                print("error!")
                continue
                
            # Append seat if it passed all validations
            seats.append((row_idx, col_idx))
           
        except ValueError:
            print("Invalid input! Please use format like 'A5'")
            
    return seats

def cancel_ticket():
    movie = show_movies()   
    if movie == 4:
        return
    
    show_seats(movie)
    number_of_seats = int(input("Enter the number of seats to cancel: "))
    seats = get_seat_number_to_cancle(number_of_seats, movie)

    movie_array = {
        11: Movie_1_2D,
        12: Movie_2_3D,
        2: Movie_3_2D,
        3: Movie_4_3D
    }.get(movie)
    
    for row_idx, col_idx in seats:
        # Calculate the seat number based on column position
        if col_idx < 7:
            seat_number = str(col_idx - 1)  # Convert back to visible seat number
        else:
            seat_number = str(col_idx - 2)  # Adjust for aisle gap
            
        movie_array[row_idx, col_idx] = seat_number
    
    print("\nCancellation confirmed! Seats have been unbooked.")
    print("\nUpdated seating arrangement:")
    show_seats(movie)

if __name__ == "__main__":
    initialize_movie_halls()  # Initialize all movie halls
    name = input("Enter your name: ")
    while True:
        try:
            choice = int(input("Select option :\n0)exit\n1)Book Ticket\n2)Cancle Ticket\nEnter your Choice: "))
            print()
            if not choice.is_integer():
                raise ValueError("Please enter a number")
            if(choice == 0):
                break
            elif(choice == 1):
                book_ticket()
            elif(choice == 2):
                cancel_ticket()
            else:
                print("Please only enter only 0,1 or 2")    
        except ValueError as e:
            print(f"Error:{e}")    
            continue