from flask import Blueprint, render_template
from models import StockCocktails

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    cocktails = StockCocktails.query.all()
    return render_template('index.html', cocktails=cocktails)
