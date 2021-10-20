string_global = open("rick.txt", "r").read().replace("\n", "\\n")

substrings = [
    "\\nNever gonna ",
    "give, never gonna give\\n(G",
    "ive you up)\\n",
    "\\nI just wanna tell you how I'm feeling\\nGotta make you understand\\n",
    "\\nWe've known each other for so long\\nYour heart's been aching but\\nYou're too shy to say it\\nInside we both know what's been going on\\nWe know the game and we're gonna play it\\n",
    "\\nNever gonna give you up\\nNever gonna let you down\\nNever gonna run around and desert you\\nNever gonna make you cry\\nNever gonna say goodbye\\nNever gonna tell a lie and hurt you\\n",
]

substrings.append(string_global)

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

def main():
    mn = 10000;
    bs = "";
    print("Starting...")
    # subs = substrings
    mn, bs = main_bake(substrings, string_global)
    print("\r" + str(mn + 66) + " ")
    w = open("output_tmp_r.c0", "w")
    base = \
f"""
#use <conio> 
#use <string>
typedef string s;int main(){'{'}{bs}return 0;{'}'}
"""
    print(base)
    w.write(base[1:-1])

if __name__ == "__main__":
    main()