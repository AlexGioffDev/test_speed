text = '''The Mole had been working very hard all the morning, spring-cleaning his little home. First with brooms, then with dusters; then on ladders and steps and chairs, with a brush and a pail of whitewash; till he had dust in his throat and eyes, and splashes of whitewash all over his black fur, and an aching back and weary arms. Spring was moving in the air above and in the earth below and around him, penetrating even his dark and lowly little house with its spirit of divine discontent and longing. It was small wonder, then, that he suddenly flung down his brush on the floor, said ‘Bother!' and ‘O blow!' and also ‘Hang spring-cleaning!' and bolted out of the house without even waiting to put on his coat. Something up above was calling him imperiously, and he made for the steep little tunnel which answered in his case to the gravelled carriage-drive owned by animals whose residences are nearer to the sun and air. So he scraped and scratched and scrabbled and scrooged and then he scrooged again and scrabbled and scratched and scraped, working busily with his little paws and muttering to himself, ‘Up we go! Up we go!' till at last, pop! his snout came out into the sunlight, and he found himself rolling in the warm grass of a great meadow. ('The Wind in the Willows' by Kenneth Grahame)'''

text = text.replace('.', '').replace(',', '').replace(';', '').replace(':', '')
class Dictionary():
    def __init__(self):
        self.dictionary = text.split(' ')
        self.idx = 0
        self.word_active = self.dictionary[self.idx]
        self.word_guess = 0
        self.end = False

    def print_words(self):
        for word in self.dictionary:
            print(word, end=', ')
        print("\n")

    def check_word(self, word_user):
        if self.word_active == word_user:
            self.word_guess += 1
        try:
            self.idx += 1
            self.word_active = self.dictionary[self.idx]
        except IndexError:
            self.end = True
    
    def create_text(self):
        return ' '.join(self.dictionary)
        
    def reset(self):
        self.word_guess = 0
        self.idx = 0
        self.end = False
        self.word_active = self.dictionary[self.idx]
