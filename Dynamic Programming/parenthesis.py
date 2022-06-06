'''
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
'''

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return []
    if n == 1:
        return ["()"]
    if n == 2:
        return ["()()", "(())"]
    else:
        res = []
        for i in range(n):
            for j in generateParenthesis(i):
                for k in generateParenthesis(n-i-1):
                    res.append("({}){}".format(j, k))
        return res

if __name__ == '__main__':
    print(generateParenthesis(3))
    print(generateParenthesis(4))

