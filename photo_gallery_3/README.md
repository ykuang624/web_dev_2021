# Restaurant 3

**15 points**

For easiest viewing of these instructions, view online or use a Markdown previewer.

### Preparation

1. Copy this entire folder into the top level of your own repository.  Make sure the folder name remains the same.
2. Commit and push to your repository.  Verify that you can see it online.
3. You can continue to commit and push often.
4. When you think you're done, create a file named "GRADE.md" with one line in the file that says "I'm done", a riddle, or an interesting tidbit of computer science trivia. (This is because Git won't push empty files). Then commit and push your changes.

### Instructions

This assignment will challenge you in two ways:

* You will invent your own page design
* You will use a third-party JSON API to retrieve data

The API you will use is hosted by [Unsplash.com](https://unsplash.com/). 

1. Sign up for a free demo account at [https://unsplash.com/developers](https://unsplash.com/developers). 
2. Once you're logged in, select `New Application` and agree to the `API Use Guidelines`.  
4. Use the `Get a Random Photo` option for this assignment. Read the [https://unsplash.com/documentation#get-a-random-photo](https://unsplash.com/documentation#get-a-random-photo) to learn the parameters required to query the image database. 

**WARNING**: Keep in mind that Unsplash limits demo accounts to 50 images each hour!  You can quickly hit this limit during development.  See the section "How To Avoid The Unsplash API Limit" below.


### The Challenge

Create an image gallery that meets the following requirements:

* Includes a title
* Includes a numeric input control titled `Number of Images to Display`. The control lists numbers 1 through 4 and determines how many pictures are displayed each time `Update` is clicked.
* Includes an `Update` button that 
  * Displays from 1 to 4 images at a time, either vertically or horizontally
  * Replaces previous set of pictures each time it is clicked

HINT: In the JSON file returned by Unsplash, use the `regular` property to point to the image source.


### Grading Rubric

You may use any HTML/CSS technique you want, including use of a CSS framework.  However, you cannot use a JavaScript framework.

* 10 points: Proper usage of the Unsplash API
* 5 points: Nice overall page design

---

### How To Avoid the Unsplash API Limit

 Here's a technique for avoiding the API limit (50 calls per hour):

 * As soon as you have your API call working, capture the resulting data object by emitting it to the Console.
 * Copy the data from the Console to have as a hardcoded version of a typical Unsplash response.
 * Use the hardcoded data while you develop the rest of your page, avoiding all further usage of Unsplash.
 * Once you feel your page is working well with the hardcoded data, re-enable the code necessary to call the real Unsplash API.


