import json
import os
from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename + datetime.now().strftime("%d-%m-%Y") + ".json"
        self.live_people = filename + "/extra/people"
        self.live_violations = filename + "/extra/violations"
        self.live_total_violations = filename + "/extra/total_violations"


    # Deprecated
    def write_log_entry(self, date = 0, time = 0, violations = 0, people = 0):
        data = {
                "date": date,
                "time": time,
                "violations": violations,
                "people": people
            } 

            
        print(f"trying to put {data} in {self.filename}")

        if not os.path.exists(self.filename):
            with open(self.filename, 'a+') as f:
                json.dump({"entries": []}, f)

        if os.path.exists(self.filename) and os.path.getsize(self.filename) == 0:
            with open(self.filename, 'w') as f:
                json.dump({"entries": []}, f)

        with open(self.filename, 'r') as f:
            contents = json.load(f)

        with open(self.filename, 'w') as f:
            contents['entries'].append(data) 
            json.dump(contents, f)
            
    def write_live_counter(self, people = 0, violations = 0, total_violations = 0):
        with open(self.live_people, 'w') as f:
            f.write(str(people))
        with open(self.live_violations, 'w') as f:
            f.write(str(violations))
        with open(self.live_total_violations, 'w') as f:
            f.write(str(total_violations))

    def write_violation(self, date = 0, time = 0):
        data = {
                "date": date,
                "time": time
            } 

            
        print(f"trying to put {data} in {self.filename}")

        if not os.path.exists(self.filename):
            with open(self.filename, 'a+') as f:
                json.dump({"violations": []}, f)

        if os.path.exists(self.filename) and os.path.getsize(self.filename) == 0:
            with open(self.filename, 'w') as f:
                json.dump({"violations": []}, f)

        with open(self.filename, 'r') as f:
            contents = json.load(f)

        with open(self.filename, 'w') as f:
            contents['violations'].append(data) 
            json.dump(contents, f)




        

    

