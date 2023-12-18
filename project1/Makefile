DATAPATH	= dataset
OUTPUTPATH	= output

all: data install compile


data: # decompress enron mail data
	@cd $(DATAPATH) && if [ -d "maildir/" ]; then \
        echo "maildir/ folder already exists."; \
    else \
        echo "decompressing mail data to maildir/"; tar -xzf enron_mail_20150507.tar.gz; \
    fi

install: # install python dependencies
	@pip install -r requirements.txt
	@python -c "import nltk; nltk.download('punkt')"
	@python -c "import nltk; nltk.download('stopwords')"
	@python -c "import nltk; nltk.download('wordnet')"

compile: # text dataset preprocessing
	@mkdir -p $(OUTPUTPATH)
	@cd ./src/ && python preprocessing.py -i ../$(DATAPATH) -o ../$(OUTPUTPATH)

bool: # boolean retrieval
	@cd ./src/ && python bool_search.py -i ../$(DATAPATH) -o ../$(OUTPUTPATH)

semantic: # semantic retrieval
	@cd ./src/ && python semantic_search.py -i ../$(DATAPATH) -o ../$(OUTPUTPATH)

