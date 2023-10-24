from pyspark import SparkConf, SparkContext

# 创建SparkConf, 初始化配置SparkContext对象
    # 链式调用（只有返回值都相同时才能链式调用）
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 创建SparkContext对象
sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()

