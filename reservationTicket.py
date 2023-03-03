class ReservationTicket:
    def __init__(self, name, hotel):
        self.customer_name = name
        self.booked_hotel = hotel

    def generate_ticket(self):
        content = f"""
        Thank you for your reservation!
        Booking info:
        Name: {self.customer_name}
        Hotel: {self.booked_hotel.name}
        """

        return content
