from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model

odqa = build_model(configs.odqa.ru_odqa_infer_wiki)
answers = odqa([ "Как отводятся излишки тепла у млекопитающих?"])
