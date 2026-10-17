"""
595. Big Countries
Solved
Easy
Topics
premium lock icon
Companies
SQL Schema
Pandas Schema
Table: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
 

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
"""

import pandas as pd

df = pd.DataFrame({'name':['Afghanistan','Albania','Algeria','Andora','Angola'],
                   'continent':['Asia','Europe','Africa','Europe','Africa'],
                   'area':[652230,28748,2381741,468,1246700],
                   'population':[25500100,2831741,37100000,78115,20609294],
                   'gdp':[ 20343000000,12960000000,188681000000,3712000000,100990000000]})

def solution(df:pd.DataFrame):
    is_big_mask = df['area'] >= 3000000
    is_pop = df['population'] >=25000000

    return (df.loc[is_big_mask | is_pop, ['name','population','area']])     
z = solution(df)


"""
Kada koristim df.loc -> Mogu tu da filtriram uslovima za redove, ili ukoliko sam vec uradio masku,
samo je prosledim u df.loc[].
ukoliko mi je potrebna samo jedna kolona, pisem 'col1' , a ukoliko imam vise od jedne onda idu zagrade


"""
z = solution(df)


def solution_query(df:pd.DataFrame):

    q = df.query("area>=3000000 or population>=25000000")[['name','population','area']]
    print(q)

z = solution_query(df)
