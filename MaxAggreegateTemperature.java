package FebruaryAmazon;
//https://leetcode.com/discuss/interview-question/1792978/Amazon-or-OA
//Alexa AI voice assistant 
public class MaxAggreegateTemperature {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr[]=new int[] {6,-2,5};
		
		int n = arr.length, left =arr[0];
		
		if (n == 0) 
			System.out.println(0);
		
        if (n == 1) 
        	System.out.println(arr[0]);
        
        int allSum = 0;
        int maxTemp = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
        	
            allSum += arr[i];
        }

        for (int i = 1; i < n; i++) {
        	
            left = left + arr[i]; //take the left and 
            allSum = allSum - arr[i-1]; // the rest is right + curr 

            int currMaxAgreegate = Math.max(left, allSum);  //find max between left and right
            maxTemp = Math.max(maxTemp, currMaxAgreegate);  //at last get the max one 
        }

        System.out.println(maxTemp);
	}

}
