# RL_gridworld
User friendly code to see Reinforcement Learning algorithms at work in a set of gridworld environments.
Gridworld environments are a subset of elementary yet nontrivial playground environments to test RL ideas.
Implemented gridworlds are based on the Example 6.5 and Exercise 6.6 from the book "Reinforcement Learning:an introduction" by Sutton and Barto.

## How to start?
To start a simple learning just run
```
python gridworld_learn.py
```
which learns a pure gridworld environment with SARSA algorithm.

### What is going on?
Agent starts on the green cell and should move to the blue field. Each movement gives a reward of -1 and so the task is to find the shortest path. There are four environment variants:
* **pure gridworld**

The agent can move up/down/left and right. Besides the initial and final cells, world is featureless.

* **King's moves gridworld**

The agent can also move on the diagonals, world is featureless.

* **Windy gridworld**

Agent can move in a classic manner however the world gains a windy strip between initial and final cells. This strip is colored in either light or dark-gray denoting weak and strong wind respectively. Upon stepping on a windy tile, on top of agent's normal motion, the gust translates him either one or two tiles up depending on the strength of the wind.  

* **Windy King's moves gridworld**

Combination of two previous cases i.e. agent in a Windy gridworld has King's moves.

Four arrows located at the center of each cell depict the possible actions with their probabilities encoded in their sizes. An actual trajectory chosen by the agent is shown by a thick black line and it is drawn only when it is complete or reaches the final cell.

## Options
All available options are found through
```
python gridworld_learn.py --help
```

## Algorithms

There are three algorithms implemented
* SARSA
* SARSA(LAMBDA)
* Q-Learning

## Examples
In the **/examples** directory working examples are provided.

- *SARSA_lambda*

Explore the SARSA(LAMBDA) algorithm as a function of the lambda parameter which measures how much into the future our algorithm looks. To run:
```
./SARSA_lambda.sh
```

- *comparison*

Compare all algorithms. To run:
```
./comparison.sh
```
