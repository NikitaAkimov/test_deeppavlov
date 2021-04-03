from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model
odqa = build_model(configs.odqa.en_odqa_infer_wiki, download = False)
result = odqa(['Who is the Greek god of War?'])
print(result)
