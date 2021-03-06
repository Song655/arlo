#!/bin/bash

make cleaners

if [ $? -ne 0 ]; then
	exit 1
fi

DATA_DIR=./data
NITER=10
GAIN=0.7
THRESH=0.01
FRACTHRESH=0.001
NSCALES=4
NMOMENTS=3
NX=4096
NY=4096

if [ ! -d $DATA_DIR ]; then
    mkdir $DATA_DIR
fi

ARGS="--data_dir=$DATA_DIR --niter=$NITER --gain=$GAIN --thresh=$THRESH --fracthresh=$FRACTHRESH \
     --nscales=$NSCALES --nmoments=$NMOMENTS --nx=$NX --ny=$NY"

echo "Test Cleaners"
echo "================"
for arg in $ARGS; do
    echo $arg
done
echo "----------------"
python test_cleaners.py $ARGS
#sync; sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
./cleaners $ARGS
rm -rf $DATA_DIR

rm -f cleaners
