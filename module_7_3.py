class WordsFinder:
    def __init__(self, *strings):
        self.file_names = []
        for s in strings:
            self.file_names.append(s)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            key = file
            string = ""
            symbs = [',', '.', '=', '!', '?', ';', ':', ' - ']
            with open(file, encoding='utf-8') as f:
                for line in f:
                    string += line.strip('\n').lower()
                for s in symbs:
                    if s in string:
                        string = string.replace(s, ' ')
                all_words[key] = string.split()
        return all_words



    def find(self, word):
        new_word = word.lower()
        find_positions = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if new_word in words:
                find_positions[name] = words.index(new_word) + 1
        return find_positions



    def count(self, word):
        new_word = word.lower()
        find_count = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            find_count[name] = words.count(new_word)
        return find_count



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))