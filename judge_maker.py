def make_judge(grade, points):

    count_below_30 = sum(1 for point in points if point <= 30)

    # 一度でも10点以下の点数があれば不合格
    if any(point < 10 for point in points):
        return 3  # 不合格

    # 成績に基づいた判定
    if grade in ["A", "B", "C"]:
        return 1  # 合格
    elif grade == "D":
        if count_below_30 >= 1:
            return 2  # 再テスト
        return 1  # 合格
    elif grade == "E":
        return 3  # 不合格

    return 1  # デフォルトで合格（不明な成績の場合）


# テスト用コード（必要に応じてコメントアウト）
if __name__ == "__main__":
    # テストケース
    print(make_judge("A", [65, 70, 75, 80, 90, 85, 95, 100, 95, 80]))  # 合格: 1
    print(make_judge("D", [60, 20, 50, 40, 30, 10, 90, 100, 85, 75]))  # 再テスト: 2
    print(make_judge("E", [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]))  # 不合格: 3
    print(make_judge("C", [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]))  # 不合格: 3
