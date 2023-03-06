from fpdf import FPDF


class Ticket:
    def __init__(self, name, hotel):
        self.customer_name = name
        self.booked_hotel = hotel

    def generate_pdf(self, title, filename):
        pdf = FPDF(orientation='P', unit="mm", format="A4")
        cell_width = 50
        cell_height = 8
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style='B')
        pdf.cell(w=cell_width, h=cell_height, txt=title, ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=f"Customer Name: {self.the_customer_name}", ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=f"Hotel: {self.booked_hotel.name}", ln=1)

        pdf.output(filename)

    def generate_ticket(self):
        content = "Thank you for your reservation!"

        print(content)
        self.generate_pdf("Ticket booked successfully", "confirmation.pdf")

    @property
    def the_customer_name(self):
        name = self.customer_name.strip().title()
        return name


class HotelTicket(Ticket):
    def generate_ticket(self):
        title = "Hotel booked successfully!"
        content = f"""
        {title}
        Customer Name: {self.the_customer_name}
        Hotel: {self.booked_hotel.name}
        """

        print(content)
        self.generate_pdf(title, "hotel_confirmation.pdf")


class SpaTicket(Ticket):
    def generate_ticket(self):
        title = "Spa package booked successfully!"
        content = f"""
        {title}
        Customer Name: {self.the_customer_name}
        Hotel: {self.booked_hotel.name}
        """

        print(content)
        self.generate_pdf(title, "spa_confirmation.pdf")
