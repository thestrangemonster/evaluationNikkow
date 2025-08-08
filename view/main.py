from flask import Blueprint, render_template
from models import StockCocktails

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Debug : Compter tous les cocktails
    total_cocktails = StockCocktails.query.count()
    print(f"🔍 Total cocktails en BDD : {total_cocktails}")
    
    # Récupérer le dernier cocktail
    last_cocktail = StockCocktails.query.order_by(StockCocktails.id.desc()).first()
    
    if last_cocktail:
        print(f"🍹 Dernier cocktail : {last_cocktail.name_created} (ID: {last_cocktail.id})")
    else:
        print("❌ Aucun cocktail trouvé")
    
    return render_template('home.html', last_cocktail=last_cocktail)