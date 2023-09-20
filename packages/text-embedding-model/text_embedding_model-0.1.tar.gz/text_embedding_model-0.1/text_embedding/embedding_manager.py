import os 
import certifi
import numpy as np
import openai
from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingManager:
    """
    Choose embedding method (eg. tfidf ...) to transform text-based data into vectors for further applications.
    """
    NGrams = 3
    MaxFeatures = 2000
    api_key = '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'
    def __init__(self, text: str): 
        """
        Initialize embedding process.

        :param text: the text string to embed.
        :type text: str
        """
        self.text = text

    def ngrams(self, string: str) -> list:
        """
        Tokenizes chars in a raw text, and returns group successive chars based on n.

        :return: list of groups of successive chars
        :rtype: list
        """
        ngrams = zip(*[string[i:] for i in range(int(self.NGrams))])
        return [''.join(ngram) for ngram in ngrams]
    
    def tfidf_embedding(self, use_ngram: bool = True, max_features: int = int(MaxFeatures)):
        """
        Returns embedded document-term matrix by TFIDF model
        Reference: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

        :parm use_ngram: bool. whether the feature should be made of word or character n-grams.
        :parm max_features: int. default to build a vocabulary considering the top 2000 ordered by term frequency across the corpus.

        :return: Tf-idf-weighted embedding vector of shape (n_samples, n_features)
        :rtype: np.ndarray

        """
        if use_ngram:
            vectorizer = TfidfVectorizer(max_features=max_features, analyzer=self.ngrams)
        else:
            vectorizer = TfidfVectorizer(max_features=max_features)
        embedding = vectorizer.fit_transform(self.text)

        return embedding.toarray()

    def openai_embedding(self, model: str ='text-embedding-ada-002') -> np.ndarray:
        """
        Returns text embedded by OpenAI's embedding models as (1536,) NumPy arrays (using default model).
        By default the ADA-002 model is used, by OpenAI's recommendation.
        The cost as at 2023-08-02 is US$0.0001 per 1,000 tokens, where on average, 4 characters cost 1 token.
        Reference: https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

        :param model: str. OpenAI embedding model, other models are not recommended due to cost and performance

        :return: embedding vector of shape (X, 1536), X: the number of the text to embed
        :rtype: np.ndarray
        """
        # Paste certifi into the path where certifi.where() indicates
        # os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
        openai.api_key = self.api_key

        docs = self.text.tolist()
        embedding = openai.Embedding.create(input=docs, model=model)

        embedding_list = []
        for i in range(len(docs)):
            embedding_list.append(embedding['data'][i]['embedding'])

        return np.array(embedding_list)

 
    def embedding(self):
        """
        More embedding methods to be added, and user could choose proper ones by typing in coressponding number accordingly.
        {1: 'tfidf',
         2: 'openai'}

        :return: embedded vector.
        :rtype: np.ndarray
        """
        embedding_method = input("Please type corresponding number for following embedding methods: \n {1: 'tfidf', 2: 'openai'}, and hit 'Enter'")
        match embedding_method:
            case '1':
                return self.tfidf_embedding()
            case '2':
                return self.openai_embedding()
            case _:
                print("Please type corresponding number for following embedding methods: \n {1: 'tfidf', 2: 'openai'}, and hit 'Enter")
                return self.embedding()