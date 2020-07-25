<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome aleksandrsg,

### Final Milestone Project 4 with Django Framework
---

Web Project Adopt a Pet developed on Django framework together with other web languages and technologies  
like Stripe (e-commerce functionality implementation), Bootstrap (responsive design) ect.  
Frameworks like Django or Flask helped me to see clear full picture of web development process   
from front-end till back-end development.  
Project consists of five apps: Home, Pets, Donation, Blog and Accounts.

## UX  
---
Project wireframe you could find in directory Static / Wireframes.

As a Web Resource owner I could:  

- Manage and store Database with pets who need homes;
- Create, Update, Delete data from Database;
- Receive donations for Project development;
- Receive comments from persons who have adopted the pets

As a Web Resource user I could:

- Make donation to support a Project;
- Leave a comment to owner and for other users;
- Find a pet for adoption;

## Technologies used
---
To develop Project the author use the following basic web technologies:

Languages and Frameworks:
- Django Framework,
- HTML,
- CSS,
- Javascript,
- Bootstrap framework,
- Stripe API,
- Jinja,
- Gunicorn,
- Whitenoise,
- Pillow,
- Psycopg2,
- Dj-database-url.

Development and hosting tools:
- GitPod IDE,
- GitHub,
- Heroku,
- Postres DB ad-on.

## Testing
---
The project was created, developed and tested in GitPod IDE step by step manualy. 

Testing protocol:
1. Open Home Page and test Logo link, test all navigation links, test all buttons and elements position.
2. Open Our Pets Page and inspect Pets card position, card description, card button.
3. Click on Pet card button (Description) and redirected to full description page.
4. Inspect and check all elements and link on Pet Description Page.
5. Open Donation Page, complete the Donation Form and submit Form. Test link return to Home Page.
6. Open Blog submenu Comments, inspect comments position and all comments elements (title, author, date, description).
7. Open Blog submenu New_Comment, Sign in and complete the Comment Form, if not authorized go to  
Registration Page and complete Sign Up form. Go back to Page New_Comment, complete and submit  
New_Comment Form, test Logout button. 
8. Deployment to Heroku.

### Testing Stripe API:

Open the Donation Page, complete the Form.  
In field Credit or Debit Card type testing data  
card number: 4242 4242 4242 4242  
card expared date 09/20  
cvc 123  
post code 12345  
Submit the form and redirected to success Donation Page.
<img src= "media/stripe_form.png">

## Deployment
---
This Project was created and developed in GitPod IDE and
deployed on [Heroku](https://adopt-a-pet-1.herokuapp.com) cloud service
Stored in GitHub repository: https://github.com/aleksandrsg/adopt_a_pet  
Heroku repository: https://adopt-a-pet-1.herokuapp.com/

1. To deploy Project have to make registration on www.heroku.com
2. Press button NEW on the top right corner
3. Choose function: Create New App
4. Type App name: adopt-a-pet-1
5. Choose a region : Europe
6. Push button CREATE APP
7. Go back to GitPod IDE and make connection with Heroku
8. Type in terminal: $ heroku login (enter name and password)
9. Type in terminal: $ heroku add remote heroku https://git.heroku.com/adopt-a-pet-1.git
10. Type in terminal: $ git add .
11. Type in terminal: $ git commit -m "Adopt-a-pet-1 Deployment"
12. Type in terminal: $ git push heroku master
13. Go back to Heroku, choose Adopt-a-pet-1 on the left side
14. Press button OPEN APP on the top right coner
15. App works.

## Tehnical Reference
---
https://www.w3schools.com/