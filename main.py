import pandas as pd
import os

# providing the path of the source directory
source_dirloc = r"/Users/username/Desktop/parent_folder/source_child_folder"

# providing the path of the output directory
output_dirloc = r"/Users/username/Desktop/parent_folder/output_child_folder"

# calling listdir() fucntion
for subdir in os.listdir(source_dirloc):
    if os.path.isdir(subdir):
        for file in os.listdir(subdir):
            # find only xlsx files
            if file.endswith(".xlsx") or file.endswith(".xls") or file.endswith(".xlsm"):
                # grab file path
                filename = os.path.join(source_dirloc, file)
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
                    csv_file = os.path.join(output_dirloc, csv_filename)
                    # Save file as csv
                    df.to_csv(csv_file, index=None, header=True)
            elif file.endswith(".csv"):
                # grab file path
                filename = os.path.join(source_dirloc, file)
                #load in csv
                df = pd.read_csv(filename)
                # create path to csv copy file location
                csv_file = os.path.join(output_dirloc, filename)
                # Save file as csv
                df.to_csv(csv_file, index=None, header=True)
            else:
                continue
    else:
        continue
