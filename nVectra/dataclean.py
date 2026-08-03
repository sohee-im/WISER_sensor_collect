import pandas as pd
# import gspread

CSV_FILE_PATH = "/Ft2_EndTarget_Pipe.csv"           # Path to your local CSV file
csvbx = "bx"            # Name of the column in your CSV (or index, e.g., 0)
csvby = "by"
csvbz = "bz"
SHEET_NAME = "3\" Nominal Schedule 80 Carbon Steel Pipe A53 Hot Rolled_Data_Collection_Run_Matrix"       # Name of your Google Sheet
WORKSHEET_NAME = "Run Matrix - Trial 1"            # Worksheet tab name
bx = "M"              # Target Google Sheet column (e.g., "A", "B", "C")
by = "N"
bz = "O"
CREDENTIALS_FILE = "credentials.json"

df = pd.read_csv("Ft2_EndTarget_Pipe.csv")
data_slice = (df["distance"].iloc[:19]).tolist()
formatted_values = [[val] for val in data_slice]

df = df.sort_values(by="distance")
df=df[["distance", "bx", "by", "bz"]]
df.to_csv("Ft2_EndTarget_Pipe.csv", sep=" ")
print(df)


sh = gc.open(SHEET_NAME)
worksheet = sh.worksheet(WORKSHEET_NAME)

# 3. Define target range (rows 100 to 119 for 20 items)
start_row = 100
end_row = start_row + len(formatted_values) - 1  # 100 + 20 - 1 = 119
target_range = f"{TARGET_COL_LETTER}{start_row}:{TARGET_COL_LETTER}{end_row}"

# 4. Update the Google Sheet range
worksheet.update(range_name=target_range, values=formatted_values)

print(f"Successfully copied 20 rows to {TARGET_COL_LETTER}{start_row}:{TARGET_COL_LETTER}{end_row}!")