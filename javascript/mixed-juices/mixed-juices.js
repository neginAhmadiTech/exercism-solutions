// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  let result

  switch (name) {
    case 'Pure Strawberry Joy':
      result = 0.5
      break;
    case 'Energizer':
      result = 1.5
      break;  
    case 'Green Garden':
      result = 1.5
      break; 
    case 'Tropical Island':
      result = 3
      break;
    case 'All or Nothing':
      result = 5
      break;
    default:
      result = 2.5
      break;
  }

  return result
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {

  let number = 0
  let i = 0

  while(i < limes.length && number < wedgesNeeded) {
    switch (limes[i]) {
      case 'small':
        number += 6;
        break;
      case 'medium':
        number += 8;
        break;
      case 'large':
        number += 10;
        break;    
    }
    i += 1;
  }

  return i 
}



/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {

  let i = 0
  let timeSpent = 0

  while (i < orders.length && timeSpent < timeLeft) {
    timeSpent += timeToMixJuice(orders[i])
    i++
  }

  return orders.slice(i)
}
