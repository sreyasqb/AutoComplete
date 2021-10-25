class AutoCompleteTrie:
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

            self.child[index]=AutoCompleteTrie(i)
            self.child[index].insert(word[1:])

        else:

            self.child[index].update()
            self.child[index].insert(word[1:])

    def mostFreq(self):
        mostFreqNode=0
        max=0
        # print(self.child[4].letterCount)
        for i in range(26):
            if self.child[i]!=None and self.child[i].letterCount>max:
                mostFreqNode=self.child[i]
                max=self.child[i].letterCount
        return mostFreqNode

    def searchWord(self,word):
        if word=="":
            return self
        searchLetter=word[0]
        currentNode=self.child[self.findPosition(searchLetter)]
        if currentNode!=None:
            return currentNode.searchWord(word[1:])
        return None



    def suggestion(self,word):
        completeWord=word
        startNode=self.searchWord(word)
        # print(startNode)
        if startNode!=None:
            mostFreqNode = startNode.mostFreq()

            while mostFreqNode!=0:


                completeWord+=mostFreqNode.letter


                mostFreqNode=mostFreqNode.mostFreq()


            return completeWord



autocomplete=AutoCompleteTrie('*')
autocomplete.insert("hi")
autocomplete.insert("hive")
autocomplete.insert("hippo")
autocomplete.insert("hiv")
autocomplete.insert("apple")
autocomplete.insert("ball")

autocomplete.insert("tejas")

print(autocomplete.suggestion('h'))

# print(autocomplete.child[0])




