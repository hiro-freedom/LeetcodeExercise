/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include <stdio.h>

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode* pL1 = l1;
		ListNode* pL2 = l2;

		int x = 0;
		int plus = 0;
		int a = 0, b = 0;
		ListNode* pResult = nullptr;
		ListNode* pTmp = nullptr;

		while ((pL1 != nullptr || pL2 != nullptr) || plus != 0) {

			a = pL1 == nullptr ? 0 : pL1->val;
			b = pL2 == nullptr ? 0 : pL2->val;

			x = a + b + plus;

			if (x > 9){
				x = x - 10;
				plus = 1;
			}
			else{
				plus = 0;
			}

			if(pTmp != nullptr) {
				pTmp->next = new ListNode(x);
				pTmp = pTmp->next;
			}
			else{
				pTmp = new ListNode(x);
			}
			if (pResult == nullptr)
			{
				pResult = pTmp;
			}

			if (pL1 != nullptr) {
			pL1 = pL1->next;
			}
			if (pL2 != nullptr) {
			pL2 = pL2->next;
			}
		}

		return pResult;
    }
};


int main()
{
	ListNode* L1 = new ListNode(2);
	L1->next =  new ListNode(4);
	L1->next->next =  new ListNode(3);

	ListNode* L2 = new ListNode(5);
	L2->next =  new ListNode(6);
	L2->next->next =  new ListNode(4);

	Solution a;
	ListNode* res = a.addTwoNumbers(L1, L2);
	ListNode* pTmp = res;
	while (pTmp != nullptr) {
		printf("%d", pTmp->val);
		pTmp = pTmp->next;
	}
	printf("\n");

	return 0;
}

