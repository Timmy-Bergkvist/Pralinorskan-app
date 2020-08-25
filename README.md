# Pralinörskan-app


Milestone project: Full Stack Frameworks with Django.

![Image of responsive](https://timmy-bergkvist.github.io/Pralinorskan-app/media/pralinorskan.display.jpg)

This project is part of the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course.

**Target Audience**
 
Pralinörskan is a ecommerce app that allows customer to choose between 30+ different variations of pralines such as Vegan, Gluten free and Special Offers.
Customers can choose to have them delivered to their one country with payment using Stripe.
Customers also have the option to save their profile details for future purchases and to view order history from older purchases.


## Table of Contents
<details>
<summary>UX</summary>
 
  * [UX](#ux)
    + [Project sections:](#project-sections)
    + [User Stories](#user-stories)
    + [Mockups](#mockups)
 
</details>
<details>
<summary>Features</summary>
 
  * [Features](#features)
    + [Existing Features](#existing-features)
  	 + [Features Left to Implement](#features-left-to-implement)
 
</details>
<details>
<summary>Technologies</summary>

  * [Technologies Used](#technologies-used)
    + [Language](#language)
    + [Libraries and frameworks](#libraries-and-frameworks)
    + [Tools](#tools)
 
</details>
<details>
<summary>Database</summary>

  * [Database structure](#database-structure)
    + [Database Design](#database-design)
    + [Database Tables](#database-tables)
    + [Database Workflow](#database-workflow)
 
</details>
<details>
<summary>Testing</summary>

  * [Testing](#testing)
    + [Testing tools](#local-deployment)
    + [Tests](#tests)
    + [Stripe payment testing](#stripe-payment-testing)
    + [Bugs](#bugs)
 
</details>
<details>
<summary>Deployment</summary>

  * [Deployment](#deployment)
    + [Local deployment](#local-deployment)
    + [Heroku deployment](#heroku-deployment)
 
</details>
<details>
<summary>Credits</summary>

  * [Credits](#credits)
    + [media](#media)
    + [Acknowledgements](#acknowledgements)
 
</details>

## UX

#### Project sections:

  - **Header and navbar:** Containing a logo, Home, Products, Special Offers, My Account logo, Cart logo and Login/Logout links.
           
  - **Homepage:** Containing a welcome message and images of the stores best selling products.
  
  - **Products:** Containing all products that the store is selling.
  
  - **Product:** Containing specific information and image about the product.

  - **Sign up form:** Containing a form that enables customer to sign up for the app.
  
  - **Login form:** Containing a form that enables customer to login for the app.
  
  - **Shopping cart:** Contains information on products that are posted by the customer ready to be purchased, updated or deleted.
  
  - **Checkout:** Contains a form to be filled by the customer to make the payment and delivery.
  
  - **Profile:** Containing customer information and the options to edit customer information.
  
  - **Order history:** Containing information of previous purchases.
  
  - **Footer:** Displays information and links to social medias.

#### User Stories

None registered customer:
- As a customer, I want to access the platform from a desktop, tablet and a smartphone.
- As a customer, I want to view several kinds of products.
- As a customer, I want to buy products.
- As a customer, I want to view a specific kind of product.
- As a customer, I want to update the amount of products in my cart.
- As a customer, I want to remove products in my cart.
- As a customer, I want to make online payments.
- As a customer, I want to see details of a specific product.
- As a customer, I want to receive orderdetails to my email.
- As a customer, I want to registrate for an account.
- As a customer, I want to login and logout of the account.

Registered customer:
- As a registered customer, I want to view order history from previous purchases.
- As a registered customer, I want to view all my products to see the total amount.

Admin user:
- As a admin, I want to add, remove and update products.
  
#### Mockups
  
  I have used Figma Mockups to visualize images I can work from.

- <a href="media/mockup-desktop.jpg" target="_blank">Desktop</a>

- <a href="media/mockup-mobile.jpg" target="_blank">Phone</a>

- <a href="media/mockup-tablet.jpg" target="_blank">Tablet</a>


## Features

#### Existing Features

##### Navbar:
- A hamburger menu button that will display options in phone and tablet mode.
- Products on click a drop down menu will be displayed with different products alternatives.
- Logo on click redirects the customer to home page.
- Home on click redirects the customer to home page.
- Cart on click redirects the customer to cart page.
- Special Offers on click redirects the customer to Special Offers page.
###### Logged In:
  - My Account on click gives the customer three options to choose between Profile detail, Order History and Logout
  - Order History on click redirects the customer to order history page.
  - Profile detail on click redirects the customer to profile detail page.
  - Logout on click redirects the customer to logout form.

###### Logged Out:
  - Register on click redirects the customer to register form.
  - Login on click redirects the customer to login form.

##### Home page:
- Button. Redirects the customer to products page.
- Cards images. Four cards of the stores best selling products. If the customer click the card it will redirect 
  the customer to that specific product page.

##### Toast:
- Toast messages. Will highlight different right, wrong and info actions in the top right corner.

##### Products page:
- Cards with product name, image, price and category. Clicking the card will redirect the customer that specific product page.
- Return to top button will be displayed if page is scrolled more than 200px.
- Pagination at the bottom of the page. Displays how many pages of products there is.

##### Producks detail page:
- Add to cart button. Will add the product to the cart.
- Increment and Decrement buttons. Option to increase or decrease the amount of items to be in the cart.
- Image. Clicking the image will display a bigger image.

##### Profile page:
- Order form. Displays a form with the customer's order number and order history.
- Order number link. Redirects the customer to more detailed order information.
- Customer informaton. Displays a form with the customer's current information.
- Update button. Updates the form with the customer's information.
- Home button. Redirects the customer to products page, will only be displayed if the customer is not registered.
- Orders button. Redirects the customer to order history page, will only be displayed if the customer is registered.

##### Cart page:
- Delete button. Delete the specific product information.
- Update button. Updates the amount of items in the cart.
- Increment and Decrement buttons. Option to increase or decrease the amount.
- Back to home button. Redirects the customer to products page.
- Checkout button. Redirects the customer to checkout page.

##### Checkout page:
- Billing information form. Form that needs to be filled in by customer to make a order.
- Payment fieldset. A fieldset that needs to be filled with card number, CVC and expiration date.
- Submit button. Submits the order and redirects the customer to checkout success that displays order information.
- Save check label. Gives the customer the option to save order details for future purchase.
- Login link. Gives the customer the option to login before purchase.
- Register link. Gives the customer the option to get registered before purchase.
- Adjust cart button. Redirects the customer to cart page.

##### Footer:
- Social links. On click redirects the customer to Facebook, Twitter, Instagram and Linkedin.



#### Features Left to Implement

- Delete customer information button.

- Contact page so the customer can send emails directly from the store.

- Sort flavors function on the all product page.

- Search function on the all product page.

- Comment section so the customer can comment, review and rate.

- Ingredients information in products detail to view more information about the products.

- Automatic update on the increment and decrement buttons in cart, instead of having an update button.


## Technologies Used

#### Language

- <a href="https://en.wikipedia.org/wiki/HTML" target="_blank"> Html </a>
  
- <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" target="_blank"> Css </a>

- <a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank"> JavaScript </a>

- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank"> Python </a>


#### Libraries and frameworks

- <p><a href="https://www.djangoproject.com/" target="_blank"> Django</a>- A python web-framework to build projects.</p>

- <p><a href="https://getbootstrap.com/" target="_blank"> Bootstrap</a>- A CSS library grid.</p>

- <p><a href="https://fontawesome.com/" target="_blank"> Fontawesome</a>- Provides icons.</p>

- <p><a href="https://fonts.google.com/" target="_blank"> Google fonts</a>- Custom font styling.</p>

- <p><a href="https://jinja.palletsprojects.com/en/2.11.x/" target="_blank"> Jinja</a>- A template language for python.</p>

- <p><a href="https://pypi.org/project/psycopg2-binary/#description" target="_blank"> Psycopg2</a>- Python PostgreSQL adapter.</p>

- <p><a href="https://jquery.com/" target="_blank"> Jquery</a>- Javascript library to simplify the code.</p>

- <p><a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html" target="_blank"> Boto3 </a>- A library that enables python code to modify AWS service.</p>


#### Tools

- <p><a href="https://en.wikipedia.org/wiki/Heroku" target="_blank"> Heroku </a>- For hosting the application and deploy.</p>

- <p><a href="https://stripe.com/ie" target="_blank"> Stripe </a>- Payment platform to accept and process payments online</p>

- <p><a href="https://code.visualstudio.com/" target="_blank"> VS Code </a>- Code editor</p>

- <p><a href="https://www.figma.com/" target="_blank"> Figma </a>- A collaborative interface design tool.</p>

- <p><a href="https://en.wikipedia.org/wiki/Amazon_Web_Services" target="_blank"> Amazon Web Services</a>- A cloud computing services.</p>
  
## Database structure

I have used <a href="https://www.sqlite.org/index.html" target="_blank">SQLite 3</a> database for the project to store data locally.

I have used <a href="https://en.wikipedia.org/wiki/PostgreSQL" target="_blank">PostgreSQL</a> in Heroku for the project to store the data for the deployed application.

#### Database Tables
User profile, categories, products, cart contents, order and order details

#### Database Design

![Image of database](https://timmy-bergkvist.github.io/Pralinorskan-app/media/database-design.jpg)

#### Database Workflow
<details>
<summary>Click to see database workflow</summary>
 
![Image of workflow](https://timmy-bergkvist.github.io/Pralinorskan-app/media/database-workflow1.jpg)
 
</details>

## Testing 

#### Testing tools
  - The responsiveness is run and tested at:
    - http://ami.responsivedesign.is/#

  - The HTML code is run and tested at:
    - https://validator.w3.org/#validate_by_input
    - If you run the code you will get bad value and text not allowed in element,
    this is because I'm using
    <a href="https://en.wikipedia.org/wiki/Jinja_(template_engine)" target="_blank"> Jinja (template engine)</a>
  
  
  - The CSS code is run and tested at:
    - https://jigsaw.w3.org/css-validator/#validate_by_input
    
  - The JavaScript is run and tested at:
    - https://jshint.com/  
    
  - The Python is run and tested at:
    - http://pep8online.com/
    - 

#### Tests

|**Feature type**|**Feature**|**Tests**|**Bugs**|
| :---: |:---:| :---:|:---:|
|Button|Add to Cart|Getting  the right items. Posts the right items|No bugs|
|Button|Shop Now|Sends the customer to the right html|No bugs|
|Button|Navbar toggler|Displays all links. Sends the customer to the right html|No bugs|
|Button|Login|Logs in the customer to home page. Toast popup|No bugs|
|Button|Register|Registers the customer. Toast popup. Registration confirmation email sent|No bugs|
|Button|Add to cart|Adds items to cart. Toast popup|No bugs|
|Button|Decrement/Increment|Adds the right amount|No bugs|
|Link|Login|Sends the customer to right html|No bugs|
|Link|Register|Sends the customer to right html|No bugs|
|Link|Navbar|Sends the customer to right pages|No bugs|
|Link|Main logo|Sends the customer to home page|No bugs|
|Link|Product detail|Sends the customer to right page. Displays right item|No bugs|
|Structure|Navbar|Works in mobile and tablet view. Sends the customer to right html.|Responsive is working. No bugs|
|Structure|Navbar toggler|Works in mobile and tablet view. Sends the customer to right html.|No bugs|
|Structure|Content|Stays in the midle. Works in mobile and tablet view.|Responsive is working. No bugs|
|Structure|Footer|Stays at the bottom. Works in mobile and tablet view.|No bugs|

#### Stripe payment testing

```shell
The hosted demo is running in test mode use 4242424242424242 as a test card number with any CVC + future expiration date.
Use the 4000000000003220 test card number to trigger a 3D Secure challenge flow.
Read more about test cards on Stripe at https://stripe.com/docs/testing.
```
|**NUMBER**|**BRAND**|**CVC**|**DATE**|
| :---: |:---:| :---:|:---:|
|4242424242424242|Visa|Any 3 digits|Any future date|
|4000056655665556|Visa (debit)|Any 3 digits|Any future date|
|5555555555554444|Mastercard|Any 3 digits|Any future date|
|2223003122003222|Mastercard (2-series)|Any 3 digits|Any future date|


#### Bugs

  - Stripe card element in mobile view:
```shell
    When the customer types in the card number, CVC and date the numbers overlap and it looks messy.
    It does not affect the purchase but it looks bad from a user's experience.
    This is an issue from Stripe in card element.
```
  
## Deployment
  
  
 The hosting platform for this project is Heroku and can be run directly here: 
 https://pralinorskan-app.herokuapp.com/
  
  
To run this project you need the following tools installed:

  - <a href="https://www.python.org/downloads/" target="_blank"> Python3 </a>
  - <a href="https://code.visualstudio.com/" target="_blank"> VS Code </a> or a code editor that have a debug tool.
  - <a href="https://git-scm.com/" target="_blank"> Git </a>
  - <a href="https://en.wikipedia.org/wiki/Heroku" target="_blank"> Heroku </a>

## Local deployment
<details>

<summary>Click to see local deployment instructions</summary>

The following instructions are based on Windows 10 and VS Code editor.

> Instructions:

  I.    Clone the repository in Github
 ```shell
  git clone <repository name>.git
 ```

  II.   Install all the packages that are required
```shell
pip install python
pip install django
pip install django-allauth

For more information:
https://django-allauth.readthedocs.io/en/latest/installation.html

```
  III.   Use django-admin startproject <app-name> dot
```shell
  django-admin startproject pralinorskan_app .
```

  IV.   create a virtual environment with the command:
```shell
 python -m venv env
```

  V.   Activate an environment
```shell

virtualenv env
source env/bin/activate

For more information:
https://code.visualstudio.com/docs/python/environments
```

  VII.   Migrate the models to crete a database template.
```shell
python manage.py migrate
```

  VIII.   Create a super user to have access to the admin page.
```shell
python manage.py createsuperuser
```


  IX.   Run the application
```shell
python manage.py runserver

Open the website at http://127.0.0.1:8000
```

  X.   Set up environment variable keys.
```shell
SECRET_KEY = os.environ.get('SECRET_KEY','')

# Don't run with debug turned on/True in production!
DEBUG = 'DEVELOPMENT' in os.environ

DATABASES = {
  'default': {
     'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

""" STRIPE API Keys """
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

""" Email Keys """
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = '<your app name>@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```

  XI.  Set up the env path to manage.py
```shell
from os import path
if path.exists("env.py"):
    import env

```

  XII.  Log into your admin account add the /admin path at the end of the url link.
```shell
http://127.0.0.1:8000/admin
```

</details>

## Heroku deployment

<details>

<summary>Click to see Heroku deployment instructions</summary>

This project is hosted using Heroku.

> Instructions:

  I.  Install Heroku
```shell
npm install -g heroku
heroku login
cd my-project/
git init
       
Existing Git repository:heroku git:remote -a <app name>
```

  II. Install the necessary requirements
```shell
pip install dj_database_url
pip install psycopg2-binary
pip install gunicorn
```

  III.  Generate a requirements file and then install from it in another environment.
```shell
pip freeze > requirements.txt
```

  IV. Seting up Heroku.
```shell
On the resources tab select:
Heroku Postgres Database
```

  V.  Setting up to connect to Heroku Postgres Database In settings.py.
```shell
Step 1 import dj_database_url

Step 2 comment out the default configuration.
#DATABASES = {
#  'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#  }
#}

Step 3  replace the default database with a call to dj_database_url.parse
        And give it the database URL from Heroku.

DATABASES = {
        'default': dj_database_url.parse('postgres://<your database url>')
      }

Step 4 Migrate.
python manage.py migrate

step 5 Load the categories and products. 
It is important to do them in this order!

1. python manage.py loaddata categories
2. python manage.py loaddata products
3. python manage.py createsuperuser

Step 6 Put back everything as it was.
when everything is migrate and done remove the Heroku database config.
And uncomment the original so it doesn't end up in version control and then set up the databases like this.

if 'DATABASE_URL' in os.environ:
    DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL',''))
    }
else:
    DATABASES = {
          'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
    
  VI. Create a Procfile
```shell
echo web: python app.py > Procfile

web: gunicorn <your application name>.wsgi:application
```

  VII.  Login to Heroku and temporarily disable collectstatic,
        So that Heroku won't try to collect static files on deploy.
```shell
Heroku config:set DISABLE_COLLECTSTATIC=1 --app <your app name>
      
```
VIII. Set hostname of our Heroku app in settings.py
```shell
      ALLOWED_HOSTS = ['<your app name>', 'localhost', '127.0.0.1']
      
```
IX. Set the config variables in your Heroku settings.

|**KEY NAME**|**KEY VALUE**|
| :---: |:---:|
|AWS_ACCESS_KEY_ID|your aws access key|
|AWS_SECRET_ACCESS_KEY|your aws secret access key|
|DATABASE_URL|your database url|
|EMAIL_HOST_PASS|your email host password|
|EMAIL_HOST_USER|your email@gmail.com|
|HEROKU_HOSTNAME|your heroku hostname.herokuapp.com|
|SECRET_KEY|your secret key|
|STRIPE_PUBLIC_KEY|your stripe public key|
|STRIPE_SECRET_KEY|your stripe secret key|
|STRIPE_WH_SECRET|your stripe webhook key|
|USE_AWS|True|

 
 X. Deploy your application to Heroku
```shell
git add .
git commit -am "make it better"
git push heroku master
       
Existing Git repository:
heroku git:remote -a <app name>
```
 
</details>

## Credits
  
   #### media
  - The photos used in this site were obtained from:

    - https://pixabay.com/sv/
    
    - https://www.pngjoy.com/

    - https://www.pngwave.com/
    

   #### Acknowledgements
  - Inspiration for this project was obtained from:
    -  Code Institute Frameworks with Django.
    
    - https://nordicoil.se/eir-cbd-kraem-foer-psoriasis
    
    - https://www.templatemonster.com/blog/top-45-ecommerce-business-ideas/
    
I wanna say thank you to my mentor Oluwafemi Medale for helping me through this project.
