//
// This is only a SKELETON file for the 'Anagram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const findAnagrams = (word, words) => {
  let sortedWord = word.toLowerCase().split('').sort().join('')
  
  let result = []
  for (let i = 0; i < words.length; i++) {
    let element = words[i];

    if (word.toLowerCase() === element.toLowerCase()) {
      continue
    }
    
    let sortedElement = element.toLowerCase().split('').sort().join('')

    if (sortedWord === sortedElement) {
      result.push(element)
    }
  }
  return result
};


