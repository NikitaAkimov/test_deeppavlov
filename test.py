from deeppavlov.deprecated.skills.similarity_matching_skill import SimilarityMatchingSkill
from deeppavlov.deprecated.agents.default_agent.default_agent import DefaultAgent
from deeppavlov.deprecated.agents.processors.highest_confidence_selector import HighestConfidenceSelector
from deeppavlov.utils.server import start_agent_server

faq_skill = SimilarityMatchingSkill(data_path = '/root/test_prog/test_deeppavlov/models1.csv',
                              x_col_name = 'Question', 
                              y_col_name = 'Answer',
                              save_load_path = '/root/test_prog/model',
                              config_type = 'tfidf_autofaq',
                              train = True)

print(faq_skill(['Каккие симптомы пневмонии?'], [], []))

agent = DefaultAgent([faq_skill], skills_selector=HighestConfidenceSelector())

start_model_server(agent, port=5000)
