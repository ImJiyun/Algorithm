package coding_test;

import java.util.Arrays;

public class Array01_Sorting {
    public static void main(String[] args) {
        int[] arr = {1, -5, 2, 4, 3};
        sortArr(arr);

        int[] arr2 = {2, 1, 1, 3, 2, 5, 4};
        sortArr(arr2);

        int[] arr3 = {1, 6, 7};
        sortArr(arr3);

    }

    static void sortArr(int[] arr) {
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
