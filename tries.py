class AutoCompleteTrie:
    def __init__(self, letter):
        self.letter = letter
        self.letterCount = 1
        self.child = 26 * [None]

    def update(self):
        self.letterCount += 1

    def __str__(self):
        return f'letter : {self.letter} lettercount : {self.letterCount} child : {self.child}'

    def findPosition(self, letter):
        return ord(letter) - 97

    def levelOrder(self, root,word,n):



        def traverse(root, level,word,n):
            if not root:
                return
            if len(ret)==n:
                return
                # while len(ret) <= level:
            #     ret.append([])
            target_word=word+root.leftMost()
            if target_word not in ret:
                ret.append(target_word)

            for child in root.child:
                temp=""
                if child!=None:
                    temp=child.letter
                traverse(child, level + 1,word+temp,n)

        ret = []
        traverse(root, 0,word,n)
        return ret

    def insert(self, word):
        if word == '':
            return
        i = word[0]
        index = ord(i) - 97

        if self.child[index] == None:

            self.child[index] = AutoCompleteTrie(i)
            self.child[index].insert(word[1:])

        else:

            self.child[index].update()
            self.child[index].insert(word[1:])

    def mostFreq(self):  # gives most frequent node
        mostFreqNode = 0
        max = 0

        for i in range(26):
            if self.child[i] != None and self.child[i].letterCount > max:
                mostFreqNode = self.child[i]
                max = self.child[i].letterCount
        return mostFreqNode

    def searchWord(self, word):
        if word == "":
            return self
        searchLetter = word[0]
        currentNode = self.child[self.findPosition(searchLetter)]
        if currentNode != None:
            return currentNode.searchWord(word[1:])
        return None

    def suggestion(self, word):
        completeWord = word
        startNode = self.searchWord(word)
        # print(startNode)
        if startNode != None:
            mostFreqNode = startNode.mostFreq()

            while mostFreqNode != 0:
                completeWord += mostFreqNode.letter

                mostFreqNode = mostFreqNode.mostFreq()

            return completeWord

    def leftMost(self):

        l = list(self.child)
        l.sort(key=lambda x: x.letterCount if x != None else 0, reverse=True)

        if l[0] == None:
            return ""

        return l[0].letter + l[0].leftMost()

    def nSuggestions(self, word, n):
        # print(f"self is {self}")
        startNode = self.searchWord(word)
        # print(f"startnode: {startNode}")
        if startNode == None:
            return
        l = list(startNode.child)
        # print(startNode)

        l.sort(key=lambda x: x.letterCount if x != None else 0, reverse=True)
        # print(l)
        return startNode.levelOrder(startNode,word,n)

            # print(word+l[0].letter,l[0])
        # l[0].nSuggestions(word+l[0].letter,n-count)
        # print("hi")


# autocomplete = AutoCompleteTrie('*')
# autocomplete.insert("hi")
# autocomplete.insert("hive")
# autocomplete.insert("hippo")
#
# autocomplete.insert("hirda")
# autocomplete.insert("his")
# autocomplete.insert("hivem")
# autocomplete.insert("hill")
# autocomplete.insert("hives")
# autocomplete.insert("apple")
# autocomplete.insert("ball")
#
# autocomplete.insert("tejas")
# autocomplete.insert("arjuna")
# autocomplete.insert("arjena")
# autocomplete.insert("joy")

# autocomplete.child.sort(key=lambda x:x.letterCount if x!=None else 0 ,reverse=True)
# print(autocomplete.child[7].suggestion('i'))
# autocomplete.searchWord('hive').sort(key=lambda x: x.letterCount if x != None else 0, reverse=True)
# temp=autocomplete.searchWord('hi')
# temp.child.sort(key=lambda x: x.letterCount if x != None else 0, reverse=True)
# print(temp.child[0])
# print(autocomplete.suggestion('hi'))
# print(autocomplete.val)
# print(autocomplete.nSuggestions('h',9))
# print(autocomplete.levelOrder(autocomplete))

# print(autocomplete)