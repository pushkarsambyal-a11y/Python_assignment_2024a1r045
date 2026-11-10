import time
from rescue_utils import calculate_meals, classify_priority, summarize_donations

FILE_NAME = "rescue_records.txt"


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


def save_record(donation):
    file = open(FILE_NAME, "a")
    line = donation.donation_id + "|" + donation.donor_name + "|"
    line = line + donation.food_category + "|" + str(donation.quantity_kg)
    line = line + "|" + str(donation.hours_to_expiry) + "\n"
    file.write(line)
    file.close()


def read_records():
    donations = []
    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("ERROR:", FILE_NAME, "not found. A new file will be created.")
        return donations

    for line in file:
        if line.strip() == "":
            continue
        parts = line.strip().split("|")
        if len(parts) != 5:
            print("WARNING: malformed record skipped ->", line.strip())
            continue
        donation = FoodDonation(parts[0], parts[1], parts[2],
                                float(parts[3]), int(parts[4]))
        donations.append(donation)
    file.close()
    return donations


def display_records(donations):
    print("\n------------ STORED RECORDS ------------")
    for d in donations:
        print(d, "|", d.quantity_kg, "kg |", d.hours_to_expiry, "hours")
    print("Total records:", len(donations))


print("=" * 40)
print("JAMMU COMMUNITY FOOD RESCUE")
print("=" * 40)

donations = read_records()
display_records(donations)

count = len(donations)

print("\nEnter new donations (type DONE to stop)")
while True:
    name = input("Donor name : ")
    if name.upper() == "DONE":
        break
    category = input("Food category : ")
    try:
        quantity = float(input("Quantity (kg) : "))
        hours = int(input("Hours before expiry : "))
    except ValueError:
        print("ERROR: quantity and hours must be numbers. Enter again.\n")
        continue

    if quantity <= 0 or hours <= 0:
        print("REJECTED: values must be greater than 0\n")
        continue

    count = count + 1
    donation = FoodDonation("D" + str(count), name, category, quantity, hours)
    save_record(donation)
    donations.append(donation)
    print("SAVED:", donation, "\n")

display_records(donations)

if len(donations) > 0:
    sorted_donations = sorted(donations, key=lambda d: d.hours_to_expiry)
    print("\nPICKUP ORDER (most urgent first)")
    for d in sorted_donations:
        print(d, "-", d.hours_to_expiry, "hours left")
    start = time.perf_counter()
    total_kg, total_meals = summarize_donations(donations)
    end = time.perf_counter()
    print("\nTotal quantity :", total_kg, "kg")
    print("Total meals :", total_meals)
    elapsed = (end - start) * 1000
    print("Report processing time:", round(elapsed, 3), "milliseconds")

print("\nProgram finished.")
