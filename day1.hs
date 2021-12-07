import System.IO

-- runs second part
main :: IO Int
main = do
        contents <- readFile "input/day1.txt"
        let intList = map (read::String->Int) (lines contents)
        return (doThreeThing intList)

-- does the first part
doThing :: [Int] -> Int
doThing [] = 0
doThing [x] = 0
doThing [x, y]  | x < y = 1
                | otherwise = 0

doThing (x:y:xs)    | x < y = 1 + doThing (y:xs)
                    | otherwise = 0 + doThing(y:xs)


-- does second part
doThreeThing :: [Int] -> Int
doThreeThing [] = 0
doThreeThing [_] = 0
doThreeThing [x, y, z, x1]  | x+y+z < y+z+x1 = 1
                            | otherwise = 0

doThreeThing (x:y:z:x1:xs)  | x+y+z < y+z+x1 = 1 + doThreeThing (y:z:x1:xs)
                            | otherwise = 0 + doThreeThing(y:z:x1:xs)

