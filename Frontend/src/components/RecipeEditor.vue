<template>
  <div id="recipe-editor-root" v-if="recipe">
    <div class="header">
      <h2>{{ recipe.name }}</h2>

      <h4>Computed</h4>
      <div class="info-text">
        <span class="fancy-number-header">Proteins </span>
        <span class="fancy-number">{{ totalProteins.toFixed(1) }}</span>
      </div>

      <div class="info-text">
        <span class="fancy-number-header">Fats </span>
        <span class="fancy-number">{{ totalFats.toFixed(1) }}</span>
      </div>

      <div class="info-text">
        <span class="fancy-number-header">Carbs </span>
        <span class="fancy-number">{{ totalCarbs.toFixed(1) }}</span>
      </div>

      <div class="info-text">
        <span class="fancy-number-header">Calories </span>
        <span class="fancy-number">{{ totalCalories.toFixed(0) }}</span>
      </div>
    </div>

    <recipe-editor-item
      v-for="item in ingredients"
      :key="item"
      :item="item"
      v-on:weight-update="onWeightUpdate"
      v-on:remove="onRemoveClicked"
    />
  </div>

  <div id="recipe-editor-root" v-else>
    <div class="empty">
      <p>Select a recipe</p>
    </div>
  </div>
</template>

<script>
import { constraints, methods } from "../store";
import RecipeEditorItem from "./RecipeEditorItem.vue";

export default {
  name: "RecipeEditor",
  components: { RecipeEditorItem },
  data: function () {
    return {
      recipe: undefined,
      ingredients: [],
      weightMap: {},
    };
  },
  methods: {
    bind: async function (recipe) {
      this.recipe = recipe;
      this.weightMap = {};

      if (recipe === undefined) {
        return;
      }

      this.ingredients = await methods.get_recipe_ingredients(this.recipe.id);

      for (let item of this.ingredients) {
        this.weightMap[item.id] = item.ingredient_weight;
      }
    },

    addIngredientToRecipe: async function (ingredient) {
      if (this.recipe === undefined) {
        return;
      }

      const response = await methods.add_recipe_ingredient(
        this.recipe.id,
        ingredient.id,
        constraints.defaultWeight
      );

      this.ingredients.push(response);
      this.weightMap[response.id] = response.ingredient_weight;
    },

    onWeightUpdate: async function (item, weight) {
      this.weightMap[item.id] = +weight;

      await methods.update_recipe_ingredient(
        item.recipes_rel.id,
        item.id,
        item.ingredients_rel.id,
        +weight
      );
    },

    onRemoveClicked: async function (item) {
      this.ingredients = this.ingredients.filter((it) => it.id !== item.id);
      await methods.remove_recipe_ingredient(item.recipes_rel.id, item.id);
    },
  },
  computed: {
    totalProteins: function () {
      return this.ingredients.reduce(
        (prev, cur) =>
          prev + (cur.ingredients_rel.proteins / 100) * this.weightMap[cur.id],
        0
      );
    },

    totalFats: function () {
      return this.ingredients.reduce(
        (prev, cur) =>
          prev + (cur.ingredients_rel.fats / 100) * this.weightMap[cur.id],
        0
      );
    },

    totalCarbs: function () {
      return this.ingredients.reduce(
        (prev, cur) =>
          prev + (cur.ingredients_rel.carbs / 100) * this.weightMap[cur.id],
        0
      );
    },

    totalCalories: function () {
      return this.totalProteins * 4 + this.totalFats * 9 + this.totalCarbs * 4;
    },
  },
};
</script>

<style scoped>
#recipe-editor-root {
  padding: 16px 8px;
  overflow-y: auto;
  height: 100%;
  flex: 2;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

#recipe-editor-root::-webkit-scrollbar {
  display: none;
}

h2 {
  font-size: 30px;
  margin-bottom: 8px;
}

h4 {
  color: #444;
  font-size: 12px;
  margin-bottom: 4px;
}

.header {
  margin-bottom: 16px;
  border: 1px solid #ddd;
  background: white;
  padding: 16px;
  border-radius: 8px;
}

.empty {
  margin-bottom: 16px;
  border: 2px dashed #ccc;
  padding: 64px;
  border-radius: 8px;
}

.empty > p {
  text-align: center;
  font-weight: 700;
  color: #aaa;
}

.info-text {
  margin-bottom: 4px;
  display: flex;
}

.fancy-number-header {
  width: 70px;
}
</style>