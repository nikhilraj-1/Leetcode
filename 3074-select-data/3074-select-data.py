import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # df_idx= students.set_index('student_id')
    # temp = df_idx.loc[101,['name', 'age']]
    #temp =students.loc[students['student_id']==101,['name', 'age']]
    #temp = students[students['student_id'] == 101][['name', 'age']]
    temp = students.query('student_id == 101')[['name', 'age']]
    return temp


    