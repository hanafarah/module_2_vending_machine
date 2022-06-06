"""
A virtual vending machine.
"""
# A list of coins allowed
ACCEPTABLE_COINS = [200, 100, 25, 10, 5]

# A mapping of products and their prices
PRODUCT_PRICES = {
    'drink': 275,
    'chips': 225,
    'candy': 315
}


def insert_coin(coin, inserted_coins):
    """
    Accepts a coin and appends it to inserted_coins list.
    """
    if coin not in ACCEPTABLE_COINS:
        raise ValueError
    inserted_coins.append(coin)


def return_change(balance):
    """
    Returns balance in coins.
    """
    change = []
    balance -= balance % 5

    while balance > 0:
        for coin in ACCEPTABLE_COINS:
            if balance % coin == 0:
                change.append(coin)
                balance -= coin
                break

    return sorted(change, reverse=True)


def buy_product(product, balance):
    """
    Debits the balance using the product's price. A sufficient
    balance must be provided to complete the purchase.
    """
    if product not in PRODUCT_PRICES:
        raise ValueError
    price = PRODUCT_PRICES[product]

    if balance < price:
        raise InsufficientFunds

    return balance - price


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
    pass
