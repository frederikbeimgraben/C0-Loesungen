import builtins
from re import sub

def longestRepeatedSubstring(str):
 
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + str[i - 1]
 
    return res

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
    return len(string), string

import random
import sys

def get_random_str(main_str, substr_len):
    idx = random.randrange(0, len(main_str) - substr_len + 1)    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
    return main_str[idx : (idx+substr_len)]

string_global = open("rick.txt", "r").read().replace("\n", "\\n")

def substr(string, a, b=-1):
    return string[a:a+b] if b != -1 else string[a:]

def find_intersection(a, b, mlen=3):
    # b-end <-> a-start
    for i in range(mlen, min(len(a), len(b))):
        k = 0
        while (a[len(a)-(i-k)] == b[k]):
            if k >= 3: return i
            k += 1
    for i in range(mlen, min(len(a), len(b))):
        k = 0
        while (b[len(b)-(i-k)] == a[k]):
            if k >= 3: return -i
            k += 1
    return 0

def clean(a, b):
    i = find_intersection(a, b)
    r = b[i:] if i >= 0 else b[:i]
    # print([a, b], " -> ", [r], i)
    return r

substrings = [
    "ive you up)\\n",
    "\\nI just wanna tell you how I'm feeling\\nGotta make you understand\\n",
    "\\nWe've known each other for so long\\nYour heart's been aching but\\nYou're too shy to say it\\nInside we both know what's been going on\\nWe know the game and we're gonna play it\\n",
    "\\nNever gonna give you up\\nNever gonna let you down\\nNever gonna run around and desert you\\nNever gonna make you cry\\nNever gonna say goodbye\\nNever gonna tell a lie and hurt you\\n",
]

def remove_duplicates(x):
  return list(dict.fromkeys(x))

string_div = string_global

substrings.reverse()

for e in substrings:
    string_div = string_div.replace(e, "|")

substrings += string_div.split("|")

substrings = remove_duplicates(substrings)

substrings.remove("")

o = "#use <conio>\ntypedef string s;void p(s t){print(t);}int main(){"

i = 0
for e in substrings:
    o += f"s {chr(97+i)}=\"{e}\";"
    i += 1

p = string_global

i = 0
for e in substrings:
    p = p.replace(e, f"{chr(97+i)}")
    i += 1

o += p
o += "return 0;}"

print(o)

print(len(o))

print(sum([len(el)+13 for el in substrings]))

exit()

def main():
    mn = 10000;
    bs = "";
    print("Starting...")
    substrings_tmp.append(string_global)
    # subs = substrings
    mn, bs = main_bake(substrings, string_global)
    sys.stdout.write("\r" + str(mn + 66) + " ")
    sys.stdout.flush()
    w = open("output_tmp.c0", "w")
    base = \
f"""
#use <conio>
typedef string s;void p(s t){'{'}print(t);{'}'}int main(){'{'}{bs}return 0;{'}'}
"""
    print(base)
    w.write(base[1:-1])

if __name__ == "__main__":
    main()