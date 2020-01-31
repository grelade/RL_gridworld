#!/bin/sh
SIMPATH="../../RL_gridworlds.py"

echo "### S1: SARSA with varied epsilon/exploration parameter"
echo "*** S1: cliff.txt environment"

echo "### SARSA small exploration parameter /w dropout"
python $SIMPATH -m sarsa --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 0.1 -de --nogui
if [ ! -d "sarsa_smallepsilon" ]; then
  mkdir sarsa_smallepsilon
fi
mv *.pkl sarsa_smallepsilon
echo "### SARSA completed"



echo "### SARSA large exploration parameter /w dropout"
python $SIMPATH -m sarsa --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 1 -de --nogui
echo "### SARSA completed"
if [ ! -d "sarsa_largeepsilon" ]; then
  mkdir sarsa_largeepsilon
fi
mv *.pkl sarsa_largeepsilon



echo "### SARSA medium exploration parameter /w dropout"
python $SIMPATH -m sarsa --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 0.6 -de --nogui
echo "### SARSA completed"
if [ ! -d "sarsa_mediumepsilon" ]; then
  mkdir sarsa_mediumepsilon
fi
mv *.pkl sarsa_mediumepsilon



echo "### plots"
python SARSAepsilon_plots.py
