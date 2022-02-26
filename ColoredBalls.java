package FebruaryAmazon;

import java.util.Arrays;
//https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

public class ColoredBalls {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ColoredBalls cb = new ColoredBalls();

		System.out.println(cb.maxProfitt(new int[] { 2, 5 }, 4));
	}

	public int maxProfitt(int[] inventory, int orders) {
		
		int max = 0;
		for (int inv : inventory) {
			max = Math.max(max, inv);
		}
		int lo = 0, hi = max;
		while (lo < hi) {
			int mid = hi + (lo - hi) / 2;
			if (getThreshold(inventory, orders, mid)) {
				lo = mid;
			} else {
				hi = mid - 1;
			}
		}
		long res = 0L;
		for (int inv : inventory) {
			if (inv > lo) {
				res += (long) (inv + lo + 1) * (inv - lo) / 2;
				orders -= (inv - lo);
			}
		}
		res += (long) (lo + 1) * orders;
		return (int) (res % 1000000007);
	}

	private boolean getThreshold(int[] nums, int k, int mid) {
		int res = 0;
		for (int num : nums) {
			if (num > mid) {
				res += num - mid;
				if (res >= k) {
					return true;
				}
			}
		}
		return false;
	}
//19 ms ends here. 

	public int maxProfit(int[] inventory, int orders) {

		int lo = 1, hi = Arrays.stream(inventory).max().getAsInt();
		Arrays.sort(inventory);

		while (lo < hi) {
			int mid = lo + (hi - lo + 1) / 2;
			if (getCount(inventory, mid) < orders)
				hi = mid - 1;
			else
				lo = mid;
		}

		int minPrice = lo, ordered = 0;
		long profit = 0;

		for (int i = inventory.length - 1; i >= 0; i--) {
			int curPrice = inventory[i];
			if (curPrice <= minPrice)
				break;
			profit += (long) (curPrice + minPrice + 1) * (curPrice - minPrice) / 2;
			ordered += curPrice - minPrice;
		}

		profit += (long) minPrice * (orders - ordered);
		profit = profit % 1000000007;

		// System.out.println(profit);
		return (int) profit;
	}

	private long getCount(int[] inventory, int mid) {
		long count = 0;
		for (int i = inventory.length - 1; i >= 0; i--) {
			if (inventory[i] < mid)
				break;
			count += inventory[i] - mid + 1;
		}
		return count;
	}

}
