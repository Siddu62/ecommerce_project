 E-Commerce Web Application (Django + REST API)
This is a **Full Stack Django-based E-Commerce Platform** built for the **Full Stack Developer Assignment (Sepnoty)**.  
It includes complete user and admin functionalities with JWT Authentication, Product Management, Order Management, and an elegant UI

 Features
- User registration and login (JWT Authentication)
- Browse and search products by category
- Add to Cart, manage quantity
- Add shipping address and checkout
- Place orders and view order history
Admin Panel
- Admin authentication (JWT + Role-based access)
- Product CRUD (Create, Read, Update, Delete)
- Pagination, search, and category filters
- Order management with status updates
- Export orders to CSV
- Dashboard with key metrics

Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Backend | Django, Django REST Framework |
| Database | SQLite (can switch to MySQL easily) |
| Auth | JWT Authentication |
| Tools | VS Code / PyCharm, CMD, Git, GitHub |

 Setup Instructions (Local Development)

1. **Clone this repo**
   ```bash
   git clone https://github.com/Siddu62/ecommerce_project.git
   cd ecommerce_project

2.Install dependencies
  pip install -r requirements.txt
3. Run migrations
  python manage.py makemigrations
  python manage.py migrate
4. Seed data (products & admin user)
  python seed_scripts/seed_data.py  
5. Run the development server
  python manage.py runserver  
