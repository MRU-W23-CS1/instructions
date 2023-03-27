# Exceptions and dealing with data files
The following exercise is intended to give you practice with handling exceptions and dealing with real-world data files.

## Reading CPI data
Comma Separated Value (CSV) files are a common way to store data. They can be loaded in a spreadsheet program like Excel or Google Sheets and displayed as data in cells. As the name suggests, CSVs contain lines of text with values separated by commas.

Download the file [CPI_MONTHLY.csv](https://www.bankofcanada.ca/valet/observations/group/CPI_MONTHLY/csv) from the [Bank of Canada](https://www.bankofcanada.ca/rates/price-indexes/cpi/) website. Open the file in a **text editor** (VS Code or Notepad or similar, **not Excel**) to see what it looks like. The first 26 lines are a header describing the data, while the rest is the data itself. The last header line contains column labels for the data. The column labels and first two data lines look as follows:

```plaintext
"date","V41690973","V41690914","STATIC_TOTALCPICHANGE","CPI_TRIM","CPI_MEDIAN","CPI_COMMON","ATOM_V41693242","STATIC_CPIXFET","CPIW"
"1995-01-01","86.6","86.6","0.6","1.8","1.8","1.0","","2.2","1.7"
"1995-02-01","87.0","87.0","1.9","1.9","1.8","1.0","","1.8","1.7"
```

These would be interpreted by Excel as:

|date| V41690973 | V41690914 | STATIC_TOTALCPICHANGE | CPI_TRIM | CPI_MEDIAN | CPI_COMMON | ATOM_V41693242 | STATIC_CPIXFET | CPIW |
| - | - | - | - | - | - | - | - | - | - |
| 1995-01-01 | 86.6 | 86.6 | 0.6 | 1.8 | 1.8 | 1.0 |  | 2.2 | 1.7 |
| 1995-02-01 | 87.0 | 87.0 | 1.9 | 1.9 | 1.8 | 1.0 |  | 1.8 | 1.7 |


Notice that column 7 (`ATOM_V41693242`) contains **empty records**. This will require some exception handling to parse! Later on in the file this value is populated - it is a measure that wasn't recorded prior to 2000.

The exact meaning of these values is beyond the scope of this class, but fortunately, we can work with data even if we don't understand it.

### Steps
1. Move the `CPI_MONTHLY.csv` file to your **working directory**. This is the folder that you open in VS Code.
2. Download the [starter code](https://github.com/MRU-W23-CS1/instructions/raw/main/tutorials/09-exceptions/cpi.py) and put it in your working directory. This code has two functions defined in addition to main:
   1. `read_CPI_file`: This function reads the file and returns a list of strings. It removes the header and the `"` characters, and is functioning as intended.
   2. `clean_CPI_list`: This function takes the list of strings and converts it into a list of lists of floats. It skips over the header line and the date column, but still isn't working quite right.
3. Run the code and observe the error messages. Can you pinpoint the statement where things go wrong?
4. Fix `clean_CPI_list` so that it can handle missing data. Hint: attempting to cast an empty string to a float will generate a `ValueError`.
   > Try replacing non-numeric values with `math.nan`. This is a special number that indicates a value is not a number. Why would we choose this value instead of something like 0 or -1?
5. Write a **new function** that takes the list returned from `clean_CPI_list` as an argument and returns an `int`. With reference to the CPI_TRIM column (a measure of inflation over the past 12 months), count and **return** how many months inflation has exceeded 3%.
   > Hint: you'll need to figure out which column index corresponds to the CPI_TRIM value.

### Thinking about classes
In general, it's not a great idea to mix data types in a single list, yet this is what `clean_CPI_list` does (the first item in each row is a date while the rest are floats). It would be better to define a **custom class** to represent each row of information. Not only would this separate the date from the float data, it would allow us to refer to each column by **name** instead of by **index**. This would make the code more readable and easier to maintain.

For now we'll just think about how to do this, without actually implementing.
1. Come up with a name for a class to represent the data in each row using Python naming convention for classes.
2. Decide on the attributes that the class should have and their data types. For example, the **date** should be a string.

This particular class doesn't really have much in the way of **methods** - it's just a bundle of data. On Wednesday we'll discuss how to create instances of this class and how to use them.

### Extra challenges
1. Rather than just counting how many months inflation has exceeded 3%, display the date and corresponding CPI-trim value for each year above the threshold.
2. Modify your previous function to accept a variable threshold as an argument instead of hard-coding to 3%.
3. Write a new function that returns the date corresponding to the highest inflation value.