class FoodDonation:
    organization_name = "Jammu Community Food Rescue"
    MEAL_SIZE_KG = 0.40

    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):
        self.donation_id = donation_id
        self.donor_name = donor_name.strip().title()
        self.food_category = food_category.strip().title()
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self):
        meals = self.quantity_kg / FoodDonation.MEAL_SIZE_KG
        return int(round(meals, 6))

    def priority_level(self):
        if self.hours_to_expiry <= 4:
            return "CRITICAL"
        elif self.hours_to_expiry <= 12:
            return "PRIORITY"
        else:
            return "NORMAL"

    def display_summary(self):
        print("-" * 40)
        print("Organization :", FoodDonation.organization_name)
        print("Donation ID :", self.donation_id)
        print("Donor :", self.donor_name)
        print("Food Category :", self.food_category)
        print("Quantity :", self.quantity_kg, "kg")
        print("Hours to Expiry :", self.hours_to_expiry)
        print("Estimated Meals :", self.estimated_meals())
        print("Priority Level :", self.priority_level())
        print("-" * 40)

    def __str__(self):
        text = self.donation_id + " | " + self.donor_name + " | "
        text = text + self.food_category + " | " + self.priority_level()
        return text


print("=" * 40)
print(FoodDonation.organization_name.upper())
print("=" * 40)

donation1 = FoodDonation("D1", "green oven bakery", "baked food", 8.5, 6)
donation2 = FoodDonation("D2", "hotel royal feast", "cooked rice", 12.0, 3)

donation1.display_summary()
donation2.display_summary()

print("\nUsing __str__():")
print(donation1)
print(donation2)
