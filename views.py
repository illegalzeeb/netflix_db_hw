from flask import Blueprint, render_template, request, jsonify

from utils import search_by_title, search_by_date, search_by_children_rating, search_by_family_rating, \
    search_by_adult_rating, search_by_genre

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/movie/<str:title>")
def movie_page(title):
    return jsonify(search_by_title(title))


@main_blueprint.route("/movie/<int:start_year>/to/<int:end_year>")
def year_page(start_year, end_year):
    return jsonify(search_by_date(start_year, end_year))


@main_blueprint.route("/movie/children")
def children_page():
    return search_by_children_rating()


@main_blueprint.route("/movie/family")
def family_page():
    return search_by_family_rating()


@main_blueprint.route("/movie/adult")
def adult_page():
    return search_by_adult_rating()


@main_blueprint.route("/movie/<str:genre>")
def genre_page(genre):
    return jsonify(search_by_genre(genre))