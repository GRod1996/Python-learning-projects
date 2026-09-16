# CS 1350 Mini-Project 1: Contact Manager
# Gabriel Rodriguez, Adonis Robinson, Joaquin Goldman

# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}


# ============================================================
# PHASE 1 - Creating Contact Manager
# ============================================================

print("=== Phase 1: Quick Contacts ===")

# 1. Create quick_contacts with five entries and print the whole dictionary.
quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"
print(quick_contacts)

print("--- Access and Modify ---")

# 2. Print Mom's number using bracket notation.
print("Mom's number:", quick_contacts["Mom"])

# 3. Update Dad's number.
quick_contacts["Dad"] = "555-4321"

# 4. Add Dentist.
quick_contacts["Dentist"] = "555-2222"

# 5. Look up a missing key with get() so the program does not crash.
print("Looking up Grandma:", quick_contacts.get("Grandma", "Contact not found"))

# 6. Print the updated dictionary.
print("Updated contacts:", quick_contacts)

print("--- Delete and Analyze ---")

# 7. Remove Pizza Place with del.
del quick_contacts["Pizza Place"]

# 8. Remove Work with pop(), keeping the old value.
old_work = quick_contacts.pop("Work")
print("Removed work number:", old_work)

# 9. Report what is left.
print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))


# ============================================================
# PHASE 2 - Per-Contact Statistics: Nested Iteration
# ============================================================

print("\n=== Phase 2: Contact Activity ===")

# total_minutes maps each contact to their total minutes. Later phases need it.
total_minutes = {}

for name, months in call_log.items():

    month_count = len(months)
    total = 0

    busiest_month = ""
    busiest_minutes = 0

    for month, minutes in months.items():

        total += minutes

        # Running maximum for the busiest month.
        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    average = total / month_count
    total_minutes[name] = total

    print(
        f"{name}: {month_count} month(s), {total} min total, "
        f"avg: {average:.2f}, busiest: {busiest_month} ({busiest_minutes})"
    )


# ============================================================
# PHASE 3 - Flipping the Data & Aggregating with get()
# ============================================================

print("\n=== Phase 3: Aggregations ===")

# --- Part A: month_stats, organized by month ---
month_stats = {}

for contact, months in call_log.items():

    for month, minutes in months.items():

        if month not in month_stats:
            month_stats[month] = {
                "minutes": [],
                "total": 0,
                "avg": 0,
                "contacts": 0,
            }

        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["total"] += minutes
        month_stats[month]["contacts"] += 1

# Fill in the average for each month.
for month, stats in month_stats.items():
    stats["avg"] = stats["total"] / stats["contacts"]

print("Monthly summary (sorted by average, highest first):")

for month, stats in sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True,
):
    print(
        f"  {month}: {stats['total']} min total, "
        f"{stats['avg']:.2f} avg ({stats['contacts']} contacts)"
    )

# --- Part B: category, city, and headcount rollups (get() accumulation) ---
minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for contact, months in call_log.items():

    contact_total = sum(months.values())

    category = contact_book[contact]["category"]
    city = contact_book[contact]["city"]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + contact_total
    minutes_by_city[city] = minutes_by_city.get(city, 0) + contact_total
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)


# ============================================================
# PHASE 4 - Dictionary Comprehensions
# ============================================================

print("\n=== Phase 4: Comprehensions ===")

phone_book = {name: details["phone"] for name, details in contact_book.items()}

local_contacts = {
    name: details["phone"]
    for name, details in contact_book.items()
    if details["city"] == "Fort Wayne"
}

activity_level = {
    name: "Frequent" if minutes >= 200 else "Occasional"
    for name, minutes in total_minutes.items()
}

print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)


# ============================================================
# PHASE 5 - Tiers, Distribution, and Rankings
# ============================================================

print("\n=== Phase 5: Tier Report ===")


# --- Part A: classify each contact ---
def get_tier(minutes):
    """Return the loyalty tier for a given total-minutes value."""
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


for name, minutes in total_minutes.items():
    print(f"{name}: {minutes} min ({get_tier(minutes)})")

# --- Part B: count how many contacts fall in each tier ---
print("--- Tier Distribution ---")

platinum = 0
gold = 0
silver = 0
bronze = 0
inactive = 0

for name, minutes in total_minutes.items():

    tier = get_tier(minutes)

    if tier == "Platinum":
        platinum += 1
    elif tier == "Gold":
        gold += 1
    elif tier == "Silver":
        silver += 1
    elif tier == "Bronze":
        bronze += 1
    else:
        inactive += 1

print("Platinum:", platinum)
print("Gold:", gold)
print("Silver:", silver)
print("Bronze:", bronze)
print("Inactive:", inactive)

# --- Part C: rankings ---
print("--- Top and Bottom ---")

most_name = ""
most_minutes = -1

least_name = ""
least_minutes = float("inf")  # start larger than any real value

grand_total = 0

for name, minutes in total_minutes.items():

    grand_total += minutes

    if minutes > most_minutes:
        most_minutes = minutes
        most_name = name

    if minutes < least_minutes:
        least_minutes = minutes
        least_name = name

avg_per_contact = grand_total / len(total_minutes)

print(f"Most contacted: {most_name} ({most_minutes} min)")
print(f"Least contacted: {least_name} ({least_minutes} min)")
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {avg_per_contact:.2f}")

print("--- Above Average Contacts ---")

for name, minutes in total_minutes.items():
    if minutes > avg_per_contact:
        print(f"{name}: {minutes}")


# ============================================================
# PHASE 6 - The Contact Hub Report
# ============================================================

print("\n=== Phase 6: Contact Hub Report ===")

print(f"{'Name':<13}{'Category':<11}{'City':<15}{'Minutes':>8}  Tier")
print("-" * 55)

for name, total in sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True,
):
    category = contact_book[name]["category"]
    city = contact_book[name]["city"]
    tier = get_tier(total)

    print(f"{name:<13}{category:<11}{city:<15}{total:>8}  {tier}")

print("-" * 55)
print(
    f"{len(total_minutes)} contacts | "
    f"{sum(total_minutes.values())} total minutes | "
    f"{avg_per_contact:.2f} average"
)
