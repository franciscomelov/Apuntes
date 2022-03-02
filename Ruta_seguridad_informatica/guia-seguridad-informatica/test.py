s = "abcd"

sub = ""

for i, i_leter in enumerate(s):
    print("_________")

    for j,j_letter in enumerate(s[i:]):
        sub += j_letter
        print(sub)
    sub = ""
