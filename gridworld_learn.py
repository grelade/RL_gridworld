import numpy as np
import matplotlib.pyplot as plt
import pickle
import tkinter
import threading
import argparse
import conf

# environment function returning reward and state from state and action
# extended model
def envExt(s,a):
    snew = s.copy()
    wind = 0
    # wind part
    # no wind
    if snew[0] == 0 or snew[0] == 1 or snew[0] == 2 or snew[0] == 9: wind = 0
    # wind 1
    elif snew[0] == 3 or snew[0] == 4 or snew[0] == 5 or snew[0] == 8: wind = -1
    # wind 2
    elif snew[0] == 6 or snew[0] == 7: wind = -2
    snew[1] += wind

    # movement
    if a == 0:
        snew[1] -= 1
    elif a == 1:
        snew[0] += 1
    elif a == 2:
        snew[1] += 1
    elif a == 3:
        snew[0] -= 1
    # elif a == 4:
    #     snew[1] -= 1
    #     snew[0] += 1
    # elif a == 5:
    #     snew[0] += 1
    #     snew[1] += 1
    # elif a == 6:
    #     snew[1] += 1
    #     snew[0] -= 1
    # elif a == 7:
    #     snew[0] -= 1
    #     snew[1] -= 1

    # x borders
    if snew[0] < 0:
        snew[0] = 0
    elif snew[0] > (conf.xsize-1):
        snew[0] = (conf.xsize-1)

    # y borders
    if snew[1] < 0:
        snew[1] = 0
    elif snew[1] > 5*(conf.ysize-1):
        snew[1] = 5*(conf.ysize-1)

    if snew == stateend.copy(): reward = 10
    else: reward = -1

    return reward,snew


# environment function returning reward and state from state and action
# Kings movement + Windy + Gridworld
def envKW(s,a):
    snew = s.copy()

    # wind part
    # no wind
    if snew[0] == 0 or snew[0] == 1 or snew[0] == 2 or snew[0] == 9: wind = 0
    # wind 1
    elif snew[0] == 3 or snew[0] == 4 or snew[0] == 5 or snew[0] == 8: wind = -1
    # wind 2
    elif snew[0] == 6 or snew[0] == 7: wind = -2
    snew[1] += wind

    # movement
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

    # x borders
    if snew[0] < 0:
        snew[0] = 0
    elif snew[0] > conf.xsize-1:
        snew[0] = conf.xsize-1

    # y borders
    if snew[1] < 0:
        snew[1] = 0
    elif snew[1] > conf.ysize-1:
        snew[1] = conf.ysize-1

    if snew == stateend.copy(): reward = 10
    else: reward = -1

    return reward,snew

# environment function returning reward and state from state and action
# Windy + Gridworld
def envW(s,a):
    snew = s.copy()
    wind = 0
    # wind part
    # no wind
    if snew[0] == 0 or snew[0] == 1 or snew[0] == 2 or snew[0] == 9: wind = 0
    # wind 1
    elif snew[0] == 3 or snew[0] == 4 or snew[0] == 5 or snew[0] == 8: wind = -1
    # wind 2
    elif snew[0] == 6 or snew[0] == 7: wind = -2
    snew[1] += wind

    # movement
    if a == 0:
        snew[1] -= 1
    elif a == 1:
        snew[0] += 1
    elif a == 2:
        snew[1] += 1
    elif a == 3:
        snew[0] -= 1
    # elif a == 4:
    #     snew[1] -= 1
    #     snew[0] += 1
    # elif a == 5:
    #     snew[0] += 1
    #     snew[1] += 1
    # elif a == 6:
    #     snew[1] += 1
    #     snew[0] -= 1
    # elif a == 7:
    #     snew[0] -= 1
    #     snew[1] -= 1

    # x borders
    if snew[0] < 0:
        snew[0] = 0
    elif snew[0] > conf.xsize-1:
        snew[0] = conf.xsize-1

    # y borders
    if snew[1] < 0:
        snew[1] = 0
    elif snew[1] > conf.ysize-1:
        snew[1] = conf.ysize-1

    if snew == stateend.copy(): reward = 10
    else: reward = -1

    return reward,snew

# environment function returning reward and state from state and action
# Kings movement + Gridworld
def envK(s,a):
    snew = s.copy()

    # # wind part
    # # no wind
    # if snew[0] == 0 or snew[0] == 1 or snew[0] == 2 or snew[0] == 9: wind = 0
    # # wind 1
    # elif snew[0] == 3 or snew[0] == 4 or snew[0] == 5 or snew[0] == 8: wind = -1
    # # wind 2
    # elif snew[0] == 6 or snew[0] == 7: wind = -2
    # snew[1] += wind

    # movement
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

    # x borders
    if snew[0] < 0:
        snew[0] = 0
    elif snew[0] > conf.xsize-1:
        snew[0] = conf.xsize-1

    # y borders
    if snew[1] < 0:
        snew[1] = 0
    elif snew[1] > conf.ysize-1:
        snew[1] = conf.ysize-1

    if snew == stateend.copy(): reward = 10
    else: reward = -1

    return reward,snew

# environment function returning reward and state from state and action
# Gridworld
def env(s,a):
    snew = s.copy()

    # # wind part
    # # no wind
    # if snew[0] == 0 or snew[0] == 1 or snew[0] == 2 or snew[0] == 9: wind = 0
    # # wind 1
    # elif snew[0] == 3 or snew[0] == 4 or snew[0] == 5 or snew[0] == 8: wind = -1
    # # wind 2
    # elif snew[0] == 6 or snew[0] == 7: wind = -2
    # snew[1] += wind

    # movement
    if a == 0:
        snew[1] -= 1
    elif a == 1:
        snew[0] += 1
    elif a == 2:
        snew[1] += 1
    elif a == 3:
        snew[0] -= 1
    # elif a == 4:
    #     snew[1] -= 1
    #     snew[0] += 1
    # elif a == 5:
    #     snew[0] += 1
    #     snew[1] += 1
    # elif a == 6:
    #     snew[1] += 1
    #     snew[0] -= 1
    # elif a == 7:
    #     snew[0] -= 1
    #     snew[1] -= 1

    # x borders
    if snew[0] < 0:
        snew[0] = 0
    elif snew[0] > conf.xsize-1:
        snew[0] = conf.xsize-1

    # y borders
    if snew[1] < 0:
        snew[1] = 0
    elif snew[1] > conf.ysize-1:
        snew[1] = conf.ysize-1

    if snew == stateend.copy(): reward = 10
    else: reward = -1

    return reward,snew

# coding and decoding functions of state-action pair
def codeSA(state,action):
    return str(state[0])+"_"+str(state[1])+"_"+str(action)
def decodeSA(stateaction):
    split = stateaction.split("_")
    return [[int(split[0]),int(split[1])],int(split[-1])]

# coding and decoding function of states
def codeS(state):
    return str(state[0])+"_"+str(state[1])
def decodeS(statecoded):
    split = statecoded.split("_")
    return [int(split[0]),int(split[1])]

# find policy globally for Q-value function
def greedy(Q,epsilon):
    global actions

    policy = {}
    for state in states:
        Qpoint = [Q[codeSA(state,action)] for action in actions]
        maxaction_indices = np.argwhere(Qpoint == np.amax(Qpoint)).flatten().tolist()
        prob = [epsilon/len(Qpoint)  for action in actions]
        for i in maxaction_indices: prob[i] = prob[i] + (1-epsilon)/len(maxaction_indices)
        policy[codeS(state)] = prob
    return policy

# exploration parameter is held constant over training
def epsilonconst(n):
    return epsilon

# exploration parameter is modified during training
def epsilondrop(n):
    return epsilon/(n+1)

# alpha parameter is held constant over training
def alphaconst(n):
    return alpha

# alpha parameter is modified during training
def alphadrop(n):
    return alpha/(n+1)


# choose a move for a state according to policy
def choosemove(state,policy):
    statePolicy = policy[state]
    return np.random.choice(actions,p=statePolicy)

def savepolicy(policy):
    print('saving the policy')
    with open('policy.pkl', 'wb') as f: pickle.dump(policy, f, pickle.HIGHEST_PROTOCOL)

def savemeanlength(meanlengthlist):
    print('saving the meanlengthlist')
    with open('meanlength.pkl', 'wb') as f: pickle.dump(meanlengthlist, f, pickle.HIGHEST_PROTOCOL)

def savemeanR(meanRlist):
    print('saving the meanRlist')
    with open('meanR.pkl', 'wb') as f: pickle.dump(meanRlist, f, pickle.HIGHEST_PROTOCOL)

def savesuccess(successful_episodes):
    print('saving the successful_episodes')
    with open('efficacy.pkl', 'wb') as f: pickle.dump(successful_episodes, f, pickle.HIGHEST_PROTOCOL)

def sarsa():

    # init Q-value function
    Q = {}
    for stateaction in stateactions: Q[stateaction] = initQ

    # initial policy
    policy = greedy(Q,epsilonfunc(0))

    # efficiency measures
    successful_episodes = {}
    meanlengthlist = []
    meanRlist = []

    # init values
    meanlength = 0 # mean time within an
    episodetime = 0 # time within an episode
    Slist=[]
    totaltime = 0 # total simulation time

    # draw init policy
    app.drawpolicy(policy)

    for n in range(0,noepisodes):
        episodetime = 0
        sumR = 0
        S = statestart.copy()
        Slist.append(S)
        policy = greedy(Q,epsilonfunc(n)) # derive policy from Q
        A = choosemove(codeS(S),policy) # choose A from policy
        while not S == stateend:
            totaltime+=1
            episodetime += 1
            R,Sp = environment(S,A)
            sumR += R
            Slist.append(Sp.copy())
            policy = greedy(Q,epsilonfunc(n))
            Ap = choosemove(codeS(Sp),policy)
            Q[codeSA(S,A)] += alphafunc(n)*(R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)])
            S,A = Sp,Ap

        if S == stateend:
            Slist.append(S)
            successful_episodes[totaltime] = 1
            meanlength += episodetime
            app.clearCanvas()
            app.drawgrid()
            app.drawtrajectory(Slist)
            app.drawpolicy(policy)
            Slist=[]
            #print(sumR)
            meanRlist.append(sumR)
            #print('epsilon=',epsilonfunc(n))

        if n % conf.windowsize == 0:
            print(n,'mean path length',meanlength/conf.windowsize,'; mean reward',meanRlist[-1],'epsilon=',epsilonfunc(n),'alpha=',alphafunc(n))
            meanlengthlist.append(meanlength/conf.windowsize)
            meanlength = 0

    return policy,successful_episodes,meanlengthlist,meanRlist

# a.s. convergent SARSA variant
def sarsaconv():

    # init Q-value function
    Q = {}
    for stateaction in stateactions: Q[stateaction] = initQ

    # init N counting function
    N = {}
    for stateaction in stateactions: N[stateaction] = 0

    # init N-s counting function
    Ns = {}

    for state in states: Ns[codeS(state)] = 0

    # initial policy
    policy = greedy(Q,epsilonfunc(0))

    # efficiency measures
    successful_episodes = {}
    meanlengthlist = []
    meanRlist = []

    # init values
    meanlength = 0 # mean time within an
    episodetime = 0 # time within an episode
    Slist=[]
    totaltime = 0 # total simulation time

    # draw init policy
    app.drawpolicy(policy)

    for n in range(0,noepisodes):
        episodetime = 0
        sumR = 0
        S = statestart.copy()
        Slist.append(S)
        #policy = greedy(Q,epsilonfunc(n)) # derive policy from Q
        policy = greedy(Q,epsilon) # derive policy from Q
        A = choosemove(codeS(S),policy) # choose A from policy
        while not S == stateend:
            totaltime+=1
            episodetime += 1
            N[codeSA(S,A)]+=1
            Ns[codeS(S)]+=1
            R,Sp = environment(S,A)
            sumR += R
            Slist.append(Sp.copy())
            #policy = greedy(Q,epsilonfunc(n))
            policy = greedy(Q,epsilon/Ns[codeS(S)])
            Ap = choosemove(codeS(Sp),policy)
            #Q[codeSA(S,A)] += alphafunc(n)*(R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)])
            Q[codeSA(S,A)] += alpha/N[codeSA(S,A)]*(R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)])
            S,A = Sp,Ap

        if S == stateend:
            Slist.append(S)
            successful_episodes[totaltime] = 1
            meanlength += episodetime
            app.clearCanvas()
            app.drawgrid()
            app.drawtrajectory(Slist)
            app.drawpolicy(policy)
            Slist=[]
            #print(sumR)
            meanRlist.append(sumR)
            #print('epsilon=',epsilonfunc(n))

        if n % conf.windowsize == 0:
            print(n,'mean path length',meanlength/conf.windowsize,'; mean reward',meanRlist[-1],'epsilon=',epsilonfunc(n),'alpha=',alphafunc(n))
            meanlengthlist.append(meanlength/conf.windowsize)
            meanlength = 0

    return policy,successful_episodes,meanlengthlist,meanRlist

def sarsalambda():

    # init Q-value function
    Q = {}
    for stateaction in stateactions: Q[stateaction] = initQ

    # initial policy
    policy = greedy(Q,epsilonfunc(0))

    # init eligibility traces
    E = {}
    for stateaction in stateactions: E[stateaction] = 0

    # efficiency measures
    successful_episodes = {}
    meanlengthlist = []
    meanRlist = []

    # init values
    meanlength = 0 # mean time within an
    episodetime = 0 # time within an episode
    Slist=[]
    totaltime = 0 # total simulation time

    for n in range(0,noepisodes):
        sumR = 0
        episodetime = 0
        S = statestart.copy()
        Slist.append(S.copy())
        policy = greedy(Q,epsilonfunc(n)) # derive policy from Q
        A = choosemove(codeS(S),policy) # choose A from policy
        #if n % 100 == 0: print(n)

        while not S == stateend:
            totaltime+=1
            episodetime += 1
            R,Sp = environment(S,A)
            sumR += R
            Slist.append(Sp.copy())
            policy = greedy(Q,epsilonfunc(n))
            Ap = choosemove(codeS(Sp),policy)
            #print(Q[codeSA(S,A)])
            delta = R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)]
            #E[codeSA(S,A)] += 1 # accumulating traces
            E[codeSA(S,A)] += 1 - alphafunc(n)*E[codeSA(S,A)] # dutch traces
            #E[codeSA(S,A)] = 1 # replacing traces
            for s in states:
                for a in actions:
                    Q[codeSA(s,a)] += alphafunc(n)*delta*E[codeSA(s,a)]
                    E[codeSA(s,a)] *= gamma*lambda0
            #print(Q[codeSA(S,A)])
            S,A = Sp,Ap

        if S == stateend:
            successful_episodes[totaltime] = 1
            meanlength += episodetime
            app.clearCanvas()
            app.drawgrid()
            app.drawpolicy(policy)
            app.drawtrajectory(Slist)
            Slist=[]
            meanRlist.append(sumR)

        if n % conf.windowsize == 0:
            print(n,'mean trajectory timelength',meanlength/conf.windowsize,'; mean reward',meanRlist[-1])
            meanlengthlist.append(meanlength/conf.windowsize)
            meanlength = 0

    return policy,successful_episodes,meanlengthlist,meanRlist

def Qlearn():

    # init Q-value function
    Q = {}
    for stateaction in stateactions: Q[stateaction] = initQ

    # initial policy
    policy = greedy(Q,epsilonfunc(0))

    # init eligibility traces
    E = {}
    for stateaction in stateactions: E[stateaction] = 0

    # efficiency measures
    successful_episodes = {}
    meanlengthlist = []
    meanRlist = []

    # init values
    meanlength = 0 # mean time within an
    episodetime = 0 # time within an episode
    Slist=[]
    totaltime = 0 # total simulation time

    # draw init policy
    app.drawpolicy(policy)

    for n in range(0,noepisodes):
        #print(n)
        episodetime = 0
        sumR = 0
        S = statestart.copy()
        Slist.append(S)
        #if n % 100 == 0: print(n)

        while not S == stateend:

            totaltime+=1
            episodetime += 1
            policy = greedy(Q,epsilonfunc(n)) # derive policy from Q
            A = choosemove(codeS(S),policy) # choose A from policy
            R,Sp = environment(S,A)
            sumR += R
            Slist.append(Sp.copy())
            policy = greedy(Q,epsilonfunc(n))
            #Ap = choosemove(codeS(Sp),policy)
            #print(Q[codeSA(S,A)])
            Q[codeSA(S,A)] += alphafunc(n)*(R+ gamma*np.max([Q[codeSA(Sp,a)] for a in actions]) - Q[codeSA(S,A)])
            #print(Q[codeSA(S,A)])
            S = Sp

        if S == stateend:
            successful_episodes[totaltime] = 1
            meanlength += episodetime
            app.clearCanvas()
            app.drawgrid()
            app.drawpolicy(policy)
            app.drawtrajectory(Slist)
            Slist=[]
            meanRlist.append(sumR)

        if n % conf.windowsize == 0:
            print(n,'mean path length',meanlength/conf.windowsize,'; mean reward',meanRlist[-1])
            meanlengthlist.append(meanlength/conf.windowsize)
            meanlength = 0

    return policy,successful_episodes,meanlengthlist,meanRlist


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

        # stop event
        super(App, self).__init__()
        self._stop_event = threading.Event()

        # GUI x and y scalings
        self.scalex=100
        self.scaley=100

    def drawgrid(self):
        for x in range(0,conf.xsize):
            id = self.myCanvas.create_line(x*self.scalex,0,x*self.scalex,self.scaley*conf.ysize,width=.1)
        for y in range(0,conf.ysize):
            id = self.myCanvas.create_line(0,y*self.scaley,self.scalex*conf.xsize,self.scaley*y,width=.1)

        # color the wind areas
        if args.envtype == 'W' or args.envtype == 'KW':
            for y in range(0,conf.ysize):
                self.colorfield([3,y],"lightgray")
                self.colorfield([4,y],"lightgray")
                self.colorfield([5,y],"lightgray")
                self.colorfield([6,y],"darkgray")
                self.colorfield([7,y],"darkgray")
                self.colorfield([8,y],"lightgray")


        # color start and end states
        self.colorfield(statestart,"green")
        self.colorfield(stateend,"blue")


    def colorfield(self,field,color):
        self.myCanvas.create_rectangle(field[0]*self.scalex,field[1]*self.scaley,(field[0]+1)*self.scalex,(field[1]+1)*self.scaley,fill=color)

    def drawpolicy(self,policy):

        for state in list(policy.keys()):
            state_decoded = decodeS(state)
            x0=self.scalex/2 + self.scalex*state_decoded[0]
            y0=self.scaley/2 + self.scaley*state_decoded[1]
            p = policy[state]

            id0 = self.myCanvas.create_line(x0,y0,x0,y0-p[0]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[0],10*p[0],3*p[0]))
            id1 = self.myCanvas.create_line(x0,y0,x0+p[1]*self.scalex/2,y0,arrow=tkinter.LAST,arrowshape=(8*p[1],10*p[1],3*p[1]))
            id2 = self.myCanvas.create_line(x0,y0,x0,y0+p[2]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[2],10*p[2],3*p[2]))
            id3 = self.myCanvas.create_line(x0,y0,x0-p[3]*self.scalex/2,y0,arrow=tkinter.LAST,arrowshape=(8*p[3],10*p[3],3*p[3]))

            if args.envtype == 'K' or args.envtype == 'KW':
                id4 = self.myCanvas.create_line(x0,y0,x0+p[4]*self.scalex/2,y0-p[4]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[4],10*p[4],3*p[4]))
                id5 = self.myCanvas.create_line(x0,y0,x0+p[5]*self.scalex/2,y0+p[5]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[5],10*p[5],3*p[5]))
                id6 = self.myCanvas.create_line(x0,y0,x0-p[6]*self.scalex/2,y0+p[6]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[6],10*p[6],3*p[6]))
                id7 = self.myCanvas.create_line(x0,y0,x0-p[7]*self.scalex/2,y0-p[7]*self.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[7],10*p[7],3*p[7]))

    def clearCanvas(self):
        self.myCanvas.delete("all")

    def drawtrajectory(self,Slist):
        #print(len(Slist))
        if len(Slist) < conf.drawingcap:
            for i in range(0,len(Slist)-1):

                x0 = self.scalex*Slist[i][0]
                y0 = self.scaley*Slist[i][1]
                x1 = self.scalex*Slist[i+1][0]
                y1 = self.scaley*Slist[i+1][1]
                self.myCanvas.create_line(x0+self.scalex/2,y0+self.scaley/2,x1+self.scalex/2,y1+self.scaley/2,fill="red",width=3)

    # def savepolicy(self):
    #     print('saving the policy')
    #     with open('policy.pkl', 'wb') as f: pickle.dump(policy, f, pickle.HIGHEST_PROTOCOL)
    #
    # def savemeanlength(self):
    #     print('saving the meanlengthlist')
    #     with open('meanlength.pkl', 'wb') as f: pickle.dump(meanlengthlist, f, pickle.HIGHEST_PROTOCOL)
    #
    # def savemeanR(self):
    #     print('saving the meanRlist')
    #     with open('meanR.pkl', 'wb') as f: pickle.dump(meanRlist, f, pickle.HIGHEST_PROTOCOL)
    #
    # def savesuccess(self):
    #     print('saving the successful_episodes')
    #     with open('efficacy.pkl', 'wb') as f: pickle.dump(successful_episodes, f, pickle.HIGHEST_PROTOCOL)

    # def saveall(self):
    #     self.savepolicy()
    #     self.savemeanlength()
    #     self.savemeanR()
    #     self.savesuccess()

    def run(self):
        self.root = tkinter.Tk()

        self.myCanvas = tkinter.Canvas(self.root, bg="white", height=self.scaley*conf.ysize, width=self.scalex*conf.xsize)
        #self.drawpolicybutton = tkinter.Button(self.root,text="refresh",command=self.drawpolicy)
        # self.savepolicybutton = tkinter.Button(self.root,text="save policy",command=self.savepolicy)
        # self.savemeanlengthbutton = tkinter.Button(self.root,text="save mean episode length",command=self.savemeanlength)
        # self.savemeanRbutton = tkinter.Button(self.root,text="save mean rewards",command=self.savemeanR)
        # self.savesuccessbutton = tkinter.Button(self.root,text="save successful_episodes",command=self.savesuccess)
        # self.saveallbutton = tkinter.Button(self.root,text="save all",command=self.saveall)
        #self.drawtrajbutton = tkinter.Button(self.root,text="draw trajectory",command=self.drawtrajectory)

        # draw the gridworld
        self.drawgrid()

        self.myCanvas.pack(side=tkinter.TOP)
        #self.drawpolicybutton.pack(side=tkinter.TOP)
        # self.savepolicybutton.pack(side=tkinter.LEFT)
        # self.savemeanlengthbutton.pack(side=tkinter.LEFT)
        # self.savemeanRbutton.pack(side=tkinter.LEFT)
        # self.savesuccessbutton.pack(side=tkinter.LEFT)
        # self.saveallbutton.pack(side=tkinter.RIGHT)
        #self.drawtrajbutton.pack(side=tkinter.TOP)

        self.root.mainloop()

    def stop(self):
        self._stop_event.set()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='gridworld_learn',description='reinforce-learn the gridworld')

    parser.add_argument('-E','--envtype',type=str,default='0',choices=['0','K','W','KW'],help='pick the environment type: "0" - pure; "K" - King\'s moves; "W" - Windy; "KW" - King\'s moves+Windy Gridworlds')
    parser.add_argument('-m','--model',type=str,default='sarsa',choices=['sarsa','sarsaconv','sarsalambda','Q'],help='pick the learning model: "sarsa" for SARSA algorithm; "sarsaconv" for convergent SARSA algorithm; "sarsalambda" for SARSA(LAMBDA) algorithm; "Q" for Q-learning')
    parser.add_argument('-l','--lambda',dest='lambda0',metavar='LAMBDA',type=float,default=conf.defaultlambda,help='set the lambda parameter for SARSA(LAMBDA) algorithm; between (0,1)')
    parser.add_argument('-a','--alpha',type=float,default=conf.defaultalpha,help='set the initial learning rate; between (0,1)')
    parser.add_argument('-n','--noepisodes',type=int,default=conf.defaultnoepisodes,help='set the number of learning episodes')
    parser.add_argument('-g','--gamma',type=float,default=conf.defaultgamma,help='set the discount parameter; between (0,1)')
    parser.add_argument('-e','--epsilon',type=float,default=conf.defaultepsilon, help='set the initial exploration parameter in epsilon-greedy policy improvement; between (0,1)')
    parser.add_argument('-N','--nogui',dest='nogui',default=False,const=True, action='store_const', help='do not use graphical UI')
    parser.add_argument('-de','--noepsilondrop',dest='noepsilondrop',default=False,const=True, action='store_const', help='keep epsilon fixed during training')
    parser.add_argument('-da','--noalphadrop',dest='noalphadrop',default=False,const=True, action='store_const', help='keep alpha fixed during training')
    parser.add_argument('-b','--batchmode',dest='batchmode',default=False,const=True, action='store_const', help='run in batch mode i.e. supress most controls')
    parser.add_argument('-q','--initq',type=float,default=conf.defaultinitq,help='set the initial Q-value')
    parser.add_argument('-s','--saveoutput',default=False,const=True,action='store_const',help='store output data in external files')
    args = parser.parse_args()

    environment = {'0':env,'K':envK,'W':envW,'KW':envKW}[args.envtype]

    # define the epsilon dynamics in greedy improvement
    if args.noepsilondrop: epsilonfunc = epsilonconst
    else: epsilonfunc = epsilondrop

    # define the alpha dynamics in the update rules
    if args.noalphadrop: alphafunc = alphaconst
    else: alphafunc = alphadrop

    # init states and actions
    states = [[x,y] for x in range(0,conf.xsize) for y in range(0,conf.ysize)]

    actions = {'0':[0,1,2,3],'K':[0,1,2,3,4,5,6,7],'W':[0,1,2,3],'KW':[0,1,2,3,4,5,6,7],'ext':[0,1,2,3]}[args.envtype]
    stateactions = [codeSA(state,action) for state in states for action in actions]

    # set initial and final states
    statestart = conf.statestart
    stateend = conf.stateend

    # number of training episodes
    noepisodes = args.noepisodes
    # alpha parameter
    alpha = args.alpha
    # discount gamma parameter
    gamma = args.gamma
    # exploration parameter
    epsilon = args.epsilon
    # lambda parameter (SARSA(LAMBDA) parameter)
    lambda0 = args.lambda0
    # initial Q-value
    initQ = args.initq

    # some console info
    envtype0 = {'0':'Pure Gridworld','K':'King\'s moves Gridworld','W':'Windy Gridworld','KW':'King\'s moves Windy Gridworld','ext': 'Extended Gridworld'}[args.envtype]
    print('environment type:',envtype0)
    print('learning model:',args.model)
    print('number of episodes:',args.noepisodes)
    print('general parameters: init alpha=',args.alpha,'gamma=',args.gamma,'init epsilon=',args.epsilon,'init Q=',args.initq)
    specargs = ''
    if args.model=='sarsalambda': specargs = 'lambda= '+str(args.lambda0)
    print('model specific parameters:',specargs)
    print('use GUI?',not args.nogui)
    print('keep epsilon fixed during training?',args.noepsilondrop)
    print('keep alpha fixed during training?',args.noalphadrop)
    print('save output to external files?',args.saveoutput)

    # gui
    if not args.nogui: app = App()

    # run learning algorithm
    learnmodel = {'sarsa':sarsa,'sarsaconv':sarsaconv,'sarsalambda':sarsalambda,'Q':Qlearn}[args.model]
    policy,successful_episodes,meanlengthlist,meanRlist = learnmodel()

    # policy = greedy(Q,epsilon)
    # As = [2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
    # Ss = [[0,3]]
    # Rs = []
    # Snew = []
    # for a in As:
    #     R,Snew = env(Ss[-1],a)
    #     Rs.append(R)
    #     Ss.append(Snew.copy())
    #
    # Slist = Ss.copy()
    # app.drawpolicy()
    # app.drawtrajectory()
    # print(As,Ss,Rs)

    if args.saveoutput:
        savepolicy(policy)
        savesuccess(successful_episodes)
        savemeanlength(meanlengthlist)
        savemeanR(meanRlist)

    if not args.batchmode:
        print('<RETURN>')
        input()
    app.stop()
