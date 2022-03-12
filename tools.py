import json


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def len_list(filename):
    with open(filename, encoding='utf-8') as f:
        return len(json.load(f))


def get_posts(data, word):
    result = []
    word_2 = f"{word}"
    for record in data:
        if word_2.casefold() in record["content"].casefold():
            result.append(record)
    return result