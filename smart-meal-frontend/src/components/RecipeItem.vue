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
  display: flex;
  align-items: flex-start;
  border: 1px solid #ddd;
}

#recipe-item-root:hover {
  box-shadow: 0 2px 1px rgba(0, 0, 0, 0.2);
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
  margin-left: 16px;
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
  border: 1px solid #2364aa !important;
}
</style>