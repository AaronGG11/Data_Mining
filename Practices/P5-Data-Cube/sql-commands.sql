-- CREACION DE ESTRUCTURA BASICA DE TABLA DE HECHOS
-- se descarto el ID y el año completo
SELECT 
      [elemento]
      ,[anio]
      ,[month]
      ,[week]
      ,[localizacion]
      ,[medicion]
INTO [precipitacion_pluvial].[dbo].[pph_min]
FROM [precipitacion_pluvial].[dbo].[pph]


-- CONSULTA A LA TABLA ANTERIOR CREADA
SELECT TOP (1000) [elemento]
      ,[anio]
      ,[month]
      ,[week]
      ,[localizacion]
      ,[medicion]
FROM [precipitacion_pluvial].[dbo].[pph_min]

-- {DELEGACION}{NOSEMANA}{ANIO}
SELECT 
	[precipitacion_pluvial].[dbo].[estaciones].[Delegación_o_Municipio] AS "Delegación", 
	[precipitacion_pluvial].[dbo].[pph_min].[week] AS "semana",
	[precipitacion_pluvial].[dbo].[pph_min].[anio] AS "año", 
	[precipitacion_pluvial].[dbo].[pph_min].[medicion]
INTO [precipitacion_pluvial].[dbo].[Cube01WeekYearStationMeasure]
FROM [precipitacion_pluvial].[dbo].[pph_min] INNER JOIN [precipitacion_pluvial].[dbo].[estaciones]
ON [precipitacion_pluvial].[dbo].[pph_min].[localizacion] = [precipitacion_pluvial].[dbo].[estaciones].[id]
WHERE [precipitacion_pluvial].[dbo].[pph_min].[medicion] != -99

-- {DELEGACION}{NOSEMANA}{MONTH}
SELECT 
	[precipitacion_pluvial].[dbo].[estaciones].[Delegación_o_Municipio] AS "Delegación", 
	[precipitacion_pluvial].[dbo].[pph_min].[week] AS "semana",
	[precipitacion_pluvial].[dbo].[pph_min].[anio] AS "año", 
	[precipitacion_pluvial].[dbo].[pph_min].[medicion]
INTO [precipitacion_pluvial].[dbo].[Cube02MonthYearStationMeasure]
FROM [precipitacion_pluvial].[dbo].[pph_min] INNER JOIN [precipitacion_pluvial].[dbo].[estaciones]
ON [precipitacion_pluvial].[dbo].[pph_min].[localizacion] = [precipitacion_pluvial].[dbo].[estaciones].[id]
WHERE [precipitacion_pluvial].[dbo].[pph_min].[medicion] != -99

-- Vista Week Year Station Measure
SELECT dbo.estaciones.Delegación_o_Municipio AS Delegación, 
        dbo.pph_min.week AS semana, 
        dbo.pph_min.anio AS año, 
        dbo.pph_min.month AS mes, 
        dbo.pph_min.medicion
FROM dbo.pph_min INNER JOIN dbo.estaciones 
ON dbo.pph_min.localizacion = dbo.estaciones.id
WHERE (dbo.pph_min.medicion <> - 99)


-- {Delegacion}{NoSemana}
SELECT [Delegación]
      ,[semana]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube03WeekStationMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [Delegación], [semana]
ORDER BY "PROMEDIO" DESC

-- {Delegacion}{Mes}
SELECT [Delegación]
      ,[month]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube04MonthStationMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [Delegación], [month]
ORDER BY [Delegación], [month], "PROMEDIO" DESC  

-- {Delegacion}{Año}
SELECT [Delegación]
      ,[año]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube05YearStationMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [Delegación], [año]
ORDER BY [Delegación], [año], "PROMEDIO" DESC  


-- {Delegacion}
SELECT [Delegación]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube06StationMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [Delegación]
ORDER BY "PROMEDIO" DESC 


-- {Año}
SELECT [año]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube07YearMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [año]
ORDER BY [año] ASC

-- {Mes}
SELECT [mes]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube08MonthMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [mes]
ORDER BY [mes] ASC

-- {NoSemana}
SELECT [semana]
      ,AVG([medicion]) AS "PROMEDIO"
INTO [precipitacion_pluvial].[dbo].[Cube09WeekMeasure]
FROM [precipitacion_pluvial].[dbo].[View01WeekYearStationMeasure]
GROUP BY [semana]
ORDER BY [semana] ASC
