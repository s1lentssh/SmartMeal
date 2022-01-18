<template>
  <div class="ingredient">
    <div class="header-section button-holder">
      <h3>{{ item.ingredients_rel.name }}</h3>
      <span @click.stop="$emit('remove', item)" class="material-icons">
        delete_outline
      </span>
    </div>

    <div class="compare-sections">
      <img :src="item.ingredients_rel.image" />
      <div>
        <h4>100 g.</h4>
        <div class="info-text">
          <span class="fancy-number-header">Proteins </span>
          <span class="fancy-number">{{
            item.ingredients_rel.proteins.toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Fats </span>
          <span class="fancy-number">{{
            item.ingredients_rel.fats.toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Carbs </span>
          <span class="fancy-number">{{
            item.ingredients_rel.carbs.toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Calories </span>
          <span class="fancy-number">{{
            (
              item.ingredients_rel.carbs * 4 +
              item.ingredients_rel.proteins * 4 +
              item.ingredients_rel.fats * 9
            ).toFixed(0)
          }}</span>
        </div>
      </div>

      <div>
        <h4>Computed ({{ weight }} g.)</h4>
        <div class="info-text">
          <span class="fancy-number-header">Proteins </span>
          <span class="fancy-number">{{
            ((item.ingredients_rel.proteins / 100) * weight).toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Fats </span>
          <span class="fancy-number">{{
            ((item.ingredients_rel.fats / 100) * weight).toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Carbs </span>
          <span class="fancy-number">{{
            ((item.ingredients_rel.carbs / 100) * weight).toFixed(1)
          }}</span>
        </div>

        <div class="info-text">
          <span class="fancy-number-header">Calories </span>
          <span class="fancy-number">{{
            (
              ((item.ingredients_rel.proteins / 100) * 4 +
                (item.ingredients_rel.fats / 100) * 9 +
                (item.ingredients_rel.carbs / 100) * 4) *
              weight
            ).toFixed(0)
          }}</span>
        </div>
      </div>
    </div>

    <div class="input-section">
      <input
        type="number"
        v-model="weight"
        step="10"
        placeholder="Weight"
        @change="$emit('weight-update', item, weight)"
      />

      <input
        type="range"
        min="1"
        max="500"
        v-model="weight"
        @input="$emit('weight-update', item, weight)"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeEditorItem",
  props: ["item"],
  data: function () {
    return {
      weight: this.item.ingredient_weight,
    };
  },
};
</script>

<style scoped>
.header-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.button-holder > span {
  margin-left: 16px;
  background: #2364aa;
  color: white;
  border-radius: 50%;
  padding: 4px;
  font-size: 14px;
  cursor: pointer;
}

h3 {
  margin-bottom: 15px;
  font-size: 15px;
}

h4 {
  color: #444;
  font-size: 12px;
  margin-bottom: 4px;
}

.input-section {
  flex: auto;
  margin-top: 16px;
  display: flex;
}

input[type="number"] {
  border: none;
  border-radius: 4px;
  background: #eee;
  padding: 8px;
  width: 40px;
  margin-right: 16px;
}

input[type="range"] {
  flex: auto;
}

.ingredient {
  background: white;
  padding: 16px;
  border: 1px solid #ddd;
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  margin-bottom: 16px;
}

.info-text {
  margin-bottom: 4px;
  display: flex;
}

.compare-sections {
  display: flex;
}

.compare-sections > div {
  margin-right: 32px;
}

.fancy-number-header {
  width: 70px;
}

img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 16px;
  border: 1px solid #888;
}
</style>