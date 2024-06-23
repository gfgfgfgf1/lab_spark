#!/bin/bash

hdfs dfs -mkdir /data/
hdfs dfs -D dfs.block.size=32M -put /Master_Ranked_Games.csv /data/
hdfs dfsadmin -setSpaceQuota 5g /
exit