## Testing

## Testing User Stories

#### New User
1. As a new user, I want to be able to navigate to Sign-Up page to register an account.
   - Login/Register features are easily accessible via navigation bar

#### Returning User Goals

1. As a returning user, I want to be able to access my account on the website.
   - feature is available via 'Account' on navigation bar. User can view their profile and order history.
2. View my previous orders, to keep a record of my transaction.
3. Edit default information, to update any necessary fields.
   - this feature is available in Profiles as well as in the checkout where user can edit tgeir details.
4. View shopping bag to get an overview of products I wish to order.
   - feature is available in bag, where user can view order, quantity, total amount and delivery amount.
5. Remove products from my bag.
6. Update a product's quantity.
7. Proceed to a secure checkout, to make a purchase.
   - removing/updating and checkout are avialble in the shopping bag 
8. Have clear visual feedback of the order process, to understand all steps of the process.
   - FAQs are avialle to answer questions that user may have.
10. Be able to edit my bag at all times, to allow change of mind.
    - available in the bag, where user can adjust quantity
11. Receive a summary of my order via email to confirm that my transaction has been process.
    - feature available and included after checkout.

#### User

1. View all products, to purchase my desired items.
   - products are accessable through a navigation bar, where user can also use categories to view only specific products.
2. Filter through categories, to only see relevant products.
3. Use a search query, to find a specific product or product type.
   - search bar is functional and allows user to view specific products 
4. Add items to my shopping bag, to begin the order process.
   Adding item to bag is available after clicking into a product of interest
5. Receive visual feedback that my item has been added to the bag, to confirm my selection.
   - toasts are used to give live feedback to the user
6. View contact informtation for the shop
   - contact information are available in the footer as well as in the nav bar under 'Contact Us'
7. Navigate to a page that could help me with my enquiry, to answer my question.
   - navigation of the page is easy and intuitive.

## Manual Testing

### Common Elements Testing

Manual testing was conducted on the following elements that appear on every page:

- Clicking on the navigation bar menu items to take the user to the correct page on the
  website
- Clicking on the footer items to take the user to the correct page on the
website
Facebook
Twitter
Instagram

### Home Page

Manual testing was conducted on the following elements of the [Home Page](index.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/responsive_home_page.png" width="100%" alt="responsiveness of the page">
</p>

- Navigation bar changes into a dropdown menu on smaller screens
<p>
  <img src="media/TESTING_media/responsive_small_screen.png" width="100%" alt="small screen responsiveness">
</p>

- Footer is visible and functionable, with links and layout working on all screens.
<p>
  <img src="media/TESTING_media/footer.png" width="100%" alt="footer">
</p>

- 'Shop Now' button will take user to all products section of the shop
<p>
  <img src="media/TESTING_media/responsive_home_page.png" width="100%" alt="shop now button">
</p>

- Search bar will search products based on name and description
<p>
  <img src="media/TESTING_media/search_products.png" width="100%" alt="search bar">
</p>

- Products are divided by categories on the nav-bar and take the user to the right page annd show correct products.
<p>
  <img src="media/TESTING_media/responsive_products.png" width="100%" alt="products">
</p>

- "My Account" page gives the user opportunity to log in /register
<p>
  <img src="media/TESTING_media/Register_or_login_menu.png" width="100%" alt="Log in or register dropdown">
</p>

- Upon logging in "My Account button shows relevant options for logged in user, like Profiles and Product Management for superusers
<p>
  <img src="media/TESTING_media/my_account_options.png" width="100%" alt="my account upon logging in">
</p>

- Bag updates with correct amount to reflect products added to the bag
<p>
  <img src="media/TESTING_media/chrome.png" width="100%" alt="updated bag with grand total">
</p>

- Users get feedback via toasts upon updating the basket
<p>
  <img src="media/TESTING_media/toasts.png" width="100%" alt="toasts">
</p>

### Products Page

Manual testing was conducted on the following elements of the [Products Page](products.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/responsive_products.png" width="100%" alt="responsiveness of the page">
</p>

- Various options to sort products by
<p>
  <img src="media/TESTING_media/sort_by.png" width="100%" alt="sorting products">
</p>

- Scrollable page with product pictures and names
<p>
  <img src="media/TESTING_media/responsive_products.png" width="100%" alt="products view">
</p>

- Edit/Delete buttons available for superuser
<p>
  <img src="media/TESTING_media/responsive_products.png" width="100%" alt="edit/delete visibility">
</p>

### Product detail Page

Manual testing was conducted on the following elements of the [Product detail Page](product_detail.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/product_detail.png" width="100%" alt="responsiveness of the page">
</p>

- Product description, price, category and name visible on the page
<p>
  <img src="media/TESTING_media/product_detail.png" width="100%" alt="product details">
</p>

- Ability to add different quantity of product to the bag + add to bag button
<p>
  <img src="media/TESTING_media/product_detail.png" width="100%" alt="product details quantity button">
</p>


### Contact page 

Manual testing was conducted on the following elements of the [Contact Page](contact.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/contact_responsive.png" width="100%" alt="responsiveness of the page">
</p>

- Fully functional form with required fields and send button
<p>
  <img src="media/TESTING_media/contact_responsive.png" width="100%" alt="contact form">
</p>

- Reason for contact is a collabsable option
<p>
  <img src="media/TESTING_media/reason_for_contact.png" width="100%" alt="contact dropdown">
</p>

### FAQs Page

Manual testing was conducted on the following elements of the [FAQ Page](faq.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/faq_responsive.png" width="100%" alt="responsiveness of the page">
</p>

- Collabsable Answers option and Question with show/hide text button - all functional
<p>
  <img src="media/TESTING_media/faq_unrolled.png" width="100%" alt="faq unrolled">
  <img src="media/TESTING_media/faq_hidden.png" width="100%" alt="faq rolled">
</p>


### Shopping Bag Page

Manual testing was conducted on the following elements of the [Bag Page](bag.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/responsive_bag.png" width="100%" alt="responsiveness of the page">
</p>

- Product is visible including price, quantity, delivery fee etc.
<p>
  <img src="media/TESTING_media/responsive_bag.png" width="100%" alt="bag details">
</p>

- Quantity can be adjusted via the buttons in the bag 
<p>
  <img src="media/TESTING_media/responsive_bag.png" width="100%" alt="quantity in the bag">
</p>

- secure checkout available
<p>
  <img src="media/TESTING_media/responsive_bag.png" width="100%" alt="checkout">
</p>


### Product Management

Manual testing was conducted on the following elements of the [product Management Page](add_product.html):

- The responsiveness of the page
<p>
  <img src="media/TESTING_media/add_product.png" width="100%" alt="responsiveness of the page">
</p>

- Functional form with submit button
<p>
  <img src="media/TESTING_media/add_product.png" width="100%" alt="add form">
</p>

### Edit Product

Manual testing was conducted on the following elements of the [Edit Product Page](edit_product.html):

- The responsiveness of the page

<p>
  <img src="media/TESTING_media/edit_product.png" width="100%" alt="responsiveness of the page">
</p>

### Profile

Manual testing was conducted on the following elements of the [Profile Page](profile.html):

- The responsiveness of the page

<p>
  <img src="media/TESTING_media/profilesd.png" width="100%" alt="profiles ">
</p>

- Ability to view and update information via a form
<p>
  <img src="media/TESTING_media/profilesd.png" width="100%" alt="profiles form">
</p>

### Log/Register

Manual testing was conducted on the following elements of the [Log in/Register Page]:

- The responsiveness of the page

<p>
  <img src="media/TESTING_media/Register_or_login_menu.png" width="100%" alt="account menu">
</p>

- Registration form
<p>
  <img src="media/TESTING_media/register.png" width="100%" alt="register">
</p>

- Log in 
<p>
  <img src="media/TESTING_media/log_in.png" width="100%" alt="log in">
</p>


## Automated Testing

Both manual and automated testing are used to check if the project's code is written in a way the project works correctly.
Automated testing can be performed via a Python testing framework like Pytest. I am aware of the advantages the automated testing carries like high reliability, as it is run and performed by a programme as the code is developed and it is a lot quicker as hundreds of tests can be performed against the project in a short time frame.
Although more time-consuming, I have decided to utilise the manual way of testing as the project is quite small and I didn’t have the time capacity in the project window to get automated testing set up correctly.
Manual testing checks if the project works by user stories by testing it in different browsers and resolutions. The testing can be performed manually by a potential user, code creator or another third party.

In a real-life scenario, I fully acknowledge I would use PyTest to further practice my skills with automated testing and make sure that errors are picked up early and corrected promptly.


### Code Validation

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML` and `CSS` code used.
The [Extends Class](https://extendsclass.com/) service was used to validate Python.

**Results:**

- HTML Pages
  <p>
  <img src="media/TESTING_media/html.png" width="100%" alt=" HTML Validator">

</p>
- CSS
  <p>
  <img src="media/TESTING_media/css.png" width="100%" alt=" CSS Validator">
</p>

### Browser Validation

- Chrome
  <p>
  <img src="media/TESTING_media/chrome.png" width="100%" alt=" Chrome">

</p>
- Safari
<p>
  <img src="media/TESTING_media/safari.png" width="100%" alt=" Safari">
</p>

## User testing

A few friends and family members were asked to review the page for user experience and to point out any bugs/issues. The input of this group led to small UX adjustments to improve the overall site appearance and user experience. Some of them included: Improving CSS for better visibility, Changing the footer, Adding FAQs, Changing contact form questions.
DEBUG function was turned off.