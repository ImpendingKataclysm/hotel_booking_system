import pandas

hotel_file = "hotels.csv"
hotel_df = pandas.read_csv(hotel_file, dtype={"id": str})

card_file = "cards.csv"
card_df = pandas.read_csv(card_file, dtype=str).to_dict(orient="records")
