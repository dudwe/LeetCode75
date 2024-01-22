"""
394. Decode String
https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

3[a2[c]]

Put 3,[] on stack
Pop and put 3,[a] on stack
put 2,[] on stack
pop and put 2,[c] on stack
detect ] so pop stack and process -> [2,c] -> cc , append to current top in stack  [3,acc]
detect ] so pop stack and process -> >accaccacc

2[abc]3[cd]ef

[2,abc ] -> abcabc append ot result as stack is empyu
[3,cd] -> cdcd append to result as stack is empty -> abcabccdcd
ef

Algo:
stack = []
ptr = 0

while ptr < len(s):
    if s[ptr] is digit:
        move ptr until we encounter a "["
        extract the number
        stack.append([number,""])
        ptr+=1
    elif stack is alpha:
        if not stack
            result.append(s[ptr])
        else:
            stack[-1][-1].append(s[ptr])
    else:
        #We hit a  ]
        tup = stack.pop()
        process = ''.join(tup[0] * [tup[1]])
        if not stack:
            result.append(process)
        else:
            stack[-1][-1].append(process)

O(maxK *n) time complexity where maxk is max val of k and n is the length of a string. Ie length of the list * max digit
O(m+n) space complexity m is number letters n is number of digits
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ptr = 0
        result = ""
        while ptr < len(s):
            if s[ptr].isdigit():
                char = ""
                while s[ptr].isdigit():
                    char += s[ptr]
                    ptr += 1
                print(char)
                stack.append([int(char), ""])
                ptr+=1 #Skip the [

            elif s[ptr].isalpha():
                if not stack:
                    result += s[ptr]
                else:
                    stack[-1][-1] += s[ptr]
                ptr += 1
            else:
                #Pop the stack
                tup = stack.pop()
                substr = ''.join(tup[0] * [tup[1]])
                if not stack:
                    result += substr
                else:
                    stack[-1][-1] += substr
                ptr += 1
        return result


