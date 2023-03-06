from hotel import Hotel
# from user import User
from reservationTicket import ReservationTicket
from dataframes import hotel_df
from credit_card import CreditCard

if __name__ == "__main__":
    print(hotel_df)
    search_id = input("Enter hotel id: ")
    hotel = Hotel(search_id)

    try:
        if hotel.available():
            print("Enter credit card information:")
            user_name = input("\nCardholder name: ")
            credit_card_no = input("\nCredit card number: ")
            expiry = input("\nExpiry date: ")
            cvc = input("\nCVC: ")
            credit_card = CreditCard(credit_card_no)

            if credit_card.validate(user_name, expiry, cvc):
                hotel.book_reservation()
                reservation_ticket = ReservationTicket(user_name, hotel)
                reservation_ticket.generate_ticket()
            else:
                print("Invalid credit card details")
        else:
            print("Sorry, that hotel is unavailable.")
    except ValueError:
        print("Hotel ID does not exist, please try again")
