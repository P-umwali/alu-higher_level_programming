#!/usr/bin/node
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (fetch) {
  $('#hello').text(fetch.hello);
});
