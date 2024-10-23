const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.trim().split('\n');

      const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

      let result = `Number of students: ${students.length}\n`;
      const fields = {};

      students.forEach((student) => {
        const [firstname, lastname, age, field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      for (const [field, names] of Object.entries(fields)) {
        result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      console.log(result.trim());
      return result.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
