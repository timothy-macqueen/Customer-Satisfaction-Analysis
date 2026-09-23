import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# -----------------------------
# SETUP
# -----------------------------
fake = Faker("en_GB")
random.seed(42)
Faker.seed(42)

ROWS = 10000

# -----------------------------
# LOOKUP LISTS
# -----------------------------
provinces = [
    "Eastern Cape",
    "Western Cape",
    "KwaZulu-Natal",
    "Gauteng",
    "Limpopo",
    "Mpumalanga",
    "North West",
    "Free State",
    "Northern Cape"
]

products = [

    # Electronics
    "Samsung 55-inch Smart TV",
    "Apple AirPods Pro",
    "HP Pavilion Laptop",
    "Lenovo ThinkPad Laptop",
    "Dell Inspiron Laptop",
    "Sony PlayStation 5",
    "Xbox Series X",
    "Nintendo Switch OLED",
    "Canon EOS DSLR Camera",
    "Nikon Mirrorless Camera",
    "JBL Bluetooth Speaker",
    "Bose Soundbar",
    "Logitech Wireless Mouse",
    "Logitech Mechanical Keyboard",
    "Apple iPad",
    "Samsung Galaxy Tablet",
    "Garmin Smartwatch",
    "Fitbit Fitness Tracker",

    # Food
    "Organic Coffee Beans",
    "Breakfast Cereal",
    "Olive Oil",
    "Pasta",
    "Chocolate Gift Box",
    "Frozen Pizza",
    "Protein Bars",
    "Trail Mix",
    "Peanut Butter",
    "Green Tea",
    "Instant Noodles",
    "Bottled Water",
    "Fruit Juice",
    "Energy Drink",
    "Potato Chips",
    "Mixed Nuts",

    # Home Devices
    "Air Fryer",
    "Microwave Oven",
    "Vacuum Cleaner",
    "Electric Kettle",
    "Coffee Machine",
    "Washing Machine",
    "Blender",
    "Rice Cooker",
    "Toaster",
    "Steam Iron",
    "Robot Vacuum",
    "Ceiling Fan",
    "Portable Heater",
    "Water Purifier",

    # Accessories
    "Leather Wallet",
    "Phone Charger",
    "USB-C Cable",
    "Power Bank",
    "Wireless Earbuds",
    "Laptop Backpack",
    "Travel Backpack",
    "Duffel Bag",
    "Sunglasses",
    "Watch Strap",
    "Phone Case",
    "Screen Protector",
    "Bluetooth Tracker",

    # Apparel
    "Men's T-Shirt",
    "Women's Jeans",
    "Running Shoes",
    "Hoodie",
    "Winter Jacket",
    "Dress Shirt",
    "Sneakers",
    "Baseball Cap",
    "Socks",
    "Sports Shorts",
    "Polo Shirt",
    "Rain Jacket",
    "Sandals",

    # Home & Living
    "Dining Chair",
    "Coffee Table",
    "Bookshelf",
    "Floor Lamp",
    "Wall Clock",
    "Curtains",
    "Bed Linen Set",
    "Throw Pillow",
    "Storage Basket",
    "Laundry Hamper",
    "Kitchen Knife Set",
    "Cookware Set",
    "Ceramic Dinner Set",

    # Beauty
    "Facial Cleanser",
    "Shampoo",
    "Conditioner",
    "Perfume",
    "Electric Toothbrush",
    "Hair Dryer",
    "Body Lotion",
    "Sunscreen",
    "Face Moisturizer",
    "Lip Balm",
    "Beard Trimmer",
    "Hair Straightener",
    "Body Wash",

    # Sports
    "Yoga Mat",
    "Dumbbell Set",
    "Camping Tent",
    "Hiking Backpack",
    "Soccer Ball",
    "Tennis Racket",
    "Fitness Tracker",
    "Bicycle Helmet",
    "Skipping Rope",
    "Resistance Bands",
    "Camping Chair",
    "Fishing Rod",

    # Toys
    "LEGO Building Set",
    "RC Car",
    "Board Game",
    "Barbie Doll",
    "Puzzle 1000 Pieces",
    "Nerf Blaster",
    "Plush Teddy Bear",
    "Chess Set",
    "Jigsaw Puzzle",
    "Toy Dinosaur",
    "Remote Control Drone",
    "Toy Train Set"
]

comments = [
    "Excellent product",
    "Worth the money",
    "Great customer service",
    "Very fast delivery",
    "Arrived damaged",
    "Packaging could improve",
    "Product exceeded expectations",
    "Would definitely buy again",
    "Average quality",
    "Excellent value",
    "Helpful staff",
    "Long waiting time",
    "Easy online ordering",
    "Item missing accessories",
    "Delivery delayed",
    "Fantastic experience",
    "Battery life disappointing",
    "Very comfortable",
    "Fits perfectly",
    "Looks premium",
    "Instructions unclear",
    "Easy to assemble",
    "Highly recommend",
    "Poor packaging",
    "Exactly as advertised",
    "Customer support was excellent",
    ""
]

payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "EFT",
    "Mobile Payment"
]

delivery_types = [
    "Home Delivery",
    "Click & Collect",
    "In Store"
]

# -----------------------------
# GENERATE DATA
# -----------------------------
records = []

start_date = datetime(2024, 1, 1)

for i in range(1, ROWS + 1):

    purchase_date = start_date + timedelta(
        days=random.randint(0, 730)
    )

    records.append({

        "RespondentID": f"R{i:05d}",

        "Date": purchase_date.strftime("%Y-%m-%d"),

        "Age": random.randint(18, 80),

        "Gender": random.choice([
            "Male",
            "Female",
            "Other"
        ]),

        "Province": random.choice(provinces),

        "Product": random.choice(products),

        "Satisfaction": random.randint(1, 5),

        "Recommend": random.choice([
            "Yes",
            "No"
        ]),

        "Purchase Amount": round(
            random.uniform(5, 3500), 2
        ),

        "Payment Method": random.choice(payment_methods),

        "Delivery Type": random.choice(delivery_types),

        "Loyalty Member": random.choice([
            "Yes",
            "No"
        ]),

        "Comments": random.choice(comments)

    })

df = pd.DataFrame(records)

# ======================================
# INSERT ERRORS
# ======================================

# -----------------------------
# Missing values (4%)
# -----------------------------
for col in [
    "Age",
    "Gender",
    "Province",
    "Product",
    "Purchase Amount",
    "Comments"
]:
    idx = random.sample(
        range(len(df)),
        int(len(df) * 0.04)
    )
    df.loc[idx, col] = None

# -----------------------------
# Invalid ages (1%)
# -----------------------------
idx = random.sample(
    range(len(df)),
    int(len(df) * 0.01)
)

invalid_ages = [-5, 0, 8, 130, 180]

for i in idx:
    df.loc[i, "Age"] = random.choice(invalid_ages)

# -----------------------------
# Misspelled provinces (2%)
# -----------------------------
province_errors = {
    "Western Cape": "Western Cap",
    "Eastern Cape": "Eastrn Cape",
    "KwaZulu-Natal": "Kwazulu Natal",
    "Gauteng": "Gautengg",
    "Northern Cape": "Northen Cape"
}

idx = random.sample(
    range(len(df)),
    int(len(df) * 0.02)
)

for i in idx:
    value = df.loc[i, "Province"]
    if value in province_errors:
        df.loc[i, "Province"] = province_errors[value]

# -----------------------------
# Misspelled products (2%)
# -----------------------------
product_errors = {
    "Apple AirPods Pro": "Apple Airpod Pro",
    "Samsung 55-inch Smart TV": "Samsung SmartTV",
    "Sony PlayStation 5": "Sony Playstation5",
    "Coffee Machine": "Coffee Machne",
    "Microwave Oven": "Micowave Oven",
    "Leather Wallet": "Leather Walet",
    "Running Shoes": "Runing Shoes",
    "Dining Chair": "Dinning Chair",
    "Facial Cleanser": "Facial Clenser",
    "LEGO Building Set": "Lego Building Set"
}

idx = random.sample(
    range(len(df)),
    int(len(df) * 0.02)
)

for i in idx:
    value = df.loc[i, "Product"]
    if value in product_errors:
        df.loc[i, "Product"] = product_errors[value]

# -----------------------------
# Extra spaces & capitalization (4%)
# -----------------------------
idx = random.sample(
    range(len(df)),
    int(len(df) * 0.04)
)

for i in idx:

    if pd.notna(df.loc[i, "Province"]):

        value = df.loc[i, "Province"]

        style = random.randint(1, 4)

        if style == 1:
            value = value.upper()

        elif style == 2:
            value = value.lower()

        elif style == 3:
            value = " " + value + " "

        else:
            value = value.title() + "  "

        df.loc[i, "Province"] = value

# -----------------------------
# Invalid dates (0.8%)
# -----------------------------
bad_dates = [
    "2024-13-01",
    "2025-02-30",
    "31/02/2025",
    "2024/15/01",
    "not a date"
]

idx = random.sample(
    range(len(df)),
    int(len(df) * 0.008)
)

for i in idx:
    df.loc[i, "Date"] = random.choice(bad_dates)

# -----------------------------
# Duplicate rows (1.5%)
# -----------------------------
duplicates = df.sample(
    frac=0.015,
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# -----------------------------
# Shuffle rows
# -----------------------------
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# -----------------------------
# SAVE TO EXCEL
# -----------------------------
output_file = "Retail_Customer_Satisfaction_10000.xlsx"

df.to_excel(
    output_file,
    index=False
)

print(f"Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Saved as: {output_file}")