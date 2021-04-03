from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model
odqa = build_model(configs.odqa.ru_odqa_infer_wiki, download = True)
answers = odqa(["Сколько детей родилось в 2008 году у граждан Швейцарии?"])
print(answers)
