# Restaurant 2

**15 points**

For easiest viewing of these instructions, view online or use a Markdown previewer.

### Preparation 

1. Copy this entire folder into the top level of your own repository.  Make sure the folder name remains the same.
2. Commit and push to your repository.  Verify that you can see it online.
3. You can continue to commit and push often.
4. When you think you're done, create a file named "GRADE.md" with one line in the file that says "I'm done", a riddle, or an interesting tidbit of computer science trivia. (This is because Git won't push empty files). Then commit and push your changes.

### Instructions

This assignment will help you gain experience using Javascript and creating forms using HTML and CSS.

Take a look at the example page [target.png](target.png).  

Challenge: Build a mobile-only page similar to the example. The page should meet the requirements listed below. Your page does NOT need to look exactly like the example - feel free to use your own design  - but should contain the same behavior. Text for the page is provided in [restaurant-2.txt](restaurant-2.txt). Also provided is the logo image named [taco.png](taco.png).   

* Display six sections: 
  * Restaurant logo and name
  * Address and hours
  * Menu
  * Shopping cart
  * Totals at the bottom

* In the Menu portion:
  * Display the menu item, description, and price
  * Place an "Add to Cart!" button next to each menu item
  * When the "Add to Cart!" button is clicked:
    * change the button text to "Added To Cart!"
    * add the item to the `Shopping Cart`

* Each time an item is selected in the menu, add it to the cart as follows:
  * (3 pts) Display the name of the menu item
  * (2 pts) For each item, use a number input control to capture the order quantity (the default is 1, but the lowest number that can be selected is 0)
  * (3 pts) Multiply the item quantity and cost and display the item total
  * (2 pts) Add the costs of all the orders and display the total

* You may use any HTML/CSS techniques you want including any CSS framework, but you may not use a JS framework.
* You do NOT need to include the Checkout or Clear buttons even though they are in the target screenshot.
* You do NOT need to optimize the design for devices larger than a phone, but the mechanics of the site should still work.

**Grading Rubric**

* 10 points: Page functions as described
* 3 points: Fine details: all required content is present and correctly aligned
* 2 points: Reasonable choice of typography
 
