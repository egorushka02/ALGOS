"""
Topological Sort
"""

"""
2115. Find al Possible Recipes from Given Supplies
"""
from collections import defaultdict, deque


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        in_degree = {}
        g = defaultdict(list)

        for recipe, components in zip(recipes, ingredients):
            in_degree[recipe] = len(components)
            for component in components:
                g[component].append(recipe)

        q = deque(supplies)
        result = []

        while q:
            supply = q.popleft()
            for recipe in g[supply]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    q.append(recipe)
                    result.append(recipe)

        return result
        