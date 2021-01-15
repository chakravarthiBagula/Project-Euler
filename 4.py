"""  Project Euler #4: Largest palindrome product """


class Palindrome():
    def __init__(self):
        self.palindromes = []
        self.makePalindromes()

    def isPalindrome(self, num):
        num = str(num)
        return num == num[::-1]

    def makePalindromes(self):
        for i in range(100, 1000):
            for j in range(i, 1000):
                p = i * j
                if self.isPalindrome(p):
                    self.palindromes.append(p)
        self.palindromes.sort()


class Problem():
    def __init__(self):
        self.palindrome = Palindrome()
        self.palindrome.makePalindromes()

    def solve(self, limit):
        for i, ele in enumerate(self.palindrome.palindromes):
            if ele >= limit:
                return self.palindrome.palindromes[i-1]


p = Problem()

t = int(input())
while t > 0:
    n = int(input())
    print(p.solve(n))
    t -= 1
