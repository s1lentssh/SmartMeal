from sqlalchemy.sql.expression import null
import uvicorn
import fastapi
import pydantic
import sqlalchemy
import databases
import typing
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://home",
    "http://home:8080",
]

DATABASE_URL = "sqlite:///./database.db"
metadata = sqlalchemy.MetaData()

db_ingredients = sqlalchemy.Table(
    "ingredients", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("image", sqlalchemy.String),
    sqlalchemy.Column("fats", sqlalchemy.Float),
    sqlalchemy.Column("carbs", sqlalchemy.Float),
    sqlalchemy.Column("proteins", sqlalchemy.Float),
)

db_recipes = sqlalchemy.Table(
    "recipes", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

db_recipes_ingredients = sqlalchemy.Table(
    "recipes_ingredients", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True, autoincrement=True),
    sqlalchemy.Column("recipe_id", sqlalchemy.ForeignKey(
        db_recipes.c.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
    sqlalchemy.Column("ingredient_id", sqlalchemy.ForeignKey(
        db_ingredients.c.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
    sqlalchemy.Column("ingredient_weight", sqlalchemy.Float)
)

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = databases.Database(DATABASE_URL)
db_engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={
                                     "check_same_thread": False})
metadata.create_all(db_engine)


class Ingredient(pydantic.BaseModel):
    id: int
    name: str
    description: typing.Optional[str]
    image: str
    fats: float
    carbs: float
    proteins: float


class Recipe(pydantic.BaseModel):
    id: int
    name: str


class RecipeIngredient(pydantic.BaseModel):
    id: int
    recipe_id: int
    ingredient_id: int
    ingredient_weight: float


@app.on_event("startup")
async def database_connect():
    await db.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await db.disconnect()


@app.get("/ingredients/", response_model=typing.List[Ingredient])
async def get_ingredients():
    query = db_ingredients.select()
    return await db.fetch_all(query)


@app.post("/ingredients/", response_model=Ingredient)
async def create_ingredient(item: Ingredient):
    query = db_ingredients.insert().values(
        name=item.name,
        description=item.description,
        image=item.image,
        fats=item.fats,
        carbs=item.carbs,
        proteins=item.proteins)
    record_id = await db.execute(query)
    return item.dict()


@app.put("/ingredients/", response_model=Ingredient)
async def update_ingredient(item: Ingredient):
    query = db_ingredients.update().where(db_ingredients.c.id == item.id).values(
        name=item.name,
        description=item.description,
        image=item.image,
        fats=item.fats,
        carbs=item.carbs,
        proteins=item.proteins)
    record_id = await db.execute(query)
    return item.dict()


@app.delete("/ingredients/{id}")
async def delete_ingredient(id: int):
    query = db_ingredients.delete().where(db_ingredients.c.id == id)
    record_id = await db.execute(query)
    return {"ok": True}


@app.get("/recipes/", response_model=typing.List[Recipe])
async def get_recipes():
    query = db_recipes.select()
    return await db.fetch_all(query)


@app.post("/recipes/", response_model=Recipe)
async def create_recipe(item: Recipe):
    query = db_recipes.insert().values(
        name=item.name)
    record_id = await db.execute(query)
    return item.dict()


@app.put("/recipes/", response_model=Recipe)
async def update_recipe(item: Recipe):
    query = db_recipes.update().where(db_recipes.c.id == item.id).values(
        name=item.name)
    record_id = await db.execute(query)
    return item.dict()


@app.delete("/recipes/{id}")
async def delete_recipe(id: int):
    query = db_recipes.delete().where(db_recipes.c.id == id)
    record_id = await db.execute(query)
    return {"ok": True}


@app.post("/recipes_ingredients/")
async def create_recipe_ingredient(item: RecipeIngredient):
    query = db_recipes_ingredients.insert().values(
        recipe_id=item.recipe_id,
        ingredient_id=item.ingredient_id,
        ingredient_weight=item.ingredient_weight)
    record_id = await db.execute(query)

    query = db_recipes_ingredients.select().column(db_ingredients).where(
        db_recipes_ingredients.c.recipe_id == item.recipe_id
    ).join(
        db_ingredients, db_ingredients.c.id == db_recipes_ingredients.c.ingredient_id
    )

    return (await db.fetch_all(query))[0]


@app.get("/recipes_ingredients/{recipe_id}")
async def get_recipes_ingredients(recipe_id: int):
    query = db_recipes_ingredients.select().column(db_ingredients).where(
        db_recipes_ingredients.c.recipe_id == recipe_id
    ).join(
        db_ingredients, db_ingredients.c.id == db_recipes_ingredients.c.ingredient_id
    )

    return await db.fetch_all(query)


@app.put("/recipes_ingredients/", response_model=RecipeIngredient)
async def update_recipe_ingredient(item: RecipeIngredient):
    query = db_recipes_ingredients.update().where(db_recipes_ingredients.c.id == item.id).values(
        recipe_id=item.recipe_id,
        ingredient_id=item.ingredient_id,
        ingredient_weight=item.ingredient_weight)
    record_id = await db.execute(query)
    return item.dict()


@app.delete("/recipes_ingredients/{id}")
async def delete_recipe_ingredient(id: int):
    query = db_recipes_ingredients.delete().where(db_recipes_ingredients.c.id == id)
    record_id = await db.execute(query)
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
