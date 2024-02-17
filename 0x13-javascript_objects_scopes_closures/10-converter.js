#!/usr/bin/node

exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return 'Invalid choice';
  }

  return function (number) {
    this.result = '';
    while (number > 0) {
      this.result = (number % base).toString(base).toUpperCase() + this.result;
      number = Math.floor(number / base);
    }

    return this.result;
  };
};
