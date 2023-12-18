import pickle
import os
import argparse
import warnings
from retriever import DocumentProcessed

DOCUMENT_NAME = 'document.pk'

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    parser = argparse.ArgumentParser(description='Bool search')
    parser.add_argument('-i', '--data_path', default='../dataset', type=str, help='set the data directory')
    parser.add_argument('-o', '--output_path', default='../output', type=str, help='set the output directory')
    args = parser.parse_args()
  
    # documents preprocessing: tokenization, stop words removal, stemming, etc.
    if DOCUMENT_NAME not in os.listdir(args.output_path):
        document = DocumentProcessed(in_path=args.data_path)
        document.attr_show()
        with open(os.path.join(args.output_path, DOCUMENT_NAME), 'wb') as f:
            pickle.dump(document, f)
    else:
        print('{} already exists!'.format(DOCUMENT_NAME))
