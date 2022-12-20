#!/usr/bin/node
exports.logMe = function foo (item) {
  if (typeof foo.alreadyPrinted === 'undefined') {
    foo.alreadyPrinted = 0;
  }
  console.log(`${foo.alreadyPrinted}: ${item}`);
  foo.alreadyPrinted++;
};
