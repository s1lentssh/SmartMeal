<template>
  <div id="recipe-item-root" v-bind:class="{ item_selected: selected }">
    <h3>{{ data.name }}</h3>
    <div class="button-holder">
      <span @click="$emit('edit')" class="material-icons"> edit_note </span>
      <span @click.stop="$emit('remove')" class="material-icons">
        delete_outline
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeItem",
  props: ["data", "selected"],
};
</script>

<style scoped>
#recipe-item-root {
  padding: 16px;
  cursor: pointer;
  background: #fff;
  margin-bottom: 16px;
  border-radius: 8px;
  transition: 0.2s;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: flex-start;
  border: 2px solid #fff;
}

#recipe-item-root:hover {
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

h3 {
  font-size: 15px;
}

.button-holder {
  margin-left: auto;
  display: flex;
  flex-direction: column;
}

.button-holder > span {
  background: #2364aa;
  color: white;
  border-radius: 50%;
  padding: 4px;
  font-size: 18px;
}

span:not(:last-child) {
  margin-bottom: 8px;
}

.item_selected {
  border: 2px solid #2364aa !important;
}
</style>