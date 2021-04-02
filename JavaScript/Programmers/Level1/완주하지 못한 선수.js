function solution(participant, completion) {
  let answer = '';
  
  const plen = participant.length;
  
  participant.sort();
  completion.sort();
  
  for (let i = 0; i < plen; i++) {
      if (participant[i] !== completion[i]) {
          answer = participant[i]
          break
      }
  }
  
  return answer;
}