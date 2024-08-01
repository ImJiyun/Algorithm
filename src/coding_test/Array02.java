package coding_test;

import java.util.*;

public class Array02 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{4, 2, 2, 1, 3, 4})));
        System.out.println(Arrays.toString(solution(new int[] {2, 1, 1, 3, 2, 5, 4})));
    }

    static int[] solution(int[] arr) {
        // int array를 Integer array로 변환
        Integer[] newArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        // 내림차순 정렬
        Arrays.sort(newArr, Collections.reverseOrder());
        // Integer array를 int array로 변환
        int[] intArray = Arrays.stream(newArr).mapToInt(Integer::intValue).toArray();
        // 중복된 값을 제거하기 위해 set 선언
        LinkedHashSet<Integer> set = new LinkedHashSet<>();
        // int array에 있던 값을 set에 추가함으로써 중복된 값 제거
        for (int i = 0; i < intArray.length; i++) {
            set.add(intArray[i]);
        }
        // answer array 선언
        int[] answer = new int[set.size()];
        int index = 0;
        // iterator를 이용해 set에 있던 값을 answer array에 넣어주기
        Iterator<Integer> itr = set.iterator();
        while (itr.hasNext()) {
            answer[index++] = itr.next();
        }
        return answer;
    }
}
