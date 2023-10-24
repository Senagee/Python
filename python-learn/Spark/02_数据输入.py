# RDD对象： 数据计算的载体类似于数据容器，内置许多数据计算的方式


from pyspark import SparkConf, SparkContext

# 创建SparkConf, 初始化配置SparkContext对象
    # 链式调用（只有返回值都相同时才能链式调用）
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 创建SparkContext对象
sc = SparkContext(conf=conf)

# 创建RDD对象（输入数据到Spark） 有两种方式
    # sc.parallelize(数据容器)： 将Python数据容器转换为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6])
rdd2 = sc.parallelize((1, 2, 3, 4, 5, 6))
rdd3 = sc.parallelize("123456")
rdd4 = sc.parallelize({1, 2, 3, 4, 5, 6})
rdd5 = sc.parallelize({1: 2, 3: 4, 5: 6})
    # sc.textFile("path")：读取文本文件得到RDD对象
rdd6 = sc.textFile("write_test.text")

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())
print(rdd6.collect())

sc.stop()