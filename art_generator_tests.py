"""UNIT TESTING IS THE BEST!"""
import unittest
import cifar10utils


class TestCiFar10(unittest.TestCase):

    def test_create(self):
        tracker = cifar10utils.CiFarClassTracker()
        self.assertIsNotNone(tracker)

    def test_addclass_withone(self):
        tracker = cifar10utils.CiFarClassTracker()
        tracker.add_class(cifar10utils.CiFar10Classes.AIRPLANE)
        tracker.state()
        self.assertFalse(tracker.found_all())

    def test_addclass_withall(self):
        tracker = cifar10utils.CiFarClassTracker()
        tracker.add_class(cifar10utils.CiFar10Classes.AIRPLANE)
        tracker.add_class(cifar10utils.CiFar10Classes.AUTOMOBILE)
        tracker.add_class(cifar10utils.CiFar10Classes.BIRD)
        tracker.add_class(cifar10utils.CiFar10Classes.DEER)
        tracker.add_class(cifar10utils.CiFar10Classes.DOG)
        tracker.add_class(cifar10utils.CiFar10Classes.FROG)
        tracker.add_class(cifar10utils.CiFar10Classes.HORSE)
        tracker.add_class(cifar10utils.CiFar10Classes.SHIP)
        tracker.add_class(cifar10utils.CiFar10Classes.TRUCK)
        tracker.add_class(cifar10utils.CiFar10Classes.CAT)
        tracker.state()
        self.assertTrue(tracker.found_all())

    def test_addclass_truefalse(self):
        tracker = cifar10utils.CiFarClassTracker()
        self.assertTrue(tracker.add_class(
            cifar10utils.CiFar10Classes.AIRPLANE))
        self.assertFalse(tracker.add_class(
            cifar10utils.CiFar10Classes.AIRPLANE))


if __name__ == '__main__':
    unittest.main()
