from hotel import Hotel, SpaHotel
# from user import User
from hotel_ticket import HotelTicket, SpaTicket
from dataframes import hotel_df
from credit_card import SecureCreditCard

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
            credit_card = SecureCreditCard(credit_card_no)

            if credit_card.validate(user_name, expiry, cvc):
                password = input("Enter password: ")
                if credit_card.authenticate(password):
                    hotel.book_reservation()
                    reservation_ticket = HotelTicket(user_name, hotel)
                    reservation_ticket.generate_ticket()

                    book_spa = input("Do you want to book a spa package? (yes/no): ")
                    if book_spa.lower() == "yes":
                        hotel = SpaHotel(search_id)
                        hotel.book_spa_package()
                        spa_res_ticket = SpaTicket(user_name, hotel)
                        spa_res_ticket.generate_ticket()
                else:
                    print("Credit Card authentication failed")
            else:
                print("Invalid credit card details")
        else:
            print("Sorry, that hotel is unavailable.")
    except ValueError:
        print("Hotel not found")
