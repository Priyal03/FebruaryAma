package FebruaryAmazon;
//https://leetcode.com/discuss/interview-question/1779795/Amazon-or-OA-1-or-SDE-Summer-Intern-2022
//took the ans from GFG   https://www.geeksforgeeks.org/count-of-buttons-pressed-in-a-keypad-mobile/


public class MinimumKeypadClickCount {

	static final int arr[] = { 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4 };

// Function to return the count of
// buttons pressed to type the given string
	public static int countKeyPressed(String str, int len) {
		
		int count = 0;

// Count the key presses
		for (int i = 0; i < len; i++)
			count = count + arr[str.charAt(i) - 'a'];

// Return the required count
		return count;
	}

// Driver code
	public static void main(String[] args) {
		String str = "hello";
		int len = str.length();
		System.out.print(countKeyPressed(str, len));
	}

}
