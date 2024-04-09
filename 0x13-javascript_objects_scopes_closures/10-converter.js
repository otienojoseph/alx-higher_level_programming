#!/usr/bin/node

exports.converter = function (base) {
  return function (b) {
    if (base) {
      return parseInt(b).toString(base);
    }
  };
};
