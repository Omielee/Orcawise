import json
import random

class JSONLinesProcessor:
    # Initialization the method
    def __init__(self,filename):
        self.filename = filename
        self.data_list = []
    
    # Read and shuffle the JSON file data
    def read_shuffle(self):
        with open(self.filename,'r') as file:
            for line in file:
                data = json.loads(line)
                self.data_list.append(data)
        random.shuffle(self.data_list)
    
    # Retrieve the first n data
    def get_n_data(self,n=1000):
        return self.data_list[:n]

    # Retrieve one random data
    def get_random(self):
        return random.choice(self.data_list)
  
    # Save the new Json file
    def save_to_file(self,data,new_filename):
        with open(new_filename,'w') as file:
            for item in data:
                json_line = json.dumps(item) # convert the element into a JSON string
                file.write(json_line+'\n') # write the JSON string to the file, one element per line

# Use the class
processor = JSONLinesProcessor('/Users/Alpha/Documents/GitHub/Orcawise/final_data_chatgpt.jsonl1')
processor.read_shuffle()

# Save the first 1000 data into a new file
first_50=processor.get_n_data(50)
processor.save_to_file(first_50,'first_50.jsonl')

# Save the one random data into a new file
# random_data = [processor.get_random()]
# processor.save_to_file(random_data,'random_data.jsonl')

