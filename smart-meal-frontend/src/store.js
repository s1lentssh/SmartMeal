import axios from "axios";

const server = 'http://home:8000'

const constraints = {
    defaultWeight: 50
}

const methods = {
    get_ingredients: async () => {
        const response = await axios.get(`${server}/ingredients/`);
        return response.data;
    },

    create_ingredient: async (name, description, image, fats, carbs, proteins) => {
        const params = {
            id: -1,
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
            id: id,
            name: name,
            description: description,
            image: image,
            fats: fats,
            carbs: carbs,
            proteins: proteins
        };
        const response = await axios.put(`${server}/ingredients/`, params);
        return response.data;
    },

    remove_ingredient: async (id) => {
        const response = await axios.delete(`${server}/ingredients/${id}`);
        return response.data;
    },

    get_recipes: async () => {
        const response = await axios.get(`${server}/recipes/`);
        return response.data;
    },

    create_recipe: async (name) => {
        const params = {
            id: -1,
            name: name
        };
        const response = await axios.post(`${server}/recipes/`, params);
        return response.data;
    },

    update_recipe: async (id, name) => {
        const params = {
            id: id,
            name: name
        };
        const response = await axios.put(`${server}/recipes/`, params);
        return response.data;
    },

    remove_recipe: async (id) => {
        const response = await axios.delete(`${server}/recipes/${id}`);
        return response.data;
    },

    add_recipe_ingredient: async (recipe_id, ingredient_id, ingredient_weight) => {
        const params = {
            id: -1,
            recipe_id: recipe_id,
            ingredient_id: ingredient_id,
            ingredient_weight: ingredient_weight
        };
        const response = await axios.post(`${server}/recipes_ingredients/`, params);
        return response.data;
    },

    get_recipe_ingredients: async (recipe_id) => {
        const response = await axios.get(`${server}/recipes_ingredients/${recipe_id}`);
        return response.data;
    },

    update_recipe_ingredient: async (id, recipe_id, ingredient_id, ingredient_weight) => {
        const params = {
            id: id,
            recipe_id: recipe_id,
            ingredient_id: ingredient_id,
            ingredient_weight: ingredient_weight
        };
        const response = await axios.put(`${server}/recipes_ingredients/`, params);
        return response.data;
    },

    remove_recipe_ingredient: async (id) => {
        const response = await axios.delete(`${server}/recipes_ingredients/${id}`);
        return response.data;
    }
}

export {
    methods,
    constraints
}