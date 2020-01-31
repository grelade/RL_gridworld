import numpy as np
import matplotlib.pyplot as plt
import pickle
import tkinter
import threading
import argparse
import conf
import os,sys
import time
from envs import env

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
    return epsilon/(n+1)**(1)

# alpha parameter is held constant over training
def alphaconst(n):
    return alpha

# alpha parameter is modified during training
def alphadrop(n):
    return alpha/(n+1)**(1)


# choose a move for a state according to policy
def choosemove(state,policy):

    statePolicy = policy[state]
    return np.random.choice(actions,p=statePolicy)


class compute(threading.Thread):
    def __init__(self):
        super(compute,self).__init__()
        self.policy = 0
        self.successful_episodes = 0
        self.meanlengthlist = []
        self.meanRlist = []

    def setModel(self,model):
        self.model = model
        # {'sarsa':self.sarsa,'sarsaconv':self.sarsaconv,'sarsalambda':self.sarsalambda,'Q':self.Qlearn}[model]
    def setEnv(self,currenv):
        self.env = currenv

    def setRenderer(self,renderer):
        self.renderer = renderer

    def setStop(self,stopevent):
        self.stopevent = stopevent


    def train(self):

        # init Q-value function
        Q = {}
        for stateaction in stateactions: Q[stateaction] = initQ

        # initial policy
        policy = greedy(Q,epsilonfunc(0))

        # init N counting function
        N = {}
        for stateaction in stateactions: N[stateaction] = 0

        # init N-s counting function
        Ns = {}
        for state in states: Ns[codeS(state)] = 0

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
        if not self.renderer == None: self.renderer.drawpolicy(policy)

        for n in range(0,noepisodes+1):
            episodetime = 0
            sumR = 0
            S = self.env.start.copy()
            Slist.append(S)
            policy = greedy(Q,epsilonfunc(n)) # derive policy from Q
            A = choosemove(codeS(S),policy) # choose A from policy
            while not S == self.env.end:
                if self.stopevent.isSet(): return None
                totaltime+=1
                episodetime += 1
                if self.model == 'sarsaconv':
                    N[codeSA(S,A)]+=1
                    Ns[codeS(S)]+=1
                R,Sp = e.act(S,A)
                sumR += R
                Slist.append(Sp.copy())
                if self.model == 'sarsaconv': policy = greedy(Q,epsilon/Ns[codeS(S)])
                else: policy = greedy(Q,epsilonfunc(n))
                Ap = choosemove(codeS(Sp),policy)

                if self.model =='sarsa':
                    Q[codeSA(S,A)] += alphafunc(n)*(R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)])
                elif self.model == 'sarsaconv':
                    Q[codeSA(S,A)] += alpha/N[codeSA(S,A)]*(R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)])
                elif self.model == 'sarsalambda':
                    #print(Q[codeSA(S,A)])
                    delta = R+ gamma*Q[codeSA(Sp,Ap)] - Q[codeSA(S,A)]
                    #E[codeSA(S,A)] += 1 # accumulating traces
                    E[codeSA(S,A)] += 1 - alphafunc(n)*E[codeSA(S,A)] # dutch traces
                    #E[codeSA(S,A)] = 1 # replacing traces
                    for s in states:
                        for a in actions:
                            Q[codeSA(s,a)] += alphafunc(n)*delta*E[codeSA(s,a)]
                            E[codeSA(s,a)] *= gamma*lambda0

                elif self.model =='Q':
                    Q[codeSA(S,A)] += alphafunc(n)*(R+ gamma*np.max([Q[codeSA(Sp,a)] for a in actions]) - Q[codeSA(S,A)])

                S,A = Sp,Ap

                if episodetime % 40 == 0 and not self.renderer == None:
                    self.renderer.clearCanvas()
                    self.renderer.drawgrid()
                    self.renderer.drawtrajectory(Slist[-40:])
                    self.renderer.drawpolicy(policy)
            if S == self.env.end:
                Slist.append(S)
                successful_episodes[totaltime] = 1
                meanlength += episodetime
                if not self.renderer == None:
                    self.renderer.clearCanvas()
                    self.renderer.drawgrid()
                    self.renderer.drawtrajectory(Slist)
                    self.renderer.drawpolicy(policy)
                Slist=[]
                #print(sumR)
                meanRlist.append(sumR)
                #print('epsilon=',epsilonfunc(n))

            if n % conf.windowsize == 0:
                #print(meanRlist)
                print(n,'mean path length',meanlength/conf.windowsize,'; mean reward',meanRlist[-1],'epsilon=',epsilonfunc(n),'alpha=',alphafunc(n))
                meanlengthlist.append(meanlength/conf.windowsize)
                meanlength = 0
        if args.nogui: self.stopevent.set()
        else: print('simulation finished; close the window to save session.')
        self.policy = policy
        self.successful_episodes = successful_episodes
        self.meanlengthlist = meanlengthlist
        self.meanRlist = meanRlist

    def run(self):
        self.train()

    def savepolicy(self):
        print('saving the policy')
        with open('policy.pkl', 'wb') as f: pickle.dump(self.policy, f, pickle.HIGHEST_PROTOCOL)

    def savemeanlength(self):
        print('saving the meanlengthlist')
        with open('meanlength.pkl', 'wb') as f: pickle.dump(self.meanlengthlist, f, pickle.HIGHEST_PROTOCOL)

    def savemeanR(self):
        print('saving the meanRlist')
        with open('meanR.pkl', 'wb') as f: pickle.dump(self.meanRlist, f, pickle.HIGHEST_PROTOCOL)

    def savesuccess(self):
        print('saving the successful_episodes')
        with open('efficacy.pkl', 'wb') as f: pickle.dump(self.successful_episodes, f, pickle.HIGHEST_PROTOCOL)


class render():

    def __init__(self,canvas):
        self.myCanvas = canvas

    def setEnv(self,currenv):
        self.env = currenv

    def drawgrid(self):

        for x in range(0,self.env.xsize):
            id = self.myCanvas.create_line(x*conf.scalex,0,x*conf.scalex,conf.scaley*self.env.ysize,width=.1)
        for y in range(0,self.env.ysize):
            id = self.myCanvas.create_line(0,y*conf.scaley,conf.scalex*self.env.xsize,conf.scaley*y,width=.1)

        #colors
        colordict = {'#': 'black','.':'white','S':'green','E':'blue','|':'lightgray','V':'lightblue','W':'darkblue'}
        for i in range(0,self.env.xsize):
            for j in range(0,self.env.ysize):
                self.colorfield([i,j],colordict[(self.env.table)[j][i]])


    def colorfield(self,field,color):
        self.myCanvas.create_rectangle(field[0]*conf.scalex,field[1]*conf.scaley,(field[0]+1)*conf.scalex,(field[1]+1)*conf.scaley,fill=color)

    def drawpolicy(self,policy):
        #print(policy.keys())
        for state in list(policy.keys()):
            state_decoded = decodeS(state)
            x0=conf.scalex/2 + conf.scalex*state_decoded[0]
            y0=conf.scaley/2 + conf.scaley*state_decoded[1]
            p = policy[state]

            id0 = self.myCanvas.create_line(x0,y0,x0,y0-p[0]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[0],10*p[0],3*p[0]))
            id1 = self.myCanvas.create_line(x0,y0,x0+p[1]*conf.scalex/2,y0,arrow=tkinter.LAST,arrowshape=(8*p[1],10*p[1],3*p[1]))
            id2 = self.myCanvas.create_line(x0,y0,x0,y0+p[2]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[2],10*p[2],3*p[2]))
            id3 = self.myCanvas.create_line(x0,y0,x0-p[3]*conf.scalex/2,y0,arrow=tkinter.LAST,arrowshape=(8*p[3],10*p[3],3*p[3]))

            if args.envtype == 'K' or args.envtype == 'KW':
                id4 = self.myCanvas.create_line(x0,y0,x0+p[4]*conf.scalex/2,y0-p[4]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[4],10*p[4],3*p[4]))
                id5 = self.myCanvas.create_line(x0,y0,x0+p[5]*conf.scalex/2,y0+p[5]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[5],10*p[5],3*p[5]))
                id6 = self.myCanvas.create_line(x0,y0,x0-p[6]*conf.scalex/2,y0+p[6]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[6],10*p[6],3*p[6]))
                id7 = self.myCanvas.create_line(x0,y0,x0-p[7]*conf.scalex/2,y0-p[7]*conf.scaley/2,arrow=tkinter.LAST,arrowshape=(8*p[7],10*p[7],3*p[7]))

    def clearCanvas(self):
        self.myCanvas.delete("all")

    def drawtrajectory(self,Slist):
        #print(len(Slist))
        if len(Slist) < conf.drawingcap:
            for i in range(0,len(Slist)-1):

                x0 = conf.scalex*Slist[i][0]
                y0 = conf.scaley*Slist[i][1]
                x1 = conf.scalex*Slist[i+1][0]
                y1 = conf.scaley*Slist[i+1][1]
                self.myCanvas.create_line(x0+conf.scalex/2,y0+conf.scaley/2,x1+conf.scalex/2,y1+conf.scaley/2,fill="red",width=3)

if __name__ == "__main__":

    stopevent = threading.Event()

    parser = argparse.ArgumentParser(prog='cliff_learn',description='reinforce-learn the cliff')

    parser.add_argument('-E','--envtype',type=str,default='simple.txt',help='pick the environment from envs')
    parser.add_argument('-A','--actions',type=str,default='0',choices=['0','K'],help='pick action repertoire')
    parser.add_argument('-m','--model',type=str,default='sarsa',choices=['sarsa','sarsaconv','sarsalambda','Q'],help='pick the learning model: "sarsa" for SARSA algorithm; "sarsaconv" for convergent SARSA algorithm; "sarsalambda" for SARSA(LAMBDA) algorithm; "Q" for Q-learning')
    parser.add_argument('-l','--lambda',dest='lambda0',metavar='LAMBDA',type=float,default=conf.defaultlambda,help='set the lambda parameter for SARSA(LAMBDA) algorithm; between (0,1)')
    parser.add_argument('-a','--alpha',type=float,default=conf.defaultalpha,help='set the initial learning rate; between (0,1)')
    parser.add_argument('-n','--noepisodes',type=int,default=conf.defaultnoepisodes,help='set the number of learning episodes')
    parser.add_argument('-g','--gamma',type=float,default=conf.defaultgamma,help='set the discount parameter; between (0,1)')
    parser.add_argument('-e','--epsilon',type=float,default=conf.defaultepsilon, help='set the initial exploration parameter in epsilon-greedy policy improvement; between (0,1)')
    parser.add_argument('-N','--nogui',dest='nogui',default=False,const=True, action='store_const', help='do not use graphical UI')
    parser.add_argument('-de','--epsilondrop',dest='epsilondrop',default=False,const=True, action='store_const', help='drop epsilon during training')
    parser.add_argument('-da','--alphadrop',dest='alphadrop',default=False,const=True, action='store_const', help='drop alpha during training')
    parser.add_argument('-q','--initq',type=float,default=conf.defaultinitq,help='set the initial Q-value')

    args = parser.parse_args()
    print(os.path.join(sys.path[0],'envs',args.envtype))
    e = env(os.path.join(sys.path[0],'envs',args.envtype))

    #print(e.xsize,e.ysize)
    #environment = {'0':env}[args.envtype]

    # define the epsilon dynamics in greedy improvement
    if args.epsilondrop: epsilonfunc = epsilondrop
    else: epsilonfunc = epsilonconst

    # define the alpha dynamics in the update rules
    if args.alphadrop: alphafunc = alphadrop
    else: alphafunc = alphaconst

    # init states and actions
    states = e.getStates()

    actions = {'0':[0,1,2,3],'K':[0,1,2,3,4,5,6,7]}[args.actions]
    stateactions = [codeSA(state,action) for state in states for action in actions]

    # set initial and final states
    # statestart = conf.statestart
    # stateend = conf.stateend

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

    print('environment file:',args.envtype)
    print('action repertoire:',args.actions)
    print('learning model:',args.model)
    print('number of episodes:',args.noepisodes)
    print('general parameters: init alpha=',args.alpha,'gamma=',args.gamma,'init epsilon=',args.epsilon,'init Q=',args.initq)
    specargs = ''
    if args.model=='sarsalambda': specargs = 'lambda= '+str(args.lambda0)
    print('model specific parameters:',specargs)
    print('use GUI?',not args.nogui)
    print('decrease epsilon during training?',args.epsilondrop)
    print('decrease alpha during training?',args.alphadrop)

    # renderer
    if args.nogui: renderer = None
    else:
        #print('teta')
        root = tkinter.Tk()
        myCanvas = tkinter.Canvas(root, bg="white", height=conf.scaley*e.ysize, width=conf.scalex*e.xsize)
        renderer = render(myCanvas)
        renderer.setEnv(e)
        myCanvas.pack(side=tkinter.TOP)
        renderer.drawgrid()

    computer = compute()
    computer.setModel(args.model)
    computer.setEnv(e)
    computer.setRenderer(renderer)
    computer.setStop(stopevent)
    computer.start()

    if args.nogui:
        while not stopevent.isSet():
            time.sleep(1)
    else: root.mainloop()
    #if not args.nogui: root.mainloop()

    computer.savepolicy()
    computer.savesuccess()
    computer.savemeanlength()
    computer.savemeanR()

    stopevent.set()
