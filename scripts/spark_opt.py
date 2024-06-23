import numpy as np
import os
import psutil
import time
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession 
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler 
from pyspark.ml.classification import GBTClassifier 

time_start = time.time()

SparkContext.getOrCreate(SparkConf().setMaster('spark://spark-master:7077')).setLogLevel("INFO")
spark = SparkSession.builder.master("spark://spark-master:7077").appName("practice").getOrCreate() 

data = spark.read.format("csv").option("header", "true").option('inferSchema', 'true').load("hdfs://namenode:9000/data/Master_Ranked_Games.csv") 
data.cache()
data = data.repartition(4)

for col in ['redWins','redFirstBlood','redFirstTower','redFirstBaron','redFirstDragon','redFirstInhibitor','redDragonKills','redBaronKills','redTowerKills','redInhibitorKills','redWardPlaced','redWardkills','redKills','redDeath','redAssist','redChampionDamageDealt','redTotalGold','redTotalMinionKills','redTotalLevel','redAvgLevel','redJungleMinionKills','redKillingSpree','redTotalHeal', 'redObjectDamageDealt']:
  data = data.drop(col)

features = ['gameId','gameDuraton','blueFirstBlood','blueFirstTower','blueFirstBaron','blueFirstDragon','blueFirstInhibitor','blueDragonKills','blueBaronKills','blueTowerKills','blueInhibitorKills','blueWardPlaced','blueWardkills','blueKills','blueDeath','blueAssist','blueChampionDamageDealt','blueTotalGold','blueTotalMinionKills','blueTotalLevel','blueAvgLevel','blueJungleMinionKills','blueKillingSpree','blueTotalHeal','blueObjectDamageDealt']
assembler = VectorAssembler(inputCols=features, outputCol='features_vectorized') 
data = assembler.transform(data) 

data_train, data_test = data.randomSplit([0.7, 0.3]) 

data_train.cache()
data_train = data_train.repartition(4)
data_test.cache()
data_test = data_test.repartition(4)

model = GBTClassifier(featuresCol="features_vectorized", labelCol="blueWins", maxBins=700) 
model = model.fit(data_train) 


pred_test = model.transform(data_test)

time_res = time.time() - time_start
RAM_res = psutil.Process(os.getpid()).memory_info().rss / (float(1024)**2)

spark.stop()

with open('/res_opt.txt', 'a') as f:
    f.write("Time: " + str(time_res) + " seconds, RAM: " + str(RAM_res) + " Mb.\n")
