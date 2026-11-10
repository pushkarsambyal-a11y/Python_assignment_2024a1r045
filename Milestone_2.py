MEAL_SIZE_KG = 0.40
donations = []
categories = set()
priority_count = {"CRITICAL": 0, "PRIORITY": 0, "NORMAL": 0}

print("=" * 50)
print(" FOOD RESCUE SYSTEM - MULTIPLE DONATIONS")
print("=" * 50)
print("Type DONE as the donor name to finish.\n")

while True:
    donor_name = input("Donor name : ").strip()
    if donor_name.upper() == "DONE":
        break

    food_category = input("Food category : ").strip()
    quantity_kg = float(input("Quantity (kg) : "))
    hours_remaining = int(input("Hours before expiry : "))

    if quantity_kg <= 0 or hours_remaining <= 0:
        print(">> REJECTED: quantity and hours must be above 0.\n")
        continue

    if hours_remaining <= 4:
        priority = "CRITICAL"
    elif hours_remaining <= 12:
        priority = "PRIORITY"
    else:
        priority = "NORMAL"

    meals = int(round(quantity_kg / MEAL_SIZE_KG, 6))

    donation = {
        "donor": donor_name.title(),
        "category": food_category.title(),
        "quantity": quantity_kg,
        "hours": hours_remaining,
        "meals": meals,
        "priority": priority
    }

    donations.append(donation)
    categories.add(food_category.title())
    priority_count[priority] = priority_count[priority] + 1
    print(">> ACCEPTED as", priority, "-", meals, "meals\n")

total_quantity = 0
total_meals = 0
for donation in donations:
    total_quantity = total_quantity + donation["quantity"]
    total_meals = total_meals + donation["meals"]

print("\n" + "-" * 50)
print(" SESSION SUMMARY")
print("-" * 50)
for donation in donations:
    print(donation["donor"], "|", donation["quantity"], "kg |",
          donation["hours"], "hours |", donation["priority"])
print("-" * 50)
print("Valid donations :", len(donations))
print("Total quantity :", total_quantity, "kg")
print("Total estimated meals:", total_meals)
print("CRITICAL :", priority_count["CRITICAL"])
print("PRIORITY :", priority_count["PRIORITY"])
print("NORMAL :", priority_count["NORMAL"])
print("Unique categories :", categories)
print("-" * 50)
