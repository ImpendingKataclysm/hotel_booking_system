from dataframes import card_df, secure_card_df


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, holder, expiry, cvc):
        card_data = {"holder": holder.upper(),
                     "number": self.number,
                     "expiry": expiry,
                     "cvc": cvc}
        return card_data in card_df


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = secure_card_df.loc[secure_card_df["number"] == self.number, "password"].squeeze()
        return given_password == password


if __name__ == "__main__":
    my_card = SecureCreditCard("1357")
    my_card.authenticate("mypass3")
