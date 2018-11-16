# IP518bb QUizGenerator

Repository for the practical part of IP518bb QuizGenerator. Consists of an iPython notebook and associated functions/vendors/etc

**This application serves a research/educational purpose only! All texts belong to their respective owners!**

## Getting started

1. **Installing dependencies**

Install the following packages:

 -  Pattern.de : https://www.clips.uantwerpen.be/pattern
 -  nltk : https://www.nltk.org/install.html
 -  numpy : https://docs.scipy.org/doc/numpy/user/install.html
 -  Stanford core nlp: https://pypi.org/project/stanfordcorenlp/
 -  TextBlob : https://textblob.readthedocs.io/en/dev/
 -  StandfordCoreNLP server version 2018-02-27 (Needs to be put into `vendor/stanford-corenlp-full-2018-02-27/`)

2. **Start the Stanford Core CLP server**

From project root, execute:

```
cd vendor/stanford-corenlp-full-2018-02-27/
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000
```

3. **Start the IPython notebook**

From project root, execute:

```
jupyter-notebook ./IP518bb_QuizGenerator.ipynb
```

4. **Execute the code**

Within jupyter notebook, click `Cell -> Run all`. As the CoreNLP server is likely not trained yet, it might take a few minutes to execute everything.

## Or:

Execute `start.sh`
