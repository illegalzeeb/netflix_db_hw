from flask import Blueprint, render_template, request, jsonify

from utils import search_by_title, search_by_date

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/movie/title")
def movie_page():
    search_query = request.args.get('s', '')
    return search_by_title(search_query)


@main_blueprint.route("/movie/year")
def year_page():
    start_year = request.args.get('s', '')
    end_year = request.args.get('e', '')
    return search_by_date(start_year, end_year)


@main_blueprint.route("/movie/children")
def children_page():
    return search_by_children_rating()


@main_blueprint.route("/movie/family")
def family_page():
    return search_by_family_rating()


@main_blueprint.route("/movie/adult")
def adult_page():
    return search_by_adult_rating()