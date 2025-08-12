def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(text):
    text_all_lowercase = text.lower()
    character_count = {}
    for uniqe_letter in text_all_lowercase:
        if uniqe_letter not in character_count:
            character_count[uniqe_letter] = 1
        else:
            character_count[uniqe_letter] += 1
    return character_count
            
def sort_on(items):
    return items["num"]

def sorted_char_counts(char_counts):
    filtered = [{"char": ch, "num": count}
                for ch, count in char_counts.items()
                if ch.isalpha()]
    filtered.sort(key=sort_on, reverse=True)

    return filtered        