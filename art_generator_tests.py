"""UNIT TESTING IS THE BEST!"""
import unittest
import cifar10utils
import artmaker
from PIL import Image, ImageDraw


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


class TestArtMaker(unittest.TestCase):

    def test_randomdirectionalsquig(self):
        testimage = artmaker.create_blank_canvas()
        draw = ImageDraw.Draw(testimage)
        artmaker.draw_random_directionsquig(
            draw, artmaker.create_random_color())
        self.assertIsNotNone(testimage)
        testimage.save("images/squiqtest.png")


if __name__ == '__main__':
    unittest.main()
