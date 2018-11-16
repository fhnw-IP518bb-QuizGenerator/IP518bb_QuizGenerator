#!/bin/sh

cd vendor/stanford-corenlp-full-2018-02-27/
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000 &
cd ../../
sudo jupyter-notebook ./IP518bb_QuizGenerator.ipynb --allow-root