import csv
import pandas as pd

class Title:
  def __init__(mysillyobject, title_name, type, number):
    mysillyobject.type = type
    mysillyobject.number = number
    mysillyobject.title_name = title_name

  def getName(specific_title):
    print("Hello! I am a " + specific_title.title_name +"! My type is " + specific_title.type + " and my number is " + str(specific_title.number))

with open('catan_sample.csv', 'r') as f:
  rows = csv.DictReader(f) #Opening the csv as a dictionary
  for row in rows:
    if row['title'] == 't0':
      t0 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't1':
      t1 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't2':
      t2 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't3':
      t3 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't4':
      t4 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't5':
      t5 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't6':
      t6 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't7':
      t7 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't8':
      t8 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't9':
      t9 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't10':
      t10 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't11':
      t11 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't12':
      t12 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't13':
      t13 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't14':
      t14 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't15':
      t15 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't16':
      t16 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't17':
      t17 = Title(row['title'], row['type'], row['number'])
    if row['title'] == 't18':
      t18 = Title(row['title'], row['type'], row['number'])

titles = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18]
for i in titles:
  if i.number == '2':
    i.number = 1
  if i.number == '3':
    i.number = 2
  if i.number == '4':
    i.number = 3
  if i.number == '5':
    i.number = 4
  if i.number == '6':
    i.number = 5
  if i.number == '7':
    i.number = 6
  if i.number == '8':
    i.number = 5
  if i.number == '9':
    i.number = 4
  if i.number == '10':
    i.number = 3
  if i.number == '11':
    i.number = 2
  if i.number == '12':
    i.number = 1

##########
class Vertex:
    def __init__(self, settlement, edges):
        self.settlement = settlement
        self.edges = edges

    
v0 = Vertex('s0', [t0])
v1 = Vertex('s1', [t1])
v2 = Vertex('s2', [t2])
v3 = Vertex('s3', [t0])
v4 = Vertex('s4', [t0, t1])
v5 = Vertex('s5', [t1, t2])
v6 = Vertex('s6', [t2])
v7 = Vertex('s7', [t0, t3])
v8 = Vertex('s8', [t0, t1, t4])
v9 = Vertex('s9', [t1, t2, t5])
v10 = Vertex('s10', [t2, t6])
v11 = Vertex('s11', [t3])
v12 = Vertex('s12', [t0, t3, t4])
v13 = Vertex('s13', [t1, t4, t5])
v14 = Vertex('s14', [t2, t5, t6])
v15 = Vertex('s15', [t6])
v16 = Vertex('s16', [t3, t7])
v17 = Vertex('s17', [t3, t4, t8])
v18 = Vertex('s18', [t4, t5, t9])
v19 = Vertex('s19', [t5, t6, t10])
v20 = Vertex('s20', [t6, t11])
v21 = Vertex('s21', [t7])
v22 = Vertex('s22', [t3, t7, t8])
v23 = Vertex('s23', [t4, t8, t9])
v24 = Vertex('s24', [t5, t9, t10])
v25 = Vertex('s25', [t6, t10, t11])
v26 = Vertex('s26', [t11])
v27 = Vertex('s27', [t7])
v28 = Vertex('s28', [t7, t8, t12])
v29 = Vertex('s29', [t8, t9, t13])
v30 = Vertex('s30', [t9, t10, t14])
v31 = Vertex('s31', [t10, t11, t15])
v32 = Vertex('s32', [t11])
v33 = Vertex('s33', [t7, t12])
v34 = Vertex('s34', [t8, t12, t13])
v35 = Vertex('s35', [t9, t13, t14])
v36 = Vertex('s36', [t10, t14, t15])
v37 = Vertex('s37', [t11, t15])
v38 = Vertex('s38', [t12])
v39 = Vertex('s39', [t12, t13, t16])
v40 = Vertex('s40', [t13, t14, t17])
v41 = Vertex('s41', [t14, t15, t18])
v42 = Vertex('s42', [t15])
v43 = Vertex('s43', [t12, t16])
v44 = Vertex('s44', [t13, t16, t17])
v45 = Vertex('s45', [t14, t17, t18])
v46 = Vertex('s46', [t15, t18])
v47 = Vertex('s47', [t16])
v48 = Vertex('s48', [t16, t17])
v49 = Vertex('s49', [t17, t18])
v50 = Vertex('s50', [t18])
v51 = Vertex('s51', [t16])
v52 = Vertex('s52', [t17])
v53 = Vertex('s53', [t18])

vertices = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53]
probs = []

for i in vertices:
  prob = 0
  for j in i.edges:
    prob = int(j.number) + prob
  probs.append(prob)

  

print(probs)
