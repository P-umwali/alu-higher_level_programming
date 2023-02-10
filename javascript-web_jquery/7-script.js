#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (change) {
  $('#character').html(change.name);
});
