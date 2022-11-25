class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::set<char> set_s;
        std::set<char> set_t;
        std::set<tuple<int, int>> pairs;
        for(int i = 0; i < s.length(); i++) {
            set_s.insert(s[i]);
            set_t.insert(t[i]);
            tuple<int, int> tuple;
            tuple = make_tuple(s[i], t[i]);
            pairs.insert(tuple);
        }
    // std::cout << set_s.size() << set_t.size() << pairs.size();
    if (set_s.size() == set_t.size() && set_s.size() == pairs.size()) {
        return true;
    } else {
        return false;
    }
    }
};
