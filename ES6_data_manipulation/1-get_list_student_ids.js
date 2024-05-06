export default function getListStudentIds() {
  if (!Array.isArray(list)) {
    return[]
  }
  return list.map((student) => student.id);
}