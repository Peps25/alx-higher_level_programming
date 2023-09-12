#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let ui = 0; ui < list.length; ui++) {
    if (searchElement === list[ui]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
