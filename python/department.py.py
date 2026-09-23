import random
import pandas as pd


products = [
    # Electronics
    ("Electronics", "Samsung 55-inch Smart TV"),
    ("Electronics", "Apple AirPods Pro"),
    ("Electronics", "HP Pavilion Laptop"),
    ("Electronics", "Lenovo ThinkPad Laptop"),
    ("Electronics", "Dell Inspiron Laptop"),
    ("Electronics", "Sony PlayStation 5"),
    ("Electronics", "Xbox Series X"),
    ("Electronics", "Nintendo Switch OLED"),
    ("Electronics", "Canon EOS DSLR Camera"),
    ("Electronics", "Nikon Mirrorless Camera"),
    ("Electronics", "JBL Bluetooth Speaker"),
    ("Electronics", "Bose Soundbar"),
    ("Electronics", "Logitech Wireless Mouse"),
    ("Electronics", "Logitech Mechanical Keyboard"),
    ("Electronics", "Apple iPad"),
    ("Electronics", "Samsung Galaxy Tablet"),
    ("Electronics", "Garmin Smartwatch"),
    ("Electronics", "Fitbit Fitness Tracker"),

    # Food
    ("Food", "Organic Coffee Beans"),
    ("Food", "Breakfast Cereal"),
    ("Food", "Olive Oil"),
    ("Food", "Pasta"),
    ("Food", "Chocolate Gift Box"),
    ("Food", "Frozen Pizza"),
    ("Food", "Protein Bars"),
    ("Food", "Trail Mix"),
    ("Food", "Peanut Butter"),
    ("Food", "Green Tea"),
    ("Food", "Instant Noodles"),
    ("Food", "Bottled Water"),
    ("Food", "Fruit Juice"),
    ("Food", "Energy Drink"),
    ("Food", "Potato Chips"),
    ("Food", "Mixed Nuts"),

    # Home Devices
    ("Home Devices", "Air Fryer"),
    ("Home Devices", "Microwave Oven"),
    ("Home Devices", "Vacuum Cleaner"),
    ("Home Devices", "Electric Kettle"),
    ("Home Devices", "Coffee Machine"),
    ("Home Devices", "Washing Machine"),
    ("Home Devices", "Blender"),
    ("Home Devices", "Rice Cooker"),
    ("Home Devices", "Toaster"),
    ("Home Devices", "Steam Iron"),
    ("Home Devices", "Robot Vacuum"),
    ("Home Devices", "Ceiling Fan"),
    ("Home Devices", "Portable Heater"),
    ("Home Devices", "Water Purifier"),

    # Accessories
    ("Accessories", "Leather Wallet"),
    ("Accessories", "Phone Charger"),
    ("Accessories", "USB-C Cable"),
    ("Accessories", "Power Bank"),
    ("Accessories", "Wireless Earbuds"),
    ("Accessories", "Laptop Backpack"),
    ("Accessories", "Travel Backpack"),
    ("Accessories", "Duffel Bag"),
    ("Accessories", "Sunglasses"),
    ("Accessories", "Watch Strap"),
    ("Accessories", "Phone Case"),
    ("Accessories", "Screen Protector"),
    ("Accessories", "Bluetooth Tracker"),

    # Apparel
    ("Apparel", "Men's T-Shirt"),
    ("Apparel", "Women's Jeans"),
    ("Apparel", "Running Shoes"),
    ("Apparel", "Hoodie"),
    ("Apparel", "Winter Jacket"),
    ("Apparel", "Dress Shirt"),
    ("Apparel", "Sneakers"),
    ("Apparel", "Baseball Cap"),
    ("Apparel", "Socks"),
    ("Apparel", "Sports Shorts"),
    ("Apparel", "Polo Shirt"),
    ("Apparel", "Rain Jacket"),
    ("Apparel", "Sandals"),

    # Home & Living
    ("Home & Living", "Dining Chair"),
    ("Home & Living", "Coffee Table"),
    ("Home & Living", "Bookshelf"),
    ("Home & Living", "Floor Lamp"),
    ("Home & Living", "Wall Clock"),
    ("Home & Living", "Curtains"),
    ("Home & Living", "Bed Linen Set"),
    ("Home & Living", "Throw Pillow"),
    ("Home & Living", "Storage Basket"),
    ("Home & Living", "Laundry Hamper"),
    ("Home & Living", "Kitchen Knife Set"),
    ("Home & Living", "Cookware Set"),
    ("Home & Living", "Ceramic Dinner Set"),

    # Beauty & Personal Care
    ("Beauty & Personal Care", "Facial Cleanser"),
    ("Beauty & Personal Care", "Shampoo"),
    ("Beauty & Personal Care", "Conditioner"),
    ("Beauty & Personal Care", "Perfume"),
    ("Beauty & Personal Care", "Electric Toothbrush"),
    ("Beauty & Personal Care", "Hair Dryer"),
    ("Beauty & Personal Care", "Body Lotion"),
    ("Beauty & Personal Care", "Sunscreen"),
    ("Beauty & Personal Care", "Face Moisturizer"),
    ("Beauty & Personal Care", "Lip Balm"),
    ("Beauty & Personal Care", "Beard Trimmer"),
    ("Beauty & Personal Care", "Hair Straightener"),
    ("Beauty & Personal Care", "Body Wash"),

    # Sports & Outdoors
    ("Sports & Outdoors", "Yoga Mat"),
    ("Sports & Outdoors", "Dumbbell Set"),
    ("Sports & Outdoors", "Camping Tent"),
    ("Sports & Outdoors", "Hiking Backpack"),
    ("Sports & Outdoors", "Soccer Ball"),
    ("Sports & Outdoors", "Tennis Racket"),
    ("Sports & Outdoors", "Fitness Tracker"),
    ("Sports & Outdoors", "Bicycle Helmet"),
    ("Sports & Outdoors", "Skipping Rope"),
    ("Sports & Outdoors", "Resistance Bands"),
    ("Sports & Outdoors", "Camping Chair"),
    ("Sports & Outdoors", "Fishing Rod"),

    # Toys & Games
    ("Toys & Games", "LEGO Building Set"),
    ("Toys & Games", "RC Car"),
    ("Toys & Games", "Board Game"),
    ("Toys & Games", "Barbie Doll"),
    ("Toys & Games", "Puzzle 1000 Pieces"),
    ("Toys & Games", "Nerf Blaster"),
    ("Toys & Games", "Plush Teddy Bear"),
    ("Toys & Games", "Chess Set"),
    ("Toys & Games", "Jigsaw Puzzle"),
    ("Toys & Games", "Toy Dinosaur"),
    ("Toys & Games", "Remote Control Drone"),
    ("Toys & Games", "Toy Train Set"),
]
# Create DataFrame
df = pd.DataFrame(products, columns=["Department", "Product"])

# Export to Excel
df.to_excel("Department.xlsx", index=False)

print("Department.xlsx has been created.")
