#!/bin/sh
SIMPATH=../../gridworld_learn.py

echo "### S2: SARSA/SARSA(LAMBDA)/Q-LEARN comparison"


echo "### SARSA"
python $SIMPATH -m sarsa -E W -n 600 -a 0.1 -g 1 -e 0.3 -da -b -s
if [ ! -d "sarsa2_pure" ]; then
  mkdir sarsa2_pure
fi
mv *.pkl sarsa2_pure
echo "### SARSA completed"


echo "### SARSA(LAMBDA=0.5)"
python $SIMPATH -m sarsalambda -E W -n 600 -l 0.5 -a 0.1 -g 1 -e 0.3 -da -b -q 100 -s
if [ ! -d "sarsa2_lambda=0.9" ]; then
  mkdir sarsa2_lambda=0.9
fi
mv *.pkl sarsa2_lambda=0.9
echo "### SARSA(LAMBDA=0.9) completed"


echo "### Q-LEARNING"
python $SIMPATH -m Q -E W -n 600 -a 0.1 -g 1 -e 0.3 -da -b -s
if [ ! -d "qlearn_pure" ]; then
  mkdir qlearn_pure
fi
mv *.pkl qlearn_pure
echo "### Q-LEARNING completed"



echo "### plots"
python comparison_plots.py
