
st = "how do you do today and how did you do yesterday"

words = st.split(" ")

for w in set(words):
    print(f"{w}  - {words.count(w)}")


