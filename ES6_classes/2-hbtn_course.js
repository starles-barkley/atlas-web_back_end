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
      throw new Error('Name must be a string.');
    }
  }
}