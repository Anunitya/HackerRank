SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY RLIKE '^[aeiou].*[aeiou]$'


/*

SELECT DISTINCT CITY 
FROM STATION
WHERE CITY RLIKE '^[aeiou]' 
      and 
      CITY IN (SELECT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','e','i','o','u'))
*/
