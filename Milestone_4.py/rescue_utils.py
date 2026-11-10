def calculate_meals(quantity_kg, meal_size_kg=0.40):
    meals = quantity_kg / meal_size_kg
    return int(round(meals, 6))


def classify_priority(hours):
    if hours <= 4:
        return "CRITICAL"
    elif hours <= 12:
        return "PRIORITY"
    else:
        return "NORMAL"


def summarize_donations(donations, meal_size_kg=0.40):
    total_kg = 0
    total_meals = 0
    for donation in donations:
        total_kg = total_kg + donation.quantity_kg
        meals = calculate_meals(donation.quantity_kg, meal_size_kg)
        total_meals = total_meals + meals
    return total_kg, total_meals
