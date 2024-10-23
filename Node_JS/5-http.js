const http = require('http');
const fs = require('fs');
const path = require('path');

const app = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
        res.statusCode = 200;
        res.end('Hello Holberton School!\n');
    } else if (req.url === '/students') {
        res.statusCode = 200;
        res.write('This is the list of our students\n');
        
        const database = process.argv[2]; // Assume the database is passed as a command-line argument
        if (!database) {
            res.end('No database provided\n');
            return;
        }

        fs.readFile(database, 'utf8', (err, data) => {
            if (err) {
                res.statusCode = 500;
                res.end(`Error reading file: ${err.message}\n`);
                return;
            }

            const students = data.split('\n')
                .filter(line => line.trim() !== '') // Remove empty lines
                .map(line => line.split(',')[0]) // Assuming the first column is the student's name
                .filter(name => name); // Ensure we only get valid names
            
            res.end(students.join('\n') + '\n');
        });
    } else {
        res.statusCode = 404;
        res.end('Not Found\n');
    }
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
