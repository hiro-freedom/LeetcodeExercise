// easiest way to understand

#include <vector>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {

		int a, b;
		int found = 0;
		for( int i=0; i<nums.size() - 1; i++)
		{
			a = i;
			for( int j=i+1; j<nums.size(); j++)
			{
				b = j;
				if ((nums[a]+nums[b]) == target)
				{
					found = 1;
					break;
				}
			}

			if (found)
			{
				break;
			}
		}

		vector<int> result;
		if (found)
		{
			result.push_back(a);
			result.push_back(b);
		}
		return result;
	}
};

int main()
{
	return 0;
}
