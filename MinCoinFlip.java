package FebruaryAmazon;

public class MinCoinFlip {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println(minCoinFlip("HTTHHT"));
	}
//works for 010101 too 
	private static int minCoinFlip(String S) {
		
		int N = S.length();
        int[] P = new int[N + 1];
        
        for (int i = 0; i < N; ++i)
            P[i+1] = P[i] + (S.charAt(i) == 'T' ? 1 : 0);
        
        int ans = Integer.MAX_VALUE;
        for (int j = 0; j <= N; ++j) {
            ans = Math.min(ans, P[j] + N-j-(P[N]-P[j]));
        }

        return ans;
	}

}
