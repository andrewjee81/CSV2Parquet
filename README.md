# CSV 2 Parquet

The Mrs needed a script to read and convert CSV to Parquet file and asked if I could do something in Python. A bit of research on Google and we can do just that with pandas and pyarrow.



## Install Necessary Libraries

```python
pip install pandas pyarrow
```
## Test Code
My initial test code to try out pandas and pyarrow

```python
import pandas as pd

# Load the CSV file
csv_file = "input_file.csv"

data = pd.read_csv(csv_file)

# Convert to Parquet and save
parquet_file = "output_file.parquet" 
data.to_parquet(parquet_file, engine='pyarrow', index=False)

print(f"CSV file converted to Parquet and saved at: {parquet_file}")
```
## What Next?
Just for fun i expanded the test code further

1. Check in a source folder for a CSV file
2. Check if the output and converted folders exists
3. Error handling
4. Display a ASCII art and a time delay before executing the conversion

## Executable file
The Mrs work machine does not have Python setup so an executable file it is.

```python
pyinstaller --onefile --icon=cat_ghost.ico main.py
```
