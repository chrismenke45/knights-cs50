from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

game_knowledge = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0_OLD = And(
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(AKnave,And(AKnight, AKnave))
)

knowledge0 = And(
    game_knowledge,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1_OLD = And(
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(AKnave, And(AKnave, BKnave)),
    Implication(AKnave, Or(
                            And(AKnight, BKnave),
                            And(AKnave, BKnight)
    ))
)

knowledge1 = And(
    game_knowledge,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Or(And(AKnight,BKnave), And(AKnave, BKnight)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2_OLD = And(
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(
        AKnave, 
        Or(
            And(AKnave,BKnave), 
            And(Not(AKnave), Not(BKnave)))
    ),
    Implication(
                AKnave,
                Or(
                    And(AKnave,BKnight),
                    And(AKnight,BKnave)
                )
                
    ),
    Or(
        BKnave, 
        Or(
            And(AKnave, Not(BKnave)), 
            And(Not(AKnave), BKnave))
    )
)

knowledge2 = And(
    game_knowledge,
    Implication(AKnave, Or(And(AKnight,BKnave), And(AKnave, BKnight))),
    Implication(AKnight, Or(And(AKnight,BKnight), And(AKnave, BKnave))),
    Implication(BKnave, Or(And(AKnight,BKnight), And(AKnave, BKnave))),
    Implication(BKnight, Or(And(AKnight,BKnave), And(AKnave, BKnight)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3_OLD = And(
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Implication(CKnight, Not(CKnave)),
    Implication(CKnave, Not(CKnight)),
    AKnight,
    Or(AKnave, Or(AKnight, AKnave)),
    Or(
        BKnave,
        AKnave
    ),
    Or(BKnave, CKnave),
    Or(CKnave, AKnight),
    Biconditional(CKnight, AKnight)
)

knowledge3 = And(
    game_knowledge,
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnight, AKnave),
    Implication(BKnight, CKnave),
    Biconditional(CKnight, AKnight),
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
