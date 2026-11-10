import time
from rescue_utils import calculate_meals, classify_priority, summarize_donations


class FoodDonation:
    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):
        self.donation_id = donation_id
        self.donor_name = donor_name.title()
        self.food_category = food_category.title()
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self):
        return calculate_meals(self.quantity_kg)

    def priority_level(self):
        return classify_priority(self.hours_to_expiry)

    def __str__(self):
        text = self.donation_id + " | " + self.donor_name + " | "
        text = text + self.food_category + " | " + self.priority_level()
        return text


print("=" * 40)
print("JAMMU COMMUNITY FOOD RESCUE")
print("=" * 40)
print("Type DONE as donor name to finish.\n")

donations = []
count = 0

while True:
    name = input("Donor name : ")
    if name.upper() == "DONE":
        break
    category = input("Food category : ")
    quantity = float(input("Quantity (kg) : "))
    hours = int(input("Hours before expiry : "))
    if quantity <= 0 or hours <= 0:
        print("REJECTED: values must be greater than 0\n")
        continue
    count = count + 1
    donation = FoodDonation("D" + str(count), name, category, quantity, hours)
    donations.append(donation)
    print("ACCEPTED:", donation, "\n")

sorted_donations = sorted(donations, key=lambda d: d.hours_to_expiry)
print("\nPICKUP ORDER (most urgent first)")
for d in sorted_donations:
    print(d, "-", d.hours_to_expiry, "hours left")

start = time.perf_counter()
total_kg, total_meals = summarize_donations(donations)
end = time.perf_counter()

print("\n------------ SUMMARY REPORT ------------")
print("Total donations :", len(donations))
print("Total quantity :", total_kg, "kg")
print("Total meals :", total_meals)

elapsed = (end - start) * 1000
print("Report processing time:", round(elapsed, 3), "milliseconds")

total_kg, new_meals = summarize_donations(donations, meal_size_kg=0.50)
print("Meals if one meal = 0.50 kg:", new_meals)
