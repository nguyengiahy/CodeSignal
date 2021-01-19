class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        unordered_map<int, int> map;
        vector<int> result, dryIndex;
        
        for (int i = 0; i < rains.size(); i++)
        {
            if (rains[i])
            {
                if (map.find(rains[i]) != map.end())
                {
                    // This lake is found before
                    // Find the closest 0 to the right from this lake
                    bool flag = false;
                    for (auto it = dryIndex.begin(); it != dryIndex.end(); it++)
                        if (*it > map[rains[i]])
                        {
                            result[*it] = rains[i];
                            dryIndex.erase(it);
                            flag = true;
                            break;
                        }
                    if (!flag)
                        return {};
                }
                map[rains[i]] = i;  // Map value with its index
                result.push_back(-1);
            }
            else
            {
                dryIndex.push_back(i);
                result.push_back(1);
            }
        }

        return result;
    }
};