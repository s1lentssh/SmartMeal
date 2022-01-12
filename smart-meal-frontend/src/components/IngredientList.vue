<template>
  <div id="ingredient-list-root">
    <button @click="$emit('add')">
      <span class="material-icons"> add </span>Add
    </button>
    <ingredient-item
      v-for="item in ingredients"
      v-on:edit="$emit('edit', item)"
      v-on:remove="remove(item)"
      :key="item"
      :data="item"
      @click="$emit('select', item)"
    />
  </div>
</template>

<script>
import IngredientItem from "./IngredientItem.vue";
import { methods } from "../store";

export default {
  components: { IngredientItem },
  name: "IngredientList",
  data: function () {
    return {
      ingredients: [],
    };
  },
  mounted: async function () {
    await this.update();
  },
  methods: {
    update: async function () {
      this.ingredients = await methods.get_ingredients();
    },

    remove: async function (item) {
      await methods.remove_ingredient(item.id);
      await this.update();
    },
  },
};
</script>

<style scoped>
#ingredient-list-root {
  width: 300px;
  padding: 16px;
}

button {
  width: 100%;
  padding: 16px;
  border-radius: 8px;
  border: none;
  margin-bottom: 16px;
  cursor: pointer;
  transition: 0.2s;
  background: #2364aa;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
}

button:hover {
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.3);
}

span {
  margin-right: 2px;
  font-size: 15px;
}
</style>