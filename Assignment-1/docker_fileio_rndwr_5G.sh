#!/bin/bash
sysbench  --num-threads=16 --test=fileio  --file-total-size=5G  --file-test-mode=rndwr prepare
sysbench  --num-threads=16 --test=fileio  --file-total-size=5G  --file-test-mode= rndwr run
sysbench  --num-threads=16 --test=fileio  --file-total-size=5G  --file-test-mode= rndwr cleanup