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
    Or(AKnight, AKnave),
    # Since the "Or" is inclusive, we have to use the same logic from Quiz 1:
    Not(And(AKnight, AKnave)),
    # A says "I am both a knight and a knave.", but since this is false, the biconditional consequently associates AKnight to false, so it must be a Knave.
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # A can't be a knight, because it would be a paradox. Therefore, A must be a Knave.
    Implication(AKnight, And(AKnight, AKnave)),
    # A says "We are both knaves."
    # Since A is a knave, what they said is not true
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # If A is telling the truth, then A and B are knights
    Biconditional(AKnight, And(AKnight, BKnight)),
    # If B is telling the truth, B is a Knight and A is a Knave
    Biconditional(BKnight, And(BKnight, AKnave)),
    # If A is not telling the truth, then A is a Knave and B is a Knight
    # If B is not telling the truth, then B is a Knave and A is a Knight
    Implication(AKnave, BKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # B says "A said 'I am a knave'." If B is telling the truth, B is a Knight but A could be both
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B says "C is a knave."
    Biconditional(BKnight, CKnave),
    # C says "A is a knight."
    Biconditional(CKnave, Not(AKnight)),
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Biconditional(Or(AKnight, AKnave), Or(AKnave, AKnight))
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
