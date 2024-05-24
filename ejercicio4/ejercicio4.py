# Analysis of Tourist Accommodation Data in Asturias

## Introduction
# In this notebook, we will analyze the tourist accommodation data in Asturias using RDF data.
# We will use the rdflib library to parse and query the RDF data and pandas for data manipulation and visualization.

# Install necessary libraries
!pip install rdflib pandas matplotlib

import rdflib
import pandas as pd
import matplotlib.pyplot as plt

# Define the RDF data
rdf_data = """
@prefix schema: <http://schema.org/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

wd:Q3934 a schema:Place ;
	schema:name "Asturias" ;
	schema:containedInPlace wd:Q29 ;  # Spain
	schema:containsPlace [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2006"^^xsd:gYear ;
    	schema:numberOfUnits 189 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1060
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2007"^^xsd:gYear ;
    	schema:numberOfUnits 201 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1130
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2008"^^xsd:gYear ;
    	schema:numberOfUnits 227 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1260
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2009"^^xsd:gYear ;
    	schema:numberOfUnits 246 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1354
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2010"^^xsd:gYear ;
    	schema:numberOfUnits 263 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1441
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2011"^^xsd:gYear ;
    	schema:numberOfUnits 273 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1513
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2012"^^xsd:gYear ;
    	schema:numberOfUnits 294 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1678
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2013"^^xsd:gYear ;
    	schema:numberOfUnits 309 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1769
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2014"^^xsd:gYear ;
    	schema:numberOfUnits 325 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 1903
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2015"^^xsd:gYear ;
    	schema:numberOfUnits 378 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 2175
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2016"^^xsd:gYear ;
    	schema:numberOfUnits 461 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 2639
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2017"^^xsd:gYear ;
    	schema:numberOfUnits 649 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 3836
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2018"^^xsd:gYear ;
    	schema:numberOfUnits 933 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 5619
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2019"^^xsd:gYear ;
    	schema:numberOfUnits 1142 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 6957
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2020"^^xsd:gYear ;
    	schema:numberOfUnits 1354 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 8276
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2021"^^xsd:gYear ;
    	schema:numberOfUnits 1599 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 9667
    	]
	], [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2022"^^xsd:gYear ;
    	schema:numberOfUnits 1917 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 11616
    	]
	] .
"""

# Create a graph and parse the RDF data
graph = rdflib.Graph()
graph.parse(data=rdf_data, format="turtle")

# Define a SPARQL query to extract data
query = """
PREFIX schema: <http://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT ?year (SUM(?units) AS ?totalUnits) (SUM(?beds) AS ?totalBeds)
WHERE {
  wd:Q3934 schema:containsPlace ?place .
  ?place a schema:TouristAccommodation ;
     	schema:datePosted ?year ;
     	schema:numberOfUnits ?units ;
     	schema:bed ?bedDetails .
  ?bedDetails schema:numberOfBeds ?beds .
}
GROUP BY ?year
ORDER BY ?year
"""

# Execute the query and convert the results to a DataFrame
results = graph.query(query)
data = []
for row in results:
	data.append([str(row.year), int(row.totalUnits), int(row.totalBeds)])

df = pd.DataFrame(data, columns=["Year", "Total Units", "Total Beds"])

# Display the DataFrame
print(df)

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(df["Year"], df["Total Units"], marker="o", label="Total Units")
plt.plot(df["Year"], df["Total Beds"], marker="o", label="Total Beds", linestyle="--")
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Tourist Accommodation Data in Asturias")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
