import pandas as pd


class Annotator:
    
    def __init__(self, data: pd.DataFrame, file_path="./labelled_data.csv"):
        """
        Class the wraps functionality to annotate the Market data to mark important price actions like
        Break-Outs, Trends etc. The class does not have any intelligence at of yet to identify the 
        price action point rather provide the functionality to mark the events given the timestamp
        
        Parameters:
        -----------
        
            data: pd.DataFrame
                market data in the order of OHLC and pandas.DateTimeIndex as Index
                
            file_path: str
                path to save the DataFrame as csv file
                
        Methods:
        --------
            annotate(timestamp: str, label:int, save_instant: bool)
                Annotates and Stores the annotated dataframe to file
            
        """
        self.data = data
        self.data["label"] = 0
        self.file_path = file_path
        
    def annotate(self, timestamp: str, label: int, save_instant=False):

        self.data[timestamp, "label"] = label

        if save_instant:
            self.data.to_csv(self.file_path)

    def __del__(self):
        self.data.to_csv(self.file_path)
            
            
            
            