class env:

    def __init__(self,envmap):
        self.envmap = envmap
        self.table = []
        self.start = [0,0]
        self.end = [0,0]

        f = open(self.envmap,'r')
        temp = []
        for line in f.readlines():
            self.table.append(list(line.strip()))
        f.close()

        #find ysize
        self.ysize = len(self.table)

        #find xsize
        self.xsize = 0
        for row in self.table:
            l = len(row)
            if self.xsize < l: self.xsize = l

        #pad level to a rectangle
        i=0
        for row in self.table:
            l = len(row)
            self.table[i]+=list('#'*(self.xsize-l))
            i+=1

        self.findstartend()
        #print(self.start,self.end)

    def findstartend(self):
        x,y=0,0
        for row in self.table:
            x=0
            for cell in row:
                if cell == 'S': self.start = [x,y]
                if cell == 'E': self.end = [x,y]
                x+=1
            y+=1

    def getStates(self):
        return [[x,y] for x in range(0,self.xsize) for y in range(0,self.ysize)]

    def act(self,s,a):

        snew = s.copy()
        reward = 0
        # movement of [x,y]
        if a == 0:
            snew[1] -= 1
        elif a == 1:
            snew[0] += 1
        elif a == 2:
            snew[1] += 1
        elif a == 3:
            snew[0] -= 1
        elif a == 4:
            snew[1] -= 1
            snew[0] += 1
        elif a == 5:
            snew[0] += 1
            snew[1] += 1
        elif a == 6:
            snew[1] += 1
            snew[0] -= 1
        elif a == 7:
            snew[0] -= 1
            snew[1] -= 1


        # vertical borders
        if snew[0] < 0:
            snew[0] = 0
        elif snew[0] > self.xsize-1:
            snew[0] = self.xsize-1

        # horizontal borders
        if snew[1] < 0:
            snew[1] = 0
        elif snew[1] > self.ysize-1:
            snew[1] = self.ysize-1

        symbnew = self.table[snew[1]][snew[0]]

        if symbnew == 'V': #light wind
            snew[1]+=1
        elif symbnew == 'W': #heavy wind
            snew[1]+=2

        # vertical borders
        if snew[0] < 0:
            snew[0] = 0
        elif snew[0] > self.xsize-1:
            snew[0] = self.xsize-1

        # horizontal borders
        if snew[1] < 0:
            snew[1] = 0
        elif snew[1] > self.ysize-1:
            snew[1] = self.ysize-1

        symbnew = self.table[snew[1]][snew[0]]

        if symbnew == '#': # wall
            snew = s
            reward = -1
        elif symbnew == 'E': #endpoint
            reward = 10
        elif symbnew == '|': # cliff
            reward = -100
            snew = self.start.copy()
        else:
            reward = -1
        # print(s,a)
        # print(reward,snew)
        # input()
        return reward,snew
