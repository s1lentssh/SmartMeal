<template>
  <main-header />

  <div id="main-content">
    <ingredient-list
      v-on:add="showIngredientModal"
      v-on:edit="showIngredientModal"
      v-on:select="addIngredientToRecipe"
      ref="ingredientList"
    />

    <recipe-list
      v-on:add="showRecipeModal"
      v-on:edit="showRecipeModal"
      v-on:selected="editRecipe"
      ref="recipeList"
    />

    <ingredient-modal
      v-on:close="closeIngredientModal()"
      v-show="ingredientModalVisible"
      ref="ingredientModal"
    />

    <recipe-modal
      v-on:close="closeRecipeModal()"
      v-show="recipeModalVisible"
      ref="recipeModal"
    />

    <recipe-editor ref="recipeEditor" />
  </div>
</template>

<script>
import IngredientModal from "./components/IngredientModal.vue";
import IngredientList from "./components/IngredientList.vue";
import RecipeModal from "./components/RecipeModal.vue";
import RecipeList from "./components/RecipeList.vue";
import RecipeEditor from "./components/RecipeEditor.vue";
import MainHeader from "./components/MainHeader.vue";

export default {
  name: "App",
  components: {
    IngredientList,
    IngredientModal,
    RecipeList,
    RecipeModal,
    RecipeEditor,
    MainHeader,
  },
  methods: {
    closeIngredientModal: async function () {
      this.ingredientModalVisible = false;
      this.$refs.ingredientModal.clear();
      await this.$refs.ingredientList.update();
    },
    closeRecipeModal: async function () {
      this.recipeModalVisible = false;
      this.$refs.recipeModal.clear();
      await this.$refs.recipeList.update();
    },
    showIngredientModal: async function (data) {
      this.ingredientModalVisible = true;

      if (data) {
        this.$refs.ingredientModal.bind(data);
      }
    },
    showRecipeModal: async function (data) {
      this.recipeModalVisible = true;

      if (data) {
        this.$refs.recipeModal.bind(data);
      }
    },
    editRecipe: async function (item) {
      await this.$refs.recipeEditor.bind(item);
    },
    addIngredientToRecipe: function (item) {
      this.$refs.recipeEditor.addIngredientToRecipe(item);
    },
  },
  data: function () {
    return {
      ingredientModalVisible: false,
      recipeModalVisible: false,
    };
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

html,
body {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

#app {
  font-family: "Lato", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;

  background: #eee;
}

.fancy-number {
  background: #ccc;
  border-radius: 4px;
  padding: 2px 4px;
  color: #555;
  font-size: 12px;
  border: 1px solid #777;
}

#main-content {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 64px;
  height: calc(100% - 80px);
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}
</style>
