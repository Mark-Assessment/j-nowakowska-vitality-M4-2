# Julia's Cooking Company

<p>
  <img src="" width="100%" alt="mock up photos">
</p>

[Click here to view the live project]
(<>)

## Table of contents

1. Introduction
2. UX
   1. User Demographic
   2. User Stories
   3. Development Planes
   4. Design
3. Features
   1. Design Features
   2. Existing Features
   3. Features to Implement in the Future
4. Issues and Bugs
5. Technologies Used
   1. Main Languages Used
   2. Frameworks, Libraries & Programs Used
6. Testing
   1. Testing User Stories
   2. Manual Testing
   3. Automated Testing
   - Code Validation
   - Browser Validation
   4. User Testing
7. Deployment
   1. Deploying on GitHub Pages
8. Credits
   1. Content
   2. Media
   3. Code
9. Acknowledgements

---

## Introduction

The primary goals of Vitality website is to provide a web-based application that is intuitive and easy to navigate, and allows users purchase health supplemets and healthy snacks .

This is the fourth of four Milestone Projects that the developer must complete during their Full Stack Web Development Program at The Code Institute.

The main requirements of this project are to build a responsive, simple site using HTML, CSS, JavaScript, Python, Django.

## UX

### User Demographic

The ideal user for this website is:

- New user
- Returning user
- User

### User-Stories

#### New User

1. As a new user, I want to be able to navigate to Sign-Up page to register an account.

#### Returning User

1. As a returning user, I want to be able to access my account on the website.
2. View my previous orders, to keep a record of my transaction.
3. Edit default information, to update any necessary fields.
4. View shopping bag to get an overview of products I wish to order.
5. Remove products from my bag, to suit my needs.
6. Update a product's quantity, to suit my needs.
7. Proceed to a secure checkout, to make a purchase.
8. Have clear visual feedback of the order process, to understand all steps of the process.
9. Be able to edit my bag at all times, to allow change of mind.
10. Receive a summary of my order via email to confirm that my transaction has been process.

#### User

1. View all products, to purchase my desired items.
2. Filter through categories, to only see relevant products.
3. Use a search query, to find a specific product or product type.
4. Add items to my shopping bag, to begin the order process.
5. Receive visual feedback that my item has been added to the bag, to confirm my selection.
6. View contact informtation for the shop
7. Navigate to a page that could help me with my enquiry, to answer my question.

### Development-Planes

For the site to function as intended and fulfil its purpose for the user, the developer needs to develop all aspects of a functional web-based application.

#### Strategy

Strategy incorporates user needs as well as product objectives. This website will focus on the following target audience, divided into three main categories:

- **Roles:**

  - New user
  - Returning user
  - User

- **Demographic:**

  - healthy lifestyle
  - shopping intrest
  - teens
  - adults

- **Psychographic:**
  - Any socioeconomic status and age group

The website needs to enable the **user** to:

- Create an account or log in to an existing one
- View past purchases
- Edit/Save Delivery Information
- Get in touch with the shop

The website needs to enable the **site manager** to:

- Add/deleyte and edit items
- Improve the site as necessary with various new features

#### Scope

The scope plane is about defining requirements based on the goals established on the strategy plane. Using the information in the strategy plane, the identified required features have been broken into the following two categories.

- Content Requirements:
  - The user will be looking for:
    - Products are visible on the site
    - Visible button
    - Intuitive navigation bar
    - Social Media links for those with further interest in the company
   	- View Categories
    - Functionality Requirements
  - The user will be able to:
    - Log in/ Register/ Log out of the website
    - Be able to easily navigate the site to find the information they require, like social media links etc
    - Add products to basket
    - View basket 
    - Checkout shopping
    - Filter and search bar - options to find products user requires

#### Structure

The information above was organized in a hierarchical tree structure, showing how users can navigate through the interactive site with ease and efficiency, with the following results:

<details>

<summary>Structure of the Site</summary>

<p>
  <img src="" width="100%" alt="structure photos">
</p>

</details>

The structure of the models and database is included below :
<summary>Structure of the Database</summary>

<p>
  <img src="" width="100%" alt="structure photos">
</p>

</details>

### Skeleton

Wireframes were made to showcase the appearance of the site pages while keeping a positive user experience in mind. The wireframes were created using an online version of [Figma](https://www.figma.com).

<p>
    <img src="" width="100%" alt="website-vision">
    <img src="" width="100%" alt="website-vision">
</p>

</details>

### Design

#### Colour Scheme

I have chosen my colour scheme by using [SheCodes](https://palettes.shecodes.io/) colour scheme palettes.
The colours used are :
  
# b45555 - text of the body;
# 000000 - black for text like titles, nav-bar etc;
# c13131 - red for footer links;
# FFFFFF - white for some text and background of some text ;
# c13131 - red for delete button;
# 007bff - blue for edit button
# aab7c4 - light grey for placeholders

White was used as the background colour for the website as graphic is full of colour creating a good contrast for reading and browsing.  
The main content text is in a black shade, as this colour creates the best contrast to guarantee the high readability of the text. Following the standard procedure, the delete buttons are red; the edit buttons are blue.
Shades picked are generally soft with a few contrasting colours like red, black and white and grey to focus the user on colorful products.

#### Typography

The typography pairing used on this site is [Lato]. A backup of Sans-Serif had been applied in case of an error.

#### Imagery

The selected imagery has been sourced from various sites.
There is an image on the main page that also shows on other pages.
A user can view image of a product, if image was not icludede a simple imgge will show in its place.
Browser logo was created by the author of the website using canva.

## Features

### Design Features

Each page within the site has a responsive and consistent navigation system. Detailed features are included below.

- The **Header** is across the top of the page. It is 100% in width and includes the title of the page.
- The **Navigation Bar** is positioned on the right-hand side of the title, it includes the "Home", Products and Categories' buttons.

It appears on all screen sizes. If the screen size becomes too small the menu will become collapsable with a button for access.
- The **Footer** is 100% in width. The footer is located permanently at the bottom of the page on all screen sizes. The footer contains all social media links;corresponding media logos;links to contact page; links to freaquently used pages.

<dl>
    <dt><a href="index.html" target="_blank" alt="Vitality">Home Page</a></dt>
    <dd>
        The <em>Home Page</em> is a scrollable page and it includes a navigation bar, footer and menu on the top. It also includes a search bar and logo in top left corner. In the top right conner a shopping bag and Account buttons can be located.
        <ul>
            <li>
            <em>Navigation Bar</em> - This inludes the logo, links, account access and shopping bag.
            </li>
            <li>
            <em>The Description</em> - This section contains a short description of the page and its purpose. This will give a clear overview of the website for a new user.
            </li>
	     <li>
            <em>Footer</em> - This section contains social media links to Facebook, Gitpod and Twitter as well as links to useful pages on the site and address and contact details of the company.
            </li>
        </ul>
    </dd>
</dl>
<dl>
    <dt><a href="categories.html" target="_blank" alt="Categories page">Categories Page</a></dt>
    <dd>
        The <em>Product page</em> is a scrollable page that includes cards with products. It consists of an image and product name; The cards also have a button to edit and delete products - only for the admin.
        <ul>
            <li>
            <em>Title</em> - this reflect the sites purpose.
            </li>
            <li>
            <em>Main Content</em> - cards with prodcuts
            </li>
            <li>
            <em>Footer</em> - This section contains social media links to Facebook, Gitpod and Twitter plus other features specified above.
            </li>
        </ul>
    </dd>
</dl>

### Existing Features

- **Header** - Appears on every page; This includes the title of the page and a graphic that carries the theme of the website.
- **Navigation Bar** - Appears on every page to provide visible and easily accessible navigation.
- **Footer** - Appears on the bottom of every page. This provides easy access to external links.
- **Social Media Links** - Appears in the footer, at the bottom of every page. Links are embedded in the social media icons and open in a new tab to provide a better user experience.
- ** ** - 
- ** ** - 


### Features To Implement In The Future

- **Comments**
  - **Feature** - Create a feature where users can add comments on products.
  - **Reasons For The Feature Not Being Currently Included** - not a sufficient amount of time to execute this on a desired level as well as more coding practice required.
- **Wish list**
  - **Feature** - The user can add products to a wish list which is visible to other users to view ands share.
  - **Reasons For The Feature Not Being Currently Included** - not a sufficient amount of time to execute this on a desired level;
- **Different delivery options available**
  - **Feature** - Add different delivery features like click and coillect and different charges for each.
  - **Reasons For The Feature Not Being Currently Included** - not a sufficient amount of time to execute this on a desired level. More practice and expertise in coding is needed.
- **Club card**
  - **Feature** - Create a feature where users can gather points and then spend them back at the store. Also add different discounts.
  - **Reasons For The Feature Not Being Currently Included** - not a sufficient amount of time to execute this on a desired level.

## Issues and Bugs

The developer ran into several issues during the development of this site. The most interesting ones have been described below, this includes the fix for the bugs.


**Adding FAQs to the page** - The developer had issues with viewing/hiding text on FAQs feature. The help was found online via Slack and Stack Overflow and error fixed.

**Footer** - There was an issue with footer lenghth as it was featured on top of the page rather then bottom. The issues was solved by including footer into a different content block and then calling it on base.html page.


## Technologies Used

### Main Languages Used

- HTML5
- CSS3
- JavaScript
- Python
- Django
- Bootstrap

### Frameworks, Libraries & Programs Used

[GitHub](https://github.com/ "Link to Github") - was used to store the project after pushing from Codeanywhere.
[Codeanywhere](https://codeanywhere.com/signin"Link to Codeanywhere") - was used to write and commit the code as well as push it to GitHub.
[Font Awesome](https://fontawesome.com/ "Link to Font Awesome") - was used to obtain icons for the project.
[Figma](https://www.figma.com/ "Link to Figma") - was used to create Wireframes.
[Google Fonts](https://fonts.google.com/ "Link to Google fonts")- was used to source fonts for the project.
[Canva](https://www.canva.com/ "Link to Canva") - was used to create graphics for the project.
[Am I Responsive?](https://ui.dev/amiresponsive "Link to Am I Responsive?") - was utilised to check if the site is responsive.
[Heroku](https://heroku.com/ "Link to Heroku") - was used to deploy the website.
[Favicon](https://favicon.io/ "Link to Favicon") - was used to create a logo for the business and browser tab.

## Deployment

 This milestone project was developed using [Codeanywhere](https://codeanywhere.com/signin "Link to Codeanywhere site"), which was then committed and pushed to GitHub using the Codeanywhere terminals.

### Deploying on Heroku

Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
 pip freeze --local > requirements.txt
Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it
Inside the file, add the following command web: python run.py
Ensure you do not add a blank line to the end of the file as this can cause problems for deployment.
Open your **init**.py file
Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
 app = Flask(**name**)
 app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
 if os.environ.get("DEVELOPMENT") == "True": app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") else app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:
 if os.environ.get("DEVELOPMENT") == "True": app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
 uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"): uri = uri.replace("postgres://", "postgresql://", app.config["SQLALCHEMY_DATABASE_URI"] = uri
Save all your files and then add, commit and push your changes to GitHub

## Credits

### Content

- Text used in the project was borrowed and adapted from various ecommerce stores online .

### Code

- Multiple websites were consulted and visited whilst developing this project to better understand the code that is being used and utilise the developer's knowledge gained so far. Pages used for reference are included below :
  - [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
  - [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow")
- Any borrowed code is mentioned and acknowledged in the notes in the Gitpod

### Media

- Various platforms and pages were used for sourcing images included in this project, the main page used was [Google Images](https://www.google.com/imghp?hl=EN "Link to Google Images Page")

## Acknowledgements

- I would like to thank my mentor Owonikoko Oluwaseun for useful advice and guidance on this project.
- I would also like to thank the coders' community who created various documents explaining how Python and SQL work, so I could use that as a base to create my own, unique project.
- I would like to thank my family and friends for their objective feedback and support.
