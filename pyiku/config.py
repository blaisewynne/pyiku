class Pyiku:
    def count_syllables(word: str):
        word_length = len(word) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


        count = 0
        word = word.lower()

        for index, letter in enumerate(word):
            if letter == 'e':
                if index == word_length:
                    break
                if word[index-1] in consonants:
                    count += 1
                    break
                if word[index+1] == 'e':
                    break
                else:
                    count += 1
            elif letter == 'o':
                if word[index+1] in consonants:
                    count += 1
            elif letter in vowels:
                count += 1
        if count == 0:
            count += 1
        return count

    def is_haiku(haiku: str):
        haiku = haiku.lower()
        total_syllables = []
        for sentence in haiku.split(' '):
            print(sentence)
            syllables = Pyiku.count_syllables(sentence)
            print(syllables)
            total_syllables.append(syllables)
        print(total_syllables)
        print(sum(total_syllables))
            


Pyiku.is_haiku('Light of a candle, Morning glories in the breeze, A new day begins')
#Pyiku.is_haiku('Morning glories in the breeze, A new day begins')
#Pyiku.is_haiku('absolute')
#Pyiku.count_syllables('morning')
#Pyiku.count_syllables('glories')
#Pyiku.count_syllables('breeze')
#Pyiku.is_haiku('should')
