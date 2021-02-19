import json
import os

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def write_log_entry(self, time = 0, violations = 0, people = 0):
        data = {
                "timeStamp": time,
                "violations": violations,
                "people": people
            } 

            
        print(f"trying to put {data} in {self.filename}")

        if os.path.getsize(self.filename) == 0:
            with open(self.filename, 'w') as f:
                json.dump({"entries": []}, f)


        with open(self.filename, 'r') as f:
            contents = json.load(f) 

        with open(self.filename, 'w') as f: 
            contents['entries'].append(data) 
            json.dump(contents, f)
            


        

    

