from statistics import mode
from unicodedata import name
from sqlalchemy.orm import Session
from . import models, schemas


def read_ingredients(db: Session):
    return db.query(models.Ingredient).all()


def create_ingredient(db: Session, ingredient: schemas.IngredientCreate):
    entry = models.Ingredient(
        name=ingredient.name,
        description=ingredient.description,
        image=ingredient.image,
        fats=ingredient.fats,
        carbs=ingredient.carbs,
        proteins=ingredient.proteins)

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def update_ingredient(db: Session, id: int, item: schemas.IngredientCreate):
    entry = db.query(models.Ingredient).filter(
        models.Ingredient.id == id).first()
    entry.name = item.name
    entry.description = item.description
    entry.image = item.image
    entry.fats = item.fats
    entry.carbs = item.carbs
    entry.proteins = item.proteins

    db.commit()
    db.refresh(entry)
    return entry


def delete_ingredient(db: Session, id: int):
    try:
        entry = db.query(models.Ingredient).filter(
            models.Ingredient.id == id).first()
        db.delete(entry)
        db.commit()
        return schemas.ResultMessage(result="ok")
    except Exception:
        db.rollback()
        entry = db.query(models.Association).filter(
            models.Association.ingredient_id == id).all()
        return schemas.RecipeRemovalError(result="error", relations=entry)


def read_recipes(db: Session):
    return db.query(models.Recipe).all()


def create_recipe(db: Session, item: schemas.RecipeCreate):
    entry = models.Recipe(name=item.name)

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def update_recipe(db: Session, id: int, item: schemas.RecipeCreate):
    entry = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    entry.name = item.name

    db.commit()
    db.refresh(entry)
    return entry


def delete_recipe(db: Session, id: int):
    entry = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    db.delete(entry)

    db.commit()
    return True


def get_recipe_ingredients(db: Session, recipe_id: int):
    return db.query(models.Association).filter(models.Association.recipe_id == recipe_id).all()


def create_recipe_ingredient(db: Session, recipe_id: Session, item: schemas.AssociationBase):
    entry = models.Association(
        recipe_id=recipe_id,
        ingredient_id=item.ingredient_id,
        ingredient_weight=item.ingredient_weight)

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def update_recipe_ingredient(db: Session, recipe_id: int, item_id: int, item: schemas.AssociationCreate):
    entry = db.query(models.Association).filter(
        models.Association.id == item_id).first()
    entry.ingredient_id = item.ingredient_id
    entry.ingredient_weight = item.ingredient_weight

    db.commit()
    db.refresh(entry)
    return entry


def delete_recipe_ingredient(db: Session, recipe_id: int, item_id: int):
    entry = db.query(models.Association).filter(
        models.Association.id == item_id).first()
    db.delete(entry)

    db.commit()
    return True
