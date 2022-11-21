from django.shortcuts import render
from django.http import Http404
from django.views import View
import itertools as it
import random

ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}

# Create your views here.


class SandwichBaseView(View):
    def get(self, request):
        return render(request=request, template_name='sandwich_base.html', context={'ingredients': ingredients.keys()})

# class IngredientsListView(View):
#     def get(self, request, ingredient_type):
#         return render(
#             request=request,
#             template_name='ingredientslist.html',
#             context={'ingredients': ingredients[ingredient_type], 'ingredient_type': ingredient_type}
#         )


class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')
        return render(
            request=request,
            template_name='ingredients_list.html',
            context={
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type
            }
        )


class SandwichGeneratorView(View):
    def get(self, request):
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheeses'])
        selected_toppings = random.choice(ingredients['toppings'])
        sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
        return render(request, 'sandwich_generator.html', context={'sandwich': sandwich})


class SandwichMenuView(View):
    def get(self, request):
        meats = ingredients['meats']
        cheeses = ingredients['cheeses']
        toppings = ingredients['toppings']
        stuff = [meats, cheeses, toppings]
        possibilities = list(it.product(*stuff))
        sandwiches = []
        for i in possibilities:
            sandwiches.append({'meat': i[0], 'cheese': i[1], 'toppings': i[2]})

        print(sandwiches)

        return render(request, 'sandwich_menu.html', context={'meats': meats, 'cheeses': cheeses, 'toppings': toppings, 'all_combos': sandwiches})
