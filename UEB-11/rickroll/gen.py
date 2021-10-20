from collections import defaultdict

def getsubs(loc, s):
    substr = s[loc:]
    i = -1
    while(substr):
        yield substr
        substr = s[loc:i]
        i -= 1

def longestRepetitiveSubstring(r, minocc=3):
    occ = defaultdict(int)
    # tally all occurrences of all substrings
    for i in range(len(r)):
        for sub in getsubs(i,r):
            occ[sub] += 1

    # filter out all substrings with fewer than minocc occurrences
    occ_minocc = [k for k,v in occ.items() if v >= minocc]

    if occ_minocc:
        maxkey =  max(occ_minocc, key=len)
        return maxkey, occ[maxkey]
    else:
        return (None,0)

def compress(string):
    compressed = []
    length = len(string)
    for l in range(length/2, 0):
        for i in range(0, length - l - 1):
            sub = string[i:i+l]
            c = 1
            j = i + l
            while (j < length - l):
                if sub == string[j:j+l]:
                    c += 1
                else:
                    break
                j += l
            
            if c > 1:
                if i > 0:
                    compressed.append(compress(string[0:i]))
    pass

def shorter(s, o):
    return len(s) * o > len(s) + 7 + 4 * o

def get_all(string, substrings=[]):
    strw = string
    while True:
        substring_raw = longestRepetitiveSubstring(strw, 3)
        substring = substring_raw[0]
        occ = substring_raw[1]
        if substring != None and len(substring) > 10:
            if shorter(substring, occ): 
                if substring not in substrings: substrings.append(substring.replace("\n", "\\n"))
                substrings = get_all(substring)
                strw = strw.replace(substring, "")
                print(substring)
        else:
            break
    return substrings

def parse(string, invert=False):
    lst = string.split("|")
    if invert:
        lst.reverse()
    args = ""
    out = ""
    if len(lst[0]) > 0 and lst[0][0] == '~':
        out += "%s"
        n = lst[0].replace("~", "")
        args += f',{chr(97+int(n))}'
    else:
        out += lst[0]
    for e in lst[1:]:
        if len(e) > 0 and e[0] == '~':
            out += "%s"
            n = e.replace("~", "")
            args += f',{chr(97+int(n))}'
        else:
            out += e
    return f'format("{out}"{args})'

def make_definition(i, a):
    for e in a:
        a[i][1] = a[i][1].replace(e[0],)

f = open("rick.txt", "r")
s = f.read();
# print([s])
a = get_all(s)


print(get_all(s))