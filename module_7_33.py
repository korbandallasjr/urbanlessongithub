class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def find(self,word):
        new_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
               new_dict[name] = words.index(word.lower())+1
        return new_dict


    def count(self,word):
        new_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                new_dict[name] = words.count(word.lower())
        return new_dict

    def get_all_words(self):
        all_words = {}
        for value in self.file_names:
            with open(value, 'r+', encoding='utf-8') as file:
                lines = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', '-']:
                    lines =  lines.replace(sym, '')
                all_words[value] = lines.split()
        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


finder3 = WordsFinder('test1.txt', 'test2.txt', 'test3.txt')
print(finder3.__dir__())