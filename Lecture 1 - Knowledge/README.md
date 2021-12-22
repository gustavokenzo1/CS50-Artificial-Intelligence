# Resumo da Aula 1: Knowledge

- Use statements to infer other statements
- Ex.:
    - If it didn't rain, Harry visited Hagrid today.
    - Harry visited Hagrid or Dumbledore today, but not both.
    - Harry visited Dumbledore today.
- Conclusion: It rained

## Sentence
- An assertion about the world in a knowledge representation language

## Propositional Logic
- Proposition Symbols: P, Q, R...
- Logical Connectives:
    - Not: ¬
        - If P is true, then ¬P is false.
        - If P is false, then ¬P is true.
    - And: ^
        - If P is false and Q is false, then P^Q is false.
        - If P is false and Q is true, then P^Q is false.
        - If P is true and Q is false, then P^Q is false.
        - If P is true and Q is true, then P^Q is true.
    - Or: v
        - If P is false and Q is false, then PvQ is false.
        - If P is false and Q is true, then PvQ is true.
        - If P is true and Q is false, then PvQ is true.
        - If P is true and Q is true, then PvQ is true.
    - Implication: -> (P implies Q)
        - If P is false and Q is false, then P->Q is true.
        - If P is false and Q is true, then P->Q is true.
        - If P is true and Q is false, then P->Q is false.
        - If P is true and Q is true, then P->Q is true. 
    - Biconditional: <-> (If and only if, only true when P and Q are the same)
        - If P is false and Q is false, then P<->Q is true.
        - If P is false and Q is true, then P<->Q is false.
        - If P is true and Q is false, then P<->Q is false.
        - If P is true and Q is true, then P<->Q is true.

## Model
- Assignment of a truth value to every propositional symbol (a "possible world")
- Example:
    - P: It is raining.
    - Q: It is a Tuesday.
    Model: {P = true, Q = false}

## Knowledge Base
- A set of sentences known by a knowledge-based agent

## Entailment
- a |= B
- Read "a entails b'
- In every model in which sentence a is true, then sentence b is also true

## Inference
- The process of deriving new sentences from old ones

- P: It is Tuesday.
- Q: It is raining.
- R: Harry will go for a run.

- KB (knowledge base): (P ^ ¬Q) -> R: "If it is a Tuesday, and it is not raining, then Harry will go for a run."
- Inference: R is true

## Does KB |= a?

### Model Checking
- To determine if KB |= a:
    - Enumerate all possible models
    - If in every model where KB is true, a is true, then KB entails a

- P: It is Tuesday.
- Q: It is raining.
- R: Harry will go for a run.
- KB: (P ^ ¬Q) -> R and we know P and ¬Q
- Query: R
- Since we have 3 propositional symbols of true or false, we can have 2^3 = 8 cases

| P     | Q      | R     | KB    |
|-------|--------|-------|-------|
| false | false  | false | false |
| false | false  | true  | false |
| false | true   | false | false |
| false | true   | true  | false |
| true  | false  | false | false |
| true  | false  | true  | true  |
| true  | true   | false | false |
| true  | true   | true  | false |

- We have only one possible world where our KB is true

## Knowledge Engineering
- Clue
    - Propositional Symbols:
        - mustard, plum, scarlet
        - ballroom, kitchen, library
        - knife, revolver wrench
    - Who? (mustard v plum v scarlet)
    - Where? (ballroom v kitchen v library)
    - How? (knife v revolver v wrench)
    - ¬plum
    - ¬mustard v ¬library v ¬revolver
    - Watch video at around 45 mins for demonstration

## Inference Rules
- Draw a horizontal line
- Above: premise, something we know to be true
- Below: conclusion after inference rule

- Modus Ponens: if a implies b, and a is true, then b is true
- And Elimination: if a is true and b is true, a is true
    - Ex.:
        - Above: Harry is friends with Ron and Hermione
        - Below: Hary is friends with Hermione

- Double Negation Elimination: if ¬(¬a), then: a
    - Ex.: 
        - Above: It is not true that Harry did not pass the test
        - Below: Harry passed the test
    
- Implication Elimination: if a -> b: ¬a v b
    - Ex.: 
        - Above: If it is raining, then Harry is inside
        - Below: It is not raining or Harry is inside
    
- Bicionditial Elimination: if a <-> b: (a -> b) ^ (b -> a)
    - Ex.: 
        - Above: It is raining if and only if Harry is inside
        - Below: If it is raining, then Harry is inside, and if Harry is inside, then it is raining

- De Morgan's Law: ¬(a^b): ¬a v ¬b or the opposite
    - Ex.: 
        - Above: It is not true that both Harry and Ron passed the test
        - Below: Harry did not pass the test or Ron did not pass the test

- Distributive Law: (a ^ (b v g)): (a ^ b) v (a ^ g) or the opposite
#
- P v Q
- ¬P, then Q
- Q doesn't need to be only one statement, it can be a list of statements
#
- P v Q
- ¬P v R, then Q v R
- Ex.:
    - Above: (Ron is in the Great Hall) v (Hermione is in the library)
    - Above: (Ron is not in the Great Hall) v (Harry is sleeping)
    - Below: (Hermione is in the library) v (Harry is sleeping)

### Search Problems
- initial state
- actions
- transition model
- goal test
- path cost function

### Theorem Proving
- initial state: starting KB
- actions: inference rules
- transition model: new KB after inference
- goal test: check statement we're trying to prove
- path cost function: number of steps in proof

### Clause
- a disjunction of literals
- Ex.: (P v Q v R)

### Conjunctive Normal Form (CNF)
- Logical sentence that is a conjunction of clauses
- Ex.: (A v B v C) ^ (D v ¬E) ^ (F v G)

- Conversion to CNF:
    - Eliminate biconditionals:
        - turn (a <-> b) into (a -> b) ^ (b -> a)
    - Eliminate implications:
        - turn (a -> b) into ¬a v b
    - Move ¬ inwards using De Morgan's Laws
        - e.g. turn ¬(a ^ b) into ¬a v ¬b
    - Use distributive law to distribute v wherever possible

- Ex.:
    - (P v Q) -> R
    - ¬(P v Q) v R (eliminate implication)
    - (¬P ^ ¬Q) v R (De Morgan's Law)
    - (¬P v R) ^ (¬Q v R) (distributive law)

## Resolution

### Inference by Resolution
- P v Q
- ¬P v R, then (Q v R)
#
- P v Q v S
- ¬P v R v S, then (Q v S v R v S) and eliminate duplicates (Q v R v S)
#
- P
- ¬P, then () (empty clause, always False)
#
- To determine if KB |= a:
    - Check if (KB ^ ¬a) is a contradiction
        - If so, then KB |= a
        - Else, no entailment
- How to check if (KB ^ ¬a) is a contradiction:
    - Convert (KB ^ ¬a) to CNF
    - Keep checking to see if we can use resolution to produce a new clause
        - if we produce an empty clause (False), then we have a contradiction. and KB |= a
        - else, if we can't add new clauses, there is no entailment
- Ex.:
#### Does (A v B) ^ (¬B v C) ^ (¬C) entail A?
1. Assume A is false: (A v B) ^ (¬B v C) ^ (¬C) ^ (¬A) (already in CNF)
2 We have 4 different clauses:
    - (A v B)
    - (¬B v C)
    - (¬C)
    - (¬A)
3. We can resolve the two middle clauses, because we have two complimentary literals (C and not C), and get a new clause: (¬B)
- (A v B) (¬B v C) (¬C) (¬A) (¬B)
- Picking the two extreme ones, we have the same case, and we can generate the (A) clause
- (A v B) (¬B v C) (¬C) (¬A) (¬B) (A)
- Now we have A and not A, which is an empty clause
- (A v B) (¬B v C) (¬C) (¬A) (¬B) (A) ()
- Since we have an empty clause, which is False, we have a contradiction, which means our KB entails A

## First-Order Logic
- Constant Symbol: objects, like people or houses
- Predicate Symbol: relations or functions, that take an input and evaluate to us True or False

Ex.:
- Person(Minerva): Minerva is a person
- House(Gryffindor): Gryffindor is a house
- ¬House(Minerva): Minerva is not a house
- BelongsTo(Minerva, Gryffindor): Minerva belongs to Gryffindor

### Universal Quantification
- Something is going to be True for all values of a variable
- ∀x.BelongsTo(x, Gryffindor) -> ¬BelongsTo(x, Hufflepuff)
- For all objects x, if x belongs to Gryffindor, x does not belong to Hufflepuff
- or: Anyone in Gryffindor is not in Hufflepuff


### Existential Quantification
- Something is going to be True for some value of a variable
- ∃x.House(x) ^ BelongsTo(Minerva, x)
- There exists an object x such that x is a house and Minverva belongs to x
- Minverva belongs to a house
#
- ∀x.Person(x) -> (∃y.House(y) ^ BelongsTo(x, y))
- For all objects x, if x is a person, then there exists an object y such that y is a house and x belongs to y
- Every person belongs to a house