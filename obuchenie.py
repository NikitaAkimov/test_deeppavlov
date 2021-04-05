from deeppavlov.deprecated.skills.similarity_matching_skill import SimilarityMatchingSkill

faq_skill = SimilarityMatchingSkill(data_path = './model.csv',
                              x_col_name = 'Question', 
                              y_col_name = 'Answer',
                              save_load_path = './model',
                              config_type = 'tfidf_autofaq',
                              train = True)
a = faq_skill(['Что такое бронхит?'], [], [])
print(a)
