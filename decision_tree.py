#-------------------------------------------------------------------------
# AUTHOR: Michael Phu
# FILENAME: decision_tree.py
# SPECIFICATION: This program transforms data read from an external .csv file to numerical representation in order to fit a decision tree
# to the transformed data and display it. 
# FOR: CS 4210.01 - Assignment #1
# TIME SPENT: 4 Hours
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
     
# transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
features = {'Young':1,'Prepresbyopic':2,'Presbyopic':3,'Myope':1,'Hypermetrope':2,'Yes':1,'No':2,'Reduced':1,'Normal':2}
for i in range(0,len(db)):
  curRow = [] 
  for j in range(0,len(db[0])-1):
    if db[i][j] in features: 
      curRow.append(features[db[i][j]])
  X.append(curRow)

#transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
classes = {'Yes':1,'No':2}
for i in range(0,len(db)):
  Y.append(classes[db[i][4]])

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()