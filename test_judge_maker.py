from judge_maker import make_judge


def test_make_judge_no1():
    result = make_judge("A", [9, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3  # 不合格


def test_make_judge_no2():
    result = make_judge("B", [30, 30, 30, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2  # 再テスト


def test_make_judge_no3():
    result = make_judge("C", [50, 50, 50, 50, 50, 50, 50, 50, 50, 50])
    assert result == 1  # 合格


def test_make_judge_no4():
    result = make_judge("D", [40, 40, 30, 10, 50, 60, 70, 80, 90, 100])
    assert result == 2  # 再テスト


def test_make_judge_no5():
    result = make_judge("E", [5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    assert result == 3  # 不合格
