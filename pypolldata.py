import pandas as pd
import numpy as np
polldata = pd.read_csv("/Users/gayanmeerigama/Creative Cloud Files/Data Analytics Boot Camp/Assingnment3/PyPoll/Resources/election_data.csv")

polldata.columns = ["Ballot_ID","County","Candidate"]

votes = list(polldata.Ballot_ID)


Total_Votes = len(votes)

# applying groupby() function to
# group the data on candidate value.
gk = polldata.groupby('Candidate')
  
# Let's print the first entries
# in all the groups formed.

Charlesvotes=len(gk.get_group('Charles Casper Stockham'))
Dianavotes =len(gk.get_group('Diana DeGette'))
Raymonvotes =len(gk.get_group('Raymon Anthony Doane'))

Charlesvotes_percentsge = round(Charlesvotes/(Charlesvotes+Dianavotes+Raymonvotes)*100,3)
Dianavotes_percentage = round(Dianavotes/(Charlesvotes+Dianavotes+Raymonvotes)*100,3)
Raymonvotes_percentage = round(Raymonvotes/(Charlesvotes+Dianavotes+Raymonvotes)*100,3)





#winner = pd.DataFrame({'Candidate': ['Charles Casper Stockham', 'Diana DeGette', 'Diana DeGette'], 'percentage': [Charlesvotes_percentsge, Dianavotes_percentage, Raymonvotes_percentage]})

winner = {'Charles Casper Stockham':Charlesvotes_percentsge,'Diana DeGette':Dianavotes_percentage, 'Raymon Anthony Doane':Raymonvotes_percentage}

Greatest_increase_in_Candidate =  max(winner, key=winner.get)

#maxChangeMonth = winner[winner.index(Greatest_increase_in_Candidate)] 

print("\nElection Results\n----------------------------------\n")

print("Total Votes:",Total_Votes)
print("----------------------------------")

print("Charles Casper Stockham:" ,Charlesvotes_percentsge,Charlesvotes)
print("Diana DeGette",Dianavotes_percentage,Dianavotes)
print("Raymon Anthony Doane",Raymonvotes_percentage,Raymonvotes)
print("----------------------------------")
print("Winner :",Greatest_increase_in_Candidate)
print("----------------------------------")


