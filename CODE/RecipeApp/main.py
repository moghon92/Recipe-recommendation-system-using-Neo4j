from flask import Blueprint, render_template, request, redirect, url_for
from models import get_csv_dict, PyNeoGraph

main = Blueprint('main', __name__)
ingredients_dict = dict()
main_ingredients = list()
side_ingredients = list()


@main.route('/main/<user_id>', methods=['GET', 'POST'])
def initial_search(user_id):
    if request.method == 'GET':
        global ingredients_dict, main_ingredients, side_ingredients

        if not ingredients_dict:
            ingredients_dict = get_csv_dict()

        is_db_up = False
        try:
            driver_neo4j = PyNeoGraph()
            is_db_up = driver_neo4j.test_conn()
        except:
            pass
        return render_template('main.html', user_id=user_id, ingredients=ingredients_dict, db_connected=is_db_up)


    elif request.method == 'POST':
        main_ingredients = request.form['main_ingredients'][:-1]
        side_ingredients = request.form['side_ingredients'][:-1]

        if request.form['search_type'] == 'visual_search':
            return redirect(url_for('visualSearch.matching_recipes', user_id=user_id,
                                    main_ingredients=main_ingredients, side_ingredients=side_ingredients))
        elif request.form['search_type'] == 'text_search':
            return redirect(url_for('textSearch.text_search', user_id=user_id,
                                    main_ingredients=main_ingredients, side_ingredients=side_ingredients))


@main.route('/main/<user_id>/recipe_details/<recipe>', methods=['GET', 'POST'])
def recipe_details(user_id, recipe):
    global main_ingredients, side_ingredients

    recipe_id, recipe_name = recipe.split("&")
    recipe_decode = recipe.replace('%20', ' ')

    driver_neo4j = PyNeoGraph()

    result_1 = driver_neo4j.get_recipe_details(int(recipe_id))
    result_2 = driver_neo4j.get_relevant_ingredients(int(recipe_id))
    result_3 = driver_neo4j.get_recipe_details_ratings(int(recipe_id))
    result = {'data': result_1['data'] + ";" + result_2['data'] + ";" + result_3['data']}

    return render_template('recipe_details.html', user_id=user_id, recipe=recipe_decode, result=result,
                           main_ingredients=main_ingredients, side_ingredients=side_ingredients)


@main.route('/main/<user_id>/text_search_recipe_details/<recipe>', methods=['GET', 'POST'])
def text_search_recipe_details(user_id, recipe):
    global main_ingredients, side_ingredients

    recipe_id, recipe_name = recipe.split("&")
    recipe_decode = recipe.replace('%20', ' ')

    driver_neo4j = PyNeoGraph()

    result_1 = driver_neo4j.get_recipe_details(int(recipe_id))
    result_2 = driver_neo4j.get_relevant_ingredients(int(recipe_id))
    result_3 = driver_neo4j.get_recipe_details_ratings(int(recipe_id))
    result = {'data': result_1['data'] + ";" + result_2['data'] + ";" + result_3['data']}

    return render_template('text-search-recipe_details.html', user_id=user_id, recipe=recipe_decode, result=result,
                           main_ingredients=main_ingredients, side_ingredients=side_ingredients)
