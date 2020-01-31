#!/bin/sh
SIMPATH="../../RL_gridworlds.py"

echo "### S2: Q-LEARN with varied epsilon/exploration parameter"

echo "### Q-LEARN small exploration parameter /w dropout"
python $SIMPATH -m Q --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 0.1 -de --nogui
if [ ! -d "Q_smallepsilon" ]; then
  mkdir Q_smallepsilon
fi
mv *.pkl Q_smallepsilon
echo "### Q-LEARN completed"



echo "### Q-LEARN large exploration parameter /w dropout"
python $SIMPATH -m Q --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 1 -de --nogui
echo "### Q-LEARN completed"
if [ ! -d "Q_largeepsilon" ]; then
  mkdir Q_largeepsilon
fi
mv *.pkl Q_largeepsilon



echo "### Q-LEARN medium exploration parameter /w dropout"
python $SIMPATH -m Q --envtype cliff.txt -n 600 -a 0.1 -g 1 -e 0.6 -de --nogui
echo "### Q-LEARN completed"
if [ ! -d "Q_mediumepsilon" ]; then
  mkdir Q_mediumepsilon
fi
mv *.pkl Q_mediumepsilon



echo "### plots"
python Qepsilon_plots.py
