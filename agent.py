import tools
import spacy

def agent_response(user_query):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_query.lower())
    
    if "search" in user_query or "find" in user_query:
        return tools.search_products("Floral Skirt", 40, "S")
    elif "shipping" in user_query or "delivery" in user_query:
        return tools.estimate_shipping("New York", "2024-02-09")
    elif "discount" in user_query or "promo" in user_query:
        return tools.apply_discount(40, "SAVE10")
    elif "compare" in user_query or "cheaper" in user_query:
        return tools.compare_prices("Casual Denim Jacket")
    elif "return policy" in user_query or "returns" in user_query:
        return tools.check_return_policy("Amazon")
    return "I don't understand. Try asking about product search, shipping, discounts, price comparison, or return policies."

