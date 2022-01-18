from urllib import response
import uvicorn
import fastapi as fa
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import typing as tp

from db import database, crud, models, schemas

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://home",
    "http://home:8080",
]

app = fa.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ingredients/", response_model=tp.List[schemas.Ingredient])
async def get_ingredients(db: Session = fa.Depends(get_db)):
    return crud.read_ingredients(db)


@app.post("/ingredients/", response_model=schemas.Ingredient)
async def create_ingredient(item: schemas.IngredientCreate, db: Session = fa.Depends(get_db)):
    return crud.create_ingredient(db, item)


@app.put("/ingredients/{ingredient_id}", response_model=schemas.Ingredient)
async def update_ingredient(ingredient_id: int, item: schemas.IngredientCreate, db: Session = fa.Depends(get_db)):
    return crud.update_ingredient(db, ingredient_id, item)


@app.delete("/ingredients/{ingredient_id}", response_model=tp.Union[schemas.RecipeRemovalError, schemas.ResultMessage])
async def delete_ingredient(ingredient_id: int, db: Session = fa.Depends(get_db)):
    return crud.delete_ingredient(db, ingredient_id)


@app.post("/recipes/", response_model=schemas.Recipe)
async def create_recipe(item: schemas.RecipeCreate, db: Session = fa.Depends(get_db)):
    return crud.create_recipe(db, item)


@app.get("/recipes/", response_model=tp.List[schemas.Recipe])
async def get_recipes(db: Session = fa.Depends(get_db)):
    return crud.read_recipes(db)


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
async def update_recipe(recipe_id: int, item: schemas.RecipeCreate, db: Session = fa.Depends(get_db)):
    return crud.update_recipe(db, recipe_id, item)


@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = fa.Depends(get_db)):
    return crud.delete_recipe(db, recipe_id)


@app.post("/recipes/{recipe_id}/ingredients/", response_model=schemas.Association)
async def create_recipe_ingredient(recipe_id: int, item: schemas.AssociationCreate, db: Session = fa.Depends(get_db)):
    return crud.create_recipe_ingredient(db, recipe_id, item)


@app.get("/recipes/{recipe_id}/ingredients/", response_model=tp.List[schemas.Association])
async def get_recipe_ingredients(recipe_id: int, db: Session = fa.Depends(get_db)):
    return crud.get_recipe_ingredients(db, recipe_id)


@app.put("/recipes/{recipe_id}/ingredients/{item_id}", response_model=schemas.Association)
async def update_recipe_ingredient(recipe_id: int, item_id: int, item: schemas.AssociationCreate, db: Session = fa.Depends(get_db)):
    return crud.update_recipe_ingredient(db, recipe_id, item_id, item)


@app.delete("/recipes/{recipe_id}/ingredients/{item_id}")
async def delete_recipe_ingredient(recipe_id: int, item_id: int, db: Session = fa.Depends(get_db)):
    return crud.delete_recipe_ingredient(db, recipe_id, item_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
