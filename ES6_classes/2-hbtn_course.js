class HolbertonCourse {
  constructor(name, length, students) {
    this._name = typeof name === 'string' ? name : '';
    this._length = typeof length === 'number' ? length : 0;
    this._students = Array.isArray(students) ? students : [];
  }
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this.name = newName;
    } else {
      throw TypeError('Name must be a string.');
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this ._length = newLength;
    } else {
      throw TypeError('Length must be a number.');
    }
  }

  get students () {
    return this._students;
  }

  set students (newStudents) {
    if (Array.isArray(newStudents)) {
      this._students = newStudents;
    } else {
      throw TypeError('Students must be an array.')
    }
  }
}
