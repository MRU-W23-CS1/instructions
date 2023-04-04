# Classes
[GitHub Classroom Link](https://classroom.github.com/a/3puV4ug-)

## Instructions 
In [yesterday's tutorial](https://github.com/MRU-W23-CS1/instructions/tree/main/tutorials/09-exceptions), I asked you to add some exception handling to a program that reads a CSV file containing consumer price index (CPI) data. In today's starter code, I've provided a solution! However, I also asked you to think about how to rewrite this code to use a **custom class** instead of the list of mixed data types.

I have written a custom classed called `CPIRecord` in the module `cpi_record.py`. **Do not modify this file**. Instead, all your modifications should be made to `cpi.py`.

1. Modify the `clean_CPI_list` function so that it returns a list of `CPIRecord` objects instead of a list of lists.
   > Hint: you will need to import the `CPIRecord` object from the `cpi_record` module, then create a new instance for each line in the file.
2. Implement the `count_over_3` function to count and return the number of months where the `CPI_TRIM` value exceeded 3%. Remember, you can access an **attribute** of an object with `.` syntax. Feel free to look at the `cpi_record.py` file to see the names of all the attributes.
3. Implement the `highest_inflation_date` function to go through all the CPI records and find and return the **date** corresponding to the highest `CPI_TRIM` value.
4. Call both of your new functions and print out the results in `main`.

## Testing
Try to test your code first **before** running the automated tests - these should just confirm what you already know, not be used as a tool to exclusively check your work.

This lab has 5 tests. 3 of them must be passed to pass the lab.