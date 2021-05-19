SELECT *
INTO [airbnb].[dbo].[View01_AirBnB2019]
FROM [airbnb].[dbo].[airbnb]
WHERE [airbnb].[dbo].[airbnb].[year_data] = 2019;

SELECT *
INTO [airbnb].[dbo].[View02_AirBnB2020]
FROM [airbnb].[dbo].[airbnb]
WHERE [airbnb].[dbo].[airbnb].[year_data] = 2020;

SELECT *
INTO [airbnb].[dbo].[View03_AirBnB2021]
FROM [airbnb].[dbo].[airbnb]
WHERE [airbnb].[dbo].[airbnb].[year_data] = 2021;


-- {DELEGACION}{NO HOTELES}{# AIRBNB DIFERENTES OFERTADOS}
SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(DISTINCT([airbnb].[dbo].[metro].[id])) AS "METRO",
	COUNT(DISTINCT([airbnb].[dbo].[airbnb].[host_id])) AS "AIRBNB"
into [airbnb].[dbo].[Cube01_Delegacion#Metro#AirBnB]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[metro] ON [airbnb].[dbo].[metro].[delegación] = [airbnb].[dbo].[delegaciones].[id]
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía]
ORDER BY "AIRBNB", "METRO";


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(DISTINCT([airbnb].[dbo].[metrobus].[id])) AS "METROBUS",
	COUNT(DISTINCT([airbnb].[dbo].[airbnb].[host_id])) AS "AIRBNB"
into [airbnb].[dbo].[Cube02_Delegacion#MetroBus#AirBnB]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[metrobus] ON [airbnb].[dbo].[metrobus].[delegacion] = [airbnb].[dbo].[delegaciones].[id]
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía]
ORDER BY "AIRBNB", "METROBUS";


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(DISTINCT([airbnb].[dbo].[hotels].[id])) AS "HOTEL",
	COUNT(DISTINCT([airbnb].[dbo].[airbnb].[host_id])) AS "AIRBNB"
into [airbnb].[dbo].[Cube03_Delegacion#Hoteles#AirBnB]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[hotels] ON [airbnb].[dbo].[hotels].[alcaldia] = [airbnb].[dbo].[delegaciones].[id]
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía]
ORDER BY "AIRBNB", "HOTEL";


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(DISTINCT([airbnb].[dbo].[airbnb].[host_id])) AS "# HOST AIRBNB",
	[airbnb].[dbo].[airbnb].[year_data] AS "ANIO"
INTO [airbnb].[dbo].[Cube04_Delegacion#Anio#AirBnB]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[airbnb].[year_data]
ORDER BY "ANIO", "# HOST AIRBNB" ASC


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(*) AS "# OFERTAS",
	[airbnb].[dbo].[View01_AirBnB2019].[month_data] AS "MES"
INTO [airbnb].[dbo].[Cube05_Delegacion#Mes#AirBnB_2019]
FROM [airbnb].[dbo].[delegaciones]
JOIN [airbnb].[dbo].[View01_AirBnB2019] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View02_AirBnB2019].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View01_AirBnB2019].[month_data]
ORDER BY "MES", "# OFERTAS" ASC


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(*) AS "# OFERTAS",
	[airbnb].[dbo].[View02_AirBnB2020].[month_data] AS "MES"
INTO [airbnb].[dbo].[Cube05_Delegacion#Mes#AirBnB_2020]
FROM [airbnb].[dbo].[delegaciones]
JOIN [airbnb].[dbo].[View02_AirBnB2020] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View02_AirBnB2020].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View02_AirBnB2020].[month_data]
ORDER BY "MES", "# OFERTAS" ASC


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	COUNT(*) AS "# OFERTAS",
	[airbnb].[dbo].[View03_AirBnB2021].[month_data] AS "MES"
INTO [airbnb].[dbo].[Cube06_Delegacion#Mes#AirBnB_2021]
FROM [airbnb].[dbo].[delegaciones]
JOIN [airbnb].[dbo].[View03_AirBnB2021] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View03_AirBnB2021].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View03_AirBnB2021].[month_data]
ORDER BY "MES", "# OFERTAS" ASC



SELECT 
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[airbnb].[month_data] AS "Mes",
	AVG([airbnb].[dbo].[airbnb].[calculated_host_listings_count]) AS "Ocupacion"
INTO [airbnb].[dbo].[Cube07_TipoAirBnB#Mes#Ocupacion]
FROM [airbnb].[dbo].[airbnb]
GROUP BY [airbnb].[dbo].[airbnb].[room_type], [airbnb].[dbo].[airbnb].[month_data]
ORDER BY "Mes" ASC, "Tipo AirBnB"


SELECT 
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[airbnb].[price]) AS "Precio Promedio 2019 - 2021"
INTO [airbnb].[dbo].[Cube08_TipoAirBnB#Delegacion#PrecioPromedio]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[airbnb].[room_type]
ORDER BY "Tipo AirBnB", "Precio Promedio 2019 - 2021" ASC


SELECT 
	[airbnb].[dbo].[View01_AirBnB2019].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[View01_AirBnB2019].[price]) AS "Precio Promedio 2019"
INTO [airbnb].[dbo].[Cube09_TipoAirBnB#Delegacion#PrecioPromedio_2019]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[View01_AirBnB2019] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View01_AirBnB2019].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View01_AirBnB2019].[room_type]
ORDER BY "Tipo AirBnB", "Precio Promedio 2019" ASC


SELECT 
	[airbnb].[dbo].[View02_AirBnB2020].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[View02_AirBnB2020].[price]) AS "Precio Promedio 2020"
INTO [airbnb].[dbo].[Cube10_TipoAirBnB#Delegacion#PrecioPromedio_2020]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[View02_AirBnB2020] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View02_AirBnB2020].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View02_AirBnB2020].[room_type]
ORDER BY "Tipo AirBnB", "Precio Promedio 2020" ASC



SELECT 
	[airbnb].[dbo].[View03_AirBnB2021].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[View03_AirBnB2021].[price]) AS "Precio Promedio 2021"
INTO [airbnb].[dbo].[Cube11_TipoAirBnB#Delegacion#PrecioPromedio_2021]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[View03_AirBnB2021] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[View03_AirBnB2021].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[View03_AirBnB2021].[room_type]
ORDER BY "Tipo AirBnB", "Precio Promedio 2021" ASC



SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	[airbnb].[dbo].[airbnb].[year_data] AS "ANIO",
	AVG([airbnb].[dbo].[airbnb].[availability_365]) AS "Disponibilidad anual"
INTO [airbnb].[dbo].[Cube12_Delegacion#Anio#Disponibilidad365]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[airbnb].[year_data]
ORDER BY "ANIO", "Disponibilidad anual" ASC



SELECT 
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[airbnb].[year_data] AS "Anio",
	AVG([airbnb].[dbo].[airbnb].[minimum_nights]) AS "Noches minimas"
INTO [airbnb].[dbo].[Cube14_TipoAirBnB#Anio#NochesMinimas]
FROM [airbnb].[dbo].[airbnb] 
GROUP BY [airbnb].[dbo].[airbnb].[room_type], [airbnb].[dbo].[airbnb].[year_data]
ORDER BY [airbnb].[dbo].[airbnb].[room_type], "Anio" ASC



SELECT 
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[airbnb].[minimum_nights]) AS "Noches minimas"
INTO [airbnb].[dbo].[Cube15_TipoAirBnB#Delegacion#NochesMinimas]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[airbnb].[room_type], [airbnb].[dbo].[delegaciones].[Alcaldía]
ORDER BY "Tipo AirBnB", [airbnb].[dbo].[delegaciones].[Alcaldía] ASC


SELECT 
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	[airbnb].[dbo].[airbnb].[month_data] AS "Mes",
	AVG([airbnb].[dbo].[airbnb].[minimum_nights]) AS "Noches minimas"
INTO [airbnb].[dbo].[Cube16_TipoAirBnB#Mes#NochesMinimas]
FROM [airbnb].[dbo].[airbnb] 
GROUP BY [airbnb].[dbo].[airbnb].[room_type], [airbnb].[dbo].[airbnb].[month_data]
ORDER BY [airbnb].[dbo].[airbnb].[room_type], "Mes" ASC


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	AVG([airbnb].[dbo].[airbnb].[price]) AS "Precio promedio",
	AVG([airbnb].[dbo].[airbnb].[minimum_nights]) AS "Noches minimas"
INTO [airbnb].[dbo].[Cube17_Delegacion#PrecioPromedio#NochesMinimas]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía]
ORDER BY [airbnb].[dbo].[delegaciones].[Alcaldía] ASC, "Noches minimas" ASC, "Precio promedio" ASC


SELECT 
	[airbnb].[dbo].[delegaciones].[Alcaldía],
	[airbnb].[dbo].[airbnb].[room_type] AS "Tipo AirBnB",
	AVG([airbnb].[dbo].[airbnb].[reviews_per_month]) AS "Reviews por mes"
INTO [airbnb].[dbo].[Cube18_Delegacion#TipoAirBnB#ReviewsPorMes]
FROM [airbnb].[dbo].[delegaciones] 
JOIN [airbnb].[dbo].[airbnb] ON [airbnb].[dbo].[delegaciones].[id] = [airbnb].[dbo].[airbnb].[neighbourhood]
GROUP BY [airbnb].[dbo].[delegaciones].[Alcaldía], [airbnb].[dbo].[airbnb].[room_type]
ORDER BY [airbnb].[dbo].[delegaciones].[Alcaldía] ASC, "Reviews por mes" ASC



