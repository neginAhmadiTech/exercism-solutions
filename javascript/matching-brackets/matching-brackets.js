//
// This is only a SKELETON file for the 'Matching Brackets' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPaired = (text) => {
  const brackets = ["(", "[", "{"];

  let result = [];

  for (let i = 0; i < text.length; i++) {
    const element = text[i];

    if (brackets.includes(element)) {
      result.push(element);
    } else if (element === ")") {
      if (result.pop() !== "(") return false;
    } else if (element === "]") {
      if (result.pop() !== "[") return false;
    } else if (element === "}") {
      if (result.pop() !== "{") return false;
    }
  }
  return result.length === 0;
};
