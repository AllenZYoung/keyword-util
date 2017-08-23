# keyword-util

.py scipts of which the filename start with prefix 'util-' are mainly used for data processing.

# introduction

the logical structure of the .py scripts: 

- to transform all source cases to lowercase letters: **util-lower-source-generator.py**
- to generate nouns and verbs in source cases:**util-nounsandverb-generator-v2.py**
- to select 3 top-ranked words in nouns and verbs (sometimes the base data contains words that's neither verb nor noun):**util-keyword-ranker-v2.py**
- to allocate keywords, part1 of the source, part2 of the source, or all sources (into one file):**util-all-allocate.py**
- to shuffle the data and allocate them: **util-shuffle-allocate.py**
- to seperate data into three sets(train, valid, test): **util-811.py**

None of files of which the filename contains the word 'statistic' or 'counter' is used in generate files.

You may run **util-postag-launcher.py** first before you are ready to run other scripts.
