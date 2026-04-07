class Robot(object):

    def __init__(self, width, height):
        self.w, self.h = width, height
        self.p = 2 * (width - 1) + 2 * (height - 1)
        self.curr = 0
        self.moved = False
        """
        :type width: int
        :type height: int
        """
        

    def step(self, num):
        self.moved = True
        self.curr = (self.curr + num) % self.p
        """
        :type num: int
        :rtype: None
        """
        

    def getPos(self):
        idx, w, h = self.curr, self.w, self.h
        if idx < w: return [idx, 0]
        if idx < w + h - 1: return [w - 1, idx - (w - 1)]
        if idx < 2 * w + h - 2: return [w - 1 - (idx - (w + h - 2)), h - 1]
        return [0, h - 1 - (idx - (2 * w + h - 3))]
        """
        :rtype: List[int]
        """
        

    def getDir(self):
        idx, w, h = self.curr, self.w, self.h
        if not self.moved or idx == 0: return "South" if self.moved else "East"
        if 1 <= idx <= w - 1: return "East"
        if w <= idx <= w + h - 2: return "North"
        if w + h - 1 <= idx <= 2 * w + h - 3: return "West"
        return "South"
        """
        :rtype: str
        """
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()