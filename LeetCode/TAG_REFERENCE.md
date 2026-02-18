# Problem Approach Tags Reference

This document explains the approach tags assigned to each problem based on the key differences within their category.

## Tag Categories

### Parentheses - Stack-based tracking, different removal strategies
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 001 | Minimum Remove to Make Valid Parentheses | Stack+Indices | Uses stack to track indices for removal |
| 020 | Valid Parentheses | Stack+Matching | Stack for matching pairs |
| 052 | Minimum Add to Make Parentheses Valid | Greedy Count | Greedy counting without stack |
| 056 | Remove Invalid Parentheses | BFS+Removal | BFS to find minimum removals |

### Palindrome - Two-pointers vs DP, string modification allowed
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 004 | Valid Palindrome II | 2-Ptr, 1 Skip | Two pointers with one deletion allowed |
| 029 | Valid Palindrome | 2-Ptr, Validation | Two pointers for read-only validation |
| 057 | Palindromic Substrings | Expand Center | Expand around center technique |
| 083 | Valid Palindrome III | DP, K Deletions | DP allowing k deletions |
| 096 | Longest Palindromic Substring | Expand+DP | Hybrid expand and DP approach |

### BST-Binary-Search-Tree - In-order traversal, BST property pruning
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 027 | Range Sum of BST | DFS+Pruning | DFS with BST property pruning |
| 051 | Binary Search Tree Iterator | Iterator+Stack | Stack-based iterator |
| 060 | Closest Binary Search Tree Value | Binary Search | Binary search on BST |
| 092 | Kth Smallest Element in a BST | Inorder+Counter | In-order traversal with counter |

### Binary-Search - Search target vs search answer space
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 010 | Find Peak Element | Search Peak | Search for peak element |
| 041 | Kth Missing Positive Number | Search Answer | Binary search on answer space |
| 042 | Find First and Last Position | Dual Binary Search | Two separate binary searches |
| 074 | Cutting Ribbons | Search Answer | Binary search on answer (length) |
| 079 | Capacity To Ship Packages | Search Capacity | Binary search on capacity |
| 084 | Kth Smallest Element in Matrix | Search Value Range | Binary search on value range |
| 094 | Koko Eating Bananas | Search Speed | Binary search on eating speed |
| 100 | Median of Two Sorted Arrays | Search Partition | Binary search on partition point |

### Two-Pointers - Same direction vs opposite direction
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 002 | Valid Word Abbreviation | Same Dir | Same direction pointers |
| 028 | Dot Product of Two Sparse Vectors | Same Dir | Same direction iteration |
| 029 | Valid Palindrome | Opposite Dir | Opposite direction from ends |
| 030 | Next Permutation | Same Dir+Greedy | Same direction with greedy choice |
| 033 | Merge Sorted Array | Opposite Dir | Merge from end (opposite direction) |
| 044 | Squares of a Sorted Array | Opposite Dir | Merge squares from both ends |
| 065 | 3Sum | Opposite Dir | Sort + opposite direction pointers |
| 073 | Container With Most Water | Opposite Dir+Greedy | Opposite with greedy move |
| 078 | Strobogrammatic Number | Opposite Dir | Check from both ends |
| 088 | Interval List Intersections | Same Dir | Same direction merge |

### Math-Compute - Iterative vs recursive, carry handling
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 021 | Pow(x, n) | Recursive | Recursive divide and conquer |
| 050 | Add Strings | Iterative+Carry | Iterative with carry handling |
| 072 | Maximum Swap | Greedy+Digit | Greedy digit swapping |
| 085 | Add Two Integers | Direct | Direct computation |

### Heap-Priority-Queue - Min heap vs max heap vs dual heap
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 006 | Kth Largest Element | Min Heap | Min heap of size k |
| 012 | Random Pick with Weight | Binary Search+Prefix | Prefix sum + binary search |
| 015 | Top K Frequent Elements | Bucket Sort | Bucket sort optimization |
| 019 | Merge k Sorted Lists | Min Heap | Min heap for merging |
| 034 | Sliding Window Median | Dual Heap+Lazy | Two heaps with lazy deletion |
| 082 | Find Median from Data Stream | Dual Heap | Two heaps: max + min |
| 091 | Random Pick Index | Reservoir Sampling | Reservoir sampling technique |

### Tree - DFS vs BFS, pre/in/post-order, level-order
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 003 | Binary Tree Vertical Order | BFS+Column Track | BFS with column tracking |
| 005 | Lowest Common Ancestor III | DFS+Parent Ptr | DFS using parent pointers |
| 007 | Binary Tree Right Side View | BFS Level-Order | BFS level-order traversal |
| 009 | Lowest Common Ancestor | DFS Recursive | Recursive DFS |
| 011 | Nested List Weight Sum | DFS+Depth | DFS with depth tracking |
| 013 | Sum Root to Leaf Numbers | DFS Path Track | DFS tracking path values |
| 014 | Diameter of Binary Tree | DFS Bottom-Up | Bottom-up DFS |
| 061 | Vertical Order Traversal | DFS+Sort | DFS then sort results |
| 066 | All Nodes Distance K | BFS+Parent Map | BFS with parent mapping |
| 076 | Binary Tree Maximum Path Sum | DFS+Max Path | DFS tracking max path |

### Graph-DFS-BFS - DFS for cycles, BFS for shortest path
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 025 | Clone Graph | DFS+Clone | DFS to clone nodes |
| 031 | Shortest Path in Binary Matrix | BFS Shortest | BFS for shortest path |
| 036 | Making A Large Island | DFS+Union-Find | DFS labeling + union-find |
| 038 | Accounts Merge | Union-Find | Pure union-find approach |
| 053 | Robot Room Cleaner | DFS+Backtrack | DFS with backtracking |
| 063 | Course Schedule | DFS Cycle Detect | DFS for cycle detection |
| 070 | Swim in Rising Water | Dijkstra | Dijkstra's algorithm |
| 081 | Word Ladder | BFS Transform | BFS for transformation |
| 086 | Shortest Path in Hidden Grid | DFS+BFS Hybrid | DFS exploration + BFS path |

### Linked-List - Dummy node, two-pointer, in-place modification
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 019 | Merge k Sorted Lists | Min Heap+Merge | Heap-based merging |
| 032 | Copy List with Random Pointer | HashMap | HashMap for copying |
| 045 | Remove Nth Node From End | 2-Ptr Gap | Two pointers with gap |
| 054 | Add Two Numbers | Dummy+Carry | Dummy node with carry |
| 064 | Insert into Sorted Circular List | Edge Cases | Handle edge cases |

### Stack - Monotonic stack vs regular stack, what to store
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 008 | Basic Calculator II | Stack+Operator | Stack storing operators |
| 035 | Simplify Path | Stack+Path | Stack for path components |
| 049 | Exclusive Time of Functions | Stack+Time | Stack tracking time |
| 093 | Decode String | Stack+Nested | Stack for nested patterns |
| 098 | Remove Adjacent Duplicates II | Stack+Count | Stack with count |

### Sliding-Window - Fixed size vs variable size
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 037 | Minimum Window Substring | Variable Size | Variable window size |
| 040 | Max Consecutive Ones III | Variable Size | Variable size window |
| 059 | Continuous Subarray Sum | HashMap+Mod | HashMap with modulo |
| 068 | Contains Duplicate II | Fixed Size | Fixed size window |
| 080 | Longest Substring Without Repeating | Variable Size | Variable size optimization |
| 090 | Frequency of Most Frequent Element | Variable Size+Sort | Sort + variable window |

### Array-Hashing - Prefix sum, hash for O(1) lookup, sorting
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 016 | Merge Intervals | Sort+Merge | Sort then merge |
| 017 | Two Sum | HashMap O(1) | HashMap for O(1) lookup |
| 022 | Buildings With Ocean View | Right-to-Left | Right to left traversal |
| 023 | Custom Sort String | Count+Build | Count then build result |
| 024 | K Closest Points | Max Heap | Max heap approach |
| 026 | Subarray Sum Equals K | Prefix Sum+Hash | Prefix sum with hash |
| 062 | Group Shifted Strings | Hash Pattern | Hash by shift pattern |
| 069 | Zero Array Transformation | Heap+Greedy | Heap with greedy strategy |
| 071 | Managers with 5+ Reports | SQL Aggregate | SQL aggregation |
| 077 | Car Pooling | Difference Array | Difference array technique |
| 087 | Maximum Subarray | Kadane DP | Kadane's algorithm |
| 089 | Range Sum Query | Prefix Sum | Prefix sum array |

### Dynamic-Programming - 1D vs 2D DP, top-down vs bottom-up
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 018 | Best Time to Buy and Sell Stock | 1D DP | 1-dimensional DP |
| 055 | Subsets | Backtrack | Backtracking approach |
| 075 | Word Break | 1D DP | 1D DP array |
| 083 | Valid Palindrome III | 2D DP | 2-dimensional DP |
| 099 | Best Time to Buy and Sell Stock III | State Machine DP | State machine DP |

### Design - Trade-offs between time/space complexity
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 039 | LRU Cache | HashMap+DLL | HashMap + doubly linked list |
| 048 | Moving Average | Queue+Sum | Queue with running sum |
| 091 | Random Pick Index | HashMap+Random | HashMap for random access |

### String - In-place vs new string, validation vs parsing
| # | Problem | Tag | Meaning |
|---|---------|-----|---------|
| 043 | Longest Common Prefix | Vertical Scan | Vertical scanning |
| 046 | Diagonal Traverse | Diagonal Sim | Diagonal simulation |
| 047 | Missing Ranges | Gap Check | Check gaps |
| 058 | Valid Number | DFA Validation | DFA state machine |
| 067 | String to Integer | Parse+Validate | Parse and validate |
| 095 | Goat Latin | Transform | String transformation |
| 097 | Text Justification | Greedy Pack | Greedy packing |

---

## How to Use These Tags

1. **Compare Within Category**: Tags help you see the different approaches within the same category
2. **Study Pattern Variations**: Learn when to use each variation (e.g., same vs opposite direction pointers)
3. **Interview Preparation**: Quickly identify which variation a problem requires
4. **Practice Systematically**: Practice all variations within a category

## Tag Benefits

- 🎯 **Precise Identification**: Quickly identify the specific approach needed
- 🔄 **Compare Similar Problems**: See how similar problems differ in implementation
- 📚 **Study Efficiently**: Group problems by approach variation
- 💡 **Interview Ready**: Recognize patterns faster during interviews
