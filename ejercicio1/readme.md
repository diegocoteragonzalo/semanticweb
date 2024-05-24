"En la comunidad autónoma española de Asturias, en el año 2022 había 1917 establecimientos de viviendas vacacionales, y todas estos establecimientos contaban con un total de 11616 camas".

@prefix schema: <http://schema.org/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Definición de los datos para el año 2022 en Asturias
wd:Q2807 a schema:Place ;
	schema:name "Asturias" ;
	schema:containedInPlace wd:Q29 ;  # Spain
	schema:containsPlace [
    	a schema:TouristAccommodation ;
    	schema:datePosted "2022"^^xsd:gYear ;
    	schema:numberOfRooms 1917 ;
    	schema:bed [
        	a schema:BedDetails ;
        	schema:numberOfBeds 11616
    	]
	] .


Detalles:
	wd:Q2807: URI para la entidad "Asturias" en Wikidata.
	schema:Place: Representa un lugar.
	schema:name: Nombre del lugar, en este caso "Asturias".
	schema:containedInPlace wd:Q29: Indica que Asturias está contenida en España (URI de España en Wikidata es wd:Q29).
	schema:containsPlace: Indica que Asturias contiene establecimientos turísticos (schema:TouristAccommodation).
	schema:TouristAccommodation: Clase utilizada para representar los establecimientos de viviendas vacacionales.
	schema:datePosted: Año de los datos, en este caso "2022".
	schema:numberOfRooms: Número de establecimientos, 1917.
	schema:bed: Utilizado para anidar los detalles de las camas.
	schema:BedDetails y schema:numberOfBeds: Utilizados para representar el número de camas disponibles, 11616.

Este modelo RDF sigue las pautas de Schema.org y Wikibase para representar la frase de ejemplo.

