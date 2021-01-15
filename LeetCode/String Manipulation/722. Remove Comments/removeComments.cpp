class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> result;
        bool isCommenting = false;
	    string str;
        
        for (int i = 0; i < source.size(); i++)
        {
            for (int j = 0; j < source[i].length(); j++)
            {
                string commentOp = source[i].substr(j, 2);
                if (!isCommenting)
                {
                    // Line comment
                    if (commentOp == "//")
                        break;
                    // Block comment
                    else if (commentOp == "/*")
                    {
                        isCommenting = true;
                        j++;
                    }
                    else
                    {
                        str.push_back(source[i][j]);
                    }
                }
                else
                {
                    // End block comment
                    if (commentOp == "*/")
                    {
                        isCommenting = false;
                        j++;
                    }
                }
            }

            if (!isCommenting && str != "")
            {
                result.push_back(str);
                str.clear();
            }
        }
        return result;
    }
};