def filter_hotels(hotel):
    city = input("Enter city to filter by (leave empty to ignore): ")
    name = input("Enter hotel name to filter by (leave empty to ignore): ")
    min_price = input("Enter minimum price to filter by (leave empty to ignore): ")
    max_price = input("Enter maximum price to filter by (leave empty to ignore): ")

    filters = {
        "city": city,
        "name": name,
        "min_price": min_price,
        "max_price": max_price
    }

    hotel.filter_hotels(filters)