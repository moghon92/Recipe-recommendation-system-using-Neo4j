from flask import Blueprint, render_template, request
from models import PyNeoGraph

visualSearch = Blueprint('visualSearch', __name__)
main_ingredients = list()
side_ingredients = list()
selected_recipe = list()


@visualSearch.route('/visualSearch/<user_id>/matching_recipes', methods=['GET', 'POST'])
def matching_recipes(user_id):
    global main_ingredients, side_ingredients

    try:
        tab_type = request.form['tab_type']
    except:
        tab_type = 'recipe'
        # clear the inputs for initial case
        main_ingredients = list()
        side_ingredients = list()

    if not main_ingredients or not side_ingredients:
        main_ingredients = request.args.get('main_ingredients')
        side_ingredients = request.args.get('side_ingredients')

        main_ingredients = list(set((main_ingredients.split(","))))
        side_ingredients = list(set(side_ingredients.split(",")))

    driver_neo4j = PyNeoGraph()

    if tab_type == 'add_ingredient':
        add_ingredients = request.form['add_ingredients']
        add_ingredients = list(add_ingredients.split(","))[0:-1]
        if side_ingredients[0] != '':
            side_ingredients += add_ingredients
        else:
            side_ingredients = add_ingredients
        tab_type = 'ingredient'

    if tab_type == 'recipe':
        result = driver_neo4j.get_matching_recipes(main_ingredients, side_ingredients)
    elif tab_type == 'ingredient':
        result = driver_neo4j.get_additional_ingredients(main_ingredients, side_ingredients)
    elif tab_type == 'contentBased':
        result = driver_neo4j.get_content_based_recipes(int(user_id), main_ingredients, side_ingredients)
    elif tab_type == 'collaborative':
        result = driver_neo4j.get_collaborative_recipes(int(user_id), main_ingredients, side_ingredients)

    return render_template('visual_search.html', user_id=user_id, tab_type=tab_type, result=result,
                           main_ingredients=main_ingredients, side_ingredients=side_ingredients)


@visualSearch.route('/visualSearch/<user_id>/recipe_info/<recipe>', methods=['GET', 'POST'])
def recipe_info(user_id, recipe):
    global main_ingredients, side_ingredients

    recipe_id, recipe_name = recipe.split("&")
    driver_neo4j = PyNeoGraph()

    try:
        tab_type = request.form['tab_type']
    except:
        tab_type = 'usedIngredients'

    if tab_type == 'usedIngredients':
        result = driver_neo4j.get_relevant_ingredients(int(recipe_id))
    elif tab_type == 'userRatings':
        result = driver_neo4j.get_relevant_ratings(int(recipe_id))

    return render_template('visual_search_recipe.html', user_id=user_id, recipe=recipe, tab_type=tab_type,
                           result=result, main_ingredients=main_ingredients, side_ingredients=side_ingredients)
