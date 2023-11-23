var values = window.values
console.log(values)
var container = document.getElementById('myChart');
var selectGraph = document.getElementById('graph');

var myChart;

// Function to update the graph based on the selected attribute
function updateGraph(selectedAttribute) {
    var attributeData = values[selectedAttribute];

    // Extracting values and dates
    var vals = attributeData.value
    var dates = attributeData.date

    // Clear previous chart if exists
    if (myChart) {
        myChart.destroy();
    }

    // Create a new chart
    myChart = new Chart(container, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: selectedAttribute,
                data: vals,
                fill: false,
                borderColor: 'rgb(124, 30, 52)',
                tension: 0.1
            }]
        }
    });
}

// Event listener for select change
selectGraph.addEventListener('change', function () {
    var selectedAttribute = this.value;
    updateGraph(selectedAttribute);
});

// Initial graph creation based on the default selected value
updateGraph(selectGraph.value);





