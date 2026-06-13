//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  let numberStr = number.toString();
  let lastDigit = numberStr[numberStr.length - 1];
  let result = "";

  switch (lastDigit) {
    case "1":
      if (numberStr.length >= 2 && numberStr[numberStr.length - 2] === "1") {
        result += `${name}, you are the ${numberStr}th customer we serve today. Thank you!`;
        break;
      }
      result += `${name}, you are the ${numberStr}st customer we serve today. Thank you!`;
      break;
    case "2":
      if (numberStr.length >= 2 && numberStr[numberStr.length - 2] === "1") {
        result += `${name}, you are the ${numberStr}th customer we serve today. Thank you!`;
        break;
      }
      result += `${name}, you are the ${numberStr}nd customer we serve today. Thank you!`;
      break;
    case "3":
      if (numberStr.length >= 2 && numberStr[numberStr.length - 2] === "1") {
        result += `${name}, you are the ${numberStr}th customer we serve today. Thank you!`;
        break;
      }
      result += `${name}, you are the ${numberStr}rd customer we serve today. Thank you!`;
      break;
    default:
      result += `${name}, you are the ${numberStr}th customer we serve today. Thank you!`;
  }

  return result;
};
