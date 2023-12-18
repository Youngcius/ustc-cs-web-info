DATAPATH	= ./dataset

all: data compile


data: # decompress enron mail data
	@cd $(DATAPATH) && if [ -d "maildir/" ]; then \
        echo "maildir/ folder already exists."; \
    else \
        echo "decompressing mail data to maildir/"; tar -xzf enron_mail_20150507.tar.gz; \
    fi

compile: # text dataset preprocessing
	...

bool: # boolean retrieval
	...

semantic: # semantic retrieval
	...

