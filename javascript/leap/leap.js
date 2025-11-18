//
// This is only a SKELETON file for the 'Leap' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isLeap = (year) => {

  let result = false
  if (year % 4 === 0) {
    result = true
    if (year % 100 === 0) {
      result = false
      if (year % 400 === 0) {
        result = true
      }
    }
  }

  return result
};
