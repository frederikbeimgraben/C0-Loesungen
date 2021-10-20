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
        return None, 1

def rev(a):
    b = a.copy()
    b.reverse()
    return b

def make_defs(substrings):
    defs_a = []
    i = 0
    for s in substrings:
        defs_a.append([s, i, s, []])
        i += 1
        for x in rev(defs_a[:defs_a[-1][1]]):
            while defs_a[-1][2].find(x[0]) >= 0:
                pos = s.find(x[0])
                s = s.replace(x[0], len(x[0]) * "#", 1)
                defs_a[-1][3].append([x[1], pos])
                defs_a[-1][2] = defs_a[-1][2].replace(x[0], "%s", 1)
        defs_a[-1][3] = [
            e[0] for e in sorted(defs_a[-1][3], key=lambda x: x[1])
        ]
    return defs_a

def bake_def(d, f=True):
    out = d[2]
    fnc = 'format' if f else 'printf'
    out = f'{fnc}("{out}"' if len(d[-1]) > 0 else f'"{out}"'
    for r in d[-1]:
        out += f",{chr(97+r)}"
    out += ')' if len(d[-1]) > 0 else ''
    return f's {chr(97+d[1])}={out};' if f else f'{out};'

def bake_defs(ds):
    out = ""
    for d in ds[:-1]:
        out += bake_def(d)
    out += bake_def(ds[-1], False)
    return out

def main_bake(substrings, string):
    defs_a = make_defs(substrings)
    # print(defs_a)
    string = bake_defs(defs_a)
    return string

string_global = open("rick.txt", "r").read().replace("\n", "\\n")

lrs = []

str_tmp = string_global

minocc = 2
while True:
    s, _ = longestRepetitiveSubstring(str_tmp, minocc)
    lrss, _ = longestRepetitiveSubstring(s, 2)
    #print("   --->   ", lrss)
    #print("          ", len(s), len(lrss))
    if len(lrss) > len(s) / 4:
        s, _ = longestRepetitiveSubstring(s, 2)
    o = str_tmp.count(s)
    l = len(s)
    if minocc == 3 and l * o < 7 + 4 * o + l:
        break
    elif  l * o < 7 + 4 * o + l:
        minocc += 1

    l1 = len(main_bake(rev([string_global] + lrs + [s]), string_global))
    l2 = len(main_bake(rev([string_global] + lrs), string_global))

    if l1 < l2:
        #print(s)
        lrs.append(s)
        str_tmp = str_tmp.replace(s, "")

lrs.reverse()

res = f"""
#use <conio> 
#use <string>
typedef string s;int main(){'{'}{main_bake([string_global] + lrs, string_global)}return 0;{'}'}
"""

print(res)
print(len(res))