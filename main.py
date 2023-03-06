from hotel import Hotel
# from user import User
from reservationTicket import ReservationTicket
from hotels_df import df

if __name__ == "__main__":
    print(df)
    search_id = input("Enter hotel id: ")
    hotel = Hotel(search_id)

    try:
        if hotel.available():
            hotel.book_reservation()
            user_name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(user_name, hotel)
            reservation_ticket.generate_ticket()
        else:
            print("Sorry, that hotel is unavailable.")
    except ValueError:
        print("Hotel ID does not exist, please try again")
