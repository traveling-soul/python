import re

# s1 = 'cbccbcpower@power3g3g'
# s2 = 'appleapple56tototowidth'
#
# p = re.compile(r'(\w+)\1+')
#
# print(p.findall(s1))
# print(p.findall(s2))

word_dict = dict()
s = '''python is a magical language.
    python is simple to learn.
    python is 27-year-old.When I began to learn python, I was 18 years old.
    '''
# word_match = re.findall(r'\b(\w+)\b', s)
# for word in word_match:
#     # count = 0
#     # word_dict[word] = word_dict.get(word, 0) + count
#     # if word in word_dict:
#     #     count += 1
#     #     word_dict[word] = word_dict.get(word) + count
#
#     word_dict[word] = word_dict.get(word, 0) + 1
#
# # 从大到小排序
# result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:3]
# for each in result:
#     print(each)

word_count = {'1': 10,'4': 5, '7': 8, '9': 2}
result = sorted(word_count.items(), key=lambda d: d[1])
for each in result:
    print(each)


