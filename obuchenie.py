from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model

faq = build_model(configs.faq.tfidf_autofaq, download = False)
a = faq(["Что такое дальнозоркость?"])
print(a)
