document.addEventListener('DOMContentLoaded', function () {

    const labels = window.graphData.labels;

    const all_values = {
        'HB': window.graphData.hb, 
        'HCT': window.graphData.hct, 
        'RBC': window.graphData.rbc, 
        'MCV': window.graphData.mcv, 
        'MCH': window.graphData.mch, 
        'MCHC': window.graphData.mchc, 
        'WBC': window.graphData.wbc, 
        'PLT': window.graphData.plt, 
    }

    const container = document.getElementById('graphContainer');

    // Create an object to store references to graph instances
    const graphs = {};
    // Maintain a list of created canvas elements
    const canvases = {};

    // Add event listeners to checkboxes
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            const attribute = checkbox.id // Get CBC attribute from checkbox ID

            // Check if the checkbox is checked
            if (checkbox.checked) {
                // If checked, create a new canvas and chart
                const ctx = document.createElement('canvas');
                container.appendChild(ctx);
                canvases[attribute] = ctx;

                graphs[attribute] = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                label: attribute,
                                data: all_values[attribute],
                                borderColor: 'rgba(75, 192, 192, 1)',
                                borderWidth: 2,
                                fill: false,
                                hidden: false,
                            },
                        ],
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'category',
                            },
                            y: {
                                beginAtZero: true,
                            },
                        },
                    },
                });
            } else {
                if (graphs[attribute]){
                    graphs[attribute].destroy();
                    delete graphs[attribute];

                    // Remove the associated canvas element
                    if(canvases[attribute]){
                        canvases[attribute].remove()
                    }

                }
            }
        });
    });
});