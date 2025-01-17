import time as tm
import os
import pandas as pd

def disply_cli_art():
    print("********************************************************************")
    art = r"""
  ____ ______     __  ____    ____                            _   
 / ___/ ___\ \   / / |___ \  |  _ \ __ _ _ __ __ _ _   _  ___| |_ 
| |   \___ \\ \ / /    __) | | |_) / _` | '__/ _` | | | |/ _ \ __|
| |___ ___) |\ V /    / __/  |  __/ (_| | | | (_| | |_| |  __/ |_ 
 \____|____/  \_/    |_____| |_|   \__,_|_|  \__, |\__,_|\___|\__|
                                                |_|               
"""
    print(art)
    print("********************************************************************\n")

def convert_csv_to_parquet():
    """
    Detects a CSV file in a specified source folder, converts it to a Parquet file,
    and saves it to the output folder. Finally moves the csv file to converted folder.
    Handles errors and ensures directories exist.
    """

    source_folder = "source"
    output_folder = "output"
    converted_folder = "converted"    
    
    print("\nInitializing...\n")    
    tm.sleep(5)

    # Ensure necessary directories exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(converted_folder):
        os.makedirs(converted_folder)

    # Look for the first CSV file in the source folder
    csv_files = [f for f in os.listdir(source_folder) if f.endswith(".csv")]
    if not csv_files:
        print("No CSV files found in the source folder.")
        return

    csv_file = csv_files[0]  # Pick the first CSV file
    csv_path = os.path.join(source_folder, csv_file)

    # Define the output Parquet file path
    parquet_file = os.path.splitext(csv_file)[0] + ".parquet"
    parquet_path = os.path.join(output_folder, parquet_file)

    try:
        # Read the CSV file
        print(f"Reading CSV file: {csv_path}")
        data = pd.read_csv(csv_path)

        # Convert to Parquet
        print(f"Writing Parquet file: {parquet_path}")
        data.to_parquet(parquet_path, engine="pyarrow", index=False)

        # Move the CSV file to the converted folder
        converted_path = os.path.join(converted_folder, csv_file)
        os.rename(csv_path, converted_path)
        print(f"Moved CSV file to: {converted_path}")

        print("Conversion completed successfully.")
    except Exception as e:
        print(f"Error during conversion: {e}")

def main():
    disply_cli_art()
    convert_csv_to_parquet()

if __name__ == '__main__':
    main()