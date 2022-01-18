import sqlalchemy as sa
from .database import Base


class Association(Base):
    __tablename__ = "recipes_ingredients"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    recipe_id = sa.Column(sa.ForeignKey("recipes.id"), nullable=False)
    ingredient_id = sa.Column(sa.ForeignKey("ingredients.id"), nullable=False)
    ingredient_weight = sa.Column(sa.Float)
    recipes_rel = sa.orm.relationship("Recipe", back_populates="ingredients")
    ingredients_rel = sa.orm.relationship(
        "Ingredient", back_populates="recipes")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    image = sa.Column(sa.String)
    fats = sa.Column(sa.Float)
    carbs = sa.Column(sa.Float)
    proteins = sa.Column(sa.Float)
    recipes = sa.orm.relationship(
        "Association", back_populates="ingredients_rel")


class Recipe(Base):
    __tablename__ = "recipes"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    ingredients = sa.orm.relationship(
        "Association", back_populates="recipes_rel", cascade="all, delete")
