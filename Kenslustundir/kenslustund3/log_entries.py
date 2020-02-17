from datetime import datetime

class LOG_ENTRIES():
    def __init__(self):
        self.data_logs = dict()
    
    def add_entry(self):
        date = datetime.now()
        log = input("please enter a entry ")
        return_str = date + log
        self.data_logs[date] = log
        return return_str
    
    def __str__(self):

    def return_all_entries(self):
        for key,val in self.data_logs.items():
            print(key, val)
        

    def delete_entries(self):
        
    
    def return_newest_log(self):
        for time
    
    def add_to_database(self):