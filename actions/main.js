function template(param) {
  return `
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Probe Your Game</title>
      </head>
    
      <body>
        <h1>Zelda</h1>
        <label> the legend of zelda breath of the wild</label>
        <p>${!param || !param?.[0] ? "pas de data" : param[0].author}</p>
      </body>
      <script>
        console.log("param",${param});
      </script>  
    </html>`;
}

function main(param) {
  const dataset_rawg = param.dataset_rawg;
  const dataset_metacritic = param.dataset_metacritic;
  const renderTemplate = template(dataset_metacritic.concat(dataset_rawg));
  return {
    statusCode: 200,
    body: renderTemplate,
  };
}
module.exports = main;
