from . import db

class StockCocktails(db.Model):
    __tablename__ = 'stock_cocktails'

    id = db.Column(db.Integer, primary_key=True)
    name_created = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    story_describe = db.Column(db.Text, nullable=False)
    sound_ambiance = db.Column(db.String(100), nullable=False)
    picture_prompt = db.Column(db.String(100), nullable=False)
