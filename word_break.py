def has_prefix(words, prefix):
    for i in range(len(words)):
        if words[i].startswith(prefix):
            return True
    return False

def solve(words, sentence, string="", index=0, ans=""):
    if index == len(sentence):
        print(ans+" "+string)
        return

    if string in words:
        solve(words, sentence, sentence[index], index+1, ans+" "+string)
    if has_prefix(words, string):
        solve(words, sentence, string+sentence[index], index+1, ans)
      

arr = "i, like, sam, sung, samsung, mobile, ice, cream, and, icecream, man, go, mango".split(", ")
#sentence = "ilikesamsungmobile"
sentence = "ilikeicecreamandmango"
solve(arr, sentence)
