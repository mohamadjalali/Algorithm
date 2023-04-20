
def rotate(s, r):
    double_s = s + s

    if r <= len(s):
        return double_s[r:len(s)]


print(rotate("HassanHassan", 2))
