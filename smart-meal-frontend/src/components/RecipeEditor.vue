<template>
  <div id="recipe-editor-root" v-if="data">
    <div class="header">
      <h2>{{ data.name }}</h2>

      <h4>Computed</h4>
      <div class="info-text">
        <span>Proteins </span>
        <span class="fancy-number">{{ totalProteins.toFixed(1) }}</span>
      </div>

      <div class="info-text">
        <span>Fats </span>
        <span class="fancy-number">{{ totalFats.toFixed(1) }}</span>
      </div>

      <div class="info-text">
        <span>Carbs </span>
        <span class="fancy-number">{{ totalCarbs.toFixed(1) }}</span>
      </div>
    </div>

    <recipe-editor-item
      v-for="item in ingredients"
      :key="item"
      :item="item"
      v-on:weight-update="onWeightUpdate"
      v-on:remove="remove"
    />
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
      data: undefined,
      ingredients: [],
      weightMap: {},
    };
  },
  methods: {
    bind: async function (data) {
      this.data = data;
      this.weightMap = {};

      const ingredients = await methods.get_recipe_ingredients(this.data.id);
      this.ingredients = ingredients;

      for (let item of ingredients) {
        this.weightMap[item.id] = item.ingredient_weight;
      }
    },

    addIngredient: async function (data) {
      const response = await methods.add_recipe_ingredient(
        this.data.id,
        data.id,
        constraints.defaultWeight
      );

      this.ingredients.push(response);
      this.weightMap[response.id] = response.ingredient_weight;

      console.log(response);
    },

    onWeightUpdate: async function (item, weight) {
      this.weightMap[item.id] = +weight;

      await methods.update_recipe_ingredient(
        item.id,
        item.recipe_id,
        item.ingredient_id,
        +weight
      );
    },

    remove: async function (data) {
      this.ingredients = this.ingredients.filter((item) => item.id !== data.id);
      console.log("Removing", data);
      await methods.remove_recipe_ingredient(data.id);
    },
  },
  computed: {
    totalProteins: function () {
      return this.ingredients.reduce(
        (prev, cur) => prev + (cur.proteins / 100) * this.weightMap[cur.id],
        0
      );
    },

    totalFats: function () {
      return this.ingredients.reduce(
        (prev, cur) => prev + (cur.fats / 100) * this.weightMap[cur.id],
        0
      );
    },

    totalCarbs: function () {
      return this.ingredients.reduce(
        (prev, cur) => prev + (cur.carbs / 100) * this.weightMap[cur.id],
        0
      );
    },
  },
};
</script>

<style scoped>
#recipe-editor-root {
  width: 500px;
  padding: 16px;
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

.info-text {
  margin-bottom: 4px;
}
</style>