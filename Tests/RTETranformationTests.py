from unittest import TestCase
from operator import itemgetter

from DataStructures.Trees import findAndRemoveChild
from Tests.TestHelpers import (
    collectLiterals,
    compare_tables,
    compareTrees,
    generateReducedTruthTable,
)

from Tests.TestCases import (
    deleteInconsistentHandleTestCase,
    promoteCommonConstraintsTestCase,
    subtractRedundantConstraintTestCase,
    cutUnnecessaryOrTestCase,
    cutUnnecessaryAndTestCase,
    zeroConstraintSubsumptionTestCase,
    oneConstraintSubsumptionTestCase,
    oneConstraintComplementSubtractionTestCase,
)

from Utilities.ReduceToElegance import ReductionSignal, reduceToElegance


class TestReduceToElegance(TestCase):
    def testInconsistentHandle(self):
        result = deleteInconsistentHandleTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))
        self.assertEqual(action, ReductionSignal.DELETE)

    def testPromoteCommonConstraints(self):
        result = promoteCommonConstraintsTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))

    def testSubtractRedundantConstraint(self):
        result = subtractRedundantConstraintTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))
        self.assertEqual(action, ReductionSignal.DELETE)

    def testCutUnnecessaryOr(self):
        result = cutUnnecessaryOrTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))

    def testCutUnnecessaryAnd(self):
        result = cutUnnecessaryAndTestCase()
        current, parentOfCurrent, constraint, constraint2 = itemgetter(
            "current",
            "parentOfCurrent",
            "constraint",
            "constraint2",
        )(result)

        action = reduceToElegance(constraint, constraint, [], [])
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))
        self.assertEqual(action, ReductionSignal.KEEP)

    def testZeroConstraintSubsumption(self):
        result = zeroConstraintSubsumptionTestCase()
        current, parentOfCurrent, constraint, constraint2 = itemgetter(
            "current",
            "parentOfCurrent",
            "constraint",
            "constraint2",
        )(result)

        action = reduceToElegance(constraint, constraint, [], [])
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))
        self.assertEqual(action, ReductionSignal.DISCONNECT)

    def testOneConstraintSubsumption(self):
        result = oneConstraintSubsumptionTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DELETE:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))

    def testOneConstraintComplementSubtraction(self):
        result = oneConstraintComplementSubtractionTestCase()
        current, parentOfCurrent, dominantSet, commandSet, constraint, constraint2 = (
            itemgetter(
                "current",
                "parentOfCurrent",
                "dominantSet",
                "commandSet",
                "constraint",
                "constraint2",
            )(result)
        )

        action = reduceToElegance(parentOfCurrent, current, dominantSet, commandSet)
        match action:
            case ReductionSignal.DISCONNECT:
                parentOfCurrent.children = findAndRemoveChild(
                    parentOfCurrent.children, current
                )

        table1 = generateReducedTruthTable(constraint, collectLiterals(constraint))
        table2 = generateReducedTruthTable(constraint2, collectLiterals(constraint2))
        self.assertEqual(compareTrees(constraint, constraint2), True)
        self.assertEqual(compare_tables(table1, table2), (True, []))
        self.assertEqual(action, ReductionSignal.DELETE)
