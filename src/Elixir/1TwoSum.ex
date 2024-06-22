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
