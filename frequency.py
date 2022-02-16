#!/usr/bin/env python

import sys
import re

freq = {}
unique_words = set()
for line in sys.stdin:
        line = line.lower()
        split_all = re.findall(r"[\w']+|[.,!?;]",line)
        unique_words.update(split_all)
      
        for word in unique_words:
                count = line.count(word)

                if word in freq.keys():
                        freq[word] = freq[word] + count
                else:
                #print(word, count)
                        freq.update({word:count})
for w, c in sorted(freq.items(), key=lambda item: item[1], reverse=True):
        print(w," appears ",c," times in the text.")
