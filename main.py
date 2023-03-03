from hotel import Hotel
# from user import User
from reservationTicket import ReservationTicket

import pandas

hotel_file = "hotels.csv"
df = pandas.read_csv(hotel_file)

if __name__ == "__main__":
    print(df)
    search_id = input("Enter hotel id: ")
    hotel = Hotel(search_id)
    if hotel.available():
        hotel.book_reservation()
        user_name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(user_name, hotel)
        print(reservation_ticket.generate_ticket())
    else:
        print("Sorry, that hotel is unavailable.")
