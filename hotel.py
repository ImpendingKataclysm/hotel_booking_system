from hotels_df import df, hotel_file


class Hotel:
    def __init__(self, h_id):
        self.hotel_id = h_id

    def book_reservation(self):
        """ Books hotel by changing its availability to 'no' """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv(hotel_file, index=False)

    def available(self):
        """ Checks whether hotel is available """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
