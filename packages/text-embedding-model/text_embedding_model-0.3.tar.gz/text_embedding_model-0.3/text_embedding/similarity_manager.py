import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityManager:
    """
    Calculate the similarity between raw text and referemce text using embedding vector.
    """
    def __init__(self, is_labelled: bool):
        """Initialize the similarity calculation

        :param is_labelled: whether the text has reference (labelled) text to compare with.
        :type is_labelled: bool
        """
        self.is_labelled = is_labelled

    def get_cos_similarity(self, df_input: pd.DataFrame, embedding: np.ndarray)-> pd.DataFrame:
        """
        Calculate the consine similarity between raw text and referemce text using embedding vector.
        Each cell stands for the similarity score, the higher, the more similar.
        
        :param pd.DataFrame df_input: the raw dataframe with text to calculate similarity.
        :param np.ndarray embedding: embedding measures the relatedness of text.

        :return: cosine similarity score matrix dateframe.
        :rtype: pd.DataFrame
        """
        text = df_input['raw_text']

        if self.is_labelled:
            cutoff_value = df_input.loc[df_input['flag'] == 1, 'raw_text'].shape[0]
            cos_similarity = cosine_similarity(embedding[:cutoff_value], embedding[cutoff_value:])
            df_cos_similarity = pd.DataFrame(cos_similarity, index=list(text)[:cutoff_value], columns=list(text)[cutoff_value:])
        else:
            cos_similarity = cosine_similarity(embedding)
            df_cos_similarity = pd.DataFrame(cos_similarity, index=list(text), columns=list(text))
        
        return df_cos_similarity
    

    def get_topn_similar_comment(self, df_input: pd.DataFrame, df_similarity: pd.DataFrame, n :int = 5, retrieve_index :bool = False) -> pd.DataFrame:

        """
        Pick the compared text with topN similarity score under each raw text row, and generate a dataframe
        column 1: raw text
        column 2: topN similar text 
        column 3: topN similarity scores

        :param df_input: raw text dataframe to retrieve recordID back.
        :type df_input: pd.DataFrame
        :param df_cos_similarity: similarity score matrix dateframe.
        :type df_cos_similarity: pd.DataFrame
        :param n: topN most similar text, default as 5.
        :type n: int
        :return: topN most similar text dateframe.
        :type retrive_index: bool
        """
    
        df_topn_similar_comments = pd.DataFrame(columns=['raw_text',f'top{n}_similar_text', f'top{n}_similarity_score'])

        df_similarity_transpose = df_similarity.T

        for i in df_similarity.index:

            nlargest_scores = df_similarity_transpose[i].sort_values(ascending=False).head(n).tolist()
            nlargest_texts = df_similarity_transpose[i].sort_values(ascending=False).head(n).index.tolist()

            df_new_row = pd.DataFrame({ 'raw_text': [i], f'top{n}_similar_text': [nlargest_texts], f'top{n}_similarity_score': [nlargest_scores]})

            df_topn_similar_comments = pd.concat([df_topn_similar_comments, df_new_row], ignore_index=True)
        
        if retrieve_index:
            
            base_index_dict = dict(zip(df_input[df_input['flag'] == 1]['raw_text'], df_input[df_input['flag'] == 1]['RecordID']))
            similarity_index_dict = dict(zip(df_input[df_input['flag'] == 0]['raw_text'], df_input[df_input['flag'] == 0]['RecordID']))
        
            for row in df_topn_similar_comments.itertuples():
                index_list = []
                for i in row[2]:
                    index_list.append(str(similarity_index_dict[i]))
                index_list = '-'.join(index_list)
                df_topn_similar_comments.at[row.Index, 'similar_text_recordID'] = index_list
                df_topn_similar_comments.at[row.Index, 'raw_text_recordID'] = str(base_index_dict[row.raw_text])
                df_topn_similar_comments = df_topn_similar_comments[['raw_text', f'top{n}_similar_text', f'top{n}_similarity_score', 'similar_text_recordID']]
                
                return df_topn_similar_comments
        
        df_topn_similar_comments[f'top{n}_similar_text'] = df_topn_similar_comments[f'top{n}_similar_text'].str.join(',')
        df_topn_similar_comments = df_topn_similar_comments[['raw_text', f'top{n}_similar_text', f'top{n}_similarity_score']]

        return df_topn_similar_comments
    

    def retrieve_similar_text(self, df_similarity: pd.DataFrame, threshold: float) -> dict:
        """
        Get the similar text associated with the raw text based on similarity score threshold. (Usually pick a float greater than 0.7)

        :param df_cos_similarity: similarity score matrix dateframe.
        :type df_cos_similarity: pd.DataFrame
        :param threshold: similarity score threshold
        :type threshold: float
        :return: {'raw_text': [similar text 1, similar text 2]}
        :rtype: dict
        """

        similarity_matrix_val = df_similarity.values
        np.fill_diagonal(similarity_matrix_val, 0)
        rows, cols = np.where(similarity_matrix_val > threshold)
        row_names, col_names = df_similarity.index[rows], df_similarity.columns[cols]

        similar_words_dict = {}
        for row_name, col_name in zip(row_names, col_names):
            if row_name in similar_words_dict:
                similar_words_dict[row_name].append(col_name)
            else:
                similar_words_dict[row_name] = [col_name]

        return similar_words_dict