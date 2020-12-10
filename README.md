# Quick and Easy Python: Excel to CSV with Pandas

The purpose of this script is to automate the process of converting Excel files into CSV files.
To suit my own personal needs, the script loops through a list of subdirectories within a main directory, and then loops through all the files contained in those subdirectories.
If the file is .xlsx, .xls, or .xlsm, it is converted to CSV with Pandas and saved to an output directory.
If the file is .csv already, it saves a copy of the file in the output directory.
If the file does not contain any of those extensions, it will skip the file.

Additionally, some Excel files have more than one sheet. Therefore, I included the capability to read the sheet names of each Excel document, and save separate CSV files for each sheet. 

I hope you all find this useful - enjoy!
