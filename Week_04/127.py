class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        dict = collections.defaultdict(list)
        len_word = len(beginWord)
        for word in wordList:
            for i in range(len_word):
                dict[word[:i] + '*' + word[i+1:]].append(word)

        queue = []
        queue.append(beginWord)
        visited = {}
        visited[beginWord] = 1
        level = 1

        while len(queue) > 0:
            temp_words = []
            for i in range(len(queue)):
                current_word = queue.pop(0)
                for j in range(len_word):
                    current_word_key = current_word[:j] + '*' + current_word[j+1:]
                    if not visited.get(current_word_key):
                        visited[current_word_key] = 1
                        related_words = dict[current_word_key]
                        for related_word in related_words:
                            if related_word not in temp_words:
                                if not visited.get(related_word):
                                    if related_word == endWord:
                                        return level + 1
                                    visited[related_word] = 1
                                    queue.append(related_word)
                    
            level += 1   
        
        return 0       