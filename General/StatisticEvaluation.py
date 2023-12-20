from GptSolution import GptMain
from DiySolution import DiyMain

def main():
    seed = 1
    puzzle_count = 10
    GptMain.start(seed, puzzle_count)
    DiyMain.start(seed, puzzle_count)



if __name__ == "__main__":
    main()