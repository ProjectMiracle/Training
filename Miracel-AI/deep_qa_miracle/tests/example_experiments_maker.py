from .common.test_case import DeepQaTestCase

class TestExampleExperiments(DeepQaTestCase):
    def setUp(self):
        super(TestExampleExperiments, self).setUp()
        self.write_pretrained_vector_files()
        self.example_experiments_dir = "../example_experiments"
        self.entailment_dir = self.example_experiments_dir + "/entailment/"
        self.reading_comprehension_dir = self.example_experiments_dir + "/reading_comprehension/"
        self.sequence_tagging_dir = self.example_experiments_dir + "/sequence_tagging/"

    def test_entailment_examples_can_train(self):
        self.write_snli_files()
        self.write_snli_pretraining_file()
        self.write_sequence_tagging_files()
        self.write_true_false_model_files()
        self.write_additional_true_false_model_files()
        self.write_memory_network_files()
        self.write_multiple_true_false_memory_network_files()
        self.write_additional_multiple_true_false_memory_network_files()
        self.write_question_answer_memory_network_files()
        self.write_who_did_what_files()
        self.write_tuple_inference_files()
        self.write_span_prediction_files()
        self.write_additional_span_prediction_files()
        self.write_sentence_selection_files()
        self.write_pretrained_vector_files()







