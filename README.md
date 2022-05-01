
# CSE521 BIG DATA ANALYTICS

**Instructor : Prof. Amit Ganatra**
**Teaching Assistant: Manav Vaghrecha**


### International Student Data Analysis using Big Data.

- Samkit Kundalia (AU1940021)

- Sameep Vani (AU1940049)

- Malav Doshi (AU1940017)

##  PROBLEM STATEMENT 
This project focuses on extraction of dataset (Twitter Data) from the Twitter API regarding all the information related to international students and using different tools like Hive, Hue, Scala, pySpark, Spark SQL and Solr to show different aspects of the data in a visualization form using Tableau and Seaborn.

## SOLUTION
Big data tools help to analyze the huge data which helps to provide efficient results. The sentimental analysis provides a brief understanding of various challenges that international students are currently facing and impact of covid-19 on the visa assurance. Finally, we are using Spark using python and Scala for writing the queries by visualizing with Seaborn and Tableau.

## DATA ANALYSIS
We have extracted dataset using twitter API, these datasets are extracted using different hashtags focusing on different events related to international students, dividing the events and dataset is crucial since we want this project to be informational and focus on different aspects through different datasets. We will use sentiment analysis on the text (tweet) and use different queries to extract important features and visualize them in Tableau.

#### Data Collection

![image](https://user-images.githubusercontent.com/78001524/117752544-95dad480-b1dc-11eb-97c9-8072ac64d9e7.png)

## IMPLEMENTATION:
## Spark using Scala


**1. Starting the scala using spark-shell command.**

![image](https://user-images.githubusercontent.com/78001524/117360257-2bddca80-ae7e-11eb-87f5-9768655ebab6.png)

**2. Load the 'dat1.json' into a  data frame using sqlContext.read.json()**

![image](https://user-images.githubusercontent.com/78001524/117360378-562f8800-ae7e-11eb-89f6-f6fd366c76b1.png)

**3. Schema of the dataset.**

![image](https://user-images.githubusercontent.com/78001524/117360818-d9e97480-ae7e-11eb-88c3-eb3c7d3b6a44.png)

**4. Display the Username and Text of top 20 tweets.**

![image](https://user-images.githubusercontent.com/78001524/117361618-e15d4d80-ae7f-11eb-88db-74f5a08afe17.png)

**5. Count the number of Media Types present in the dataset.**

![image](https://user-images.githubusercontent.com/78001524/117365899-9e05dd80-ae85-11eb-809e-1f1b79365487.png)

**6. Fetching the different languages in which the tweets are made about international students.**

![image](https://user-images.githubusercontent.com/78004048/117381384-918f7e00-aea1-11eb-99c4-4efface7a84f.png)

**7. Fetching users with a greater number of hashtags in their tweets on student data.**

![image](https://user-images.githubusercontent.com/78004048/117386048-cf919f80-aeab-11eb-8527-f4cd7a0e9311.png)

**8. Fetching users who have more followers and are tweeting based on student data.**

![image](https://user-images.githubusercontent.com/78004048/117383124-a110c600-aea5-11eb-8d15-641763382fbc.png)

**9. Fetching users with a greater number of mentions in their tweets on student data.**

![image](https://user-images.githubusercontent.com/78004048/117386084-de785200-aeab-11eb-892a-5cc10a8ed1ab.png)

**10. Fetching users having account names with a greater number of tweets on web series.**

![image](https://user-images.githubusercontent.com/78004048/117385130-0ff01e00-aeaa-11eb-9ec2-2828a5591f42.png)

**11. Fetching users with a greater number of retweets for their tweets on student data**.

![image](https://user-images.githubusercontent.com/78004048/117385526-eedbfd00-aeaa-11eb-8e43-9a4a437b05e9.png)

## HIVE:

**Created the database and database table in hive and loaded the data into hive table for AbolishICE dataset:**

![image](https://user-images.githubusercontent.com/78001524/117753860-d2a7cb00-b1de-11eb-916f-63023ea5b999.png)
![image](https://user-images.githubusercontent.com/78001524/117753864-d50a2500-b1de-11eb-987a-e36760404a82.png)

**Created the database and database table in hive and loaded the data into hive table for F1visa dataset:**
**Visualized the output:**
 
![image](https://user-images.githubusercontent.com/78001524/117753868-d9364280-b1de-11eb-91a9-ca06930b395a.png)

**Created the database and database table in hive and loaded the data into hive table for h1b dataset:**
**Visualized the output:**

![image](https://user-images.githubusercontent.com/78001524/117753876-dfc4ba00-b1de-11eb-8316-806a41b708ec.png)


**Created the database and database table in hive and loaded the data into hive table for intlstudents dataset:**
**Visualized the output:**

![image](https://user-images.githubusercontent.com/78001524/117753886-e4896e00-b1de-11eb-938f-c50d8490f6ac.png)


**Created the database and database table in hive and loaded the data into hive table for study in USA dataset:**
**Visualized the output:**

![image](https://user-images.githubusercontent.com/78001524/117753893-e8b58b80-b1de-11eb-9855-0e00c3785713.png)


**Imported file into hdfs**

![image](https://user-images.githubusercontent.com/78001524/117753900-ec491280-b1de-11eb-90ae-58d436106f24.png)
![image](https://user-images.githubusercontent.com/78001524/117753906-efdc9980-b1de-11eb-83f2-2784e1cb2a93.png)

**Created the database and database table in hive and loaded the data into hive table for General dataset:**

![image](https://user-images.githubusercontent.com/78001524/117753942-fc60f200-b1de-11eb-9409-68969c160e02.png)
![image](https://user-images.githubusercontent.com/78001524/117753952-ff5be280-b1de-11eb-8319-f31748909e19.png)

**Visualized the Output:**
![image](https://user-images.githubusercontent.com/78001524/117753963-02ef6980-b1df-11eb-8fe3-eaca74514032.png)

## RESULTS EVALUATION:

![image](https://user-images.githubusercontent.com/78001524/117753738-9bd1b500-b1de-11eb-8c23-649d6091ceae.png)



![image](https://user-images.githubusercontent.com/78001524/117753743-9ffdd280-b1de-11eb-8223-913fee39f2f4.png)



![image](https://user-images.githubusercontent.com/78001524/117753753-a429f000-b1de-11eb-82d5-e551dc149010.png)



![image](https://user-images.githubusercontent.com/78001524/117753763-a8560d80-b1de-11eb-8171-4aeae086d133.png)



![image](https://user-images.githubusercontent.com/78001524/117753773-ac822b00-b1de-11eb-9837-3679b19c300f.png)

Fig. Plotting top words from Text data


![image](https://user-images.githubusercontent.com/78001524/117753802-b9068380-b1de-11eb-8887-2dcd4e6e5633.png)

Fig. Word Cloud generation using Texthero


![image](https://user-images.githubusercontent.com/78001524/117753825-bf94fb00-b1de-11eb-9aee-fcdef97508e3.png)

Fig. Scatter Plot of PCA and k-means cluster analysis