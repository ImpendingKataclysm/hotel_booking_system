import pandas

hotel_file = "hotels.csv"
card_file = "cards.csv"
security_file = "card_security.csv"

hotel_df = pandas.read_csv(hotel_file, dtype={"id": str})
card_df = pandas.read_csv(card_file, dtype=str).to_dict(orient="records")
secure_card_df = pandas.read_csv(security_file, dtype=str)
