from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model
from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model

model_config = read_json(configs.doc_retrieval.ru_ranker_tfidf_wiki)
model_config["dataset_reader"]["data_path"] = "/root/deepSearch_DoctorAi_new/test_deeppavlov/model.csv"
model_config["dataset_reader"]["dataset_format"] = "txt"
#model_config["train"]["batch_size"] = 1000

doc_retrieval = train_model(model_config)
doc_retrieval(['Бронхит'])

# Download all the SQuAD models
#squad = build_model(configs.squad.multi_squad_noans_infer, download = True)
# Do not download the ODQA models, we've just trained it
#odqa = build_model(configs.odqa.ru_odqa_infer_wiki, download = False)
#odqa(["Что такое бронхит?"])
