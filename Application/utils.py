def estimate_price(prices):
    if not prices:
        return None, None

    numeric_prices = []
    for price in prices:
        try:
            numeric_price = float(price.replace(',', ''))
            numeric_prices.append(numeric_price)
        except ValueError:
            pass

    if not numeric_prices:
        return None, None

    average_price = sum(numeric_prices) / len(numeric_prices)
    variance = sum((x - average_price) **
                   2 for x in numeric_prices) / len(numeric_prices)
    standard_deviation = variance ** 0.5

    lower_bound = max(0, average_price - standard_deviation)
    upper_bound = average_price + standard_deviation

    return round(lower_bound, 2), round(upper_bound, 2)
