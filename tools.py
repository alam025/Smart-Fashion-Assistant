
import requests
import random

def search_products(query, max_price, size):
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    if response.status_code == 200:
        products = response.json()
        return [p for p in products if p['price'] <= max_price and size in p.get('sizes', [])]
    return []

def estimate_shipping(location, delivery_date):
    return {"cost": round(random.uniform(4.99, 15.99), 2), "delivery_date": delivery_date, "feasible": True}

def apply_discount(price, promo_code):
    discounts = {"SAVE10": 0.10, "WELCOME5": 0.05, "FASHION20": 0.20}
    discount_amount = price * discounts.get(promo_code, 0)
    return price - discount_amount

def compare_prices(product_name):
    competitors = ["Amazon", "eBay", "Walmart", "BestBuy"]
    return {store: round(random.uniform(40, 100), 2) for store in competitors}

def check_return_policy(site):
    policies = {"Amazon": "30-day return policy", "eBay": "No returns", "Walmart": "15-day return policy", "BestBuy": "45-day return policy"}
    return policies.get(site, "No return policy found.")
