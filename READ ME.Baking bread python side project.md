BAKING BREAD

Baking bread is a python program that calculates the bread needed to feed people with knowing how many people are there, how much a loaf weighs and how much a slice weighs (in ounces).From these points of information, it can compute how much bread is needed by multiplying the ingredients of a loaf depending on how much bread to make.

Tech stack
The tech stack includes as follows:
Language used: Python
Tech stack type: Backend programming

Key features:
 formatting code, expressions, basic calculations, variables, floats and integers.


Build process:
I first began by understanding the description of the program, what the program does, if there is any user input, outputs expected and limitations(if the program does specify).Just by seeing the demo of how the program must work, I can tell that there are a number of variables ,so defining and trying to work with all of them from the get go really is a challenge and can cause confusion and messy code. So as always, i began mapping it down as a flow chart in my notebook as only using one metric, As i began noticing how one metric flowed in the program and how other variables were need to execute the program began to make sense.
I began structuring the program, by defining the ingredients needed for one loaf of bread. I feel uncomfortable with having so many variables that i wanted to make a list of it, i tried that but somehow got an error, a list would make so much things ordered because rather than typing in the variables again in the output or anywhere in the program. I can just use an index to access them, though, that will be an update for later. A challenge i found was how to have the values of the first four variables displayed, i initially thought that the integer and the float were multiplying due to how the description was displayed, but it turns out there is an addition of an integer and a float instead of multiplication, which made wrong calculations when output was displayed ,the rest of the variables where pretty easy and straight forward syntax.

After that came a sort of dimensional analysis, it was puzzling but as i observed, i made sense of it. To find the number of bread loaves the baker must make depended on three variables :
Bread_wieght; how much a loaf weighs (in ounces, in which an ounce is 28 grams)
Serving_size; how much a slice or slices given to one person weighs(in ounces)
Num_of_guests: how many people are present
      This was user input by the way, to find the loafs needed by the baker, multiply the number of people times the serving size to get the weight of the slices that will be consumed by each person and then  divide it by the bread weight to get how many loafs you’ll actually need. Then multiply that metric you found by each ingredient needed to make one loaf of bread.
I thought id define functions for each variable calculation , but that would be very tedious so I just used variable calculation
And them displayed the output using f strings and implicit joining of strings.
Lessons learned:
Starting with a simple idea and a flow chart on pen and paper actually helps and then add detail and complexity later.
There is no restriction to thinking ,take your time to make sense of it all and try to express something even if it gets that hard.

Areas for improvement:
Lists are one data type I should practice on how to define them and use them effectively.

      Though this was draining me moderately, I did have fun finding my way to the solution. It was a Job well done. And I wonder if an actual baker can use this.


