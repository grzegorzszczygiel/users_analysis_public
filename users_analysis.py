
import pandas as pd
from pandas import Grouper
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from classy import gen_hash, gen_n_name_list, gen_n_surname_list, gen_n_string_list, gen_n_bool_list, gen_age_list, gen_weight_list, gen_height_list

class RandomHuman:

  def __init__(self):

    self.uuid = gen_hash(8)
    self.name = gen_n_name_list(1)[0]
    self.surname = gen_n_surname_list(1)[0]
    # fullname = name + surname
    self.fullname = self.name + ' ' + self.surname
    # email => fullname
    self.email = self.name.lower() + '.' + self.surname.lower() + '@' + 'wp.pl'
    self.age = gen_age_list(1)[0]
    self.weight = gen_weight_list(1)[0]
    self.height = gen_height_list(1)[0]
    self.description = gen_n_string_list(1)[0]
    self.active = gen_n_bool_list(1)[0]


  def as_dict(self):

    return {
      'uuid':self.uuid,
      'name': self.name,
      'surname': self.surname,
      'fullname': self.fullname,
      'email': self.email,
      'age': self.age,
      'weight': self.weight,
      'height': self.height,
      'description': self.description,
      'active': self.active
    }


  def as_csv_column_entry(self):
    return 'uuid,name,surname,fullname,email,age,weight,height,description,active''\n'


  def as_csv_entry(self):
    return str(self.uuid) + ',' + str(self.name) + ',' + str(self.surname) + ',' + str(self.fullname) \
           + ',' + str(self.email) + ',' + str(self.age) + ',' + str(self.weight) + ',' + str(self.height) \
           + ',' + str(self.description) + ',' + str(self.active)+'\n'

human = RandomHuman()


list_of_people = []

for human in range(10000):
  entry = RandomHuman().as_csv_entry().replace('\n','').split(',')
  list_of_people.append( entry )

# print(list_of_people)
list_of_people = pd.DataFrame(list_of_people)
# print(list_of_people.head())

columns = RandomHuman().as_csv_column_entry().replace('\n','').split(',')

list_of_people.columns = columns
# print(list_of_people.head())

list_of_people.to_csv('people.csv', index = 0)
# print(list_of_people)

csvfile = pd.read_csv('people.csv')

rounded_age = csvfile.loc[:,'age'].round(-1)
# print(csvfile.columns)
# print(rounded_age)

csvfile.loc[:,'rounded_age'] = csvfile.loc[:,'age'].round(-1)

grouped_age = csvfile.groupby(Grouper(key='rounded_age')).count()
# print(grouped_age)

rounded_weight = csvfile.loc[:,'weight'].round(-1)
# print(rounded_weight)

csvfile.loc[:,'rounded_weight'] = csvfile.loc[:,'weight'].round(-1)

grouped_weight = csvfile.groupby(Grouper(key='rounded_weight')).count()
# print(rounded_weight)

rounded_height = csvfile.loc[:,'height'].round(-1)
# print(rounded_height)

csvfile.loc[:,'rounded_height'] = csvfile.loc[:,'height'].round(-1)

grouped_height = csvfile.groupby(Grouper(key='rounded_height')).count()
# print(rounded_height)

grouped_age_and_height = csvfile.groupby(['rounded_age', 'rounded_height']).size()
# print(grouped_age_and_height)

grouped_age_and_height_weight = csvfile.groupby(['rounded_age', 'rounded_height', 'rounded_weight']).size()
grouped_age_and_height_weight = grouped_age_and_height_weight.reset_index()

grouped_age_and_height_weight.columns = ['RA','RH','RW','S']

grouped_age_and_height_weight = grouped_age_and_height_weight.sort_values(by=['S'], ascending=False)

grouped_age_and_height_weight = grouped_age_and_height_weight.reset_index()
# print(grouped_age_and_height_weight)


threedee = plt.figure(figsize=(8,6)).gca(projection='3d')

cmap = plt.cm.Blues
colors = cmap(grouped_age_and_height_weight.loc[:,'S'] / grouped_age_and_height_weight.loc[:,'S'].max())
colors[:,-1] = grouped_age_and_height_weight.loc[:,'S'] / grouped_age_and_height_weight.loc[:,'S'].max()


threedee.scatter(grouped_age_and_height_weight.loc[:,'RA'],
                 grouped_age_and_height_weight.loc[:,'RH'],
                 grouped_age_and_height_weight.loc[:,'RW'],
                 s=grouped_age_and_height_weight.loc[:,'S'],
                 c=colors,
                 depthshade=0,
                 )

threedee.set_xlabel('age')
threedee.set_ylabel('weight')
threedee.set_zlabel('height')
plt.title('Users weight height age analysis')

plt.show()
