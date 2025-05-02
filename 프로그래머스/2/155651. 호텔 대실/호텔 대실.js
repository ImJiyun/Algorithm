function solution(book_time) {
  function toMinutes(timeStr) {
    const [hours, minutes] = timeStr.split(":").map(Number);
    return hours * 60 + minutes;
  }

  book_time.sort((a, b) => toMinutes(a[0]) - toMinutes(b[0]));

  const rooms = [];

  for (let [start, end] of book_time) {
    const startMin = toMinutes(start);
    const endMin = toMinutes(end) + 10; 

    let assigned = false;

    for (let i = 0; i < rooms.length; i++) {
      if (rooms[i] <= startMin) {
        rooms[i] = endMin;
        assigned = true;
        break;
      }
    }

    if (!assigned) {
      // 새 방이 필요함
      rooms.push(endMin);
    }
  }

  return rooms.length;
}