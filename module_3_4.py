def single_root_words(root_word, *other_words):
    same_words=[]
    for s in other_words:
        if root_word.lower() in s.lower():
            same_words.append(s)
    if len(same_words) == 0:
        for s in other_words:
            if s.lower() in root_word.lower():
                same_words.append(s)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)