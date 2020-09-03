# Pralinörskan-app


Milestone project: Full Stack Frameworks with Django.

![Image of responsive](https://timmy-bergkvist.github.io/Pralinorskan-app/media/pralinorskan.display.jpg)

This project is part of the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course.

**Target Audience**
 
Pralinörskan is a ecommerce app that allows customer to choose between 30+ different variations of pralines such as Vegan, Gluten free and Special Offers.
Customers can choose to have them delivered to their one country with payment using Stripe.
Customers also have the option to save their profile details for future purchases and to view order history from older purchases.

When testing this app, to make a payment, the following details should be provided:

- Card number: 4242 4242 4242 4242
- CVC: any three numbers
- Date: any future date
- ZIP Code: any five numbers


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
    + [User Stories Testing](#user-stories-testing)
    + [Bugs](#bugs)
 
</details>
<details>
<summary>Deployment</summary>

  * [Deployment](#deployment)
    + [Local deployment](#local-deployment)
    + [Heroku deployment](#heroku-deployment)
    + [Amazon Web Services s3 deployment](#amazon-web-services-s3-deployment)
 
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
  
  - **Profile:** Containing customer information and the options to edit and delete customer information.
  
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

![Image of database](https://timmy-bergkvist.github.io/Pralinorskan-app/media/new-database-design.jpg)

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
|Button|Shop Now|Sends the customer to the right page|No bugs|
|Button|Navbar toggler|Displays all links. Sends the customer to the right page|No bugs|
|Button|Login|Logs in the customer and redirect to home page. Toast popup|No bugs|
|Button|Register|Registers the customer. Toast popup. Registration confirmation email sent|No bugs|
|Button|Add to cart|Adds items to cart. Toast popup|No bugs|
|Button|Decrement/Increment|Adds the right amount|No bugs|
|Button|Update Information|Updates customers contact information|No bugs|
|Button|Delete user account|Delete all user information and redirects to home page|No bugs|
|Button|Complete Order|Complete customers order. Order email sent. Redirects the customer to checkout success page|No bugs|
|Link|Image|Clicking on product image redirect customer to product page|No bugs|
|Link|Order number|Sends the customer to right order number page. Displays all information about the purchase|No bugs|
|Link|Login|Sends the customer to right page|No bugs|
|Link|Register|Sends the customer to right html|No bugs|
|Link|Navbar|Sends the customer to right pages|No bugs|
|Link|Main logo|Sends the customer to home page|No bugs|
|Link|Product detail|Sends the customer to right page. Displays right item|No bugs|
|Functions|Paginator|Displays the right pages. Clicking the numbers Sends the customer to right page|No bugs|
|Functions|Sort|Sorts the right categorys|No bugs|
|Functions|Order Summary|Calculates the order summary|No bugs|
|Functions|Quantity|Calculates the quantity. Updates the quantity|No bugs|
|Functions|Delivery cost|Calculates the delivery cost|No bugs. But displaying the wrong amount|
|Functions|Forms|Displays the right form. Saves the right information|No bugs|
|Structure|Mobile view|Tested on iphone 6s and 8|No bugs|
|Structure|Tablet view|Tested on google chrome debugger tool|No bugs|
|Structure|Desktop view|Tested on Asus 13 inch and lenovo 15,6 ince|No bugs|
|Structure|Web browser|Tested on Firefox, Chrome and Brave|No bugs. But some of the font awesome features may not work properly|
|Structure|Navbar|Works in mobile and tablet view. Sends the customer to right html.|No bugs. Responsive is working|
|Structure|Navbar toggler|Works in mobile and tablet view. Sends the customer to right page|No bugs|
|Structure|Content|Stays in the midle. Works in mobile and tablet view.|No bugs. Responsive is working|
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

#### User Stories Testing
<details>

<summary>Click to see User Stories Testing</summary>

User Story 1:
- Any customer have the options to sign up and buy products and save their billing information for future purchases.
  By doing so the customer needs to registrate by using the registration form and provide email, username and password.
  Customers also have the options to buy as a non registered customer.
  
User Story 2:
- On the profile page customer can delete and update their account. By updating their account, the customer must fill in the form and then click on the update button.
  By deleting their account, the customer just click the delete button, a pop up will appear and ask the customer if they really want to delete the account.

User Story 3:
- Customer can add products that they want to buy and the cart in the right corner will show the amount for each added item.
  By adding an item, a pop up will be displayed with images of the items that the customer has added and Proceed to checkout button.
  By clicking Proceed to checkout button and the cart logo will take the customer to Shopping Cart page.

User Story 4:
- On the Shopping Cart page, customer have the options to update and remove items from the cart.
  A card will display total, delivery, grand total and a Proceed to checkout button.
  When the customer feels satisfied with the items that will be purchased he/she can then kick on Proceed to checkout button that will take the customer to checkout page.

User Story 5:
- On the checkout page, customer need to fill in a form with the billing informations and add their card information to make a purchase.
  If the customer is not registered there will be an option to login or create an account link.
  If the customer is registered there will be an option to save billing information.
  When the customer is ready, he/she can then press the Complete Order button.
  Klicking Complete Order button will send the user an email confirmation with order information and redirect the user to checkout success page
  that displays all the billing and purchase information.
  
User Story 6:
- On the order history page, the entire purchase history with order number, date, items and order total will be displayed.
  Clicking order number will redirect customer to checkout success page.
 
</details>
 
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


## Amazon Web Services s3 deployment

<details>

<summary>Click to see AWS s3 deployment instructions</summary>

This project store static files and images on Amazon Web Services s3.
Which is a cloud-based storage service.

> Instructions:

  I.  Create an account
```shell
First create a user account at https://aws.amazon.com/
And sign-in in the upper right by accessing the AWS management console under my account.
```
![Image of set up step1](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step1-img.jpg)
```shell
Search or open s3 and create a new bucket. Which will be used to store files.
```
![Image of set up step2](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step2-img.jpg)

  II.  Create bucket.
```shell
Click create bucket and give the bucket a name, recommend naming your bucket to match your Heroku app name.
```
![Image of set up step3](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step3-img.jpg)
![Image of set up step4](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step4-img.jpg)

```shell
Select a region closest to you and uncheck block all public access and acknowledge that the bucket will be public.
This bucket will need to be public in order to allow public access to our static files.
```
![Image of set up step5](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step5-img.jpg)


  III.  Settings on bucket.
```shell
Click properties tab and turn on static website hosting.
This give you a new endpoint that you can use to access it from the internet.
For the index and error document, just fill in some default values. 
```
![Image of set up step6](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step6-img.jpg)

```shell
On the permissions tab  make this three changes.
paste in a coors configuration
which is going to set up the required access between our Heroku app and this s3 bucket.

<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
![Image of set up step7](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step7-img.jpg)

```shell
Next I'll go to the bucket policy tab.
And select, policy generator to create a security policy for this bucket.
```
![Image of set up step8](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step8-img.jpg)

```shell
The policy type is going to be s3 bucket policy.
Will allow all principals by using a star.
And the action will be, get object.
```
![Image of set up step9](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step9-img.jpg)

```shell
Copy the ARN "Amazon resource name" from the other tab.
And paste it into the ARN box at the bottom.
Click Add statement then generate policy.
```
![Image of set up step10](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step10-img.jpg)

```shell
Then copy this policy into the bucket policy editor.
Before you click Save you want to allow access to all resources in this bucket.
Add a slash star onto the end of the resource key.
Now click Save.
So our bucket policy and course configuration will now allow full access to all resources in this bucket.
```
![Image of set up step11](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step11-img.jpg)

```shell
Last thing you need to do to configure it is to go to the access control list tab
and set the list objects permission for everyone under the Public Access section.
```
![Image of set up step12](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step12-img.jpg)


  IV.  Identity and Access Management.
```shell
Go to the services menu and search or open Iam. "Identity and Access Management".
Click groups and then create new group.
Give the group a name and click next two times.
```
![Image of set up step13](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step13-img.jpg)
![Image of set up step14](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step14-img.jpg)

```shell
Nex create the policy.
Click policies and then create policy.
Go to the JSON tab and then select import managed policy which will let you import one that AWS has pre-built for full access to s3.
```
![Image of set up step15](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step15-img.jpg)
![Image of set up step16](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step16-img.jpg)

```shell
Search for s3 and then import the s3 full access policy.
```
![Image of set up step17](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step17-img.jpg)

```shell
You don't want to allow full access to everything you only want to allow full access to your new bucket and everything within it.
Copy the bucket ARN from the bucket policy page in s3.
click review policy.
Give it a name and a description.
Then click create policy.
```
![Image of set up step18](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step18-img.jpg)

```shell
Then attach the policy to the group you created.
Go back to groups, click into your created group.
Click permissions and attach policy.
Search for the policy you just created and select it.
And click attach policy.
```
![Image of set up step19](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step19-img.jpg)

```shell
Nex create the user.
Click users and then add user.
```
![Image of set up step20](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step20-img.jpg)

```shell
Create a user named <your-app-name>-staticfiles-user.
Give them programmatic access.
```
![Image of set up step21](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step21-img.jpg)

```shell
Now you can put the user in our group.
You don't need to change anything else, click through to the end and then click create user.
```
![Image of set up step22](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step22-img.jpg)

```shell
Next download and save this CSV which will contain this users access key and secret access key to authenticate them from your django app.
It's important to download and save this CSV because once you gone through this process you can't download them again.
```

  V.  Conect Django
```shell
First you need to install boto and django-storages for this project I needed to install both boto and boto3.

pip install boto
pip install boto3
pip install django-storages

next do a

pip freeze > requirements.txt
```

  VI.  Setup in settings
```shell
Then add 'storages' to your settings.py file at INSTALLED_APPS

Tell it which bucket it should be communicating with.

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = '<your-app-name>'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

  VII.  Setup in Heroku

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

  VIII.  Custom storages
  
 Use s3 to store our static files whenever someone runs collectstatic.
 And that we want any uploaded product images to go there also.

Create a custom storages file.
```shell
custom_storages.py
```
Next add this function in to it.
```shell
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

Next push it up to github
```shell
git add .
git commit -m "Set up for Amazon Web Services s3"
git push origin master
```

  IX.  Upload images and files
```shell
Next go to s3 and create a new folder called media.
```
![Image of set up step23](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step23-img.jpg)

```shell
Inside it, click upload. Add files. And then select all the product images.
Now click Next and under manage public permissions select grant public read access to these objects.
Click next through to the end here. And then click upload.
```
![Image of set up step24](https://timmy-bergkvist.github.io/Pralinorskan-app/media/set-up-step24-img.jpg)

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
