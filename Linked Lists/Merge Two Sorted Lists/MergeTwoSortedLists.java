/**
    Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {

        }

        ListNode(int val) { 
            this.val = val; 
        }

        ListNode(int val, ListNode next) { 
            this.val = val; this.next = next; 
        }
    }
 */


 class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode merged = new ListNode();

        if(list1 == null){
            merged = list2;
        }
        else if(list2 == null){
            merged = list1;
        }
        else if(list1.val <= list2.val){
            merged = list1;
            merged.next = mergeTwoLists(merged.next, list2);  
        }
        else if(list1.val > list2.val){
            merged = list2;
            merged.next = mergeTwoLists(list1, merged.next);  
        }

        return merged; 

        //remove the lowest and add to the merged
        //call the function again with both list Node next node
    }
}

// 1 