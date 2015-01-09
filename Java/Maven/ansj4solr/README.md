# Ansj2.0.7对Solr4.9的支持

可以执行mvn package打项目包 再拷贝lib里的两个ansj包（一共三个）作为solr分词所需的第三方依赖。

也可以执行mvn assembly:assembly 把zip里的三个包拿出来。

目录结构:

```tree
├── lib
│   ├── ansj_seg-2.0.7.jar
│   ├── nlp-lang-0.3.jar
│   └── tree_split-1.4.jar
├── LICENSE
├── pom.xml
├── README.md
├── src
    └── main
        ├── assembly
        │   └── zip.xml
        └── java
            └── org
                └── ansj
                    └── solr
                        ├── AnsjTokenizerFactory.java
                        ├── AnsjTokenizer.java
                        ├── TestAnsj.java
                        └── UpdateKeeper.java
```

其中lib目录下有3个jar包，ansj_seg-*.jar和tree_split-*.jar是本工程直接依赖的，而nlp-lang-*.jar则是ansj依赖的，功能强大，需要在使用时导入同时导入lib库内。

## Solr配置如下:

在schema.xml中配置tokenizerfactory

     <fieldType name="text_cn" class="solr.TextField" positionIncrementGap="100">
     <analyzer type="index">
       <tokenizer class="org.ansj.solr.AnsjTokenizerFactory" conf="ansj.conf"/>
     </analyzer>
    	 <analyzer type="query">
       <tokenizer class="org.ansj.solr.AnsjTokenizerFactory" analysisType="1"/>
     </analyzer>
       </fieldType>


说明一下： 

1.

conf="ansj.conf" 这个tokenizerfactory需要的配置，里面是个properties格式的配置：

    lastupdate=123
    files=extDic.txt,aaa.txt

其中lastupdate 是一个数字，只要这次比上一次大就会触发更新操作，可以用时间戳 files是**用户词库文件**，以**英文逗号**隔开

conf配置只要在一个地方配置上了，整个索引使用的ansj都会启用定时更新功能，切词库是schema内共享的。这里和IK的设置是一致的。

2.

analysisType: 分词类型

- "0": 默认值，代表索引切分 IndexAnalysis
- "1": 标准切分 ToAnalysis
- "2": 自然语言切分 NlpAnalysis
- "3": 基本分词 BaseAnalysis

3.

rmPunc="false" 表示不去除标点符号。默认不写是true，表示去掉标点符号。
