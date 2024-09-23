# Stack S := {}; (start with an empty stack)
# for each vertex u in G do
# visited[u] := false;
# end for
# push S, v;
# reachedGoal := false;
# while S is not empty and not reachedGoal do
# u := pop S;
# if u is goal then
# reachedGoal := true;
# end if
# if not visited[u] then
# visited[u] := true;
# for each unvisited neighbour w of u do
# push S, w;
# end for
# end if
# end while
# 1
