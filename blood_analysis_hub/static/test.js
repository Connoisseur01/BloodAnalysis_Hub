const units = window.units; 
var shown = window.shown;
console.log(shown)
var addValueBtn = document.getElementById('add-value-btn');
var form = document.getElementById('form');
var selectAttribute = document.getElementById('select-attribute');


addValueBtn.addEventListener('click', function() {
    var attribute = selectAttribute.value;
    if (shown.indexOf(attribute) === -1){
        shown.push(attribute)
        var newInputFieldGroup = document.createElement('div');
        newInputFieldGroup.classList.add('form-group');

        var label = document.createElement('label');
        label.classList.add('form-label');
        label.textContent = attribute;

        var inputField = document.createElement('input');
        inputField.setAttribute('type', 'number');
        inputField.setAttribute('name', attribute);

        var unit = document.createElement('p');
        unit.textContent = units[attribute];

        newInputFieldGroup.appendChild(label);
        newInputFieldGroup.appendChild(inputField);
        newInputFieldGroup.appendChild(unit);


        form.appendChild(newInputFieldGroup);
    }
});