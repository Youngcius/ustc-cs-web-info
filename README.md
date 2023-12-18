# USTC CS Web Info Course Projects

USTC CS Web Information Processing course projects.

## Project 1: Mail Search Engine

This project realized a text search engin based on Enron Email Dataset, with both boolean retrieval and semantic retrieval modes. The former one is constructed based on inverted index and boolean logic, while the latter one is constructed based on vector space model and tf-idf weighting.


See [report](./project1/report.pdf) for detailed techniques and results.


- Requirements

    ```
    nltk
    numpy
    pandas
    scipy
    pytorch
    numba
    ```
    For compatibility, see "requirements.txt" under different project folders for details.

- Dataset: Enron Email Dataset (424 MB), including more than 517,401 text files.
  
    When you use `git clone` to pull this repository, the large-size dataset will be downloaded automatically.
    
    Also, you can manually download from:
    
    ​	Link: https://rec.ustc.edu.cn/share/12edbd70-9d61-11ee-8c53-a1517e796799 
    
    ​	Password: 63si.

### Usage

#### Install dependencies

Some python dependencies and corpora in nltk should be installed first.

```shell
make install
```

#### Decompress dataset

```shell
make data
```

#### Document preprocessing

You can preprocess the dataset and dump processed binary file for later use. Otherwise, the step will be also executed when you run "bool retrieval" or "semantic retrieval" scripts.

```shell
make compile
```


#### Run search engines

Simply use `make bool` or `make semantic` to run the search engine scripts. Then you will enter an interactive search engine environment.

Also, enter [src/](./project1/src/) and run `python bool_search.py` or `python semantic_search.py` to run the scripts and regulate some superparameters.

See details by running `python bool_search.py -h` or `python semantic_search.py -h`.

### Result demonstration

**Construction of `DocumentProcessed` object** (processed all text documents; including inverse-index info and tf-idf matrix) takes about 30 minutes for 50,000 text files.

```
Preprocessing text documents ...
100%|███████████████████████████████████████████████████████████████████████| 50000/50000 [03:12<00:00, 259.09it/s]
Constructing TF sparse matrix ...
100%|████████████████████████████████████████████████████████████████████████| 50000/50000 [21:18<00:00, 39.11it/s]
Constructing inverse index table ...
Constructing TF-iDF matrix ...
Total documents: 50000
DF length: 1000
TF Shape: (1000, 50000)
Inverted List length: 1000
```

**Boolean retrieval example**:

```
(nlp) rose@rose:project1$ make bool
Total documents: 50000
DF length: 1000
TF Shape: (1000, 50000)
Inverted List length: 1000
===============Bool retrieval system for mails===============
'and', 'or', 'not', '(', ')' are available operators for bool query; input '#' to end search action
Input your query command: team and comany or (Enron or results) and performance and price
Results (absolute file path) is/are:
1 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/analyst_meeting_2001/1
2 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/discussion_threads/480
3 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/discussion_threads/3061
4 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/whalley-l/connect_deletes/11
5 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/environmental_issues/66
6 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/shackleton-s/all_documents/11508
7 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/archiving/untitled/5150
8 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/discussion_threads/1441
9 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/discussion_threads/3142
10 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/environmental_issues/62
(There is/are still 699 results not shown)
Input your query command: meeting or english
Results (absolute file path) is/are:
1 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/323
2 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/analyst_meeting_2001/3
3 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/39
4 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/analyst_meeting_2001/1
5 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/performance_management/148
6 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/performance_management/3
7 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/255
8 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/42
9 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/325
10 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/performance_management/147
(There is/are still 10883 results not shown)
Input your query command: meeting and english
There is no document satisfying your query requirement!
Input your query command: #
Query has exited. Thank you for your performance!

```

**Semantic retrieval example**:

```
(nlp) rose@rose:project1$ make semantic 
Total documents: 50000
DF length: 1000
TF Shape: (1000, 50000)
Inverted List length: 1000
===============Bool retrieval system for mails===============
use ' ' separate your query command (tokens) ; input '#' to end search action
Input your query command: during the beta test period
Results (absolute file path) is/are:
1 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/personal/108
2 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/california/248
3 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/archiving/untitled/5429
4 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/discussion_threads/2822
5 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/calendar/untitled/7934
6 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/kean-s/all_documents/5430
7 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/shackleton-s/all_documents/3951
8 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/cash-m/inbox/192
9 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/shackleton-s/inbox/963
10 /home/rose/git-projects/ustc-courses/tmp/ustc-cs-web-info/project1/dataset/maildir/shackleton-s/confirms___paper___pulp/15
(There is/are still 49990 results not shown)
Input your query command: #
Query has exited. Thank you for your performance!

```


## Project 2: Named Entity Recognition

Named Entity Recognition task with LSTM deep learning approach.


## Project 3: Recommender System

This project realized a recommending score system, using the model-based rating prediction (SVD) and memory-based rating prediction (collaborative filtering) methods, respectively.

**Requirements**:

```
numpy
pandas
scipy
matlibplot
pytorch
numba
```

Herein "numba" library is used to accelerate calculation.

Usage of the program is like (see argument details by running `python main.py -h` in [src/](./project2/src/):

```shell
python main.py -svd -f 5 -lam 0.001 -n -e 6
```

It will take around 30 minutes construct preprocessed data structures, when initially executing.

After intermediate data structures and subsequent prediction results when will be dumped in [output/](./project3/output/) folder.

See [report](./project2/report.pdf) for detailed techniques and results.
