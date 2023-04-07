SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_code = countries.code
WHERE languages.language LIKE "Slovene"
ORDER BY languages.percentage DESC;

SELECT name, population FROM cities
WHERE country_code = "MEX" AND population > 500000
ORDER BY population DESC;

SELECT country_code, language, percentage FROM languages
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;

SELECT name FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT countries.name as country, cities.name as city, cities.population FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT region, COUNT(name) as number_of_countries FROM countries
GROUP BY region
ORDER BY COUNT(name) DESC;

SELECT countries.name as country_name, COUNT(cities.country_code) as num_cities from cities
LEFT JOIN countries ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.country_code)DESC;