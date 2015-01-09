# docTrain介绍

docTrain根据lucene的classification的Bayes算法，实现了可以自动对新添加文档根据训练数据库的分类内容进行分类。

目前使用的分词器是IKAnalyze，但是其已经停止开发，而ANSJ发展势头比较好，以后在数据训练上也会使用ANSJ，**需要注意的是训练和对新文档分类时必须选用相同的分词器**



## 目录树：

```tree
├── lib
│   └── IKAnalyzer2012FF_u1.jar
├── pom.xml
├── readme.md
└── src
    ├── main
    │   └── java
    │       └── neu
    │           └── autoClassify
    │               ├── App.java
    │               ├── CategorizationUpdateRequestProcessorFactory.java
    │               ├── CategorizationUpdateRequestProcessor.java
    │               └── DocAnalyzer.java
    └── test
        └── java
            └── neu
                └── autoClassify
                    └── AppTest.java
```

## 目录树说明：

test目录目前没有做任何test，以后应该增加对训练内容的正确率测试，但是因为测试时间比较长，影响做包时间。

App.java：用来对训练数据库做正确度测试的（训练数据找的越好，正确率越高越好，目前的训练数据大部分来自新华网新闻，但由于我们的分类较粗，在训练数据选择方面很难保证较高的正确率，建议将分类细化）

CategorizationUpdateRequestProcessorFactory和CategorizationUpdateRequestProcessor，实现的是Solr接口，用来在添加新文件时，自动添加分类。

DocAnalyzer：没有什么太大价值，主要被App调用的，初始化IndexDB和用Bayes分析分类的。

## 使用：

```
mvn package
```

生成动态jar包

```
mvn assembly:assembly
```

生成可执行的jar包，可以对IndexDB进行测试，（由于没有把IKAnalyzer安装至maven，所以需要手动把IKAnalyzer的classes拷贝进生成的jar包里）

```
java -jar target/docTrain-1.0-SNAPSHOT-jar-with-dependencies.jar
```

## TODO

分词器改为ANSJ


