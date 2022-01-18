<template>
  <div id="recipe-list-root">
    <button @click="$emit('add')">
      <span class="material-icons"> add </span>Add recipe
    </button>
    <recipe-item
      v-for="item in recipes"
      v-on:edit="$emit('edit', item)"
      v-on:remove="remove(item)"
      :selected="item.id === selected_id"
      :key="item"
      :data="item"
      @click="select(item)"
    />
  </div>
</template>

<script>
import RecipeItem from "./RecipeItem.vue";
import { methods } from "../store";

export default {
  components: { RecipeItem },
  name: "RecipeList",
  data: function () {
    return {
      recipes: [],
      selected_id: undefined,
    };
  },
  mounted: async function () {
    await this.update();
  },
  methods: {
    update: async function () {
      this.recipes = await methods.get_recipes();

      if (this.selected_id !== undefined) {
        const item = this.recipes.find((i) => i.id === this.selected_id);
        this.select(item);
      }
    },

    remove: async function (item) {
      if (item.id === this.selected_id) {
        this.select(undefined);
      }

      await methods.remove_recipe(item.id);
      await this.update();
    },

    select: function (item) {
      if (item !== undefined) {
        this.selected_id = item.id;
      } else {
        this.selected_id = undefined;
      }
      this.$emit("selected", item);
    },
  },
};
</script>

<style scoped>
#recipe-list-root {
  padding: 16px 8px;
  overflow-y: auto;
  height: 100%;
  flex: 1;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

#recipe-list-root::-webkit-scrollbar {
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