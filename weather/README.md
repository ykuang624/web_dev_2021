# Weather

**15 points**

For easiest viewing of these instructions, you may want to view online with a Markdown previewer.

### Preparation ###

1. Copy this entire folder into the top level of your own repository.  Make sure the folder name remains the same.
2. Commit and push to your repository.  Verify that you can see it online.
3. You can continue to commit and push often.
4. When you think you're done, create a file named "GRADE.md" with one line in the file that says "I'm done", a riddle, or an interesting tidbit of computer science trivia. (This is because Git won't push empty files). Then commit and push your changes.


### Instructions

Your challenge is to convert the static weather page [weather.html](weather.html) to become an interactive weather widget by using the [WeatherAPI service](https://weatherapi.com).

* Sign up for a free account at WeatherAPI.com
* Once you login, try the built-in "API Explorer" to retrieve your current weather given your current location or a US zip code
* Full documentation is at https://www.weatherapi.com/docs/
* Be sure to round all numerical data to the nearest integer.
* Be sure to convert wind direction abbreviations to full words.
* A target.png is provided for convenience, but the HTML is already provided and the actual display will depend on the current weather.

You are welcome to change the given HTML as needed, or you can keep the existing HTML and just write
the necessary JavaScript.

You can use any HTML/CSS technique you want, including any CSS framework (the example code uses Bootstrap). But you cannot use a JS framework.

### Grading Rubric

* 5 points for displaying the current weather given a US zip code.
* 5 points for display the current weather using the user's current GPS location
* 5 points for using the proper weather icons to reflect current conditions.

