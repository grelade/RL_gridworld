#!/bin/sh
SIMPATH='../../RL_gridworlds.py'
SETTINGS=''
PARAMS='-m sarsalambda --envtype windy.txt -n 600 -a 0.1 -g 1 -e 0.1 -de --nogui'

echo "### S1: SARSA(LAMBDA) with varied LAMBDA"

echo "### SARSA(LAMBDA=0.1)"
python $SIMPATH $PARAMS -l 0.1
if [ ! -d "sarsa_lambda=0.1" ]; then
  mkdir sarsa_lambda=0.1
fi
mv *.pkl sarsa_lambda=0.1
echo "### SARSA(LAMBDA=0.1t completed"



echo "### SARSA(LAMBDA=0.2)"
python $SIMPATH $PARAMS -l 0.2
if [ ! -d "sarsa_lambda=0.2" ]; then
  mkdir sarsa_lambda=0.2
fi
mv *.pkl sarsa_lambda=0.2
echo "### SARSA(LAMBDA=0.2) completed"



echo "### SARSA(LAMBDA=0.4)"
python $SIMPATH $PARAMS -l 0.4
if [ ! -d "sarsa_lambda=0.4" ]; then
  mkdir sarsa_lambda=0.4
fi
mv *.pkl sarsa_lambda=0.4
echo "### SARSA(LAMBDA=0.4) completed"



echo "### SARSA(LAMBDA=0.5)"
python $SIMPATH $PARAMS -l 0.5
if [ ! -d "sarsa_lambda=0.5" ]; then
  mkdir sarsa_lambda=0.5
fi
mv *.pkl sarsa_lambda=0.5
echo "### SARSA(LAMBDA=0.5) completed"



echo "### SARSA(LAMBDA=0.7)"
python $SIMPATH $PARAMS -l 0.7
if [ ! -d "sarsa_lambda=0.7" ]; then
  mkdir sarsa_lambda=0.7
fi
mv *.pkl sarsa_lambda=0.7
echo "### SARSA(LAMBDA=0.7) completed"



echo "### SARSA(LAMBDA=0.8)"
python $SIMPATH $PARAMS -l 0.8
if [ ! -d "sarsa_lambda=0.8" ]; then
  mkdir sarsa_lambda=0.8
fi
mv *.pkl sarsa_lambda=0.8
echo "### SARSA(LAMBDA=0.8) completed"



echo "### SARSA(LAMBDA=0.9)"
python $SIMPATH $PARAMS -l 0.9
if [ ! -d "sarsa_lambda=0.9" ]; then
  mkdir sarsa_lambda=0.9
fi
mv *.pkl sarsa_lambda=0.9
echo "### SARSA(LAMBDA=0.9) completed"





echo "### plots"
python SARSA_lambda_plots.py
