from dataframes import card_df


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, holder, expiry, cvc):
        card_data = {"holder": holder.upper(),
                     "number": self.number,
                     "expiry": expiry,
                     "cvc": cvc}
        return card_data in card_df


if __name__ == "__main__":
    my_card = CreditCard("1357")
    print(my_card.validate("katie janzen", "12/29", "777"))
