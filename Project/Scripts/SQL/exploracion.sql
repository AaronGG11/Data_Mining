SELECT COUNT(*) AS 'Numero de registros'
FROM airbnb;

SELECT COUNT(DISTINCT id) AS 'Numero de vendedores diferentes'
FROM airbnb;



SELECT COUNT(*) AS 'VALORES NULOS'
FROM airbnb
WHERE name IS NULL;

SELECT COUNT(*) AS 'VALORES NULOS STRING'
FROM airbnb
WHERE name = 'NULL';

SELECT *
FROM airbnb
WHERE name = 'NULL' 
OR name IS NULL;

UPDATE airbnb
SET name = 'Desconocido'
WHERE name = 'NULL' 
OR name IS NULL;

SELECT *
FROM airbnb
WHERE name = 'NULL' 
OR name IS NULL;



SELECT COUNT(*) AS 'VALORES NULOS'
FROM airbnb
WHERE host_name IS NULL;

SELECT COUNT(*) AS 'VALORES NULOS STRING'
FROM airbnb
WHERE host_name = 'NULL';

SELECT *
FROM airbnb
WHERE host_name = 'NULL' 
OR host_name IS NULL;

UPDATE airbnb
SET host_name = 'Desconocido'
WHERE host_name = 'NULL' 
OR host_name IS NULL;

SELECT *
FROM airbnb
WHERE host_name = 'NULL' 
OR host_name IS NULL;
