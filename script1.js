document.addEventListener('DOMContentLoaded', function () {
    vegaEmbed('#bar_chart', 'chart1.json').catch(console.error);
    vegaEmbed('#scatter_plot', 'chart2.json').catch(console.error);
    vegaEmbed('#political', 'chart3.json').catch(console.error);
    vegaEmbed('#map_chart', 'chart4.json').catch(console.error);
    vegaEmbed('#legal', 'chart5.json').catch(console.error);
    vegaEmbed('#safety', 'chart6.json').catch(console.error);
    vegaEmbed('#culture', 'chart7.json').catch(console.error);
    vegaEmbed('#freedom', 'chart8.json').catch(console.error);
    vegaEmbed('#comparison', 'chart9.json').catch(console.error);



});
