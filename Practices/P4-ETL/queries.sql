/* Cantidad de registros totales y por año */
SELECT [anio] AS "AÑO", count(*) AS "TOTAL" 
FROM [precipitacion_pluvial].[dbo].[pph]
GROUP BY [anio]
ORDER BY [anio] ASC

/* Tendencia de las semanas con mayor y menor cantidad de precipitación pluvial */
SELECT [week], AVG([medicion]) AS "PICOS"
FROM [precipitacion_pluvial].[dbo].[pph]
WHERE [medicion] != -99
GROUP BY [week]
ORDER BY "PICOS" DESC

/* Indique los lugares con mayor precipitación durante todo el periodo de estudio */
SELECT [Delegación_o_Municipio] AS "Delegación o municipio", AVG([medicion]) AS "Promedio de precipitación pluvial"
FROM [precipitacion_pluvial].[dbo].[pph] INNER JOIN [precipitacion_pluvial].[dbo].[estaciones]
ON [precipitacion_pluvial].[dbo].[pph].[localizacion] = [precipitacion_pluvial].[dbo].[estaciones].[id]
WHERE [medicion] != -99
GROUP BY [Delegación_o_Municipio]
ORDER BY "Promedio de precipitación pluvial" DESC


