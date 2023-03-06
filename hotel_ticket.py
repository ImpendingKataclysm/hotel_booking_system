from fpdf import FPDF
from abc import ABC, abstractmethod


class Ticket(ABC):
    def __init__(self, name, hotel):
        self.customer_name = name
        self.booked_hotel = hotel

    @staticmethod
    def generate_pdf(title, filename, customer, booked_hotel):
        pdf = FPDF(orientation='P', unit="mm", format="A4")
        cell_width = 50
        cell_height = 8
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style='B')
        pdf.cell(w=cell_width, h=cell_height, txt=title, ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=f"Customer Name: {customer}", ln=1)
        pdf.cell(w=cell_width, h=cell_height, txt=f"Hotel: {booked_hotel}", ln=1)

        pdf.output(filename)

    @abstractmethod
    def generate_ticket(self):
        pass

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
        self.generate_pdf(title, "hotel_confirmation.pdf", self.the_customer_name, self.booked_hotel.name)


class SpaTicket(Ticket):
    def generate_ticket(self):
        title = "Spa package booked successfully!"
        content = f"""
        {title}
        Customer Name: {self.the_customer_name}
        Hotel: {self.booked_hotel.name}
        """

        print(content)
        self.generate_pdf(title, "spa_confirmation.pdf", self.the_customer_name, self.booked_hotel.name)
