#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.job.name=epl_agg \
-D mapred.reduce.tasks=1 \
-D mapred.output.compress=true \
-D mapred.output.compression.type=BLOCK \
-D mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec \
-files /home/jejoseph/epl/mapper.py,/home/jejoseph/epl/reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /user/jejoseph/epl_data.txt \
-output /user/jejoseph/results/