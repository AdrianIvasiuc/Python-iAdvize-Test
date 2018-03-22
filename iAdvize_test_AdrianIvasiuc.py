###### Test Data Scientist

# Importation des données directement du fichier WDIData.csv
# Pour cela il faut télécharger le fichier zip du site et le dézipper



# Importation du package pandas qui permet d'enregistrer les données sous formes de data frame
import pandas as pd

# on enregistre les données du fichier dans la dataframe df
df = pd.read_csv('WDIData.csv')

# nombre de lignes et de colonnes de la data frame avec l'attribut shape he data -> shape attribute
print(df.shape)
## on apprend qu'on a 415 536 lignes et 63 colonnes 

## Que contient chaque colonne ?

# on regarde le nom des colonnes
print(df.columns)
# et le type de chaque colonne
print(df.info())
## on remarque qu'on a 4 colonnes contenant un nom et non des nombres : Country Name, Country Code, Indicator Name, Indicator Code
## Les colonnes de 1960 à 2017 contient des nombres et donc les données.


# Prenons et regardons une colonne en particulier : Indicator Name
IndicatorName = df['Indicator Name']
## Cette colonne a 415 536 lignes, ce qui paraît beaucoup 
# Regardons s'il y a des indicateurs qui se répètent 
# On prend la valeur 'Access to electricity (% of population)' 
# et on regarde le nombre de fois que cette valeur se répète dans IndicatorName
a = IndicatorName[IndicatorName == 'Access to electricity (% of population)']
len(a)
## 'Access to electricity (% of population)' se répète len(a)=264 fois
NombreIndicateursDistincts = len(IndicatorName)/len(a)
## ce qui veut dire que l'on a 1574 indicateurs distincts


# Prenons et regardons une autre colonne : Country Name
CountryName = df['Country Name']
# Regardons s'il y a des pays dont le nom est utilisé plusieurs fois
# On prend la valeur 'Arab World'
# On regarde le nombre de fois que cette valeur se répète dans CountryName
b=CountryName[CountryName=='Arab World']
len(b)
## 'Arab World' se répète len(b)=1574 fois
NombrePays = len(CountryName)/len(b)
## ce qui voudrait dire qu'il y ait 264 pays ( ce qui est un peu trop par rapport à la réalité)
## peut-être que des groupes de pays ont égalemnt été ajoutés comme 'Arab World' par exemple



################################################################################################

##########  Concentrons-nous pour l'instant sur un seul pays, par exemple la France ############

################################################################################################

# Réduisons les données de la data frame df à une data frame ne contenant que des données sur la France
# On appelle cette data frame réduite France
France=df[df['Country Name'] == 'France']
France.shape
## cette data frame contient 1574 lignes et 63 colonnes

# Regardons le nombre de données non nulles selon chaque colonne
print(France.info())
## on remarque à l'oeil nu qu'il manque beaucoup de données pour chaque année de 1960 à 2017


# Essayons de visualiser par exemple les données des années 2010 et 2011 grâce à un scatter plot
# Importons matplotlib
import matplotlib.pyplot as plt
France.plot(kind='scatter', x='2010', y='2011')
plt.title('Exemple: représentation des données de France de 2011 en fonction de 2010')
plt.show()
## on remarque une relation linéaire entre ces deux années

# Essayons de visualiser les données des années 19600 et 2011 grâce à un scatter plot
France.plot(kind='scatter', x='1960', y='2011')
plt.title('Exemple: représentation des données de France de 2011 en fonction de 1960')
plt.show()
## la relation entre ces deux années est moins évidente 
## peut-être dûe au fait que le nombre de données de 1960 est faible ?