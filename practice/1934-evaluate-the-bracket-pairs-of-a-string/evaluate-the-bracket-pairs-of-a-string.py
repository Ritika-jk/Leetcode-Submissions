class Solution(object):
    def evaluate(self, s, knowledge):
        m = {k: v for k, v in knowledge}
        words = re.split(r'[()]', s)

        out = []
        for i, w in enumerate(words):
            out.append(w if i % 2 == 0 else m.get(w, "?"))

        return "".join(out)
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        