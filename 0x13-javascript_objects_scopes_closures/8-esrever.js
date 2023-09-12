#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let ui = 0;
  while ((len - ui) > 0) {
    const aux = list[len];
    list[len] = list[ui];
    list[ui] = aux;
    ui++;
    len--;
  }
  return list;
};
