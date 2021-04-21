from deeppavlov.deprecated.skills.similarity_matching_skill import SimilarityMatchingSkill

faq_skill = SimilarityMatchingSkill(data_path = '/root/test_prog/test_deeppavlov/models1.csv',
                              x_col_name = 'Question', 
                              y_col_name = 'Answer',
                              save_load_path = '/root/test_prog/model',
                              config_type = 'tfidf_autofaq',
                              train = True)

print(faq_skill(['Каккие симптомы пневмонии?'], [], []))
