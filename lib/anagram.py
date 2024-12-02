# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if ''.join(sorted(candidate)) == self.sorted_word:
                matches.append(candidate)
        return matches


    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))