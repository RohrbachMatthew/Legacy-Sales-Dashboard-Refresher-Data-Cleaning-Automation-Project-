import pandas as pd
import random
from faker import Faker  # Generates fake but realistic data

# Initialize faker
fake = Faker()
Faker.seed(42)  # uses seed to make repeatable random data (if no seed results are different each time)

# Make inconsistent region names for practice
regions = ["North", "south ", "EAST", "West", "central", "NORTH", "weSt "]

# Generate random dates in bad format for practice
def random_bad_date():
    date = fake.date_between(start_date='-60d', end_date='today')  # dates between 60 days ago and today
    fmt = random.choice(["%m-%d-%Y", "%Y/%m/%d", "%d %b %Y", "%d.%m.%Y", "3rd %B %Y"])
    return date.strftime(fmt)

# Build and simulate messy data
rows = []
for _ in range(250):
    name = random.choice([
        " " + fake.first_name().lower() + " ",
        fake.first_name().upper(),
        fake.first_name()
    ])
    amount = random.choice([
        f'"{random.randint(500, 2500)}"',  # Simulates a value exported as a string instead of a number
        f"${random.randint(500, 2500)}",  # Forces practice to clean out currency symbols during parsing
        f"{random.randint(1, 2)}, {random.randint(100, 999)}.00",  # Introduces a comma as thousands separator
        f"{random.randint(1000, 9999)}.00"  # cleanest data to mix in the data
        f"{random.randint(500, 2500)},00"  # mimics European-style decimal notation, where ',' means cents
    ])
    date_of_sale = random_bad_date()
    region = random.choice(regions)
    notes = random.choice([
        "Sold extras", "Late entry", "bonus applied", "", "  ", None, "✓", "duplicate?"
    ])
    rows.append([name, amount, date_of_sale, region, "", notes])
#  Create dataframe with bad column names (intentionally for practice)
df = pd.DataFrame(rows, columns=["EMP_NAME", "TOT@L", "SaLe DATE", " Region ", "", "NOTES"])

#  Save as a csv using semicolon as delimiter (legacy style)
df.to_csv("legacy_weekly_sales_report.csv", sep=";", index=False, encoding="utf-8")

print('Generated legacy weekly sales csv export with messy dataset')
