class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sum = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++){
            sum.put(nums[i], i);
        }

        for(int x = 0; x < nums.length; x++){
            Integer y = sum.get(target - nums[x]);
            if( y != null && y != x){
                return new int[]{x, y};
            }
        }

        return new int[]{};
    }
}


