import pandas as pd
import os

# providing the path of the directory
dirloc = r"/Users/username/Desktop/parent_folder/child_folder"

# calling listdir() fucntion
for file in os.listdir(dirloc):
    # find only xlsx files
    if not file.endswith(".csv"):
        # grab file path
        filename = os.path.join(dirloc, file)
        # Using splitext() to get filename and extension separately
        (base_filename, ext) = os.path.splitext(file)
        # load in Excel file
        xl = pd.ExcelFile(filename)
        # get list of sheet names
        sheet_list = xl.sheet_names
        # loop through and read each sheet in workbook
        for sheet in sheet_list:
            # read current sheet
            df = pd.read_excel(filename, sheet_name=sheet)
            # Set name of csv file to previous file name with csv extension
            csv_filename = base_filename + '_' + sheet + '.csv'
            # Create csv file path for saving purposes
            csv_file = os.path.join(dirloc, csv_filename)
            # Save file as csv
            df.to_csv(csv_file, index=None, header=True)
    else:
        continue
