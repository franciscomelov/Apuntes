import pandas as pd

students_dict = {
    "name" : ["Miguel", "Juan David", "Carmen", "Facundo", "Romina"],
    "age" : [29, 19, 24, 22, 25],
    "career path" : ["Data Analyst", "Data Scientist", " Data Analyst", "Data Engineer", "ML Engineer"],
}

students_df = pd.DataFrame(students_dict)
# print(students_df)

students_list = [
    {"name": "Miguel", "age": 29, "career path": "Data Analyst"},
    {"name": "Juan David", "age": 19, "career path": "Data Scientist"},
    {"name": "Carmen", "age": 24, "career path": "Data Analyst"},
]

students_df_2 = pd.DataFrame(students_list)
# print(students_df_2)

# print(students_df.dtypes)
# print(students_df_2.dtypes)

wifu_dict = {
    "anime" : ["K-on", "lucky star", "jashin-shan dropkick" ],
    "name" : ["nodoka-chan", "Tsukasa-chan", "pekola-chan"]
}
wifu_df = pd.DataFrame(wifu_dict)

wifu_list = [
    {"anime" : "tamako market", "name" : "tamako-chan"},
    {"anime": "haruhi suzumiya", "name": "yuki-chan"},
    {"anime": "gabriel dropout", "name": "tapis-chan"}
]
wifu_df_2 = pd.DataFrame(wifu_list)
print(wifu_df_2)