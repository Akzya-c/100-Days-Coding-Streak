class Solution {
    public int[] twoSum(int[] numbers, int target) 
    {
        int i,j;
        for (i=0;i<numbers.length;i++)
        {
            for(j=i+1;j<numbers.length;j++)
            {
                if(numbers[i]+numbers[j]==target)
                {
                    return new int[]{i+1,j+1};
                }
            }
        }
      return new int[] {-1,-1};
    }
}
