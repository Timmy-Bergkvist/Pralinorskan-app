# Pralinörskan-app


Milestone project 4: Full Stack Frameworks with Django - Code Institute

![Image of responsive](https://put-your-application-image-here.jpg)


**Target Audience**
 
Pralinörskan is a ecommerce app to sell pralines with different variations of flavors and quantity.

  

## UX

**Project sections:**

  - Homepage: Containing a welcome message and a button that will redirect the user to product site and
    different options for products.
  
  - Products: Containing all products that the store is selling.
  
  - Product: Containing specific information and image about the product.

  - Sign up form: Containing a form that enables user to sign up for the app.
  
  - Login form: Containing a form that enables user to login for the app.
  
  - Shopping cart: Contains information on products that are posted by the user ready to be purchased, updated or deleted.
  
  - Checkout: Contains a form to be filled by the user to make the payment and delivery.
  
  - Profile: Containing user information and the options to delete and edit the acount.
  
  - Order history: Containing information of previous purchases.

**User Stories**

As a user of this platform, I will be able to:

|**Type**|**Have an option to**|**purpose**|
| :---: |:---:| :---:|
|User|Access the platform from a desktop, tablet and a smartphone.|Make the website user-friendly for everyone|
|User|View several kinds of products.|Makes it easier for the user to see everything quickly|
|User|To buy products.|To give the customer what they want to buy|
|User|View a specific kind of product.|To get more specific information about a product|
|User|Registrate for an account.|Have a personal account to view customer profile and to make a order|
|User|Login and logout of the account.|To have access personal account information|
|User|View order history from previous purchases.|To give the customer information from earlier purchases|
|User|View all my products to see the total amount.|To make it easier for the customer to see how much they going to spend|
|Admin|Create, read, update and delete|To be able to provide the customer with the latest information if needed|
  
**Mockups**
  
  I have used Figma Mockups to visualize images I can work from.

- <a href="#" target="_blank">Desktop</a>

- <a href="#" target="_blank">Phone</a>

- <a href="#" target="_blank">Tablet</a>


## Features

**Existing Features**

- ....................

- ....................

- ....................

**Features Left to Implement**

- ....................

- ....................

- ....................


## Technologies Used

**Language**

- <a href="https://en.wikipedia.org/wiki/HTML" target="_blank"> Html </a>
  
- <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" target="_blank"> Css </a>

- <a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank"> JavaScript </a>

- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank"> Python </a>


**Libraries and frameworks**

- <p><a href="https://www.djangoproject.com/" target="_blank"> Django</a>- A python web-framework to build projects.</p>

- <p><a href="https://getbootstrap.com/" target="_blank"> Bootstrap</a>- A CSS library grid.</p>

- <p><a href="https://fontawesome.com/" target="_blank"> Fontawesome</a>- Provides icons.</p>

- <p><a href="https://fonts.google.com/" target="_blank"> Google fonts</a>- Custom font styling.</p>

- <p><a href="https://jinja.palletsprojects.com/en/2.11.x/" target="_blank"> Jinja</a>- A template language for python.</p>

- <p><a href="https://pypi.org/project/psycopg2-binary/#description" target="_blank"> Psycopg2</a>- Python PostgreSQL adapter.</p>

- <p><a href="https://jquery.com/" target="_blank"> Jquery</a>- Javascript library to simplify the code.</p>

- <p><a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html" target="_blank"> Boto3 </a>- A library that enables python code to modify AWS service.</p>


**Tools**

- <p><a href="https://en.wikipedia.org/wiki/Heroku" target="_blank"> Heroku </a>- For hosting the application and deploy.</p>

- <p><a href="https://stripe.com/ie" target="_blank"> Stripe </a>- Payment platform to accept and process payments online</p>

- <p><a href="https://code.visualstudio.com/" target="_blank"> VS Code </a>- Code editor</p>

- <p><a href="https://www.figma.com/" target="_blank"> Figma </a>- A collaborative interface design tool.</p>

- <p><a href="https://en.wikipedia.org/wiki/Amazon_Web_Services" target="_blank"> Amazon Web Services</a>- A cloud computing services.</p>
  
## Database structure

I have used ................. database for this project

- .........................


 **Collection Name:**
 
- ....................

## Testing 

  - The responsiveness is run and tested at:
    - http://ami.responsivedesign.is/#

  - The HTML code is run and tested at:
    - https://validator.w3.org/#validate_by_input
    - If you run the code you will get Bad value and Text not allowed in element.
    This is because I'm using
    <a href="https://en.wikipedia.org/wiki/Jinja_(template_engine)" target="_blank"> Jinja (template engine)</a>
  
  
  - The CSS code is run and tested at:
    - https://jigsaw.w3.org/css-validator/#validate_by_input
    
  - The JavaScript is run and tested at:
    - https://jshint.com/  
    
  - The Python is run and tested at:
    - http://pep8online.com/
    - 

|**Feature type**|**Feature**|**Tests**|**Bugs**|
| :---: |:---:| :---:|:---:|
|..text..|..text..|..text..|..text..|
|..text..|..text..|..text..|..text..|
|..text..|..text..|..text..|..text..|
|..text..|..text..|..text..|..text..|



  - Bugs

  - ..text..

    ```shell
       ..text....text..
       ..text....text..
    ```
  
## Deployment
  
  
 The hosting platform for this project is Heroku and can be run directly here: 
 https://..text...herokuapp.com/ 
  
  
To run this project you need the following tools installed:

  - <a href="https://www.python.org/downloads/" target="_blank"> Python3 </a>
  - <a href="https://code.visualstudio.com/" target="_blank"> VS Code </a> or a code editor that have a debug tool.
  - <a href="https://www.mongodb.com/cloud/atlas" target="_blank"> MongoDB </a>
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
pip install django
pip install django-allauth
pip install 
pip install

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

Open the website at http://127.0.0.1:5000
```

  X.   Set up environment variable keys.
```shell
os.environ.setdefault('SECRET_KEY', '<secrete key>')
os.environ.setdefault('DATABASE_URL', '<postgres key>')

""" STRIPE API Keys """
os.environ.setdefault('STRIPE_PUBLISHABLE', '<stripe publishable key>')
os.environ.setdefault('STRIPE_SECRET', '<stripe secret key>')

""" AWS API Keys """
os.environ.setdefault('AWS_ACCESS_KEY_ID', '<aws access key id>')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<aws secret access key>')

""" Email Keys """
os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')
```

  XI.   Log into your admin account add the /admin path at the end of the url link.
```shell
http://127.0.0.1:5000/admin
```

</details>

## Heroku deployment

<details>

<summary>Click to see Heroku deployment instructions</summary>

This project is hosted using Heroku.

> Instructions:

I.    Install Heroku
  
```shell
       npm install -g heroku
       heroku login
       cd my-project/
       git init
       
       Existing Git repository:
       heroku git:remote -a <app name>
```

II.    Generate a requirements file and then install from it in another environment.

 ```shell
       pip freeze > requirements.txt
 ```
    
III.   Create a Procfile

 ```shell
       echo web: python app.py > Procfile
 ```
 
 IV.   Deploy your application to Heroku

 ```shell
       git add .
       git commit -am "make it better"
       git push heroku master
       
       Existing Git repository:
       heroku git:remote -a <app name>
 ```
    
V.    Set the config variables in your Heroku settings.

|**KEY NAME**|**KEY VALUE**|
| :---: |:---:|
|AWS_ACCESS_KEY_ID|<your aws access key>|
|..text..|..text..|
|..text..|..text..|
|..text..|..text..|
 
</details>

## Credits
  
   **media**
  - The photos used in this site were obtained from:

    - https://pixabay.com/sv/
    
    - ........................
    

   **Acknowledgements**
  - Inspiration for this project was obtained from:
    -  Code Institute Frameworks with Django.
    
    - https://nordicoil.se/eir-cbd-kraem-foer-psoriasis
    
    - https://www.templatemonster.com/blog/top-45-ecommerce-business-ideas/
    
I wanna say thank you to my mentor Oluwafemi Medale for helping me through this project.
