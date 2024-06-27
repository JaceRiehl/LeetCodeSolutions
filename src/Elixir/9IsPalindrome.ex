defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    Integer.to_charlist(x)
        |> Enum.reverse() == Integer.to_charlist(x)
  end
end
