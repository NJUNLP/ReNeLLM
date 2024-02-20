import csv, json, re

# read the harmful behaviors dataset
def data_reader(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        goals = []
        for row in reader:
            goal = row[0]
            goals.append(goal)
    return goals

# read the jailbroken data generated by ReNeLLM
def jailbroken_data_reader(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)
    return data

# preprocess the shorten sentences candidates generated by gpt-3.5-turbo
def remove_number_prefix(sentence):
    return re.sub(r'^\d+\.\s*', '', sentence)