<template>
  <div id="main-header-root">
    <p>Weight</p>
    <input type="number" v-model="weight" step="1" placeholder="Weight" />

    <p>Mode</p>
    <select v-model="mode">
      <option value="hwl">Hard weight loss</option>
      <option value="ewl">Easy weight loss</option>
      <option value="def">Default</option>
      <option value="emg">Easy mass gathering</option>
      <option value="hmg">Hard mass gathering</option>
    </select>

    <p>Proteins</p>
    <span class="fancy-number">{{ proteins.toFixed(1) }}</span>
    <p>Fats</p>
    <span class="fancy-number">{{ fats.toFixed(1) }}</span>
    <p>Carbs</p>
    <span class="fancy-number">{{ carbs.toFixed(1) }}</span>
  </div>
</template>

<script>
export default {
  name: "MainHeader",
  data: function () {
    return {
      weight: 0,
      mode: "def",
    };
  },
  computed: {
    calories: function () {
      switch (this.mode) {
        case "hwl":
          return 26 * this.weight;
        case "ewl":
          return 29 * this.weight;
        case "def":
          return 34 * this.weight;
        case "emg":
          return 40 * this.weight;
        case "hmg":
          return 45 * this.weight;
      }

      return 0;
    },
    proteins: function () {
      const day_calories_proteins = this.calories * 0.3;
      return day_calories_proteins / 4;
    },

    fats: function () {
      const day_calories_fats = this.calories * 0.1;
      return day_calories_fats / 9;
    },

    carbs: function () {
      const day_calories_carbs = this.calories * 0.6;
      return day_calories_carbs / 4;
    },
  },
};
</script>

<style scoped>
#main-header-root {
  background: #222;
  border-radius: 8px;
  height: 60px;
  width: calc(100% - 16px);
  top: 8px;
  left: 8px;
  margin-bottom: 16px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.15);
}

p {
  color: white;
  margin: 8px;
  margin-left: 32px;
}

input[type="number"] {
  border: none;
  border-radius: 8px;
  padding: 8px;
  width: 50px;
}

label {
  color: white;
  margin-right: 8px;
  margin-left: 4px;
}

select {
  border: none;
  border-radius: 8px;
  padding: 8px;
  background: white;
}

option {
  border-radius: 8px;
}
</style>