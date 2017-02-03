#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a|--algo)
    ALGO_NUM="$2"
    shift
    ;;
    -e|--ex_path)
    EX_PATH="$2"
    shift
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

python2 ./src/algo.py $EX_PATH $ALGO
