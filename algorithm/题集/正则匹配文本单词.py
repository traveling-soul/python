from collections import Counter

c = Counter()
with open('1.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        # 空格分割
        words = line.split()
        c1 = Counter(words)
        c.update(c1)

top_10 = c.most_common(10)
print(top_10)
