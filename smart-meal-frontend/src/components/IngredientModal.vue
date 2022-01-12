<template>
  <div id="add-ingredient-modal-root">
    <div id="add-ingredient-modal-root-inner">
      <h2>Add ingredient</h2>

      <p>Name</p>
      <input type="text" v-model="name" placeholder="Ingredient name" />

      <p>Description</p>
      <input
        type="text"
        v-model="description"
        placeholder="Ingredient description"
      />

      <p>Image</p>
      <input
        type="text"
        v-model="image"
        placeholder="URL of ingredient image"
      />

      <p>Proteins</p>
      <input
        type="number"
        v-model="proteins"
        step="0.1"
        placeholder="Proteins on 100 g."
      />

      <p>Fats</p>
      <input
        type="number"
        v-model="fats"
        step="0.1"
        placeholder="Fats on 100 g."
      />

      <p>Carbs</p>
      <input
        type="number"
        v-model="carbs"
        step="0.1"
        placeholder="Carbs on 100 g."
      />

      <div id="button-segment">
        <button id="button-save" @click="save">Save</button>
        <button id="button-discard" @click="close">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import { methods } from "../store";

export default {
  name: "IngredientModal",
  data: function () {
    return {
      id: undefined,
      name: "",
      description: "",
      image: "",
      proteins: undefined,
      fats: undefined,
      carbs: undefined,
    };
  },
  methods: {
    save: async function () {
      if (this.id !== undefined) {
        await methods.update_ingredient(
          this.id,
          this.name,
          this.description,
          this.image,
          this.fats,
          this.carbs,
          this.proteins
        );
      } else {
        await methods.create_ingredient(
          this.name,
          this.description,
          this.image,
          this.fats,
          this.carbs,
          this.proteins
        );
      }

      this.clear();
      this.$emit("close");
    },

    close: function () {
      this.clear();
      this.$emit("close");
    },

    bind: function (data) {
      this.name = data.name;
      this.description = data.description;
      this.image = data.image;
      this.fats = data.fats;
      this.carbs = data.carbs;
      this.proteins = data.proteins;
      this.id = data.id;
    },

    clear: function () {
      this.name = "";
      this.description = "";
      this.image = "";
      this.proteins = undefined;
      this.fats = undefined;
      this.carbs = undefined;
      this.id = undefined;
    },
  },
};
</script>

<style scoped>
#add-ingredient-modal-root {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
}

#add-ingredient-modal-root-inner {
  background: white;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 0px 20px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-bottom: 16px;
}

p {
  margin-top: 16px;
  margin-bottom: 4px;
}

input[type="text"],
input[type="number"] {
  border: none;
  border-radius: 4px;
  background: #eee;
  padding: 8px;
  width: calc(100% - 16px);
}

#button-segment {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 8px;
}

button {
  border-radius: 8px;
  border: none;
  padding: 8px 16px;
  margin: 8px;
  cursor: pointer;
}

#button-save {
  background: #2364aa;
  color: white;
}

#button-discard {
  background: #fff;
  border: 1px solid #ddd;
}
</style>