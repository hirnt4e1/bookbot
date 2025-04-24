def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_character_count(text):
    character_dict = {}
    for character in text.lower():
        if character not in character_dict.keys():
            character_dict[character] = 0
        character_dict[character] += 1
    return character_dict

def get_value_num(dict):
    return dict["num"]

def get_character_sorted(character_dict):
    new_dict_list = []
    for key in character_dict.keys():
        new_dict_list.append({"char" : key, "num" : character_dict[key]})
    new_dict_list.sort(key=get_value_num, reverse=True)
    return new_dict_list