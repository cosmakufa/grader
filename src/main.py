import pandas as pd

import argparse

parser = argparse.ArgumentParser(description='find top students')
parser.add_argument('filename', metavar='F', type=str)
parser.add_argument('percentage', metavar='P', type=str)
args = parser.parse_args()
filename = args.filename
percentage = int(args.percentage)

df = pd.read_csv(filename)
df1 = df.iloc[:, [0,1,3,5]]
df1['final'] = df1.apply(lambda row: (row[1] + row[2] + (2 * row[3]))/400, axis=1)
num_students = int(len(df1) * (percentage / 100))
print('number of students: ', num_students)
indicies = df1.final.argsort()
filtered_students = df1.iloc[indicies[-num_students:]][::-1]
ids = filtered_students.student_id.values
print(ids)