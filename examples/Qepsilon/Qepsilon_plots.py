import pickle
import sys
sys.path.append("..")
#from gridworld import codeS
import matplotlib.pyplot as plt

with open('Q_largeepsilon/efficacy.pkl', 'rb') as f: efficacy1 = pickle.loads(f.read())
with open('Q_largeepsilon/meanlength.pkl', 'rb') as f: meanlength1 = pickle.loads(f.read())
with open('Q_largeepsilon/meanR.pkl', 'rb') as f: meanR1 = pickle.loads(f.read())
with open('Q_mediumepsilon/efficacy.pkl', 'rb') as f: efficacy2 = pickle.loads(f.read())
with open('Q_mediumepsilon/meanlength.pkl', 'rb') as f: meanlength2 = pickle.loads(f.read())
with open('Q_mediumepsilon/meanR.pkl', 'rb') as f: meanR2 = pickle.loads(f.read())
with open('Q_smallepsilon/efficacy.pkl', 'rb') as f: efficacy3 = pickle.loads(f.read())
with open('Q_smallepsilon/meanlength.pkl', 'rb') as f: meanlength3 = pickle.loads(f.read())
with open('Q_smallepsilon/meanR.pkl', 'rb') as f: meanR3 = pickle.loads(f.read())

max=30

yA1 = meanlength1[1:max]
xA1 = [i for i in range(0,len(yA1))]
yA2 = meanlength2[1:max]
xA2 = [i for i in range(0,len(yA2))]
yA3 = meanlength3[1:max]
xA3 = [i for i in range(0,len(yA3))]



plt.figure(0)

plt.plot(xA1,yA1,label="Q-LEARN epsilon=0.9")
plt.plot(xA2,yA2,label="Q-LEARN epsilon=0.6")
plt.plot(xA3,yA3,label="Q-LEARN epsilon=0.1")
plt.ylabel('mean trajectory length')
plt.title('environment cliff.txt')
plt.legend()


yA1 = meanR1[1:max]
xA1 = [i for i in range(0,len(yA1))]
yA2 = meanR2[1:max]
xA2 = [i for i in range(0,len(yA2))]
yA3 = meanR3[1:max]
xA3 = [i for i in range(0,len(yA3))]


fig1 = plt.figure(1)

plt.plot(xA1,yA1,label="Q-LEARN epsilon=0.9")
plt.plot(xA2,yA2,label="Q-LEARN epsilon=0.6")
plt.plot(xA3,yA3,label="Q-LEARN epsilon=0.1")
plt.title('environment cliff.txt')
plt.ylabel('mean reward')
plt.legend()

# xB1=list(efficacy1.keys())
# yB1=[i for i in range(1,len(xB1)+1)]
# xB2=list(efficacy2.keys())
# yB2=[i for i in range(1,len(xB2)+1)]
# xB3=list(efficacy3.keys())
# yB3=[i for i in range(1,len(xB3)+1)]
# xB4=list(efficacy4.keys())
# yB4=[i for i in range(1,len(xB4)+1)]
#
# plt.subplot(212)
# plt.plot(xB1,yB1,label="SARSA")
# plt.plot(xB2,yB2,label="SARSA(LAMBDA=0.9)")
# plt.plot(xB3,yB3,label="Q-LEARNING")
# plt.plot(xB4,yB4,label="SARSA(LAMBDA=0.6)")
# plt.legend()
plt.show()
