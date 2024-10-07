"""
Part 1
Implement a recursive depth-first search that you fully understand and could reproduce in front of someone from scratch if you needed to.
Then, run your DFS implementation on some example graphs. This means being comfortable with how to represent a graph with nodes and edges in your preferred interview language.
This will become the foundation for the Boggle solver.


Part 2
Review how to play Boggle. Here is an example online version.
The goal of the game when played with humans is to find as many words as you can in a grid of 16 letters, in a limited amount of time. Words can only be made from connected letters — i.e. from a given letter you can only use the letters directly adjacent, including diagonally. You can’t reuse letters, and words must be at least 3 letters long.


Part 3
Implement a Boggle solver. This is the part that you can treat like a time-boxed interview if you’d like. You will likely want to break this into the follow steps:

1. Stub out a function that takes as input a grid (e.g. a 2 x 2 or 4 x 4 matrix of letters) and returns all of the words that can be made from that grid.
2. Write a function to create a graph from the grid. [Goal: complete this sub-part in 30 minutes]
    1. Refer back to your graph representations from Part I.
    2. Test that you get the correct graph back from a grid.
3. Set up a data structure containing all words in the dictionary, with efficient lookup. [Goal: complete this sub-part in < 10 minutes (you probably already have this implemented if you’ve completed the prior problems in this problem set)]
4. Use depth-first search to find all of the words in the grid. [Goal: complete this sub-part in 60 minutes]
    1. You’ll need to run DFS starting from every letter.
    2. You don’t need any fancy data structures to solve a 4x4 grid quickly.
    3. You’ll need a way of confirming if a path through the grid makes a valid word.
    4. You might find it helpful (both as a light efficiency optimization and for easier debugging) to stop pursuing paths in the grid that cannot possibly lead to a valid word, i.e. that path is not a valid prefix for any word in the dictionary.

    
Plan

put sowpods words into a set
create a set of preefixes of each word example 'happy' ha, hap, happ

for loop with recursive call
letters cannot be re-used

Functions:

consider creating an object- word_checker:
check if a path is a word
check if a path is a prefix

turns a list of tuples into a list of letters

recursive function (which nodes have been visited, the graph, where to start, prefix set, word set)
 - return a collection of valid words
 - list of letters visited, in order

* may or may not need this; solver function - pass in the grid  
main - create grid, which will be passed into solver function; create sets

-if word >16 letters, stop


dfs(grid,listof tuples - for each letter, next letter to visit as tuple)
return a list of tuples
"""