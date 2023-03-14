#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let ch = c;
    if (!c) { ch = 'X'; }
    for (let i = this.height; i > 0; i--) {
      console.log(ch.repeat(this.width));
    }
  }
};
