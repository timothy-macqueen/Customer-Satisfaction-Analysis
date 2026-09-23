import random
import pandas as pd

# Product price ranges
PRICE_RANGES = {
      # Electronics
    "Samsung 55-inch Smart TV": (8500, 18000),
    "Apple AirPods Pro": (4500, 7000),
    "HP Pavilion Laptop": (12000, 22000),
    "Lenovo ThinkPad Laptop": (18000, 35000),
    "Dell Inspiron Laptop": (13000, 25000),
    "Sony PlayStation 5": (11000, 15000),
    "Xbox Series X": (11000, 15000),
    "Nintendo Switch OLED": (6500, 9000),
    "Canon EOS DSLR Camera": (12000, 35000),
    "Nikon Mirrorless Camera": (18000, 45000),
    "JBL Bluetooth Speaker": (900, 4500),
    "Bose Soundbar": (6000, 18000),
    "Logitech Wireless Mouse": (300, 1200),
    "Logitech Mechanical Keyboard": (1200, 3500),
    "Apple iPad": (8000, 28000),
    "Samsung Galaxy Tablet": (5000, 18000),
    "Garmin Smartwatch": (4500, 18000),
    "Fitbit Fitness Tracker": (1800, 5000),

    # Food
    "Organic Coffee Beans": (120, 350),
    "Breakfast Cereal": (55, 120),
    "Olive Oil": (120, 320),
    "Pasta": (25, 70),
    "Chocolate Gift Box": (120, 500),
    "Frozen Pizza": (65, 160),
    "Protein Bars": (25, 60),
    "Trail Mix": (60, 180),
    "Peanut Butter": (45, 120),
    "Green Tea": (40, 140),
    "Instant Noodles": (12, 30),
    "Bottled Water": (12, 35),
    "Fruit Juice": (25, 70),
    "Energy Drink": (20, 45),
    "Potato Chips": (18, 50),
    "Mixed Nuts": (60, 220),

    # Home Devices
    "Air Fryer": (1200, 4500),
    "Microwave Oven": (1200, 3500),
    "Vacuum Cleaner": (1800, 8000),
    "Electric Kettle": (250, 900),
    "Coffee Machine": (1200, 12000),
    "Washing Machine": (6000, 18000),
    "Blender": (500, 2500),
    "Rice Cooker": (450, 1800),
    "Toaster": (300, 1500),
    "Steam Iron": (350, 1800),
    "Robot Vacuum": (4000, 18000),
    "Ceiling Fan": (1200, 4500),
    "Portable Heater": (500, 2500),
    "Water Purifier": (1800, 12000),

    # Accessories
    "Leather Wallet": (350, 1800),
    "Phone Charger": (150, 650),
    "USB-C Cable": (80, 300),
    "Power Bank": (350, 1800),
    "Wireless Earbuds": (500, 3500),
    "Laptop Backpack": (500, 2500),
    "Travel Backpack": (700, 3500),
    "Duffel Bag": (500, 2200),
    "Sunglasses": (350, 3500),
    "Watch Strap": (180, 1200),
    "Phone Case": (150, 700),
    "Screen Protector": (80, 350),
    "Bluetooth Tracker": (350, 1200),

    # Apparel
    "Men's T-Shirt": (180, 500),
    "Women's Jeans": (500, 1800),
    "Running Shoes": (1200, 3500),
    "Hoodie": (450, 1500),
    "Winter Jacket": (900, 4500),
    "Dress Shirt": (400, 1200),
    "Sneakers": (900, 3000),
    "Baseball Cap": (180, 650),
    "Socks": (50, 180),
    "Sports Shorts": (250, 800),
    "Polo Shirt": (350, 1200),
    "Rain Jacket": (700, 2500),
    "Sandals": (300, 1200),

    # Home & Living
    "Dining Chair": (800, 3500),
    "Coffee Table": (1800, 7000),
    "Bookshelf": (1200, 6000),
    "Floor Lamp": (700, 3500),
    "Wall Clock": (250, 1800),
    "Curtains": (450, 3500),
    "Bed Linen Set": (600, 2500),
    "Throw Pillow": (150, 600),
    "Storage Basket": (120, 500),
    "Laundry Hamper": (250, 900),
    "Kitchen Knife Set": (600, 3500),
    "Cookware Set": (1200, 6000),
    "Ceramic Dinner Set": (600, 3000),

    # Beauty
    "Facial Cleanser": (120, 450),
    "Shampoo": (70, 250),
    "Conditioner": (70, 250),
    "Perfume": (600, 3500),
    "Electric Toothbrush": (600, 3500),
    "Hair Dryer": (450, 2500),
    "Body Lotion": (80, 300),
    "Sunscreen": (120, 350),
    "Face Moisturizer": (150, 600),
    "Lip Balm": (40, 120),
    "Beard Trimmer": (500, 2500),
    "Hair Straightener": (700, 3500),
    "Body Wash": (60, 180),

    # Sports
    "Yoga Mat": (250, 1200),
    "Dumbbell Set": (700, 4500),
    "Camping Tent": (1800, 12000),
    "Hiking Backpack": (900, 4500),
    "Soccer Ball": (250, 1200),
    "Tennis Racket": (800, 6000),
    "Fitness Tracker": (1800, 5000),
    "Bicycle Helmet": (500, 2500),
    "Skipping Rope": (100, 400),
    "Resistance Bands": (150, 700),
    "Camping Chair": (350, 1800),
    "Fishing Rod": (600, 6000),

    # Toys
    "LEGO Building Set": (350, 5000),
    "RC Car": (500, 3500),
    "Board Game": (300, 1200),
    "Barbie Doll": (250, 1200),
    "Puzzle 1000 Pieces": (200, 600),
    "Nerf Blaster": (400, 1800),
    "Plush Teddy Bear": (200, 900),
    "Chess Set": (350, 2500),
    "Jigsaw Puzzle": (150, 500),
    "Toy Dinosaur": (150, 600),
    "Remote Control Drone": (1200, 12000),
    "Toy Train Set": (400, 2500),
}

rows = []

products = random.sample(list(PRICE_RANGES.keys()), len(PRICE_RANGES))

rows = []

for product in products:
    low, high = PRICE_RANGES[product]

    rows.append({
        "Product": product,
        "Purchase Amount": round(random.uniform(low, high), 2)
    })

df = pd.DataFrame(rows)

# Write to Excel
with pd.ExcelWriter("Products2.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Product_Data")

    ws = writer.sheets["Product_Data"]

    # Format Purchase Amount as a number with 2 decimals
    for cell in ws["B"][1:]:
        cell.number_format = '#,##0.00'

print("Excel file created successfully.")