# Indexing and Lists
<!-- Combination of Java 1501, 1631, and some new stuff -->

## Introduction
This tutorial is intended to familiarize you with the `list` datatype and methods.

## List methods, functions, and operators
You may find the following methods or functions useful. For a given list `a_list`:

| Method or function                            | Description                                          |
| --------------------------------------------- | ---------------------------------------------------- |
| `a_list = [element0, element1, ... elementN]` | Initializes the list with any number of elements     |
| `a_list.append(element)`                      | Adds the element to the end of the list              |
| `len(a_list)`                                 | Returns the length of the list                       |
| `a_list.insert(i, element)`                   | Inserts the element between position `i` and `i + 1` |
| `del a_list[i]`                               | Removes the element at position `i`                  |
| `a_list.remove(element)`                      | Removes the first instance of `element`              |

Additionally, there are the following list operators:

| Operator            | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `a_list[i]`         | Accesses the element at position `i` (read or write, but must exist!) |
| `a_list == b_list`  | Evaluates to `True` if both lists contain the exact same elements     |
| `a_list + b_list`   | Concatenates the two lists together                                   |
| `a_list * N`        | Evaluates to a new list with `a_list` elements repeated `N` times     |
| `element in a_list` | Returns `True` if `element` is in the list                            |

## Exercises
1. Design a Python function named `get_courses` that returns a **list of strings** containing student courses. Your function should behave as follows:
   <pre>
   Enter the name of a course to add, or press Enter to finish: <b><u>COMP 1501</u></b>
   Enter the name of a course to add, or press Enter to finish: <b><u>MATH 1505</u></b>
   Enter the name of a course to add, or press Enter to finish:
   2 courses added
   </pre>

   > Note: the number of courses added will not always be 2 - this should be calculated.

2. Assume that your previous function returns the following list:
   ```python
   courses = ["COMP 1501", "Math 1505", "GNED 1401", "GNED 1103", "MKTG 2150",
              "COMP 1502", "COMP 2511", "MGMT 3210", "HRES 2170", "GNED 1101"]
    ```
    > You can split lists across multiple lines to enhance readability.

    Design an **algorithm** that takes your course list as an argument and returns the course with the **highest course code**. For this example, the return value of your function should be `"MGMT 3210"`.

    > Hint: assume you can split a string to separate the course code and number.

3. Assume you have two lists of quiz grades for a class of students, `quiz1` and `quiz2`. Both lists have an equal number of elements.

   1. Design a function that takes the two lists as input parameters and returns a *third* list name `higher` containing the higher of the two quiz grades for each student.
   2. Design another function that takes the `higher` list and returns the maximum grade of the class. Do not use the `max` function.
   3. Modify the previous solution so that it returns the *index* position of the maximum grade.