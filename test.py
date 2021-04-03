from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model
odqa = build_model(configs.odqa.en_odqa_infer_wiki, download = True)
answers = odqa(["Where did guinea pigs originate?", "When did the Lynmouth floods happen?", "When is the Bastille Day?"])
print(answers)
