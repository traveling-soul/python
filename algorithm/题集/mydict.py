# import re
#
#
# def find_string(string, pat):
#     res = re.findall(pat, string)
#     return res
#
#
# print(find_string('hello\nworld\n','wor'))
# print(find_string('hello\nworld\n','l*d'))
# print(find_string('hello\nworld\n','o.'))

class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value