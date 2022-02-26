package FebruaryAmazon;

public class NetStockChange {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr[]=new int[] {1,3,2,3};
		
		int n = arr.length, left =arr[0], allSum=0, index=0;
		double max=Integer.MAX_VALUE;
		
		for (int i = 0; i < arr.length; i++) {
        	
            allSum += arr[i];
        }
		
		for (int i = 0; i < arr.length; i++) {
        	
            left = left + arr[i]; //take the left and 
            allSum = allSum - arr[i]; // the rest is right + curr
            
            double leftAvg = Math.floor(left/(i+1)), rightAvg = Math.floor(allSum/(n-i));
            

            double tempMax = Math.abs(leftAvg - rightAvg);  
            
            //find max between left and right
            if(tempMax < max) {
            	
            	max=tempMax;
            	index =  i;
            	System.out.println(tempMax);
            }
        }

        System.out.println(index);
	}

}
