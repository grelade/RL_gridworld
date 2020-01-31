# RL_gridworlds
User friendly code to track Reinforcement Learning algorithms at work in a set of simple gridworld environments. Has a simple interpreter for creating own environments via plain text. Contains several playgrounds based on the Example 6.5 and Exercise 6.6 from the book "Reinforcement Learning:an introduction" by Sutton and Barto. Implemented variants of SARSA and Q-learning algorithms.

## How to start?
To start an agent learning an environment just run
```
python RL_gridworlds.py
```
which runs a SARSA algorithm on a [envs/simple.txt] environment.

### What is going on?
Agent starts on the green cell and should move to the blue field. Each movement gives a reward of -1 and so the task is to find the shortest path.



There are four environments implemented:
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

## Creating own environments
[env data file and its parsed version]("imgs/env-img.png")
There is an easy way of generating own environments through plain text files found in [envs] dir.

Apart from mandatory blocks:
- 'S' the start block (reward -1; green)
- 'E' the finish or end block (reward 10; blue)
- '.' plain block (reward -1; white color)

There are additional blocks available:
- 'V' weak south wind, moves one tile (reward -1; lightblue)
- 'W' strong south wind, moves two tiles (reward -1; darkblue)
- '#' wall, cannot explore (reward -1; black)
- '|' cliff, moves back to S (reward -100; gray)

## Algorithms

There are three algorithms implemented
* SARSA
* SARSA(LAMBDA)
* Q-Learning

## Examples
In the **examples** directory working examples are provided.

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
