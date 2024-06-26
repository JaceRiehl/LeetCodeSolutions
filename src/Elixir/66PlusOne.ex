defmodule Solution do
  @spec plus_one(digits :: [integer]) :: [integer]
  def plus_one(digits) do
    Enum.reverse(digits)
        |> add_plus_one([], 1)
  end

  #   have a 1 carry
  def add_plus_one([digit | tail], res, 1) do
    if digit == 9 do
        add_plus_one(tail, [0 | res], 1)
    else
        add_plus_one(tail, [digit+1 | res], 0)
    end
  end
  #   no carry left
  def add_plus_one([digit | tail], res, 0) do
    add_plus_one(tail, [digit | res], 0)
  end

  #   no digits left
  def add_plus_one([], res, carry) do
    if carry == 0 do
        res
    else
    [1 | res]
    end
  end
end
