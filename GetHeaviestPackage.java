package FebruaryAmazon;

import java.util.ArrayList;
import java.util.List;
//https://leetcode.com/discuss/interview-question/1759164/Amazon-or-OA-or-Get-heaviest-package
public class GetHeaviestPackage {

	public static void main(String[] args) {
		
		List<Integer> w = new ArrayList<Integer>();
		w.add(2);
		w.add(9);
		w.add(10);
		w.add(3);
		w.add(7);
		int h = getPackage(w);
		System.out.println(h);
		
		int arr[]=new int[] {2,9,10,3,7};
		int x = getHeaviestPackage(arr);
		System.out.println(x);

	}

	//dp solution from the main question itself 
	private static int getHeaviestPackage(int[] weights) {
        int[] dp = new int[weights.length];
        dp[0] = weights[0];
        int max = weights[0];
        for (int i = 1; i < weights.length; i++) {
            if (weights[i] > weights[i - 1]) {
                int s = Math.max(weights[i] + dp[i - 1], weights[i]);
                dp[i] = s;
                max = Math.max(max, s);
            } else {
                dp[i] = weights[i];
            }
        }
        return max;
    }
	
	//arr version of same last one
	private static int getPack(int[] weights) {
		// TODO Auto-generated method stub
		int size = weights.length;
		int currWt=weights[size-1]; //arr version 
		int heaviestPackage=currWt;
		for(int i=size-1;i>=1;i--){ 
		    if( currWt > weights[i-1] ){
		        currWt=currWt+weights[i-1];
		    }
		    else{
		        currWt=weights[i-1];
		    }       
		    heaviestPackage=Math.max(heaviestPackage,currWt);
		}
		return heaviestPackage;
	}

	private static int getPackage(List<Integer> weights) {
		// TODO Auto-generated method stub
		
		int size=weights.size();
//		int currWt=weights[size-1]; arr version 
//		int heaviestPackage=currWt;
//		for(int i=size-1;i>=1;i--){ 
//		    if( currWt > weights[i-1] ){
//		        currWt=currWt+weights[i-1];
//		    }
//		    else{
//		        currWt=weights[i-1];
//		    }       
//		    heaviestPackage=max(heaviestPackage,currWt);
//		}

		
		int currWt=weights.get(size-1);
		int heaviestPackage=currWt;
		for(int i=size-1;i>=1;i--){ 
		    if( currWt > weights.get(i-1) ){
		        currWt=currWt+weights.get(i-1);
		    }
		    else{
		        currWt=weights.get(i-1);
		    }       
		    heaviestPackage=Math.max(heaviestPackage,currWt);
		}
		return heaviestPackage;
		
		//return 0;
	}

	
}
