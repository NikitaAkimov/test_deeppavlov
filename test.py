# from deeppavlov.deprecated.skills.similarity_matching_skill import SimilarityMatchingSkill
# from deeppavlov.deprecated.agents.default_agent.default_agent import DefaultAgent
# from deeppavlov.deprecated.agents.processors.highest_confidence_selector import HighestConfidenceSelector
# from deeppavlov.utils.server import start_model_server

# faq_skill = SimilarityMatchingSkill(data_path = '/root/test_prog/test_deeppavlov/models1.csv',
#                               x_col_name = 'Question', 
#                               y_col_name = 'Answer',
#                               save_load_path = '/root/test_prog/model',
#                               config_type = 'tfidf_autofaq',
#                               train = True)

# print(faq_skill(['Каккие симптомы пневмонии?'], [], []))

# agent = DefaultAgent([faq_skill], skills_selector=HighestConfidenceSelector())

# start_model_server(model_config=agent)

from deeppavlov import configs
from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model

model_config = read_json(configs.faq.tfidf_autofaq)
model_config["dataset_reader"]["data_path"] = "/root/test_prog/test_deeppavlov/models1.csv"
model_config["dataset_reader"]["data_url"] = None
model_config["dataset_reader"]["save_path"] = "/root/test_prog/model_test/data.db"
faq = train_model(model_config)
a = faq(["Каккие симптомы пневмонии?"])
print(a)
