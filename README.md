#Instrucciones:  
Dadas las bases de datos airbus380 (airbus_380_acad.bak) y datos (datos.bak) proporcionados en la carpeta Dropbox , en 
la base de datos airbus380, cree una tabla llamada clientes, la cual debe tener la estructura mostrada en la parte inferior, 
así mismo cree una tabla llamada detalle_vuelos y ocupaciones.   
Migre las tablas necesarias de la base de datos “datos” a la base de datos airbus380 o haga lo necesario para poder acceder 
a ellas. 
Para la tabla de clientes, genere 100,000 registros con nombres y apellidos aleatorios tomados de la base de datos “datos”, 
la fecha de nacimiento será generada también de manera aleatoria, las edades de las personas no deben superar los 90 
años y no debe ser menor a 5 años. En la misma tabla los campos cve_estados y cve_municipios deberán ser generados 
de manera aleatoria tomando como base las tablas estados y municipios de la base de datos “datos”. 
Para la tabla detalle_vuelos genere 2000 registros, el campo cve_vuelos será tomado de manera aleatoria de la tabla 
vuelos y en esta se debe generar la capacidad entre 350 y 500 (números múltiplos de 50) asientos, así como una fecha y 
hora de salida, la cual debe ser cualquier día del año 2023, solo se deben considerar de la tabla vuelos los registros con el 
campo cve_aeropuertos__origen o con el campo cve_aeropuertos__destino sea un registro que pertenezca a algún 
aeropuerto del país México; la hora de salida deberá ser cualquier hora en punto. 
Para la tabla ocupaciones el campo cve_clientes será aleatorio tomando como base la tabla clientes, pudiéndose repetir 
este dato, el campo cve_detalle_vuelos será aleatorio tomando como base la tabla datalle_vuelos, debe considerar que 
las ocupaciones (registros) no deben rebasar la capacidad de vuelo de la tabla detalle_vuelos. Esta tabla debe contener al 
menos 1,000,000 de registros.