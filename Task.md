# Task and Notes

## March 1, 2024
- What we can improve the finetuning model
    - we can see how to set the epochs and see other parameters
    - If the parameters can be set using the python code then you have to find the code where after you can save the model, train the model,load the model and do the prediction and add the result to database to check the accuracy the model
        1. Get the API key from OpenAI
        2. Upload and train the model, get the unique *model identifier*.
        3. Install OpenAI Python
        ```
        pip install openai
        ```
        4. Utilize API calls to invoke the model
        ```
        import openai
        openai.api_key = 'your-api-key-here'
        response = openai.Completion.create(
            engine="your-model-identifier",
            prompt="This is a test prompt",
            max_tokens=50
        )
        print(response.choices[0].text.strip())
        ```
        https://platform.openai.com/docs/guides/fine-tuning/iterating-on-hyperparameters
    - The best parameters to fine tune the model
        1. Learning rate
        2. Batch size
        3. Number of epochs
        4. Weight Decay
        5. Optimizers

        https://www.codecademy.com/article/setting-parameters-in-open-ai
        1. Temperature: Controls the randomness of responses.
        2. Max Tokens: Sets the maximum length for the model’s output.
        3. Top P (Nucleus Sampling): Dictates the variety in responses by only considering the top ‘P’ percent of probable words.
        4. Frequency Penalty: Reduces repetition by decreasing the likelihood of frequently used words.
        5. Presence Penalty: Promotes the introduction of new topics in the conversation.
        6. epochs
        7. learning rate multiplier
        8. batch size
        ```
        from openai import OpenAI
        client = OpenAI()

        client.fine_tuning.jobs.create(
        training_file="file-abc123", 
        model="gpt-3.5-turbo", 
        hyperparameters={
            "n_epochs":2
        }
        )
        ```