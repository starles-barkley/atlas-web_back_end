const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  if (!databasePath) {
    res.status(500).send('Cannot load the database');
    return;
  }

  countStudents(databasePath)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;