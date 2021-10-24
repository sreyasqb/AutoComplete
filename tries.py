

class Node:
    def __init__(self,letter):
        self.letter=letter
        self.letterCount=1
        self.child=26*[None]

    def update(self):
        self.letterCount+=1

    def __str__(self):
        return f'letter : {self.letter} lettercount : {self.letterCount} child : {self.child}'

    def findPosition(self,letter):
        return ord(letter)-97

    def insert(self,word):
        if word=='':
            return
        i=word[0]
        index=ord(i)-97

        if self.child[index] == None:

            self.child[index]=Node(i)
            self.child[index].insert(word[1:])

        else:

            self.child[index].update()
            self.child[index].insert(word[1:])

# class Tries:
#     def __init__(self):
#         self.child = []



autocomplete=Node('*')
autocomplete.insert("hi")
autocomplete.insert("he")
autocomplete.insert("hippo")
print(autocomplete.child[7].findPosition('i'))

# print(autocomplete.child[0])




