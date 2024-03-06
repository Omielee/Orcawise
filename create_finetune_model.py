from openai import OpenAI
client = OpenAI()

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
    "epochs" : 3,
    "temparature":0.8,
    "learning_rate":0.001,
    "batch_size":32
}

training_data_file = "path"
api_key="api_key"

# Use the fine-tuned model
finetuner = GPTFineTune(api_key,training_data_file,parameters)
response = finetuner.fine_tune()

print(response)