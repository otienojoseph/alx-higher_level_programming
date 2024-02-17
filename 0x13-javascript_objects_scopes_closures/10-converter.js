#!/usr/bin/node

exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return 'Invalid choice';
  }

  function baseConverter (number) {
    let result = '';
    while (number > 0) {
      const remainder = number % base;
      result = remainder.toString(base).toUpperCase() + result;
      number = Math.floor(number / base);
    }

    return result || 'O';
  }
  return baseConverter;
};
