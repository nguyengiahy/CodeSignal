class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
    
    if(position.length == 0)
        return 0;
    
    HashMap<Integer,Integer>map = new HashMap<>();
    for(int i=0;i<position.length;i++)
        map.put(position[i],speed[i]);
    
    Arrays.sort(position);
    
    float []time = new float[position.length];
    for(int i=0;i<time.length;i++)
        time[i] = (float)(target-position[i])/map.get(position[i]);
    
    int fleet = 1;
    float max_time = time[time.length-1];
    for(int i=time.length-2;i>=0;i--){
        if(time[i]>max_time){
            fleet++;
            max_time = time[i];
        }
    }
    
    return fleet;
    }
}