#!/usr/bin/node

exports.esrever = function (list) {
  const listCopy = [...list];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    list[j] = listCopy[i];
  }
  return list;
};
