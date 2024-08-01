package coding_test;

import java.util.*;

public class Array03 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[] {2, 1, 3, 4, 1})));
        System.out.println(Arrays.toString(solution(new int[] {5, 0, 2, 7})));
    }

    static int[] solution(int[] numbers) {
        int index = 0;
        // 두 수의 합을 담을 Set (중복 제거를 위해)
        Set<Integer> sums = new HashSet<>();
        // i : 기준 인덱스 (0부터 마지막 인덱스 - 1 까지)
        for (int i = index; i < numbers.length - 1; i++) {
            // j : (i + 1) ~ (마지막 인덱스 - 1)
            for (int j = i + 1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                sums.add(sum);
                index++;
            }
        }
        // Set을 Array로 변환
        Integer[] answer = sums.toArray(new Integer[0]);
        // Integer array를 int array로 변환해서 return
        return Arrays.stream(answer).mapToInt(Integer::intValue).toArray();

    }
}
