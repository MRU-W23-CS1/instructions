import math

def read_CPI_file(filename: str) -> list:
    """
    Reads the CPI file and returns a list of strings.
    Skips over the 25 header lines.
    """
    cpi_list = []
    try:
        f_obj = open(filename, "r")
        # skip over the first 25 lines
        for line in range(25):
            f_obj.readline()
        
        # then read the header (but don't do anything with it right now)
        header = f_obj.readline()

        line = f_obj.readline() # the priming read
        # read the rest of the file until the "REVISIONS" line
        while "REVISIONS" not in line:
            line = line.strip().replace('"', "")
            if len(line) > 0:
                cpi_list.append(line)
            line = f_obj.readline() # internal read
        
        f_obj.close()
    except OSError:
        print("Error: could not open file", filename)
        
    return cpi_list


def clean_CPI_list(cpi_list: list) -> list:
    """
    Converts the list of strings into a list of lists of floats.
    """
    data = []
    for line in cpi_list:
        values = line.split(",")
        # The first value is a date, so let's keep it as a string
        row = [values[0]]
        # All the rest can be cast to floats
        for value in values[1:]:
            row.append(float(value))
            
        data.append(row)
    
    return data


def main() -> None:
    raw_cpi_data = read_CPI_file("CPI_MONTHLY.csv")
    cpi_data = clean_CPI_list(raw_cpi_data)
    for row in cpi_data:
        print(row)

main()