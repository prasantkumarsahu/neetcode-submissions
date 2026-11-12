class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var freq = new HashMap<Integer, Integer>();

        for(var num: nums) {
            freq.merge(num, 1, Integer::sum);
        }

        var pq = new PriorityQueue<Integer>((a, b) -> freq.get(a) - freq.get(b));

        for(var key: freq.keySet()) {
            pq.offer(key);

            if(pq.size() > k) {
                pq.poll();
            }
        }

        var ans = new int[k];

        for(var i = 0; i < k; i++) {
            ans[i] = pq.poll();
        }

        return ans;
    }
}
