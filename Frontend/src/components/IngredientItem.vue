<template>
  <div id="ingredient-item-root">
    <div class="header-holder">
      <div class="image-holder">
        <img class="ingredient-image" :src="data.image" v-if="data.image" />
        <img
          class="ingredient-image"
          src="@/assets/chef.png"
          v-if="!data.image"
        />
      </div>
      <div class="info-holder">
        <h3>{{ data.name }}</h3>
        <p>{{ data.description }}</p>
      </div>
      <div class="button-holder">
        <span @click.stop="$emit('edit')" class="material-icons">
          edit_note
        </span>
        <span @click.stop="$emit('remove')" class="material-icons">
          delete_outline
        </span>
      </div>
    </div>

    <div class="info-text">
      <span>Proteins </span>
      <span class="fancy-number">{{ data.proteins }}</span>
    </div>
    <div class="info-text">
      <span>Fats </span>
      <span class="fancy-number">{{ data.fats }}</span>
    </div>
    <div class="info-text">
      <span>Carbs </span>
      <span class="fancy-number">{{ data.carbs }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "IngredientItem",
  props: ["data"],
};
</script>

<style scoped>
#ingredient-item-root {
  padding: 16px;
  cursor: pointer;
  background: #fff;
  margin-bottom: 16px;
  border-radius: 8px;
  transition: 0.5s;
  border: 1px solid #ddd;
}

#ingredient-item-root:hover {
  box-shadow: 0 2px 1px rgba(0, 0, 0, 0.2);
}

.ingredient-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1px solid #888;
}

.header-holder {
  display: flex;
  align-items: center;
  width: 100%;
}

.image-holder {
  margin-right: 16px;
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

h3 {
  font-size: 15px;
}

.info-holder > p {
  font-size: 14px;
  color: #444;
}

.info-text {
  margin-bottom: 4px;
}
</style>