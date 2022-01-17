import axios from "axios";

const server = 'http://home:8000'

const constraints = {
    defaultWeight: 50
}

const methods = {
    // Ingredients

    get_ingredients: async () => {
        const response = await axios.get(`${server}/ingredients/`);
        return response.data;
    },

    create_ingredient: async (name, description, image, fats, carbs, proteins) => {
        const params = {
            name: name,
            description: description,
            image: image,
            fats: fats,
            carbs: carbs,
            proteins: proteins
        };
        const response = await axios.post(`${server}/ingredients/`, params);
        return response.data;
    },

    update_ingredient: async (id, name, description, image, fats, carbs, proteins) => {
        const params = {
            name: name,
            description: description,
            image: image,
            fats: fats,
            carbs: carbs,
            proteins: proteins
        };
        const response = await axios.put(`${server}/ingredients/${id}`, params);
        return response.data;
    },

    remove_ingredient: async (id) => {
        const response = await axios.delete(`${server}/ingredients/${id}`);
        return response.data;
    },

    // Recipes

    get_recipes: async () => {
        const response = await axios.get(`${server}/recipes/`);
        return response.data;
    },

    create_recipe: async (name) => {
        const params = {
            name: name
        };
        const response = await axios.post(`${server}/recipes/`, params);
        return response.data;
    },

    update_recipe: async (id, name) => {
        const params = {
            name: name
        };
        const response = await axios.put(`${server}/recipes/${id}`, params);
        return response.data;
    },

    remove_recipe: async (id) => {
        const response = await axios.delete(`${server}/recipes/${id}`);
        return response.data;
    },

    // Recipes ingredients

    add_recipe_ingredient: async (recipe_id, ingredient_id, ingredient_weight) => {
        const params = {
            ingredient_id: ingredient_id,
            ingredient_weight: ingredient_weight
        };
        const response = await axios.post(`${server}/recipes/${recipe_id}/ingredients/`, params);
        return response.data;
    },

    get_recipe_ingredients: async (recipe_id) => {
        const response = await axios.get(`${server}/recipes/${recipe_id}/ingredients/`);
        return response.data;
    },

    update_recipe_ingredient: async (recipe_id, item_id, ingredient_id, ingredient_weight) => {
        const params = {
            ingredient_id: ingredient_id,
            ingredient_weight: ingredient_weight
        };
        const response = await axios.put(`${server}/recipes/${recipe_id}/ingredients/${item_id}`, params);
        return response.data;
    },

    remove_recipe_ingredient: async (recipe_id, item_id) => {
        const response = await axios.delete(`${server}/recipes/${recipe_id}/ingredients/${item_id}`);
        return response.data;
    }
}

export {
    methods,
    constraints
}