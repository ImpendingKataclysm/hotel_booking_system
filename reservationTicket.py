from fpdf import FPDF


class ReservationTicket:
    def __init__(self, name, hotel):
        self.customer_name = name
        self.booked_hotel = hotel

    def generate_ticket(self):
        name_info = f"Name: {self.customer_name}"
        hotel_info = f"Hotel: {self.booked_hotel.name}"
        content = f"""
        Thank you for your reservation!
        Booking info:
        {name_info}
        {hotel_info}
        """

        # print(content)

        pdf = FPDF(orientation='P', unit="mm", format="A4")
        cell_width = 50
        cell_height = 8
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style='B')
        pdf.cell(w=cell_width, h=cell_height, txt="Booking Confirmation:", ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=name_info, ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=hotel_info, ln=1)

        pdf.output("confirmation.pdf")
