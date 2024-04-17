#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int last = m + n - 1;
        while (m > 0 && n > 0)
        {
            if (nums1[m - 1] > nums2[n - 1])
            {
                nums1[last] = nums1[m - 1];
                m -= 1;
            }
            else
            {
                nums1[last] = nums2[n - 1];
                n -= 1;
            }
            last -= 1;
        }
        while (n > 0)
        {
            nums1[last] = nums2[n - 1];
            n -= 1;
            last -= 1;
        }
    }
};

int main()
{
    vector<int> nums1;
    nums1.push_back(2);
    nums1.push_back(5);
    nums1.push_back(6);

    int m = 3;
    vector<int> nums2;
    nums2.push_back(8);
    nums2.push_back(9);
    nums2.push_back(0);

    int n = 3;

    Solution sol;
    sol.merge(nums1, m, nums2, n);

    cout << "Merged Array: ";
    for (int i = 0; i < m + n; ++i)
    {
        cout << nums1[i] << " ";
    }
    cout << endl;
    return 0;
}
