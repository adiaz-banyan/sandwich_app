from django.urls import path
from sandwich_base.views import IngredientsListView, SandwichBaseView, SandwichGeneratorView, SandwichMenuView

urlpatterns = [
    path('', SandwichBaseView.as_view(), name='sandwich'),
    path('sandwich/ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='generator'),
    path('menu', SandwichMenuView.as_view(), name='sandwich_menu')
]
