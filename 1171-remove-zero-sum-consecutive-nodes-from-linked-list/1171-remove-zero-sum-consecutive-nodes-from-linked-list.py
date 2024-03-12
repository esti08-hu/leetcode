class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prefix_sum = 0
        prefix_sums = {}
        node = dummy

        while node:
            prefix_sum += node.val
            if prefix_sum in prefix_sums:
                
                
                node_to_remove = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + node_to_remove.val
                while temp_sum != prefix_sum:
                    del prefix_sums[temp_sum]
                    node_to_remove = node_to_remove.next
                    temp_sum += node_to_remove.val
                prefix_sums[prefix_sum].next = node_to_remove.next
            else:
                prefix_sums[prefix_sum] = node
            node = node.next

        return dummy.next