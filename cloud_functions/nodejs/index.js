const  functions = require('@google-cloud/functions-framework')

functions.http('hellohttp', (req, res) => { 
  res.send('Hello got request')
})