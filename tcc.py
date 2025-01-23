import os
import glob
import pandas as pd

def list_files(dir_name):

    return sorted(filter(os.path.isfile, glob.glob(os.path.join(dir_name, "*.csv"))))

def read_and_process_csv(file_path):

    file_name = os.path.basename(file_path)  # Extract the file name

    df = pd.read_csv(file_path, skiprows=10, encoding='iso-8859-1', sep=';', decimal=',')

    df.dropna(axis=1, how='all', inplace=True)

    df.dropna(axis=0, how='all', inplace=True)

    df.insert(0, 'FileName', file_name)

    return df

def main(input_dir, output_file):

    list_of_files = list_files(input_dir)

    all_data = []  

    for file_path in list_of_files:
        try:
            df = read_and_process_csv(file_path)
            all_data.append(df)  
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    final_df = pd.concat(all_data, ignore_index=True)

    final_df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Consolidated data saved to {output_file}")


input_directory = "dados-pais/"

output_csv = "dados_consolidados.csv"

main(input_directory, output_csv)