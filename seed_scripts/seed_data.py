import os
import sys
import django

# ✅ Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

django.setup()

from users.models import User
from products.models import Product

def run():
    # ✅ Create admin if not exists
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='Admin@12345',
            role='admin',
            is_staff=True
        )
        print("✅ Admin created (admin / Admin@12345)")
    else:
        print("ℹ️ Admin already exists")

    # ✅ Product Data (Category-wise)
    products = [
        # -------- ELECTRONICS --------
        {"name": "iPhone 15 Pro Max", "category": "Electronics", "price": 149999, "stock": 15, "description": "Apple's latest flagship smartphone with A17 Pro chip and titanium body.", "image_url": "https://m.media-amazon.com/images/I/71fVoqRC0wL._SL1500_.jpg"},
        {"name": "Samsung Galaxy S24 Ultra", "category": "Electronics", "price": 129999, "stock": 20, "description": "Premium Android phone with AI-powered camera.", "image_url": "https://m.media-amazon.com/images/I/81vxWpPpgNL._SL1500_.jpg"},
        {"name": "OnePlus 12R 5G", "category": "Electronics", "price": 45999, "stock": 40, "description": "Flagship performance smartphone with Snapdragon 8 Gen 2.", "image_url": "https://m.media-amazon.com/images/I/71xoR4A6qgL._SL1500_.jpg"},
        {"name": "Xiaomi Pad 6", "category": "Electronics", "price": 25999, "stock": 35, "description": "11-inch tablet with Snapdragon 870 and 2.8K display.", "image_url": "https://m.media-amazon.com/images/I/71cQWYVtcBL._SL1500_.jpg"},
        {"name": "HP Pavilion 15 Laptop", "category": "Electronics", "price": 61999, "stock": 25, "description": "15.6-inch FHD laptop with Ryzen 5 and 8GB RAM.", "image_url": "https://m.media-amazon.com/images/I/71iUCvG6DCL._SL1500_.jpg"},
        {"name": "Dell Inspiron 14", "category": "Electronics", "price": 57999, "stock": 20, "description": "Compact and powerful laptop with Intel i5 processor.", "image_url": "https://m.media-amazon.com/images/I/61tWzziLRfL._SL1500_.jpg"},
        {"name": "Acer Aspire 7", "category": "Electronics", "price": 55999, "stock": 30, "description": "Gaming laptop with GTX 1650 and Ryzen 5 5500U.", "image_url": "https://m.media-amazon.com/images/I/71o8Q5XJS5L._SL1500_.jpg"},
        {"name": "Asus Vivobook 16", "category": "Electronics", "price": 46999, "stock": 30, "description": "Powerful everyday laptop with 16-inch FHD display.", "image_url": "https://m.media-amazon.com/images/I/71vPRo7H5CL._SL1500_.jpg"},
        {"name": "Apple iPad Air (M2)", "category": "Electronics", "price": 64999, "stock": 25, "description": "Tablet with M2 chip and 10.9-inch Liquid Retina display.", "image_url": "https://m.media-amazon.com/images/I/61XZQXFQeVL._SL1500_.jpg"},
        {"name": "Canon EOS 200D II DSLR", "category": "Electronics", "price": 62999, "stock": 15, "description": "DSLR camera with dual pixel AF.", "image_url": "https://m.media-amazon.com/images/I/81z5UOGaO3L._SL1500_.jpg"},
    
        # -------- AUDIO --------
        {"name": "Sony WH-1000XM5", "category": "Audio", "price": 29999, "stock": 25, "description": "Noise-cancelling wireless headphones with crystal clear audio.", "image_url": "https://m.media-amazon.com/images/I/61rP6x3BzRL._SL1500_.jpg"},
        {"name": "Boat Airdopes 441", "category": "Audio", "price": 2499, "stock": 60, "description": "Wireless Bluetooth earbuds with immersive sound.", "image_url": "https://m.media-amazon.com/images/I/61u1VALn6JL._SL1500_.jpg"},
        {"name": "JBL Flip 6 Speaker", "category": "Audio", "price": 8999, "stock": 40, "description": "Portable Bluetooth speaker with deep bass.", "image_url": "https://m.media-amazon.com/images/I/71qJ0-bu3FL._SL1500_.jpg"},
        {"name": "Apple AirPods Pro 2", "category": "Audio", "price": 24999, "stock": 50, "description": "Noise-cancelling wireless earbuds.", "image_url": "https://m.media-amazon.com/images/I/61SUj2aKoEL._SL1500_.jpg"},
        {"name": "Realme Buds Wireless 3", "category": "Audio", "price": 2499, "stock": 80, "description": "Bluetooth wireless neckband with active noise cancellation.", "image_url": "https://m.media-amazon.com/images/I/61iJjBz2QCL._SL1500_.jpg"},
        {"name": "Zebronics Soundbar 2000W", "category": "Audio", "price": 7999, "stock": 35, "description": "Soundbar with subwoofer and Dolby Atmos.", "image_url": "https://m.media-amazon.com/images/I/71l1Tw4o6CL._SL1500_.jpg"},
        {"name": "Marshall Emberton II", "category": "Audio", "price": 15999, "stock": 20, "description": "Portable Bluetooth speaker with iconic design.", "image_url": "https://m.media-amazon.com/images/I/71R3iQ-3imL._SL1500_.jpg"},
        {"name": "Boult Audio Maverick", "category": "Audio", "price": 1999, "stock": 50, "description": "True wireless earbuds with ENC mic.", "image_url": "https://m.media-amazon.com/images/I/61U6oC65TTL._SL1500_.jpg"},
        {"name": "Sennheiser HD 280 Pro", "category": "Audio", "price": 7999, "stock": 25, "description": "Studio-grade headphones with rich sound.", "image_url": "https://m.media-amazon.com/images/I/81kGsTQdDGL._SL1500_.jpg"},
        {"name": "Boat Stone 350", "category": "Audio", "price": 1499, "stock": 80, "description": "Compact Bluetooth speaker with 12-hour battery.", "image_url": "https://m.media-amazon.com/images/I/71p+E8hh8kL._SL1500_.jpg"},
    
        # -------- SMARTWATCH --------
        {"name": "Fire-Boltt Phoenix Pro", "category": "Smartwatch", "price": 2499, "stock": 80, "description": "BT Calling smartwatch with HD display.", "image_url": "https://m.media-amazon.com/images/I/71EVl0z2uTL._SL1500_.jpg"},
        {"name": "Boat Smart Ring Gen 2", "category": "Smartwatch", "price": 6999, "stock": 40, "description": "Smart fitness ring with health tracking.", "image_url": "https://m.media-amazon.com/images/I/61aU3DUzEIL._SL1500_.jpg"},
        {"name": "Noise ColorFit Pulse 2", "category": "Smartwatch", "price": 1999, "stock": 60, "description": "Color display smartwatch.", "image_url": "https://m.media-amazon.com/images/I/61Y30DpqRVL._SL1500_.jpg"},
        {"name": "Amazfit Bip 5", "category": "Smartwatch", "price": 4999, "stock": 50, "description": "Smartwatch with AMOLED display and Alexa built-in.", "image_url": "https://m.media-amazon.com/images/I/61yomcUvOGL._SL1500_.jpg"},
        {"name": "Fastrack Reflex Vox", "category": "Smartwatch", "price": 2999, "stock": 60, "description": "Stylish smart band with heart rate monitor.", "image_url": "https://m.media-amazon.com/images/I/61KJ4G3v7IL._SL1500_.jpg"},
        {"name": "Samsung Galaxy Watch 6", "category": "Smartwatch", "price": 28999, "stock": 30, "description": "Premium smartwatch with advanced health tracking.", "image_url": "https://m.media-amazon.com/images/I/71clFBh-A+L._SL1500_.jpg"},
    
        # -------- APPAREL --------
        {"name": "Nike Air Zoom Pegasus", "category": "Apparel", "price": 6999, "stock": 40, "description": "Lightweight running shoes.", "image_url": "https://m.media-amazon.com/images/I/71cW9zdkSEL._SL1500_.jpg"},
        {"name": "Adidas Hoodie Men", "category": "Apparel", "price": 2999, "stock": 40, "description": "Cotton blend hoodie.", "image_url": "https://m.media-amazon.com/images/I/61G-hrP-c+L._SL1500_.jpg"},
        {"name": "Levi’s Jeans Men", "category": "Apparel", "price": 2399, "stock": 50, "description": "Slim-fit jeans for men.", "image_url": "https://m.media-amazon.com/images/I/81zJ8Z2yQtL._SL1500_.jpg"},
        {"name": "U.S. Polo Shirt", "category": "Apparel", "price": 1499, "stock": 60, "description": "Classic polo T-shirt.", "image_url": "https://m.media-amazon.com/images/I/71oXGH+pH0L._SL1500_.jpg"},
        {"name": "Puma T-Shirt Women", "category": "Apparel", "price": 999, "stock": 70, "description": "Soft cotton T-shirt.", "image_url": "https://m.media-amazon.com/images/I/71qXziE3hnL._SL1500_.jpg"},
        {"name": "Bata Formal Shoes", "category": "Apparel", "price": 2499, "stock": 30, "description": "Comfortable leather shoes.", "image_url": "https://m.media-amazon.com/images/I/61rHwSmA0IL._SL1500_.jpg"},
        {"name": "Red Tape Sneakers", "category": "Apparel", "price": 2999, "stock": 35, "description": "Casual sneakers with comfort sole.", "image_url": "https://m.media-amazon.com/images/I/71kYfjsO1FL._SL1500_.jpg"},
    
        # -------- BEAUTY --------
        {"name": "Philips Hair Dryer", "category": "Beauty", "price": 1599, "stock": 40, "description": "Compact and efficient hair dryer.", "image_url": "https://m.media-amazon.com/images/I/61Jq9Y2r8UL._SL1500_.jpg"},
        {"name": "L'Oreal Paris Shampoo", "category": "Beauty", "price": 549, "stock": 100, "description": "Anti-dandruff strengthening shampoo.", "image_url": "https://m.media-amazon.com/images/I/61qARiODm5L._SL1500_.jpg"},
        {"name": "Maybelline Fit Me Foundation", "category": "Beauty", "price": 499, "stock": 120, "description": "Matte + Poreless foundation.", "image_url": "https://m.media-amazon.com/images/I/61q9CzKXQML._SL1500_.jpg"},
        {"name": "Lakme Lipstick Set", "category": "Beauty", "price": 799, "stock": 90, "description": "Set of 3 matte lipsticks.", "image_url": "https://m.media-amazon.com/images/I/61WBGU4H3sL._SL1500_.jpg"},
        {"name": "Garnier Men Face Wash", "category": "Beauty", "price": 299, "stock": 150, "description": "Oil clear deep cleansing face wash.", "image_url": "https://m.media-amazon.com/images/I/71BR1Kk0DqL._SL1500_.jpg"},
        {"name": "Mamaearth Vitamin C Cream", "category": "Beauty", "price": 699, "stock": 80, "description": "Moisturizing face cream for glowing skin.", "image_url": "https://m.media-amazon.com/images/I/61ViPgXgG2L._SL1500_.jpg"},
    
        # -------- HOME & KITCHEN --------
        {"name": "Prestige Pressure Cooker 3L", "category": "Home & Kitchen", "price": 1499, "stock": 80, "description": "Durable aluminium cooker for daily cooking.", "image_url": "https://m.media-amazon.com/images/I/61yfXedY9bL._SL1500_.jpg"},
        {"name": "Philips Mixer Grinder 750W", "category": "Home & Kitchen", "price": 3499, "stock": 30, "description": "Powerful 3-jar mixer grinder.", "image_url": "https://m.media-amazon.com/images/I/61lKzv8Pz+L._SL1500_.jpg"},
        {"name": "Milton Thermosteel Flask 1L", "category": "Home & Kitchen", "price": 899, "stock": 100, "description": "Keeps drinks hot and cold for 24 hours.", "image_url": "https://m.media-amazon.com/images/I/61pQk13nvNL._SL1500_.jpg"},
        {"name": "Usha Ceiling Fan", "category": "Home & Kitchen", "price": 2499, "stock": 50, "description": "High-speed fan with energy-saving motor.", "image_url": "https://m.media-amazon.com/images/I/71o7XqT6iEL._SL1500_.jpg"},
        {"name": "LG Washing Machine 7kg", "category": "Home & Kitchen", "price": 34999, "stock": 10, "description": "Energy-efficient washing machine.", "image_url": "https://m.media-amazon.com/images/I/61AC3lHNfWL._SL1500_.jpg"},
        {"name": "Philips LED Bulb 12W", "category": "Home & Kitchen", "price": 299, "stock": 200, "description": "Energy-efficient bright white LED bulb.", "image_url": "https://m.media-amazon.com/images/I/61oDdU1G7xL._SL1500_.jpg"},
    
        # -------- ACCESSORIES --------
        {"name": "Skybags Laptop Bag", "category": "Accessories", "price": 1999, "stock": 35, "description": "Stylish laptop backpack.", "image_url": "https://m.media-amazon.com/images/I/71ZTKuE0j-L._SL1500_.jpg"},
        {"name": "Wildcraft Duffel Bag", "category": "Accessories", "price": 1799, "stock": 50, "description": "Travel duffel bag with large storage.", "image_url": "https://m.media-amazon.com/images/I/71hW8EJ5MEL._SL1500_.jpg"},
        {"name": "Under Armour Backpack", "category": "Accessories", "price": 2499, "stock": 40, "description": "Water-resistant backpack.", "image_url": "https://m.media-amazon.com/images/I/71vSRW1kXBL._SL1500_.jpg"},
        {"name": "Safari Trolley Bag", "category": "Accessories", "price": 3499, "stock": 30, "description": "Cabin-size rolling suitcase.", "image_url": "https://m.media-amazon.com/images/I/71U9UCPM6LL._SL1500_.jpg"},
                # -------- FRUITS --------
        {"name": "Apple (1kg)", "category": "Fruits", "price": 120, "stock": 100, "description": "Fresh and juicy apples from Himachal.", "image_url": "https://m.media-amazon.com/images/I/71ljtZyoe9L._SL1500_.jpg"},
        {"name": "Banana (1 dozen)", "category": "Fruits", "price": 60, "stock": 80, "description": "Naturally sweet bananas full of energy.", "image_url": "https://m.media-amazon.com/images/I/71xJ8ERzRvL._SL1500_.jpg"},
        {"name": "Orange (1kg)", "category": "Fruits", "price": 90, "stock": 90, "description": "Citrus fruit rich in Vitamin C.", "image_url": "https://m.media-amazon.com/images/I/71qQF1lGg4L._SL1500_.jpg"},
        {"name": "Watermelon (1 piece)", "category": "Fruits", "price": 80, "stock": 60, "description": "Refreshing summer fruit.", "image_url": "https://m.media-amazon.com/images/I/81ErKX6zSXL._SL1500_.jpg"},
        
        # -------- VEGETABLES --------
        {"name": "Tomato (1kg)", "category": "Vegetables", "price": 40, "stock": 100, "description": "Fresh red tomatoes for cooking.", "image_url": "https://m.media-amazon.com/images/I/81QRRwaZlvL._SL1500_.jpg"},
        {"name": "Potato (1kg)", "category": "Vegetables", "price": 35, "stock": 120, "description": "Premium quality potatoes.", "image_url": "https://m.media-amazon.com/images/I/91zKpQ8sDVL._SL1500_.jpg"},
        {"name": "Onion (1kg)", "category": "Vegetables", "price": 45, "stock": 110, "description": "Fresh onions directly from farm.", "image_url": "https://m.media-amazon.com/images/I/91R1k+3NSeL._SL1500_.jpg"},
        {"name": "Cabbage (1 piece)", "category": "Vegetables", "price": 30, "stock": 80, "description": "Green leafy fresh cabbage.", "image_url": "https://m.media-amazon.com/images/I/81LQnJtM7zL._SL1500_.jpg"},
        
        # -------- FOOD ITEMS --------
        {"name": "Britannia Bread", "category": "Food", "price": 45, "stock": 50, "description": "Soft and fresh bread loaf.", "image_url": "https://m.media-amazon.com/images/I/61pPqRyBf8L._SL1500_.jpg"},
        {"name": "Amul Butter 500g", "category": "Food", "price": 275, "stock": 40, "description": "Rich and creamy salted butter.", "image_url": "https://m.media-amazon.com/images/I/71hZ5l48ciL._SL1500_.jpg"},
        {"name": "Maggie Noodles 12 Pack", "category": "Food", "price": 180, "stock": 100, "description": "Instant noodles ready in 2 minutes.", "image_url": "https://m.media-amazon.com/images/I/81YxR8nKZ-L._SL1500_.jpg"},
        {"name": "Kissan Tomato Ketchup", "category": "Food", "price": 95, "stock": 70, "description": "Tasty ketchup made from real tomatoes.", "image_url": "https://m.media-amazon.com/images/I/81g1dEvWb7L._SL1500_.jpg"},
        
        # -------- SPORTS & PLAYING ITEMS --------
        {"name": "Cosco Football", "category": "Sports", "price": 899, "stock": 30, "description": "Durable and waterproof football.", "image_url": "https://m.media-amazon.com/images/I/81LSe0cDqfL._SL1500_.jpg"},
        {"name": "SG Cricket Bat", "category": "Sports", "price": 1499, "stock": 25, "description": "Lightweight cricket bat for practice.", "image_url": "https://m.media-amazon.com/images/I/71kQ5ZbW1aL._SL1500_.jpg"},
        {"name": "Nivia Badminton Racket", "category": "Sports", "price": 699, "stock": 40, "description": "Perfect racket for beginners.", "image_url": "https://m.media-amazon.com/images/I/61mDJjjW08L._SL1500_.jpg"},
        {"name": "GM Cricket Ball", "category": "Sports", "price": 199, "stock": 100, "description": "Leather cricket ball for training.", "image_url": "https://m.media-amazon.com/images/I/71oz6qPM1aL._SL1500_.jpg"},
        # -------- AUTO-GENERATED MISC PRODUCTS --------
    ] + [
        {
            "name": f"Product {i}",
            "category": "Misc",
            "price": 499 + (i * 5),
            "stock": 10 + (i % 40),
            "description": f"Auto-generated test product number {i}.",
            "image_url": f"https://picsum.photos/300?random={i}"
        }
        for i in range(51, 201)
    ]


    print("\n🛍️ Adding Products (keeping old ones)...\n")
    for p in products:
        if not Product.objects.filter(name=p['name']).exists():
            Product.objects.create(**p)
            print(f"✅ Added: {p['name']}")
        else:
            print(f"⏩ Skipped (already exists): {p['name']}")

    print("\n🎉 Done seeding all products!\n")

if __name__ == '__main__':
    run()
