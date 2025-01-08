# Char Freq
st = "this is to test"

for c in sorted(set(st)):
     print(f"{c} - {st.count(c)}")


