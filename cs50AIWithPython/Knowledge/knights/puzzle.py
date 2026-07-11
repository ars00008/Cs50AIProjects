from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    AKnight, AKnave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),  # A is either a knave or B is a knight
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight, then A's statement is true
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is a knave, then A's statement is false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # If A is a knight, then A's statement is true
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),  # If A is a knave, then A's statement is false
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),  # If B is a knight, then B's statement is true
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # If B is a knave, then B's statement is false
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Or(CKnight, CKnave),  # C is either a knight or a knave
    Implication(AKnight, AKnight),  # If A is a knight, then A's statement is true
    Implication(AKnave, AKnight),  # If A is a knave, then A's statement is false
    Implication(BKnight, And(AKnave, CKnave)),  # If B is a knight, then B's statements are true
    Implication(BKnave, Not(And(AKnave, CKnave))),  # If B is a knave, then B's statements are false
    Implication(CKnight, AKnight),  # If C is a knight, then C's statement is true
    Implication(CKnave, Not(AKnight))  # If C is a knave, then C's statement is false
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
