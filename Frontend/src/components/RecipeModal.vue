<template>
  <div id="add-recipe-modal-root">
    <div id="add-recipe-modal-root-inner">
      <h2>Add recipe</h2>

      <p>Name</p>
      <input type="text" v-model="name" placeholder="Recipe name" />

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
  name: "recipeModal",
  data: function () {
    return {
      id: undefined,
      name: "",
    };
  },
  methods: {
    save: async function () {
      if (this.id !== undefined) {
        await methods.update_recipe(this.id, this.name);
      } else {
        await methods.create_recipe(this.name);
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
      this.id = data.id;
    },

    clear: function () {
      this.name = "";
      this.id = undefined;
    },
  },
};
</script>

<style scoped>
#add-recipe-modal-root {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
}

#add-recipe-modal-root-inner {
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