from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []
        
        # We need to try offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] += 1
                    
                    # If we have more than needed, shrink from left
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                    
                    # If window size matches total_len, record answer
                    if right - left == total_len:
                        res.append(left)
                else:
                    # Reset window
                    curr_count.clear()
                    left = right
        
        return res
