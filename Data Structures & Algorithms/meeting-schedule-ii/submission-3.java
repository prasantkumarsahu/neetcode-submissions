/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort(Comparator.comparingInt(a -> a.start));

        var pq = new PriorityQueue<Integer>();
        for(var meeting: intervals) {
            if(!pq.isEmpty() && pq.peek() <= meeting.start) {
                pq.poll();
            }

            pq.offer(meeting.end);
        }

        return pq.size();
    }
}
