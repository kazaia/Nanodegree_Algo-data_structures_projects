****************************   Run time analysis (Worst Case Big-O Notation) ****************************
      

Task 0: The solution is O(1), To print the first record and the last record of calls and texts we need a constant time.ie. The algorithms does not dependent on the input data. No matter the size of the input data, the running time will always be the same.


Task 1: The solution is O(n), it means that the loops time complexity increases linearly.
We have four separate four loop each for loop has the complexity of O(n) , O(n) + O(n) = O(n + n ) = O ( 2n ), we drop the constant so it is : O(n)


Task 2: The solution is O(n), it means that the loops time complexity increases linearly.
We have five separate for loops, that are O(5n) which is also O(n) when we drop the constant.

Task 3: The solution is O(n)+ O(nlog(n)) = O(nlog(n)), 
the separate ( not nested for loops) are at least O(n) and the sort() is at least O(nlog(n)). So, the algorithm takes at least O(n) time and also at least O(nlog(n)) time. So really the complexity is the union of O(n) and O(nlog(n)) and since O(nlog(n)) is a superset of O(n) so really it is just O(nlog(n)).


Task 4: The solution is  O(nlog(n)).
The algorithm is at least O(n) and also at least O(nlog(n)). Since O(nlog(n)) is a superset of O(n) so really it is just O(nlog(n)).
