## Django POS - Coffee Shop Point of Sale System
### Project Overview
django-pos is a Point of Sale (POS) system designed for coffee shops, offering backend management and frontend ordering capabilities. The backend allows administrators to manage menu items and inventory, while the frontend provides an intuitive menu display, shopping cart, and checkout functionality. The system features a modern, responsive web design (RWD) to ensure a seamless experience across devices.
Key Features

### Backend Management
Menu Content Management: Add/edit menu items (including images, names, prices, and required ingredients).
Inventory Management: Manage ingredient items and quantities.

### Frontend Ordering
Menu Display: Showcase menu items with images and prices.
Shopping Cart: Users can add items to the cart and view the total.
Checkout: Complete orders (currently without payment gateway integration).

### Technologies Used

- Backend: Python 3.10, Django 4.2.7
- Database: MySQL 8.0
- Containerization: Docker, Docker Compose
- Frontend: HTML, Tailwind CSS (CDN), JavaScript
- Other: Pillow (image processing), Gunicorn (production server)

### Installation Steps

Follow these steps to set up and run the django-pos project. Ensure Docker and Docker Compose are installed on your system.
1. Clone the Repository
git clone <your-repository-url>
cd django-pos

2. Configure the Environment
Verify that the following files are present and correctly configured:

- Dockerfile: Defines the Django application container.
- docker-compose.yml: Configures Django and MySQL services.
- requirements.txt: Lists Python dependencies.
- pos/pos/settings.py: Ensure database connection parameters are correct.

3. Build and Start Containers
Run the following command in the project root directory to build and start the Docker containers:

``` shell
docker-compose up --build
```

This will:

Build the Django application image.
Start the MySQL database and Django server.
Automatically apply database migrations (python manage.py migrate).

The Django server will be accessible at http://localhost:8000.

4. Create a Superuser
To access the backend management features, create a superuser:
docker-compose exec web python manage.py createsuperuser

Follow the prompts to enter a username, email, and password.

5. Access the Application

Backend Management: Visit http://localhost:8000/admin/ and log in with the superuser credentials to manage menus and inventory.
Frontend Ordering: Visit http://localhost:8000/ to browse the menu, add items to the cart, and checkout.

6. Collect Static Files (Optional)
If you need to serve static files, run:
docker-compose exec web python manage.py collectstatic

7. Stop Containers
To stop the running containers, execute:
docker-compose down
