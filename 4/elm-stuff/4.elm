module AOC4 exposing (..)

import Html exposing (text)
import Debug exposing (log)
import String

testText = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

parseList list = 
    String.split "\n" list


addOne : Int -> Int
addOne x =
  x + 1

result = addOne 3
main =
    text ("this is the results " ++ toString (addOne 5))

