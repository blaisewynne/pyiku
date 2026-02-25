class Pyiku:
    def count_syllables(word: str):
        word_length = len(word) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        count = 0
        word = word.lower()

        for index, letter in enumerate(word):
            if letter in vowels:
                if word[index+1] in vowels:
                    count += 1
                elif word[index-1] in consonants:
                    count += 1

            if index == word_length and letter == 'e':
                break
        
        if count == 0:
            count += 1

    def is_haiku(haiku: str):
        haiku = haiku.lower()
        total_syllables = []
        for lines in haiku.split(','):
            for sentence in lines.split(' '):
                syllables = Pyiku.count_syllables(sentence)
                total_syllables.append(syllables)
        if sum(total_syllables) == 17:
            return True
        else:
            return False
            

Pyiku.count_syllables('supercalifragilisticexpialidocious')
Pyiku.count_syllables('coin')
Pyiku.count_syllables('button')