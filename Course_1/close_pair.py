"""
  Compute nearest pair of points using divide and conquer
  Time Complexity: O(nlogn)

  To prove why we only need to check at most 7 points during the procedure of finding split pair, hold close to
  those two Lemmas provided in video.
  1) all the points have to be within the rectangular
  2) each square (delta/2) can only have one point. If two points cohabit one square, then it violates the rule that
  their distance has to be greater than delta.   
"""
import numpy as np


def distance(pair1, pair2):
    return np.sqrt((pair1[0] - pair2[0]) ** 2 + (pair1[1] - pair2[1]) ** 2)


def brute_force(px):
    num_points = len(px)
    pm, qm, dm = px[0], px[1], distance(px[0], px[1])
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            d_temp = distance(px[i], px[j])
            if d_temp < dm:
                pm, qm, dm = px[i], px[j], d_temp

    return pm, qm, dm


def closest_split_pair(plist_y,  delta,  mid_x):
    sub_y = [pair for pair in plist_y if (pair[0] >= mid_x - delta) and (pair[0] <= mid_x + delta)]
    num_points = len(sub_y)
    pm, qm, dm = None, None, delta
    for i in range(num_points - 1):
        for j in range(i + 1, min(i + 8, num_points)):
            d_temp = distance(sub_y[i], sub_y[j])
            if d_temp < dm:
                dm = d_temp
                pm, qm = sub_y[i], sub_y[j]
    return pm, qm, dm


def closest_pair(plist_x, plist_y):
    num_points = len(plist_x)
    if num_points <= 3:
        return brute_force(plist_x)

    mid_point = num_points // 2
    Qx = plist_x[:mid_point]
    Rx = plist_x[mid_point:]
    Qy = []
    Ry = []

    mid_point_x = plist_x[mid_point][0]
    for pair in plist_y:
        if pair[0] <= mid_point_x:
            Qy.append(pair)
        else:
            Ry.append(pair)

    p1, q1, d1 = closest_pair(Qx, Qy)
    p2, q2, d2 = closest_pair(Rx, Ry)
    if d1 < d2:
        pm, qm, dm = p1, q1, d1
    else:
        pm, qm, dm = p2, q2, d2

    p3, q3, d3 = closest_split_pair(plist_y, dm, mid_point_x)

    return (pm, qm, dm) if dm <= d3 else (p3, q3, d3)


def solution(point_list):
    px = sorted(point_list, key=lambda x: x[0])
    py = sorted(point_list, key=lambda x: x[1])
    return closest_pair(px, py)


if __name__ == '__main__':
    print(solution([(1, 3), (8, 2), (2, 5), (9, 5), (7, 7)]))
    print(solution([(-1000, -10), (-729, -9), (-512, -8), (-343, -7), (-216, -6), (-125, -5), (-64, -4), (-27, -3), (-8, -2), (-1, -1), (0, 0), (8, 2), (27, 3), (64, 4), (125, 5), (216, 6), (343, 7), (512, 8), (729, 9)]))