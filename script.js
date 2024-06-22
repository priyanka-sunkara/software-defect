var t = document.querySelector('#mytemplate');
// Populate the src attribute at runtime
t.content.querySelector('img').src = 'logo.png';
var clone = document.importNode(t.content, true);
document.body.appendChild(clone);
