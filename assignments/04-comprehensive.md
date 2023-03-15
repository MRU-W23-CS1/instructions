# Assignment 4: Comprehensive Program
- Due April 2, 2023 by 11:59 pm
- [GitHub Classroom Link](https://classroom.github.com/a/HfDY8xxK)
- Weight: 10%

## Table of Contents  <!-- omit from toc --> 
- [Objectives](#objectives)
- [Outcome](#outcome)
- [Introduction and background information](#introduction-and-background-information)
  - [Examples](#examples)
    - [Trivial solution](#trivial-solution)
    - [Line solutions](#line-solutions)
    - [Irregular solutions](#irregular-solutions)
    - [Not a solution](#not-a-solution)
- [Instructions](#instructions)
  - [File format](#file-format)
  - [Assumptions](#assumptions)
- [Starter Code](#starter-code)
  - [`written_portion.md`:](#written_portionmd)
  - [`assign4.py`: Your Python program](#assign4py-your-python-program)
  - [`data` folder:](#data-folder)
- [Research efforts](#research-efforts)
- [Marking Scheme](#marking-scheme)


## Objectives
Upon completion of this assignment, students will have had the opportunity to:
- Design and implement a complete program involving:
  - Reading and writing data files
  - Representing data as lists of lists
  - Nested loops
  - Deciding on test cases and ensuring the program meets requirements

## Outcome
Done **individually or in pairs**, this assignment consists of **two products**:

1. A **written portion** describing how your program deviated from your plan and your testing methodology.
2. The **code**: a Python file that solves the problem.

## Introduction and background information
> This problem was introduced to me by Ryan Morrill, a MATH 1505 instructor.

Consider an $n \times n$ grid of people, where each person is either a truth-teller or a liar. Truth tellers, denoted as $T$, are guaranteed to tell the truth, while liars $L$ are guaranteed to lie.

Below is an example of a 3x3 grid:

$$
\begin{array}{|c|c|c|} \hline
T & L & T \\\\ \hline
L & T & L \\\\ \hline
T & L & T \\\\ \hline
\end{array}
$$

Each person in the grid can "see" the person orthogonally adjacent to them, i.e. to the left, right, above, and below. Knowing this, the truth-teller in the top left corner could say "I see 2 liars", while the liar in the top middle might say "I see 2 truth-tellers".

The problem posed in MATH 1505 is to find all of the $n \times n$ grids of people such that each person can say "I see exactly one liar"[1^]. Instead, for this assignment, your problem flips the question on its head: Given an $n \times n$ grid of liars and truth-tellers, can each person say "I see exactly one liar"?

There are three possible categories of solutions to this problem: **trivial solutions**, **line solutions**, and **irregular solutions**. Everything else is not a solution.

[1^]: As it turns out, this is a pretty tricky problem - I tried writing a brute-force script to find them all, and had to give up after $n=6$ when my code took over a week to run.

### Examples
The following are **non-comprehensive** examples of the various categories of solutions.
#### Trivial solution

$$
\begin{array}{|c|c|c|} \hline
L & L & L \\\\ \hline
L & L & L \\\\ \hline
L & L & L \\\\ \hline
\end{array}
$$

A grid made of entirely liars has more than one liar adjacent to each person, so when each lies and says "I see exactly one liar", the requirements are satisfied. However, this is pretty boring and is referred to as the **trivial solution**. 

#### Line solutions
Another category of somewhat boring solutions is called **line solutions**. This is a class of solutions where all of the truth-tellers and liars are in a single line, e.g.:

$$
\begin{array}{|c|c|c|c|} \hline
T & T & T & T \\\\ \hline
L & L & L & L \\\\ \hline
L & L & L & L \\\\ \hline
T & T & T & T \\\\ \hline
\end{array}
$$

or, with the truth-tellers in the middle:


$$
\begin{array}{|c|c|c|c|} \hline
L & L & L & L \\\\ \hline
T & T & T & T \\\\ \hline
T & T & T & T \\\\ \hline
L & L & L & L \\\\ \hline
\end{array}
$$

or rotated 90 degrees:

$$
\begin{array}{|c|c|c|c|} \hline
L & T & T & L \\\\ \hline
L & T & T & L \\\\ \hline
L & T & T & L \\\\ \hline
L & T & T & L \\\\ \hline
\end{array}
$$

Be very careful though, not every configuration of lines is a line solution!

#### Irregular solutions
Finally, we start getting to some interesting solutions. **Irregular solutions** are grids where the truth-tellers and liars are not in a line, but still satisfy the requirements. For example:

$$
\begin{array}{|c|c|c|c|} \hline
T & T & L & T \\\\ \hline
L & T & T & T \\\\ \hline
T & T & T & L \\\\ \hline
T & L & T & T \\\\ \hline
\end{array}
$$

#### Not a solution
Finally, the majority of grids are not solutions at all. For example:

$$
\begin{array}{|c|c|c|} \hline
T & L & T \\\\ \hline
L & T & L \\\\ \hline
T & L & T \\\\ \hline
\end{array}
$$

or, in a $6 \times 6$:

$$
\begin{array}{|c|c|c|c|c|c|} \hline
L & L & T & L & T & T \\\\ \hline
L & L & T & T & L & L \\\\ \hline
L & L & T & T & L & L \\\\ \hline
L & T & L & L & T & T \\\\ \hline
L & L & T & T & L & L \\\\ \hline
L & L & T & T & L & L \\\\ \hline
\end{array}
$$

or, a sneaky one that looks like a line solution, but isn't:

$$
\begin{array}{|c|c|c|c|} \hline
L & T & T & T \\\\ \hline
L & T & T & T \\\\ \hline
L & T & T & T \\\\ \hline
L & T & T & T \\\\ \hline
\end{array}
$$

Basically, if any one person (liar or truth-teller) **cannot** say "I see exactly one liar", then the grid is not a solution.

## Instructions
Your task is to write a program that:
- Read a text file named `input.txt` containing a grid of people of arbitrary size $n$, but minimum $n = 1$
- Parses the contents of the file into a list of lists
- Classifies the solution as trivial, line solution, irregular solution, or not a solution
- Writes the grid back to a new file named `output.txt` with the solution type under it

To keep your workspace organized, the input and output files should be in a folder named `data` in the same directory as your program.

### File format
The input file will be a text file named `input.txt` where each line represents a row of the grid, with "L" representing a liar and "T" representing a truth-teller, with cells separated by spaces. For example, the following is a valid input file:

```
L L L
L L L
T T T
```

After processing with your program, the output file (`output.txt`) should look like this:

```
L L L
L L L
T T T

line solution
```

The solution type is not case sensitive, but should use the language "trivial", "line", "irregular", or "not a solution". The number of spaces between the grid and classification is also not relevant.

### Assumptions
- The input file will always be a valid $n \times n$ grid, where $n \geq 1$
- Each cell will always be either "L" or "T"
- The grid will be represented as a list of lists
- The folder `data` exists in the same directory as your program and contains the input file `input.txt`
- No user input is required when running the program

## Starter Code
Click on the [GitHub Classroom Link](https://classroom.github.com/a/HfDY8xxK) to clone your starter code. There are 2 files for you to modify and submit:

### `written_portion.md`:
The written portion contains two questions:
1. How did your program deviate from your original plan? Next week, we will have a short quiz where you will be asked to plan your program by breaking down the problem into different components and defining logical functions. However, plans always change during implementation! Describe what changes you made and why. If you did not make any changes, justify this decision.
2. How did you test your program? While several test files are provided, these are not exhaustive. Describe how you tested your program to ensure it works for all possible inputs.

### `assign4.py`: Your Python program
Implement your program solution in `assign4.py`. Your program **must**:
- define and call a void `main` function that is the main entry point to your program
- store the grid as a **list of lists**

Otherwise it is up to you to design the structure!

Your script should follow Python style guides, meaning:
- Use descriptive variable names
- Use named constants where appropriate
- Include comments if needed to clarify code behaviour, and docstrings and type hinting for your functions
- Use functions to break your code into meaningful chunks

Your code **must not** use use any Python techniques that have not been covered in class. This means it **cannot** use:
- older style string formatting (`%` or `.format`)
- tuples, dictionaries, or other data types beyond `int`, `float`, `str`, `list`, and `bool`
- external modules other than `math` or `random` (though you shouldn't need them)
- **This is not a complete list!**

> Why not? There are many Python solutions to problems such as these out there in the wild, and if I see advanced concepts in your code, I have no way of knowing that you understand what you are writing. If you have prior Python experience, consider it a challenge to solve the problem using a limited set of tools.

### `data` folder:
In addition to the source code, there is a directory containing the following:
- `input.txt`. This is the input file that your program will read from.
- `2x2trivial.txt`. This is an example of a trivial solution.
- `3x3line.txt`. This is an example of a line solution.
- `4x4irregular.txt`. This is an example of an irregular solution.
- `5x5notasolution.txt`. This is an example of not a solution.

> While testing, I recommend that you modify your program to read from the various input files, otherwise it will be tedious to copy and paste to `input.txt` all the time. However, make sure that your final submission reads from `input.txt`.

## Research efforts
Although background information is presented here, a good problem solver knows to conduct their own research. If you don't understand some aspect of the material, consult with your partner and/or look it up. You will find solutions and online calculators for this type of problem on the internet, but ***you must ALWAYS cite the sources of your ideas.*** 

Citing can be done by adding comments like these to your code:

```python
# Algorithm inspired by http://citebay.com/how-to-cite/stackoverflow/
# Jordan Pratt helped me with the next four lines
```

**If you get help from a friend, cite their assistance**. Without a citation all I see is two highly similar submissions, which will result in a plagiarism report.

Note: citing a source is not carte blanche to just copy code. Try reading a source, then writing your version **without looking** at the original source.

## Marking Scheme
This time, there are no tests provided for you. Training wheels are off! You may certainly write your own test functions, but a consideration of which test cases to consider is an important learning objective.

Written portion (each part out of 4 = 8):
- [ ] Deviation from plan is clearly described and well justified, OR if plan was carried out without deviation, justify this choice.
- [ ] Testing description is clearly described and demonstrates appropriate choices and testing methodology.

Source code (each part out of 4 = 44):
- [ ] No syntax or runtime errors
- [ ] Code style (variable names, readability, comments as appropriate, etc)
- [ ] Program structure (appropriate use of functions, minimal redundancy, etc)
- [ ] Appropriate use of variables (scope, constants, list of lists, etc)
- [ ] Correct file reading/writing with **relative paths**
- [ ] Correct output file format
- [ ] Correct classification of trivial solutions
- [ ] Correct classification of horizontal line solutions
- [ ] Correct classification of vertical line solutions
- [ ] Correct classification of irregular solutions
- [ ] Correct classification of not a solution

Furthermore, you must at least attempt the classification portion of the assignment to earn a passing grade. If your program does not come close to solving the problem, the highest mark possible is 50%.

*Note:*  
0/4 means not done or missing.   
1/4 means major errors.  
2/4 means major error or many small errors.   
3/4 means a few small errors.    
4/4 is correct/complete.

Remember: Your code **must not** use use any Python techniques that have not yet been covered in class. Use of more advanced techniques will result in a penalty and a discussion with me to explain your decisions.