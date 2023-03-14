#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentValue) =>
    searchElement === currentValue ? accumulator + 1 : accumulator, 0);
};
