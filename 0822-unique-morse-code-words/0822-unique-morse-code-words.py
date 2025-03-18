class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        s = set()
        for w in words:
            t = ""
            for j in range(len(w)):
                t += d[w[j]]
            s.add(t)
        return len(s)