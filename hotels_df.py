import pandas

hotel_file = "hotels.csv"
df = pandas.read_csv(hotel_file, dtype={"id": str})
