#!/bin/bash
sysbench  --num-threads=16 --test=fileio  --file-total-size=1G  --file-test-mode=seqrewr prepare
sysbench  --num-threads=16 --test=fileio  --file-total-size=1G  --file-test-mode=seqrewr run
sysbench  --num-threads=16 --test=fileio  --file-total-size=1G  --file-test-mode=seqrewr cleanup