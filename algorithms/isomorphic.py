"""
Determine whether a one-to-one character mapping
exists from one string, s1, to another string, s2. 
For example, given s1 = abc and s2 = bcd, print 'true' since
we are able to map each character in 'abc' to a character in 'bcd'.
And, in turn, given s1 = foo and s2 = bar, 
print 'false' since the character 'o' cannot map to two characters.
"""


def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    dict = {}
    set_values = set()
    
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values:
                return False
            dict[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
   
    return True



if __name__ == "__main__":
    # Must be return False
    print(is_isomorphic('bar', 'foo'))
    # Must be return True
    print(is_isomorphic('abc', 'bcd'))
    
