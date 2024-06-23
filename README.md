# lab_spark
## 1DataNode
**Запуск выполняется следующими командами:**
```
docker-compose -f docker-compose.yml up -d
docker cp ./data/Master_Ranked_Games.csv namenode:/
docker cp ./scripts/HDFS.sh namenode:/
docker exec -it namenode bash HDFS.sh
docker cp ./scripts/spark_not_opt.py spark-master:/
docker cp ./scripts/spark_opt.py spark-master:/
docker cp ./scripts/Spark.sh spark-master:/
docker exec -it spark-master bash Spark.sh
docker cp spark-master:/res_not_opt.txt ./results/res_not_opt-docker1.txt
docker cp spark-master:/res_opt.txt ./results/res_opt-docker1.txt
docker-compose -f docker-compose.yml down
```
## 3DataNode
**Запуск выполняется следующими командами:**
```
docker-compose -f docker-compose-3.yml up -d
docker cp ./data/Master_Ranked_Games.csv namenode:/
docker cp ./scripts/HDFS.sh namenode:/
docker exec -it namenode bash HDFS.sh
docker cp ./scripts/spark_not_opt.py spark-master:/
docker cp ./scripts/spark_opt.py spark-master:/
docker cp ./scripts/Spark.sh spark-master:/
docker exec -it spark-master bash Spark.sh
docker cp spark-master:/res_not_opt.txt ./results/res_not_opt-docker3.txt
docker cp spark-master:/res_opt.txt ./results/res_opt-docker3.txt
docker-compose -f docker-compose-3.yml down
```