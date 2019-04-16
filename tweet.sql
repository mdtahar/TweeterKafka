DROP TABLE tweets;
ADD JAR hdfs:///user/json-serde-1.3.8-jar-with-dependencies.jar;
set hive.support.sql11.reserved.keywords=false;
CREATE external table tweets ( text STRING, user STRUCT <screen_name:STRING,friends_count:INT,followers_count:INT>,retweeted_status STRUCT <retweet_count:INT,favorite_count:INT> ) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION '/user/admin/';
