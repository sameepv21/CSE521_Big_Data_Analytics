!apt-get update

!apt-get install openjdk-8-jdk-headless -qq > /dev/null

!wget -q https://www-us.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop2.7.tgz

!tar xf spark-3.1.1-bin-hadoop2.7.tgz

pip install -q findspark

import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"

os.environ["SPARK_HOME"] = "/content/spark-3.1.1-bin-hadoop2.7"

import findspark

findspark.init()

findspark.find()

from pyspark.sql import SparkSession

spark = SparkSession.builder\
.master("local")\
.appName("user_info")\
.config('spark.ui.port', '4050')\
.getOrCreate()

spark

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

!unzip ngrok-stable-linux-amd64.zip

get_ipython().system_raw('./ngrok http 4050 &')

!curl -s http://localhost:4040/api/tunnels

import csv
import pyspark.sql.functions as fn
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import explode
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure

from google.colab import drive
drive.mount('/content/drive')

df=spark.read.csv(r"/content/drive/MyDrive/BDP-user/intluserdata_csv.csv", header=True)
df.createOrReplaceTempView("userData")

df.head()

df

df.count()

df.write.option("header", "true").csv("user.csv")

df=df.dropDuplicates()

df.count()

df.groupBy(df.columns).count().where(fn.col('count')>1).select(fn.sum('count')).show()

df =df.fillna(value={})

spark.sql("select `Tweets`, `Screen Name`, Location from userData ORDER BY `Tweets` desc limit 25" ).show(100)

q1= spark.sql("select count(*) as NumberOfTweets, 'TRUE' from userData where Verified like '%T%' UNION select count(*) as NumberOfTweets, 'FALSE' from userData where Verified like '%F%' ")

pd1 = q1.toPandas()
print(pd1)
pd1.plot.pie(y='NumberOfTweets', labels=['FALSE', 'TRUE'], autopct='%.2f', figsize=(5, 5),
                  title="Source of Tweets").figure

#query2 = spark.sql("select count(*) as count,`Media Type` as MediaType from stuData where `Media Type` is not null group by `Media Type` order by count desc")
#print(query2)
#pd2 = query2.toPandas()
#pd2.plot(kind="bar", x="MediaType", y="count", title="Different souces of Media used").figure

query2 = spark.sql("select count(*) as count, '2017' as Year from userData where UTC like '%2017%' UNION select count(*) as count,'2018' as Year from userData where UTC like '%2018%' UNION select count(*) as count,'2019' as Year from userData where UTC like '%2019%' UNION select count(*) as count,'2020' as Year from userData where UTC like '%2020%' UNION select count(*) as count, '2021' as Year from userData where UTC like '%2021%' ")
print(query2)
pd2 = query2.toPandas()
pd2.plot(kind="bar", x="Year", y="count", title="Year of tweet").figure

query4 = spark.sql("select count(*) as count, 'United States' as Year from userData where Location like '%US%' UNION select count(*) as count,'Canada' as Year from userData where Location like '%Can%' UNION select count(*) as count,'Australia' as Year from userData where Location like '%Aus%' UNION select count(*) as count,'India' as Year from userData where Location like '%Ind%' UNION select count(*) as count, 'China' as Year from userData where Location like '%Chi%' ")
print(query4)
pd2 = query4.toPandas()
pd2.plot(kind="bar", x="Year", y="count", title="Year of tweet").figure

