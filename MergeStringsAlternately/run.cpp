class Solution {
public:
    string mergeAlternately(string word1, string word2) {

		int min = word1.size() > word2.size() ? word2.size() : word1.size();
		string result;
		int i = 0;

		for ( i=0; i<min; i++ ) {
			result.push_back(word1.at(i));
			result.push_back(word2.at(i));
		}

		if ( i < word1.size() ) {
			result = result + word1.substr(i);
		}
		if ( i < word2.size() ) {
			result = result + word2.substr(i);
		}

		return result;
    }
};
