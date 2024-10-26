import unittest
from judge_maker import make_judge


class TestMakeJudge(unittest.TestCase):

    def test_make_judge_pass_A(self):
        result = make_judge("A", [90, 85, 95, 88, 92, 100, 76, 84, 91, 93])
        self.assertEqual(result, 1)  # 合格

    def test_make_judge_pass_B(self):
        result = make_judge("B", [80, 75, 78, 85, 70, 90, 88, 82, 76, 77])
        self.assertEqual(result, 1)  # 合格

    def test_make_judge_pass_C(self):
        result = make_judge("C", [65, 60, 70, 68, 72, 64, 58, 75, 70, 66])
        self.assertEqual(result, 1)  # 合格

    def test_make_judge_retry_D(self):
        result = make_judge("D", [50, 40, 20, 25, 30, 35, 45, 60, 70, 80])
        self.assertEqual(result, 2)  # 再テスト

    def test_make_judge_fail_E(self):
        result = make_judge("E", [10, 5, 15, 20, 25, 30, 35, 40, 45, 50])
        self.assertEqual(result, 3)  # 不合格

    def test_make_judge_fail_with_below_10(self):
        result = make_judge("B", [10, 20, 30, 40, 50, 60, 70, 80, 90, 0])
        self.assertEqual(result, 3)  # 不合格

    def test_make_judge_retry_with_below_30(self):
        result = make_judge("D", [35, 40, 25, 20, 30, 28, 29, 40, 50, 60])
        self.assertEqual(result, 2)  # 再テスト


if __name__ == "__main__":
    unittest.main()
