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

    function show_graph(buttonId) {
        console.log(buttonId)
        container.innerHTML = '';
        const canvas = document.createElement('canvas');
        container.appendChild(canvas);

        new Chart(canvas, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: buttonId,
                        data: all_values[buttonId],
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
    }
