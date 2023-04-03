"""
                                        intents.json automatic editor
    by read all the files in project and convert the patterns and responses to array in json.
    files must be started with
    patterns_ if info contain patterns of intents,
    responses_ if info contain responses of intents.
    order than that you have to modify code that have "patterns_" or "responses_" to your type of intents but trust me
    what is already working don't touch it.
"""
import os
import json

current_dir = os.getcwd()
files = os.listdir(current_dir)
list_of_files = list(files)

try:    # in case intents files doesn't exist
    with open('intents.json', 'x') as f:
        intents = {"intents": []}
        json.dump(intents, f, indent=4)
except FileExistsError:
    with open('intents.json', 'rt') as f:
        intents = json.load(f)


def list_strip(filenames):
    my_list = []
    with open(filenames, 'r') as fe:
        for line in fe:
            my_list.append(line.strip())
    return my_list


def patterns(filenames, tag_files):
    pattern = list_strip(filenames)
    print(pattern)
    for intent in intents['intents']:
        if intent['tag'] == tag_files:
            # Intent already exists, add patterns to it
            pattern_alr = intent['patterns']
            pattern = pattern_alr + pattern
            intent['patterns'] = list(set(pattern))
            print(intent['patterns'])
            return
    # Intent doesn't exist, so create it and add patterns to it
    new_intent = {"tag": tag_files, "patterns": pattern, "responses": []}
    intents['intents'].append(new_intent)


def responses(filenames, tag_files):
    response = list_strip(filenames)
    print(response)
    for intent in intents['intents']:
        if intent['tag'] == tag_files:
            # Intent already exists, add patterns to it
            response_alr = intent['responses']
            response = response_alr + response
            intent['responses'] = list(set(response))
            print(intent['responses'])
            return
    # Intent doesn't exist, so create it and add patterns to it
    new_intent = {"tag": tag_files, "patterns": [], "responses": response}
    intents['intents'].append(new_intent)


# remove type out of files
first_list = [string.replace("responses_", "") for string in list_of_files]
new_list = [string.replace("patterns_", "") for string in first_list]
tags = set()  # tags
for file in new_list:
    if '.txt' in file:
        tag = file.split('.')
        tag.pop()
        tag = str(tag[0])
        tags.add(tag)

for files in list_of_files:  # sort patterns and responses
    if 'patterns' in files:
        tag1 = files.replace("patterns_", "")
        get_tag = tag1.replace(".txt", "")
        patterns(files, get_tag)
    elif 'responses' in files:
        tag1 = files.replace("responses_", "")
        get_tag = tag1.replace(".txt", "")
        responses(files, get_tag)
    else:
        pass

with open("intents.json", "w") as f:
    json.dump(intents, f, indent=4)
