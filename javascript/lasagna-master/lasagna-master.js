/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */


/**
 * It returns several messages based on the
 * remaining time of the timer
 * 
 * @param {number | undefined} remainingTime 
 * @returns {string}
 */
export function cookingStatus(remainingTime) {
    if (remainingTime === 0) {
        return 'Lasagna is done.'
    }
    if (remainingTime === undefined) {
        return 'You forgot to set the timer.'
    }
    return 'Not done, please wait.'
}


/**
 * 
 * Calculates the total estimation time
 * based on given layers and preperation time
 * 
 * @param {Array<string>} layers 
 * @param {number | undefined} preparationTime 
 * 
 * @returns {number}
 */
export function preparationTime(layers, preparationTime = 2) {
    return layers.length * preparationTime
}


/**
 * 
 * calculates the quantity of noodles
 * and sauce in the layers array
 * 
 * @param {Array<string>} layers 
 * 
 * @returns {{noodles: number, sauce: number}}
 */
export function quantities(layers) {

    let noodlesQuantity = 0
    let sauceQuantity = 0

    for (let number = 0; number < layers.length; number++) {
        const layer = layers[number];

        if (layer === 'sauce') {
            sauceQuantity += 0.2
        }

        if (layer === 'noodles') {
            noodlesQuantity += 50
        }
        
    }
    return { noodles: noodlesQuantity, sauce: sauceQuantity }
}



/**
 * 
 * 
 * Add the last ingredient from the given list
 * of the ingredients to my list of ingrdients
 * 
 * 
 * @param {Array<string>} givenIngredients 
 * @param {Array<string>} myIngredients 
 */
export function addSecretIngredient(givenIngredients, myIngredients) {
    myIngredients.push(givenIngredients[givenIngredients.length - 1])
}


/**
 * @typedef {Object} Recipe
 * @property {number} noodles
 * @property {number} sauce
 * @property {number} mozzarella
 * @property {number} meat
 */

/**
 * 
 * @param {Recipe} recipe 
 * @param {number} portionsCount 
 * @returns {Recipe}
 */
export function scaleRecipe(recipe, portionsCount) {

    let result = Object.assign({}, recipe)

    for (let ingredient in result) {
        let key = ingredient;
        result[key] *= (portionsCount / 2); 
    }
    
    return result
}


