function solution(numbers) {
  let answer = [];
  const n = numbers.length;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let sum = numbers[i] + numbers[j]
      if (!answer.includes(sum)) {
        answer.push(sum);
      }
    }
  }

  answer.sort((a, b) => a - b);

  return answer;
}