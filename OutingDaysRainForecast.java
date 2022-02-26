package FebruaryAmazon;

import java.util.ArrayList;
import java.util.List;
//https://leetcode.com/discuss/interview-question/algorithms/1520406/Amazon-OA-count-the-outing-days/1120226
public class OutingDaysRainForecast {

   // Time O(n), Space: O(n)
   public static List<Integer> solve(int[] day, int k) {
      
	   int n = day.length;
      int[] left = new int[n], right = new int[n];
      
      // how many days before me are non increasing?
      for (int i = 1; i < n; i++) {
         if (day[i-1] >= day[i]) 
        	 left[i] = left[i-1] + 1; 
      }
      
      // how many days after me are non decreasing
      for (int i = n-2; i >= 0; i--) {
         if (day[i+1] >= day[i]) 
        	 right[i] = right[i+1] + 1;
      }
      
      List<Integer> res = new ArrayList<>();
      for (int i = 0; i < n; i++) {
         if (left[i] >= k && right[i] >= k) 
        	 res.add(i+1); // an ideal day from both sides
      }
      
      return res;
   }

   public static void main(String...args) {
      System.out.println("Expected: [3, 4], Actual: " + solve(new int[] {3,2,2,2,3,4}, 2));
      System.out.println("Expected: [2, 4], Actual: " + solve(new int[] {1,0,1,0,1}, 1));
      System.out.println("Expected: [3], Actual: " + solve(new int[] {1,0,0,0,1}, 2));
      System.out.println("Expected: [4, 5, 6, 7], Actual: " + solve(new int[] {1,1,1,1,1,1,1,1,1,1}, 3));
   }
}