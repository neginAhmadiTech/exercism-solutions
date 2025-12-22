//
// This is only a SKELETON file for the 'Space Age' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const age = (planet, seconds) => {
  const earthAge = seconds / 31557600;

  let result;

  switch (planet) {
    case "mercury":
      result = (earthAge / 0.2408467).toFixed(2);
      break;
    case "venus":
      result = (earthAge / 0.61519726).toFixed(2);
      break;
    case "earth":
      result = (earthAge / 1.0).toFixed(2);
      break;
    case "mars":
      result = (earthAge / 1.8808158).toFixed(2);
      break;
    case "jupiter":
      result = (earthAge / 11.862615).toFixed(2);
      break;
    case "saturn":
      result = (earthAge / 29.447498).toFixed(2);
      break;
    case "uranus":
      result = (earthAge / 84.016846).toFixed(2);
      break;
    case "neptune":
      result = (earthAge / 164.79132).toFixed(2);
      break;

    default:
      throw new Error("not a planet");
  }

  return Number(result);
};
