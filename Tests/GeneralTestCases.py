import enum
from unittest import TestCase
from Tests.TestHelpers import compare_tables, rteRunner
from Tests.EnfRuleTests import (
    ruleOne,
    ruleTwo,
    ruleThree,
    ruleFour,
    ruleFive,
    ruleSix,
    ruleSeven,
)
from Utilities.HelperFunctions import print_constraint_tree

EXPRESSIONS = [
    "&(B, !(|(C, |(A, &(!(B), A)))))",
    "&(B, !(|(C, |(A, &(!(B), |(K,X))))))",
    "&(B, !(|(C, |(A, &(&(B, &(C, D)), A)))))",
    "|(&(A, |(!(B), !(C))), D)",
    "&(A, &(B, &(C, &(|(A, |(B, |(C, A))), &(B, &(&(A, A), !(A)))))))",
    "|(&(A, B), |(C, D))",
    "|(a, |(b, |(c, |(d, c))))",
    "&(a, &(b, &(c, &(d,c))))",
    "&(a, &(b, &(c, &(d, !(b)))))",
    "&(a, a)",
    "!(!(a))",
    "|(|(!(a), &(a, &(b,c))), &(b, &(c, !(b))))",
    "|(a, a)",
    "|(a, |(b, |(c, |(d, !(c)))))",
    "|(A, &(B, &(C, &(D, C))))",
    "|(&(A, B), |(A, C))",
    "|(A,B)",
    "&(&(A,B),|(C,D))",
    "|(|(!(A), &(A, &(B, C))), &(B, &(C, !(B))))",
    "|(|(!(A), &(A, &(B, C))), &(C, &(B, !(B))))",
    "!(&(|(a, b), &(c,d)))",
    "|(!(a), |(!(c), !(d)))",
    "!(&(|(a, b), &(c,d)))",
    "|(&(!(a), b), |(!(c), !(d)))",
    "|(g, &(a, &(b, &(|(!(c), |(!(d), e)), |(c, &(c, f))))))",  # Example from Mosh's paper. Expected output: "|(g,&(a, &(b, &(c, |(!(d), e)))))"
    "|(g,&(a, &(b, &(c, |(!(d), e)))))",  # Reduced form of the above expression from Mosh's paper.
    "|(&(A, B), |(&(A, C), &(A, D)))",
]


class GeneralTests(TestCase):
    def testSemanticMeaning(self):
        for index, input in enumerate(EXPRESSIONS):
            constraintTree, table1, table2 = rteRunner(input)

            self.assertTrue(
                compare_tables(table1, table2),
                f"Test case {index} failed. {input} changed its semantic meaning after algorithm application.",
            )

    def testEnfRules(self):
        for index, input in enumerate(EXPRESSIONS):
            constraintTree, table1, table2 = rteRunner(input)
            if constraintTree:
                enfRules = [
                    ruleOne,
                    ruleTwo,
                    ruleThree,
                    ruleFour,
                    ruleFive,
                    ruleSix,
                    ruleSeven,
                ]

                for ruleIndex, rule in enumerate(enfRules):
                    self.assertTrue(
                        rule(constraintTree),
                        f"Test case {index} failed. Enf Rule {ruleIndex} failed.",
                    )
