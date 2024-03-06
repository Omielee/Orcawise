from openai import OpenAI

class GPTFineTune:
    def __init__(self,api_key,training_data,parameters):
        openai.api_key= api_key
        self.training_data = training_data
        self.parameters = parameters

# Read the training file
    def reading_training_file(self):
        with open (self.training_data_-file,'r') as file:
            data=file.read()
        return data
    

# Create a fine-tune model
    def fine_tune(self):
        response = openai.Finetune.create(
        data = self.training_data, **self.parameters
        )
        return response

parameters = {
    "model" :"gpt-3.5-turbo",
    "epochs" : 3, # 3-5 if less than 1000, 5-10 if 1000-10000, 10+ if over 10000
    "temparature":0.8, # higher: variation/risky; lower: focus on response, more accurate;
    "learning_rate":0.001, # if the dataset is small,eg. 700, start from 0.001 to avoid overfitting
    "batch_size":32 # 8,16,32 if less than 1000;32,64,128 if 1000-10000; 128,256 if over 10000
}

training_data_file = "path"
api_key="api_key"

# Use the fine-tuned model
finetuner = GPTFineTune(api_key,training_data_file,parameters)
response = finetuner.fine_tune()

print(response)