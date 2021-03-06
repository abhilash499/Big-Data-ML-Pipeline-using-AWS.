# Big-Data-ML-Pipeline-using-AWS.


This story represents an easy way for beginners to build an end to end pipeline for Collecting, Pre-Processing both Static/Streaming data, Build, Deploy, Monitor and Infer Real Time Machine Learning Model. Here three independent cases are used for depicting the pipeline, but similar steps can be used for a single use case to built an end to end Big Data and Machine Learning Pipeline.

Static data is collected from Freddie Mac Single Family Loan Level dataset having more than one billion records of size greater than 80 GB. EMR and Hive is used to collect and pre-process data. Processed data is then loaded to S3 for Machine Learning. Along with S3, Processed data is also loaded to SQL and Redshift from where it can be used to build Reports and Dashboards. 

Streaming data is collected from a live data generator. Live data is consumed using Kinesis Data Stream. Kinesis Data Analytics is used for Real Time data analysis and Transformation using SQL. Lambda is used in next step for data transformation and FireHose to write final data to S3. Similar pipeline can be used for Server Log analysis or Twitter analysis.

As part of ML , an Image Classifier is Trained, Built and Deployed to classify an image in real time using AWS SageMaker. A front end web app is also developed for real time inference from outside AWS using Flask.

Please visit the link https://medium.com/@abhilash.mohapatra25/big-data-ml-pipeline-using-aws-533dc9b9d774 for more information.
