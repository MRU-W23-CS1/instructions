# Decisions
[GitHub Classroom Link](https://classroom.github.com/a/90-vlORo)

## Part 1: Code analysis
1. Trace the code in `lab06part1.py` and **predict** what the output will be when you run the program. Next, run it. If the output is not what you predicted, try to figure out why.

2. Without modifying `abstract_decisions`, determine how to make the program produce the opposite output by inverting the value of just one of the arguments passed from `main`. Make the change and test to see if you were correct.

3. Next, restore the code to its original form. Can you invert a different variable to achieve the same effect? If so, which one?

> You can do this through trial and error, but try to understand why the result changes the way it does!

## Part 2: Code synthesis
Meal delivery service BypassTheCleaning has hired you to write their app. They offer free delivery for orders of \$40 or more, and they want your app to display the amount remaining to get free delivery.

1. Using the template provided in `lab06part2.py`, **design** a program that prompts the user for the dollar amount of their current order, then prints out a message according to the following table:

    | Amount                   | Message                                         |
    | ------------------------ | ----------------------------------------------- |
    | amount $\lt 0$           | `Invalid entry, orders must be positive`        |
    | $0 \leq$ amount $\lt 40$ | `Add $xx.xx to your order to get free delivery` |
    | $40 \leq$ amount         | `You get free delivery!`                        |
    
    You can assume the user input data type is always correct (e.g. a number will be entered when it is expected by the program). You may add additional functions, but 

    The program should look like the following when run, where 25.30 is an examples of user input.

    <pre>
    What is the dollar amount of the current order? <span style="font-style: italic; font-weight: bold;">25.30</span>
    Add $14.70 to your order to get free delivery</pre>

    Note that by default, Python will not print out exactly two decimal places. This is a good chance to practice your [f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) skills.

2. **Implement** the program from step 1. Is there anything you forgot during the design stage?
   > One of your variables should be defined as a **constant**. Which one?
3. **Test** the program. What test values should you use to make sure you know it is completely working?

## Bonus challenge
In Part 2, you wrote a program to check if a user gets free delivery based on their order amount. Now, BypassTheCleaning wants you to make sure that only users within **20 km** get free delivery. Modify your `main` function to prompt the user for their delivery distance, implement the `check_free_delivery_bonus` function to print messages according to the following table:

| Distance                   | Message                                         |
| -------------------------- | ----------------------------------------------- |
| distance $\lt 0$           | `Invalid entry, distance must be positive`      |
| $0 \leq$ distance $\lt 20$ | Check amount as above                           |
| $20 \leq$ distance         | `Sorry, you are not eligible for free delivery` |

## Testing
Try to test your code first **before** running the automated tests - these should just confirm what you already know, not be used as a tool to exclusively check your work.

This lab has 5 tests. You only need to pass 3 of them to get credit for the lab, but the rest might be good practice for the midterm.