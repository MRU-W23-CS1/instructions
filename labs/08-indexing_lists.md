# Indexing and Lists
[GitHub Classroom Link](https://classroom.github.com/a/vJTRbH2U)

## Part 1: Tracing
Building on the course management program introduced in the [indexing and lists tutorial](https://github.com/MRU-W23-CS1/instructions/blob/main/tutorials/08-indexing_lists.md), someone has written a function called `remove_all`. It is supposed to remove all courses matching a certain course code, but it is not working as expected.

Open the file `lab08part1.py` and read the function. Then, answer the following questions:

1. Trace the function with the following function calls:
    ```python
    courses = ["COMP 1501", "GNED 1103", "GNED 1401", "MATH 1505"]
    remove_all(courses, "GEOL")
    remove_all(courses, "MATH")
    remove_all(courses, "GNED")
    ```
2. Does an error occur every time you call the function? If not, under what circumstances does the error occur?
3. What *kind* of error occurs? The general error types are syntax, runtime, and logic.

Try to fix the function so that it behaves as intended. What additional test values should you consider to fully ensure the function is working as expected?

> Note: this is a deceptively challenging problem! Only one of the two parts of this lab are required to pass, so consider moving on to part 2 if you're totally stuck.

## Part 2: Working with parallel lists
In the last exercise of the [indexing and lists tutorial](https://github.com/MRU-W23-CS1/instructions/blob/main/tutorials/08-indexing_lists.md), you designed an algorithm that takes two lists of quiz grades as parameters and returns a *third* list containing the higher of the two quiz grades for each student.

Create a new file named `lab08part2.py` and implement your algorithm as a function called `best_quiz_grade`. Your function should take two lists of floats as parameters and return a list of floats containing the higher of the two quiz grades for each student.

You can assume that the two lists are the same length and that each contains only valid numbers.

> Hint: You will need to create an empty list to use as your accumulator, then loop through the two lists in parallel and append the higher of the two quiz grades to the accumulator list.

## Testing
Try to test your code first **before** running the automated tests - these should just confirm what you already know, not be used as a tool to exclusively check your work.

This lab has only 2 tests, one for each part. Since these are rather challenging exercises, only one test is required to pass the lab.

For both parts 1 and 2, do not prompt the user for input. Instead, you may hard-code test values.