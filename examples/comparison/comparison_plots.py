import pickle
import sys
sys.path.append("..")
#from gridworld import codeS
import matplotlib.pyplot as plt

with open('sarsa2_lambda=0.9/efficacy.pkl', 'rb') as f: efficacy1 = pickle.loads(f.read())
with open('sarsa2_lambda=0.9/meanlength.pkl', 'rb') as f: meanlength1 = pickle.loads(f.read())
with open('sarsa2_lambda=0.9/meanR.pkl', 'rb') as f: meanR1 = pickle.loads(f.read())
with open('sarsa2_pure/efficacy.pkl', 'rb') as f: efficacy2 = pickle.loads(f.read())
with open('sarsa2_pure/meanlength.pkl', 'rb') as f: meanlength2 = pickle.loads(f.read())
with open('sarsa2_pure/meanR.pkl', 'rb') as f: meanR2 = pickle.loads(f.read())
with open('qlearn_pure/efficacy.pkl', 'rb') as f: efficacy3 = pickle.loads(f.read())
with open('qlearn_pure/meanlength.pkl', 'rb') as f: meanlength3 = pickle.loads(f.read())
with open('qlearn_pure/meanR.pkl', 'rb') as f: meanR3 = pickle.loads(f.read())
# with open('sarsa_lambda=0.5/efficacy.pkl', 'rb') as f: efficacy4 = pickle.loads(f.read())
# with open('sarsa_lambda=0.5/meanlength.pkl', 'rb') as f: meanlength4 = pickle.loads(f.read())
# with open('sarsa_lambda=0.5/meanR.pkl', 'rb') as f: meanR4 = pickle.loads(f.read())
# with open('sarsa_lambda=0.7/efficacy.pkl', 'rb') as f: efficacy5 = pickle.loads(f.read())
# with open('sarsa_lambda=0.7/meanlength.pkl', 'rb') as f: meanlength5 = pickle.loads(f.read())
# with open('sarsa_lambda=0.7/meanR.pkl', 'rb') as f: meanR5 = pickle.loads(f.read())
# with open('sarsa_lambda=0.8/efficacy.pkl', 'rb') as f: efficacy6 = pickle.loads(f.read())
# with open('sarsa_lambda=0.8/meanlength.pkl', 'rb') as f: meanlength6 = pickle.loads(f.read())
# with open('sarsa_lambda=0.8/meanR.pkl', 'rb') as f: meanR6 = pickle.loads(f.read())
# with open('sarsa_lambda=0.9/efficacy.pkl', 'rb') as f: efficacy7 = pickle.loads(f.read())
# with open('sarsa_lambda=0.9/meanlength.pkl', 'rb') as f: meanlength7 = pickle.loads(f.read())
# with open('sarsa_lambda=0.9/meanR.pkl', 'rb') as f: meanR7 = pickle.loads(f.read())

max=30

yA1 = meanlength1[1:max]
xA1 = [i for i in range(0,len(yA1))]
yA2 = meanlength2[1:max]
xA2 = [i for i in range(0,len(yA2))]
yA3 = meanlength3[1:max]
xA3 = [i for i in range(0,len(yA3))]
# yA4 = meanlength4[1:max]
# xA4 = [i for i in range(0,len(yA4))]
# yA5 = meanlength5[1:max]
# xA5 = [i for i in range(0,len(yA5))]
# yA6 = meanlength6[1:max]
# xA6 = [i for i in range(0,len(yA6))]
# yA7 = meanlength7[1:max]
# xA7 = [i for i in range(0,len(yA7))]


plt.figure(0)

plt.plot(xA1,yA1,label="SARSA(lambda=0.9)")
plt.plot(xA2,yA2,label="SARSA")
plt.plot(xA3,yA3,label="Q-LEARN")
# plt.plot(xA4,yA4,label="SARSA lambda=0.5")
# plt.plot(xA5,yA5,label="SARSA lambda=0.7")
# plt.plot(xA6,yA6,label="SARSA lambda=0.8")
# plt.plot(xA7,yA7,label="SARSA lambda=0.9")

plt.ylabel('mean trajectory length')
plt.legend()


yA1 = meanR1[1:max]
xA1 = [i for i in range(0,len(yA1))]
yA2 = meanR2[1:max]
xA2 = [i for i in range(0,len(yA2))]
yA3 = meanR3[1:max]
xA3 = [i for i in range(0,len(yA3))]
# yA4 = meanR4[1:max]
# xA4 = [i for i in range(0,len(yA4))]
# yA5 = meanR5[1:max]
# xA5 = [i for i in range(0,len(yA5))]
# yA6 = meanR6[1:max]
# xA6 = [i for i in range(0,len(yA6))]
# yA7 = meanR7[1:max]
# xA7 = [i for i in range(0,len(yA7))]

fig1 = plt.figure(1)

plt.plot(xA1,yA1,label="SARSA(lambda=0.9)")
plt.plot(xA2,yA2,label="SARSA")
plt.plot(xA3,yA3,label="Q-LEARN")
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
