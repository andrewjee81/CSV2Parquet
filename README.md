# CSV 2 Parquet

The Mrs needed a script to read and convert CSV to Parquet file and asked if I could do something in Python. A bit of research on Google and we can do just that with [pandas](https://pandas.pydata.org/) and [PyArrow](https://pypi.org/project/pyarrow/).



## Install Necessary Libraries
Refer to the notes at the end for Fastparquet library.
```
pip install pandas pyarrow
# or
pip install pandas fastparquet
```
## Test Code
My initial test code to try out pandas and PyArrow

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
3. Move CSV file from source to converted folder once Parquet file is created
4. Error handling
5. Display ASCII art and a time delay before executing the conversion

## Executable file
The Mrs work machine does not have Python setup so an executable file it is.

```
pyinstaller --onefile --icon=cat_ghost.ico main.py
```

> [!NOTE]
> An alternative to PyArrow is [Fastparquet](https://pypi.org/project/fastparquet/). To use Fastparquet just change the engine to fastparquet.
> ```python
> data.to_parquet(parquet_file, engine='fastparquet', index=False)
> ```
> The engine parameter specifies the backend library (pyarrow or fastparquet). If you don't specify it, pandas will automatically select the available one. I have code OCD so I will always specify what to use.
