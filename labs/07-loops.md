# Loops
[GitHub Classroom Link](https://classroom.github.com/a/35L98xVx)

## Part 1: Tracing
Open the file `lab07part1.py`, then do the following:

1. Identify the loop components:
   1. Body of the loop (statements to iterate)
   2. Loop Control Variable (LCV)
   3. Terminating conditions
   4. Initial conditions
   5. LCV update

2. Trace the code  with some sample data (such as 1, 2, 3, -1) and **predict** what the output will be when you run the program. Next, run it. If the output is not what you predicted, try to figure out why.

4. Fix the `sum_all` function so that it behaves as described by the docstring.

5. Re-run the program and input -1 as the first input. What is the result? Is this what you would expect?

6. **Error: Forgetting the priming read**. Edit the program by commenting out the line indicated as the priming read. What kind of error occurs?

7. **Error: Forgetting the internal read**. Return the program to its original state and run it to make sure that it works. Now, comment out the line indicated as the internal read and run the program program. What kind of error occurs?

## Part 2: Loop design
In the [loop design tutorial](https://github.com/MRU-W23-CS1/instructions/blob/main/tutorials/07-loop-design.md) you designed an algorithm to read all of the integers entered by a user until an **empty string** is input, then print out the **largest integer**. Create a new file named `lab07part2.py` and write a program that implements your algorithm. You can assume that the user will always enter **at least one** integer.

> Hint: you will need to test if the string is empty **before** casting user input to an integer.

Your program must have a `main` function that is the main program entry point, but beyond that you can structure your program however you like.

## Testing
Try to test your code first **before** running the automated tests - these should just confirm what you already know, not be used as a tool to exclusively check your work.

This lab has 4 tests, one for part 1 and three for part 2. 3/4 must be passed to get credit for the lab.