# tail recursion
defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum([num | tail], target, offset \\ 1) do
    search = target - num
    index = Enum.find_index(tail,
            fn second -> second == search end
        )
    if index do
        [offset - 1, index + offset]
    else
        two_sum(tail, target, offset + 1)
    end
  end
end

# using Enum
defmodule Solution2 do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    IO.inspect(nums)
    nums
        |> Enum.with_index()
        |> Enum.reduce_while(%{}, fn {num, index}, map ->
            IO.inspect map
            case map[target - num] do
                nil -> {:cont, Map.put(map,num,index)}
                found -> {:halt, [index, found]}
            end
        end)
    end
end
