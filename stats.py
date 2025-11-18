def get_num_words(str):
    return len(str.split())


def get_char_counts(str):
    char_dict = {}
    for c in str.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_char_dict(char_dict):
    dict_list = []
    for entry in char_dict:
        dict_list.append({"char": entry, "num": char_dict.get(entry)})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
