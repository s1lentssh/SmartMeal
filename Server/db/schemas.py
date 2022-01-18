import typing as tp
import pydantic as pd


class IngredientBase(pd.BaseModel):
    name: str
    description: tp.Optional[str]
    image: str
    fats: float
    carbs: float
    proteins: float


class IngredientCreate(IngredientBase):
    pass


class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True


class RecipeBase(pd.BaseModel):
    name: str


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True


class AssociationBase(pd.BaseModel):
    ingredient_id: int
    ingredient_weight: float


class AssociationCreate(AssociationBase):
    pass


class Association(AssociationBase):
    id: int
    recipe_id: int
    recipes_rel: Recipe
    ingredients_rel: Ingredient

    class Config:
        orm_mode = True


class ResultMessage(pd.BaseModel):
    result: str

    class Config:
        orm_mode = True


class RecipeRemovalError(ResultMessage):
    relations: tp.List[Association]

    class Config:
        orm_mode = True
