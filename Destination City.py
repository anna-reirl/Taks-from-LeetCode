class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outoing_count = {}
        for path in paths:
            city_a, city_b = path
            outoing_count[city_a] = outoing_count.get(city_a, 1) + 1
            outoing_count[city_b] = outoing_count.get(city_b, 0)
        for city in outoing_count:
            if outoing_count[city] == 0:
                return city
