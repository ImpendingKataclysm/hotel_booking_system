from dataframes import hotel_df, hotel_file


class Hotel:
    def __init__(self, h_id):
        self.hotel_id = h_id
        self.name = hotel_df.loc[hotel_df["id"] == self.hotel_id, "name"].squeeze()

    def book_reservation(self):
        """ Books hotel by changing its availability to 'no' """
        hotel_df.loc[hotel_df["id"] == self.hotel_id, "available"] = "no"
        hotel_df.to_csv(hotel_file, index=False)

    def available(self):
        """ Checks whether hotel is available """
        availability = hotel_df.loc[hotel_df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        print("Booking spa package...")
