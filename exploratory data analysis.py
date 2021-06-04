import pandas as pd 
from pandas_profiling import ProfileReport

## Reading the Data Frame:
df = pd.read_csv("data.csv")
print(df)

#Generate a Report
profile = ProfileReport(df)
# Report in a file
profile.to_file(output_file ="output.html")
