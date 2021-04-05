from deeppavlov import configs, train_model

faq = train_model(configs.faq.tfidf_autofaq)
a = faq(["Что такое бронхит?"])
print(a)
