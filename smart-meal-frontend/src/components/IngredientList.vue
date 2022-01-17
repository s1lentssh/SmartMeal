<template>
  <div id="ingredient-list-root">
    <button @click="$emit('add')">
      <span class="material-icons"> add </span>Add ingredient
    </button>
    <ingredient-item
      v-for="item in ingredients"
      v-on:edit="$emit('edit', item)"
      v-on:remove="removeIngredient(item)"
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

    removeIngredient: async function (item) {
      const response = await methods.remove_ingredient(item.id);

      switch (response.result) {
        case "ok":
          await this.update();
          break;

        case "error": {
          let errorMessage = "Ingredient used in\n";

          for (let relation of response.relations) {
            errorMessage = errorMessage.concat(
              " - ",
              relation.recipes_rel.name,
              "\n"
            );
          }

          alert(errorMessage);
          break;
        }
      }
    },
  },
};
</script>

<style scoped>
#ingredient-list-root {
  padding: 16px 8px;
  overflow-y: auto;
  height: 100%;
  flex: 1;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

#ingredient-list-root::-webkit-scrollbar {
  display: none;
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
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.2);
}

button:hover {
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
}

span {
  margin-right: 2px;
  font-size: 15px;
}
</style>