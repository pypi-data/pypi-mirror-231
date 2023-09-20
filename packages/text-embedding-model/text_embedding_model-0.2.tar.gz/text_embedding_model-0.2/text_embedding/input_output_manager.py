import os
from datetime import datetime
import pandas as pd 

from .config import encoding_list

class InputOutputManager:
    """
    Handle data input and output
    """
    InputFileName = 'base_text'
    
    def __init__(self, input_path: str, output_path: str):
        """
        :param input_path: str. The path of input folder
        :param out_path: str. The path of output folder
        """
        self._input_path = input_path
        self._output_path = output_path
        self.encoding_list = encoding_list
        
        if not os.path.exists(self._output_path):
            os.mkdir(self._output_path)


    def read_data_from_csv(self) -> pd.DataFrame:
        """
        Read the csv file from input path.

        :return: 
        :rtype: pd.DataFrame
        """

        input_file_name = os.path.join(self._input_path, f'{self.InputFileName}.csv')
        for encoding in self.encoding_list:
            try:
                df = pd.read_csv(input_file_name, encoding=encoding)
                df.sort_values(by='flag', ascending=False, inplace=True)
                return df
            except Exception as err:
                print(f'Read csv error occurred: {err}, trying other encoding')
    

    def save_data(self, df_output: pd.DataFrame, output_filename: str):
        """
        Save all output as csv to the output folder.

        :param df_output: pd.DataFrame.
        :param output_filename: str.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        output_file_path = os.path.join(self._output_path, f'{output_filename}_{current_time}.csv')
        df_output.to_csv(output_file_path, index=False)

        print(f'{output_filename} saved as CSV!')