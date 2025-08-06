from . import db

class StockCocktails(db.Model):
    __tablename__ = 'stock_cocktails'

    id = db.Column(db.Integer, primary_key=True)
       