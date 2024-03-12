import json
from jsonl2json import JsonlToJsonFormatter


def convert_to_llama2(gpt_data):
    llama2_data = []
    for row in gpt_data:
        messages = row['messages']
        reformatted_segments = []

        for message in messages:
            if message['role'] == 'system':
                inst_text = message['content']
            elif message['role'] == 'user':
                human_text = message['content']
            elif message['role'] == 'assistant':
                assistant_text = message['content']
                reformatted_segments.append(
                    f'<s>[INST]<<SYS>> {inst_text} <</SYS>> {human_text} [/INST] {assistant_text} </s>')
            else:
                reformatted_segments.append(f'<s>[INST] {human_text} [/INST] </s>')

        llama2_data.append({'text': ''.join(reformatted_segments)})

    return llama2_data


def main():
    # convert the jsonl to json file
    jsonl = JsonlToJsonFormatter('first_30.jsonl', 'first_30.json')
    jsonl.to_json()
    # Read GPT JSON file
    with open('first_30.json', 'r') as f:
        gpt_json = json.load(f)

    # Convert GPT data to llama2 format
    llama2_data = convert_to_llama2(gpt_json)

    # Write llama2 data to file
    with open('output_llama2_30.json', 'w') as f:
        json.dump(llama2_data, f, indent=4)


if __name__ == "__main__":
    main()
