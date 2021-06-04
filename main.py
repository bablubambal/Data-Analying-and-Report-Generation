import pandas as pd 
from pandas_profiling import ProfileReport

## Reading the Data Frame:
df = pd.read_csv("housing.csv")
print(df)

#Generate a Report
profile = ProfileReport(df,minimal = True)
# Report in a file
profile.to_file(output_file ="housing.html")
