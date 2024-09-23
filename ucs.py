# state := start
# visited := set({})
# frontier := priority queue (Queue holds 3-tuples with (cumulative cost,
# state, previous state))
# frontier.add((0, start, null))
# reachedGoal := false
# while not reachedGoal and length(frontier) > 0 do
# (cumucost, state, prev) := frontier.pop()
# if state is goal then
# reachedGoal := true
# else
# visited.add(state)
# for each n in state.neighbors() do
# cost := distance(state, n) (Distance of taking step from state to
# neighbor)
# cumucostn := cumucost + cost
# if not n in frontier and not n in visited then
# frontier.add((cumucostn, n, state))
# else if n in frontier then
# if cumucostn < frontier.cost(n) then
# Update cost of n to be cumucostn on frontier
# end if
# end if
# end for
# end if
# end while
# 2
