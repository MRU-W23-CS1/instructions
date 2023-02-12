# Assignment 3: Functions and decisions
- Due March 5, 2023 by 11:59 pm
- [GitHub Classroom Link](https://classroom.github.com/a/qyDkb1T3)
- Weight: 10%

## Objectives
Upon completion of this assignment, students will have had the opportunity to:
- Gain experience testing software behaviour
- Practice designing and implementing complex decision structures
- Build a program with  multiple functions and function calls

## Outcome
Done **individually or in pairs**, this assignment consists of **two products**:

1. A **written description** of your experimentation process.
2. The **code**: a Python file that solves the problem.

## Introduction and background information
You are hiking through the forest one day when a tiny chipmunk scampers up and hands you a device. Gesticulating wildly while uttering a series of squeaks, you look down at the device and hear corresponding sounds that seem like it's **translating** for the chipmunk, but not into any human language that you know of. You begin fiddling with the **various switches and inputs** and eventually figure out that the chipmunk is warning you of a bear further down the trail. This seems like pretty useful technology, so you'd like to duplicate it.

The device is pretty complex, but to begin with, you decide to create a program that can **translate English phrases** into various **animal languages**. Not every device has the same language settings though, so it's up to you to play around with the settings on **your individual device** to figure out what languages can be used.

## Instructions
1. Visit [https://mru-translator.fly.dev/](https://mru-translator.fly.dev) and enter your MRU username where indicated. **Your MRU username must match your Python file** in order for you to receive full marks, as this defines the language options. If you are working in partners, **choose one username** for all of your testing and implementation.
2. Keeping the username constant, choose various phrases to translate and modify the switches A and B and the volume control, pressing the "Translate!" button for each combination. Document your experiments until you have established the behaviour. 
3. Using the provided starter code, write a Python program that duplicates the behaviour of the translator. **Do not** prompt the user for their MRU username. When executed, your program should look something like this, where text in **bold** represents user input. Note that your exact output **will be different** depending on your username.

<pre>
Enter the phrase to translate: <b>Hello, world!</b>
Is switch A on? (y/n): <b>n</b>
Is switch B on? (y/n): <b>y</b>
Enter the volume: <b>5</b>
Result:
🦫🦫🦫🦫🦫
Hello, world!
🦫🦫🦫🦫🦫
</pre>

> Tip: Emojis are **unicode characters** that display differently on different platforms. The easiest way to make sure yours matches the website is to just copy and paste from the website to your code.

## Assumptions
To make things manageable, you can assume the following:
1. Only upper case (A-Z) or lower case (a-z) English characters may be modified by the translator (i.e. numbers, punctuation, and non-English characters will pass through unmodified).
2. Only integers need to be considered in the volume input.
3. Each device has a maximum and minimum volume. When the numbers stop changing the output, it is safe to say that you've found the boundary.
4. The behaviour is always the same for a given MRU username (case insensitive).
5. When writing your code, you can assume the user provides **valid input**. This means they will always enter `y` or `n` when prompted `y/n`, and will always enter an integer when prompted for the volume.

If you make further assumptions (and you probably should), **document them** in your experimentation log.

## Deliverables
Click on the [GitHub Classroom Link](https://classroom.github.com/a/qyDkb1T3) to clone your starter code. There are 2 files for you to modify and submit:

### `experimentation.md`: Your experimentation log
Write your name (and the name of your partner) and record the results of your experimentation in `experimentation.md`. Make sure to record any **additional assumptions** that you make in your experimentation log.

If you are working in partners, **choose one username** for all of your experimentation and implementation.

The goal of the experimentation log is to make it clear what your process was, what decisions you made, and how the results support your conclusion.

### `assign3.py`: Your Python program
Implement your program solution in `assign3.py`. Make sure to define your **MRU Username** as a string constant where indicated in the starter code. This is used to compare your output with the website.

To provide some guidance, the starter code has several functions for you to complete. **Do not modify the function headers**. For each of the predefined functions, implement an algorithm solving the specified task. You **must define at least one** additional function.

Your script should follow Python style guides, meaning:
- Use descriptive variable names
- Use named constants where appropriate
- Include comments if needed to clarify code behaviour

Your code **must not** use use any Python techniques that have not yet been covered in class. This means it **cannot** use:
- older style string formatting (`%` or `.format`)
- lists, tuples, dictionaries, or other data types beyond `int`, `float`, `str`, and `bool`
- try/except
- custom classes
- modules aside from the `math` module
- **This is not a complete list!**

> Why not? There are many Python solutions to problems such as these out there in the wild, and if I see advanced concepts in your code, I have no way of knowing that you understand what you are writing. If you have prior Python experience, consider it a challenge to solve the problem using a limited set of tools.

## Research efforts
Although background information is presented here, a good problem solver knows to conduct their own research. If you don't understand some aspect of the material, consult with your partner and/or look it up. You will find solutions and online calculators for this type of problem on the internet, but ***you must ALWAYS cite the sources of your ideas.*** 

Citing can be done by adding comments like these to your code:

```python
# Algorithm inspired by http://citebay.com/how-to-cite/stackoverflow/
# Jordan Pratt helped me with the next four lines
```

Note: citing a source is not carte blanche to just copy code. Try reading a source, then writing your version **without looking** at the original source.

## Marking Scheme
A handful of tests are provided for you to check that you are on the right track. However, passing these tests is not sufficient to ensure full marks! In particular, the tests have no knowledge of your translator parameters, they just look at (some) data types and input prompting.

Experimentation log (each part out of 4 = 12):
- [ ] Assumptions reasonable and clearly stated
- [ ] Appropriate choice of test phrase(s)
- [ ] Sufficient testing of switch combinations and volume control

Source code (each part out of 4 = 44):
- [ ] No syntax or runtime errors
- [ ] Code style (variable names, readability, comments as appropriate, etc).
- [ ] Function arguments are correct data types
- [ ] Function return values are correct data types
- [ ] Variable scope is appropriate
- [ ] Effective and appropriate additional function
- [ ] Translation of **any English phrase** matches website behaviour
- [ ] Good `translate` selection structure
- [ ] Good `volume` selection structure
- [ ] Input prompts are as specified (order, `y/n`, etc)
- [ ] `main` function calls other functions and passes values as required


*Note:*  
0/4 means not done or missing.   
1/4 means major errors.  
2/4 means major error or many small errors.   
3/4 means a few small errors.    
4/4 is correct/complete.

Remember: Your code **must not** use use any Python techniques that have not yet been covered in class. Use of more advanced techniques will result in a penalty and a discussion with me to explain your decisions.