from .input_output_manager import InputOutputManager
from .embedding_manager import EmbeddingManager
from .similarity_manager import SimilarityManager

class WorkFlowManager(): 
    """
    Work flow pipeline.
    1. Load in csv text, make sure standardized fieldnames.
    2. Choose proper embedding approach. 
    3. Generate similarity calculation results based on embedding vector.
    """
    def __init__(self, input_path: str, output_path: str, is_labelled: bool):
        """
        Initialize workflow input.

        :param input_path: str. The path of input folder
        :param out_path: str. The path of output folder
        """
        self._io_manager = InputOutputManager(input_path, output_path)
        self.input_file = self._io_manager.read_data_from_csv()
        self.is_labelled = is_labelled
    
    def calc_embedding(self):
        """
        Calculate the embedding using chosen methods.

        :return: embedding matrix
        :rtype: np.ndarray
        """
        embedding_obj = EmbeddingManager(self.input_file['raw_text'])
        embedding_vector = embedding_obj.embedding()
        return embedding_vector
    
    def run_similarity(self):
        """
        Obtain the top n (default as 5) similar text for each text and save the results.
        """
        similarity_obj = SimilarityManager(self.is_labelled)
        similarity_matrix = similarity_obj.get_cos_similarity(self.input_file, self.calc_embedding())
        print(similarity_matrix.shape)
        df_topn_similar_text = similarity_obj.get_topn_similar_comment(self.input_file, similarity_matrix)
        self._io_manager.save_data(df_topn_similar_text, 'topn_similar_text')
    
    







