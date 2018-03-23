################################### iAdvize DATA SCIENTIST TEST ###############################################
###############################################################################################################

# Importation des données directement du fichier WDIData.csv
# Pour cela il faut télécharger le fichier zip du site et le dézipper

###############################################################################################################

######################### Importation et première vue des données #############################################

###############################################################################################################

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
## Cette colonne a 415 536 lignes, ce qui paraît beaucoup d'indicateurs
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
NombreRepPays=len(b)
## 'Arab World' se répète len(b)=1574 fois
NombrePays = int(len(CountryName)/len(b))
## ce qui voudrait dire qu'il y ait 264 pays 




#####################################################################################################

##########  Concentrons-nous pour l'instant sur un seul pays, par exemple sur Arab World ############

#####################################################################################################

# Réduisons les données de la data frame df à une data frame ne contenant que des données sur Arab World
# On appelle cette data frame réduite Arab_World
Arab_World=df[df['Country Name'] == 'Arab World']
Arab_World.shape
## cette data frame contient 1574 lignes et 63 colonnes


# Indicateur de Arab World
IndicatorNameArab_World = Arab_World['Indicator Name']

# On veut les indicateurs où on retrouve les lettres "CO2 emissions"
index_emission = []
for index, word in enumerate(IndicatorNameArab_World) :
    if word.count("CO2 emissions") == 1 :
        index_emission = index_emission + [index]
########################################################################################################
## on vient d'obtenir pour le pays Arab World les indices qui parlent de "CO2 emiisions"         #######
## le sujet étant sur les émissions CO2, on tient ici les premières données qui nous intéressent #######
########################################################################################################
        
        
        
        
        
        
        
        
########################################################################################################
        
##################### ESSAYONS DE GENERALISER SUR TOUS LES AUTRES PAYS #################################
        
########################################################################################################
        
# index_emission étant l'index de l'émission CO2 du premier pays, c'est l'index "initial"
# grâce à cet index on va construire tous les autres en y ajoutant un multiple du nombre d'indicateurs (qui est 1574)

# grâce à la boucle précédente on a index_emission = [209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
indexCO2emissions = []
for i in range(1,NombrePays) :
    indexCO2emissions = indexCO2emissions + [209+NombreRepPays*(i-1), 210+NombreRepPays*(i-1), 211+NombreRepPays*(i-1), 212+NombreRepPays*(i-1), 
                         213+NombreRepPays*(i-1), 214+NombreRepPays*(i-1), 215+NombreRepPays*(i-1), 216+NombreRepPays*(i-1), 
                         217+NombreRepPays*(i-1), 218+NombreRepPays*(i-1), 219+NombreRepPays*(i-1), 220+NombreRepPays*(i-1), 
                         221+NombreRepPays*(i-1), 222+NombreRepPays*(i-1), 223+NombreRepPays*(i-1), 224+NombreRepPays*(i-1)]
    
    
# Maintenant on a tous les indices de la data frame df qui représentent les différentes émissions de CO2
# On peut donc écrire la variable représentant les indicateurs des émissions CO2
IndicatorName_CO2emissions = IndicatorName[indexCO2emissions]

#########################################################################################################
## Maintenant on peut réduire la grande data frame df en une data frame ne contenant ####################
## que les indicateurs représentants les émissions de CO2                            ####################
## On va appeler df_CO2emissions la data frame réduite                               ####################
#########################################################################################################

# df_CO2emissions -> data frame ne contenant que les indicateurs d'émissions de CO2
df_CO2emissions = df.loc[indexCO2emissions,:]  # -> 4208 lignes et 63 colonnes
## Ainsi maintenant on a la data frame qui nous intéresse pour l'étude









##############################################################################################################

##############################################################################################################

##########  Concentrons-nous de nouveau sur un seul pays (Arab World) avec la nouvelle data frame ############

##############################################################################################################

# Réduisons les données de la data frame df à une data frame ne contenant que des données sur Arab World
# On appelle cette data frame réduite Arab_World
Arab_World=df_CO2emissions[df_CO2emissions['Country Name'] == 'Arab World']

# On peut utiliser la méthode describe() pour df_CO2emissions qui nous permet d'obtenir les principales 
# statistiques pour chaque colonne contenant des nombres
df_CO2emissions.describe()
## C'est assez dur d'en déduire quelque chose de ces statistiques car 
## on mélange des pourcentages avec des nombres


##########################################################################################################

######################### Queslques affichages graphiques ################################################

##########################################################################################################
# Essayons de visualiser par exemple les données des années 2010 et 2011 grâce à un scatter plot
# Importons matplotlib
import matplotlib.pyplot as plt
Arab_World.plot(kind='scatter', x='2010', y='2011')
plt.title('Exemple: représentation des données de Arab World de 2011 en fonction de 2010')
plt.show()
## on remarque une relation linéaire entre ces deux années

# Essayons de visualiser les données des années 19600 et 2011 grâce à un scatter plot
Arab_World.plot(kind='scatter', x='1960', y='2011')
plt.title('Exemple: représentation des données de Arab World de 2011 en fonction de 1960')
plt.show()
## la relation entre ces deux années est moins évidente 
##########################################################################################################

# Prenons en compte qu'un seul indicateur -> "CO2 emissions (kg per 2010 US$ of GDP)" (toujours pour Arab World)
CO2emissions_kg_per2010 = Arab_World[Arab_World['Indicator Name']=="CO2 emissions (kg per 2010 US$ of GDP)"]
# regardons quelles années ont des données
CO2emissions_kg_per2010.info()
## on a des données de 1975 à 2014 pour Arab World



##############################################################################################################

##############################################################################################################

##########  Concentrons-nous sur l'indicateur "CO2 emissions (kg per 2010 US$ of GDP)" #######################

########################## en prenant en compte tous les pays ################################################

# Prenons en compte qu'un seul indicateur -> "CO2 emissions (kg per 2010 US$ of GDP)"
CO2emissions_kg_per2010 = df_CO2emissions[df_CO2emissions['Indicator Name']=="CO2 emissions (kg per 2010 US$ of GDP)"]

# Regardons par exemple l'histogramme de l'année 2010 de cet indicateur pour tous les pays
CO2emissions_kg_per2010['2010'].plot('hist')
plt.title('Histogramme: CO2 emissions (kg per 2010 US$ of GDP)')
plt.show()
## On peut remarquer que plus de la moitié des pays émettent moins de 0.5 kg de CO2

# Regardons par exemple le boxplot de l'année 2010 de cet indicateur pour tous les pays
CO2emissions_kg_per2010.boxplot(column='2010', by='Country Name')
plt.title('CO2 emissions (kg per 2010 US$ of GDP)')
plt.show()
##################### On remarque nous avons 4 pays outliers (>2kg)

# Quels sont ces 4 pays ?
outliers = CO2emissions_kg_per2010[CO2emissions_kg_per2010['2010']>2]
pays_outliers = outliers['Country Name']
########################################## -> Trinidad and Tobago
                                        ## -> Turkmenistan
                                        ## -> Ukraine
                                        ## -> Uzbekistan
                                        
                                        
                                        
                                        
                                        
#########################################################################################################
############## On peut également regarder les autres années et les autres indicateurs ###################
###################### pour pouvoir donner une analyse plus exacte ######################################
#########################################################################################################