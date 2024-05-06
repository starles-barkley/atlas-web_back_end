export default function getStudentsByLocation(getListStudents, city) {
  if (!Array.isArray(studentList)) {
    return [];
  }
  return studentList.filter((student) => student.location === city);
}
