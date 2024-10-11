# Django Shop

This is my first e-commerce project with a lot of features

I hope you will like that


## Features

- Kavenegar code registration
- Add products from admin page
- User register and login and logout form
- categories and filter category
- shopping cart
- checkout form
## Environment Variables

To run this project, you will need to create a virtual Environment

```bash
  # Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```
    


## Installation

Install by below link

```bash
  $ git clone https://github.com/mehdiesmaeilii/Django-Shop.git

  pip install -r requirements.txt
```
Enter directory :   cd A
```bash
  $ python manage.py makemigrations
  
  $ python manage.py migrate
```

create superuser 
```bash
  $ python manage.py createsuperuser

```
    
## Deployment

To deploy this project run

```bash
  $ python manage.py runserver
```


## Related



You can add extra categories and products inside admin panel and it will be shown after 
saving 

do not forget that you have to enter your phone number to enter admin panel

I used some cabinet pictures but you can remove that from admin panel

when you choose a product and choose the quantity you will automatically redirect to shopping cart
