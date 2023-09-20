import cv2
import numpy as np
from PIL import Image
np.set_printoptions(threshold = np.inf)
import math as mt
import pandas as pd


def POSEA(file1, file2):
    def mostFrequent(arr, n):
        # Insert all elements in Hash.
        Hash = dict()
        for i in range(n):
            if arr[i] in Hash.keys():
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1

        # find the max frequency
        max_count = 0
        res = -1
        for i in Hash:
            if (max_count < Hash[i]):
                res = i
                max_count = Hash[i]
        return res

    img_cp = cv2.imread(file1, -1)
    img_gt = cv2.imread(file2, -1)
    img_cp = img_cp.astype(int)

    img_gt = img_gt.astype(int)
    img_gtt = img_gt.flatten()

    img_gtt = [x for x in img_gtt if x != 0]
    n = len(img_gtt)
    level1 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level1]
    n = len(img_gtt)
    level2 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level2]
    n = len(img_gtt)
    level3 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level3]
    n = len(img_gtt)
    level4 = mostFrequent(img_gtt, n)

    img_gt1 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt1[img_gt == level1] = 1
    img_gt2 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt2[img_gt == level2] = 1
    img_gt3 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt3[img_gt == level3] = 1
    img_gt4 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt4[img_gt == level4] = 1
    img_gt_mask = img_gt1 + img_gt2 + img_gt3 + img_gt4

    img_cp_mask = np.zeros((img_cp.shape[0], img_cp.shape[1]))
    img_cp_mask[img_cp > 0] = 1
    area_cp = sum(sum(img_cp_mask))
    combine = img_cp_mask + img_gt_mask
    combine[combine == 1] = 0
    combine[combine == 2] = 1
    TP = sum(sum(combine))
    FP = area_cp - TP
    FN = sum(sum(img_gt_mask)) - TP

    Pre_mask_cp = TP / (TP + FP)

    Re_mask_cp = TP / (TP + FN)

    F_mask_cp = 2 * Pre_mask_cp * Re_mask_cp / (Pre_mask_cp + Re_mask_cp)

    # ######Object part

    img_gt1 = np.array(img_gt1, dtype=np.uint8)
    img_gt2 = np.array(img_gt2, dtype=np.uint8)
    img_gt3 = np.array(img_gt3, dtype=np.uint8)
    img_gt4 = np.array(img_gt4, dtype=np.uint8)

    _, labels1, stats1, _ = cv2.connectedComponentsWithStats(img_gt1)
    _, labels2, stats2, _ = cv2.connectedComponentsWithStats(img_gt2)
    _, labels3, stats3, _ = cv2.connectedComponentsWithStats(img_gt3)
    _, labels4, stats4, _ = cv2.connectedComponentsWithStats(img_gt4)

    num_gt1, _ = np.shape(stats1)
    num_gt1 -= 1
    num_gt2, _ = np.shape(stats2)
    num_gt2 -= 1
    num_gt3, _ = np.shape(stats3)
    num_gt3 -= 1
    num_gt4, _ = np.shape(stats4)
    num_gt4 -= 1
    num_total = num_gt1 + num_gt2 + num_gt3 + num_gt4

    for i in range(num_gt2):
        labels2[labels2 == i + 1] = num_gt1 + 1 + i

    for i in range(num_gt3):
        labels3[labels3 == i + 1] = num_gt1 + num_gt2 + 1 + i

    for i in range(num_gt4):
        labels4[labels4 == i + 1] = num_gt1 + num_gt2 + num_gt3 + 1 + i

    img_relabel = labels1 + labels2 + labels3 + labels4

    cell_each = []
    cell_each_F = []
    cell_each_P = []
    cell_each_R = []

    TP_cp_obj = 0
    FP_cp_obj = 0
    cp_match_mask = 0
    fn_cp_obj = 0

    for i in range(num_total):
        img_blank = np.zeros((img_gt.shape[0], img_gt.shape[1]))
        img_blank[img_relabel == i + 1] = 1
        GT_area = sum(sum(img_blank))
        overlapping = np.multiply(img_cp, img_blank)

        if sum(sum(overlapping)) == 0:
            fn_cp_obj += sum(sum(img_blank))
            cell_each.append(0)

        overlapping_cp_obj = overlapping.flatten()
        overlapping_cp_obj = overlapping_cp_obj[overlapping_cp_obj != 0]
        overlapping_cp_obj = overlapping_cp_obj.astype(int)
        counts_cp_obj = np.bincount(overlapping_cp_obj)

        if counts_cp_obj.size > 0:
            mf_value_cp_obj = np.argmax(counts_cp_obj)
            img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank[overlapping == mf_value_cp_obj] = 1
            TP_cp_obj += sum(sum(img_blank))

            img_ones = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones2 = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones[img_blank > 0] = 0

            difference_cp_1 = (sum(sum(np.multiply(img_ones2, img_cp))) - sum(
                sum(np.multiply(img_ones, img_cp)))) / sum(sum(img_blank))
            img_blank_cp = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank_cp[img_cp == difference_cp_1] = 1
            cp_match_mask += img_blank_cp
            FP_cp_obj += (sum(sum(img_blank_cp)) - sum(sum(img_blank)))

            TP_cell1 = sum(sum(img_blank))
            FP_cell1 = sum(sum(img_blank_cp)) - sum(sum(img_blank))
            FN_cell1 = GT_area - sum(sum(img_blank))

            Pre_cell1 = TP_cell1 / (TP_cell1 + FP_cell1)
            Re_cell1 = TP_cell1 / (TP_cell1 + FN_cell1)
            F_cell1 = 2 * Pre_cell1 * Re_cell1 / (Pre_cell1 + Re_cell1)
            cell_each_P.append(Pre_cell1)
            cell_each_R.append(Re_cell1)
            cell_each_F.append(F_cell1)

    img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
    img_blank[img_cp > 0] = 1
    img_cp_mask = img_blank

    cp_match_mask[cp_match_mask > 0] = 1

    FP_cp_obj = FP_cp_obj + sum(sum(img_cp_mask)) - sum(sum(cp_match_mask))
    FN_cp_obj = sum(sum(img_gt_mask)) - TP_cp_obj

    F_cp_obj = (2 * TP_cp_obj) / (2 * TP_cp_obj + FN_cp_obj + FP_cp_obj)

    Pre_cp_obj = TP_cp_obj / (TP_cp_obj + FP_cp_obj)

    Re_cp_obj = TP_cp_obj / (TP_cp_obj + FN_cp_obj)

    cell_each_F.extend(cell_each)
    cell_each_R.extend(cell_each)
    cell_each_P.extend(cell_each)

    cell_each_F = np.array(cell_each_F)
    cell_each_R = np.array(cell_each_R)
    cell_each_P = np.array(cell_each_P)

    cell_each_F_average = sum(cell_each_F) / len(cell_each_F)
    cell_each_R_average = sum(cell_each_R) / len(cell_each_R)
    cell_each_P_average = sum(cell_each_P) / len(cell_each_P)

    cell_each_F = pd.DataFrame([[i] for i in np.array(cell_each_F)])
    cell_each_R = pd.DataFrame([[i] for i in np.array(cell_each_R)])
    cell_each_P = pd.DataFrame([[i] for i in np.array(cell_each_P)])

    data = np.column_stack([cell_each_F, cell_each_P, cell_each_R])

    data = pd.DataFrame(data=data, columns=['F-measure', 'Precision', 'Recall'])

    return F_mask_cp, Pre_mask_cp, Re_mask_cp, F_cp_obj, Pre_cp_obj, Re_cp_obj, cell_each_F_average, cell_each_P_average, cell_each_R_average, data

def POSEA2(file1, file2, file3):

    def mostFrequent(arr, n):
        # Insert all elements in Hash.
        Hash = dict()
        for i in range(n):
            if arr[i] in Hash.keys():
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1

        # find the max frequency
        max_count = 0
        res = -1
        for i in Hash:
            if (max_count < Hash[i]):
                res = i
                max_count = Hash[i]
        return res


    img_cp = np.array(file1)
    img_gt = cv2.imread(file2, -1)
    img_gt_CorNmask = cv2.imread(file3, -1)

    img_cp = img_cp.astype(int)
    img_gt = img_gt.astype(int)
    img_gt_CorNmask = img_gt_CorNmask.astype(int)
    img_gtt = img_gt.flatten()


    img_gtt = [x for x in img_gtt if x != 0]
    n = len(img_gtt)
    level1 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level1]
    n = len(img_gtt)
    level2 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level2]
    n = len(img_gtt)
    level3 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level3]
    n = len(img_gtt)
    level4 = mostFrequent(img_gtt, n)

    img_gt1 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt1[img_gt == level1] = 1
    img_gt2 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt2[img_gt == level2] = 1
    img_gt3 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt3[img_gt == level3] = 1
    img_gt4 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt4[img_gt == level4] = 1
    img_gt_mask = img_gt1 + img_gt2 + img_gt3 + img_gt4

    img_gt_CorNmask[img_gt_CorNmask > 0] = 1
    img_cp_mask = np.zeros((img_cp.shape[0], img_cp.shape[1]))
    img_cp_mask[img_cp > 0] = 1
    area_cp = sum(sum(img_cp_mask))
    combine = img_cp_mask + img_gt_CorNmask
    combine[combine == 1] = 0
    combine[combine == 2] = 1
    TP = sum(sum(combine))
    FP = area_cp - TP
    FN = sum(sum(img_gt_CorNmask)) - TP

    Pre_mask_cp = TP / (TP + FP)

    Re_mask_cp = TP / (TP + FN)

    F_mask_cp = 2 * Pre_mask_cp * Re_mask_cp / (Pre_mask_cp + Re_mask_cp)

    # ######Object part

    img_gt1 = np.array(img_gt1, dtype=np.uint8)
    img_gt2 = np.array(img_gt2, dtype=np.uint8)
    img_gt3 = np.array(img_gt3, dtype=np.uint8)
    img_gt4 = np.array(img_gt4, dtype=np.uint8)

    _, labels1, stats1, _ = cv2.connectedComponentsWithStats(img_gt1)
    _, labels2, stats2, _ = cv2.connectedComponentsWithStats(img_gt2)
    _, labels3, stats3, _ = cv2.connectedComponentsWithStats(img_gt3)
    _, labels4, stats4, _ = cv2.connectedComponentsWithStats(img_gt4)

    num_gt1, _ = np.shape(stats1)
    num_gt1 -= 1
    num_gt2, _ = np.shape(stats2)
    num_gt2 -= 1
    num_gt3, _ = np.shape(stats3)
    num_gt3 -= 1
    num_gt4, _ = np.shape(stats4)
    num_gt4 -= 1
    num_total = num_gt1 + num_gt2 + num_gt3 + num_gt4

    for i in range(num_gt2):
        labels2[labels2 == i + 1] = num_gt1 + 1 + i

    for i in range(num_gt3):
        labels3[labels3 == i + 1] = num_gt1 + num_gt2 + 1 + i

    for i in range(num_gt4):
        labels4[labels4 == i + 1] = num_gt1 + num_gt2 + num_gt3 + 1 + i

    img_relabel = labels1 + labels2 + labels3 + labels4
    img_relabel = np.multiply(img_gt_CorNmask, img_relabel)

    cell_each = []
    cell_each_F = []
    cell_each_P = []
    cell_each_R = []

    TP_cp_obj = 0
    FP_cp_obj = 0
    cp_match_mask = 0
    fn_cp_obj = 0

    for i in range(num_total):
        img_blank = np.zeros((img_gt.shape[0], img_gt.shape[1]))
        img_blank[img_relabel == i + 1] = 1
        GT_area = sum(sum(img_blank))
        overlapping = np.multiply(img_cp, img_blank)

        if sum(sum(overlapping)) == 0:
            fn_cp_obj += sum(sum(img_blank))
            cell_each.append(0)

        overlapping_cp_obj = overlapping.flatten()
        overlapping_cp_obj = overlapping_cp_obj[overlapping_cp_obj != 0]
        overlapping_cp_obj = overlapping_cp_obj.astype(int)
        counts_cp_obj = np.bincount(overlapping_cp_obj)

        if counts_cp_obj.size > 0:
            mf_value_cp_obj = np.argmax(counts_cp_obj)
            img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank[overlapping == mf_value_cp_obj] = 1
            TP_cp_obj += sum(sum(img_blank))

            img_ones = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones2 = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones[img_blank > 0] = 0

            difference_cp_1 = (sum(sum(np.multiply(img_ones2, img_cp))) - sum(
                sum(np.multiply(img_ones, img_cp)))) / sum(sum(img_blank))
            img_blank_cp = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank_cp[img_cp == difference_cp_1] = 1
            cp_match_mask += img_blank_cp
            FP_cp_obj += (sum(sum(img_blank_cp)) - sum(sum(img_blank)))

            TP_cell1 = sum(sum(img_blank))
            FP_cell1 = sum(sum(img_blank_cp)) - sum(sum(img_blank))
            FN_cell1 = GT_area - sum(sum(img_blank))

            Pre_cell1 = TP_cell1 / (TP_cell1 + FP_cell1)
            Re_cell1 = TP_cell1 / (TP_cell1 + FN_cell1)
            F_cell1 = 2 * Pre_cell1 * Re_cell1 / (Pre_cell1 + Re_cell1)
            cell_each_P.append(Pre_cell1)
            cell_each_R.append(Re_cell1)
            cell_each_F.append(F_cell1)

    img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
    img_blank[img_cp > 0] = 1
    img_cp_mask = img_blank

    cp_match_mask[cp_match_mask > 0] = 1

    FP_cp_obj = FP_cp_obj + sum(sum(img_cp_mask)) - sum(sum(cp_match_mask))
    FN_cp_obj = sum(sum(img_gt_CorNmask)) - TP_cp_obj

    F_cp_obj = (2 * TP_cp_obj) / (2 * TP_cp_obj + FN_cp_obj + FP_cp_obj)

    Pre_cp_obj = TP_cp_obj / (TP_cp_obj + FP_cp_obj)

    Re_cp_obj = TP_cp_obj / (TP_cp_obj + FN_cp_obj)

    cell_each_F.extend(cell_each)
    cell_each_R.extend(cell_each)
    cell_each_P.extend(cell_each)

    cell_each_F = np.array(cell_each_F)
    cell_each_R = np.array(cell_each_R)
    cell_each_P = np.array(cell_each_P)

    cell_each_F_average = sum(cell_each_F) / len(cell_each_F)
    cell_each_R_average = sum(cell_each_R) / len(cell_each_R)
    cell_each_P_average = sum(cell_each_P) / len(cell_each_P)

    cell_each_F = pd.DataFrame([[i] for i in np.array(cell_each_F)])
    cell_each_R = pd.DataFrame([[i] for i in np.array(cell_each_R)])
    cell_each_P = pd.DataFrame([[i] for i in np.array(cell_each_P)])

    data = np.column_stack([cell_each_F, cell_each_P, cell_each_R])

    data = pd.DataFrame(data=data, columns=['F-measure', 'Precision', 'Recall'])

    return F_mask_cp, Pre_mask_cp, Re_mask_cp, F_cp_obj, Pre_cp_obj, Re_cp_obj, cell_each_F_average, cell_each_P_average, cell_each_R_average, data



def POSEA3(file1, file2, file3):

    def mostFrequent(arr, n):
        # Insert all elements in Hash.
        Hash = dict()
        for i in range(n):
            if arr[i] in Hash.keys():
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1

        # find the max frequency
        max_count = 0
        res = -1
        for i in Hash:
            if (max_count < Hash[i]):
                res = i
                max_count = Hash[i]
        return res


    img_cp = np.array(file1)
    img_gt = cv2.imread(file2, -1)
    img_gt_CorNmask = cv2.imread(file3, -1)

    img_cp = img_cp.astype(int)
    img_gt = img_gt.astype(int)
    img_gt_CorNmask = img_gt_CorNmask.astype(int)
    img_gtt = img_gt.flatten()


    img_gtt = [x for x in img_gtt if x != 0]
    n = len(img_gtt)
    level1 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level1]
    n = len(img_gtt)
    level2 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level2]
    n = len(img_gtt)
    level3 = mostFrequent(img_gtt, n)

    img_gtt = [x for x in img_gtt if x != level3]
    n = len(img_gtt)
    level4 = mostFrequent(img_gtt, n)

    img_gt1 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt1[img_gt == level1] = 1
    img_gt2 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt2[img_gt == level2] = 1
    img_gt3 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt3[img_gt == level3] = 1
    img_gt4 = np.zeros((img_gt.shape[0], img_gt.shape[1]))
    img_gt4[img_gt == level4] = 1
    img_gt_mask = img_gt1 + img_gt2 + img_gt3 + img_gt4
    img_gt_CorNmask[img_gt_CorNmask > 0] = 1


    # ######Object part

    img_gt1 = np.array(img_gt1, dtype=np.uint8)
    img_gt2 = np.array(img_gt2, dtype=np.uint8)
    img_gt3 = np.array(img_gt3, dtype=np.uint8)
    img_gt4 = np.array(img_gt4, dtype=np.uint8)

    _, labels1, stats1, _ = cv2.connectedComponentsWithStats(img_gt1)
    _, labels2, stats2, _ = cv2.connectedComponentsWithStats(img_gt2)
    _, labels3, stats3, _ = cv2.connectedComponentsWithStats(img_gt3)
    _, labels4, stats4, _ = cv2.connectedComponentsWithStats(img_gt4)

    num_gt1, _ = np.shape(stats1)
    num_gt1 -= 1
    num_gt2, _ = np.shape(stats2)
    num_gt2 -= 1
    num_gt3, _ = np.shape(stats3)
    num_gt3 -= 1
    num_gt4, _ = np.shape(stats4)
    num_gt4 -= 1
    num_total = num_gt1 + num_gt2 + num_gt3 + num_gt4

    for i in range(num_gt2):
        labels2[labels2 == i + 1] = num_gt1 + 1 + i

    for i in range(num_gt3):
        labels3[labels3 == i + 1] = num_gt1 + num_gt2 + 1 + i

    for i in range(num_gt4):
        labels4[labels4 == i + 1] = num_gt1 + num_gt2 + num_gt3 + 1 + i

    img_relabel = labels1 + labels2 + labels3 + labels4
    img_relabel = np.multiply(img_gt_CorNmask, img_relabel)

    cell_each = []
    cell_each_F = []
    cell_each_P = []
    cell_each_R = []

    TP_cp_obj = 0
    FP_cp_obj = 0
    cp_match_mask = 0
    fn_cp_obj = 0

    for i in range(num_total):
        img_blank = np.zeros((img_gt.shape[0], img_gt.shape[1]))
        img_blank[img_relabel == i + 1] = 1
        GT_area = sum(sum(img_blank))
        overlapping = np.multiply(img_cp, img_blank)

        if sum(sum(overlapping)) == 0:
            fn_cp_obj += sum(sum(img_blank))
            cell_each.append(0)

        overlapping_cp_obj = overlapping.flatten()
        overlapping_cp_obj = overlapping_cp_obj[overlapping_cp_obj != 0]
        overlapping_cp_obj = overlapping_cp_obj.astype(int)
        counts_cp_obj = np.bincount(overlapping_cp_obj)

        if counts_cp_obj.size > 0:
            mf_value_cp_obj = np.argmax(counts_cp_obj)
            img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank[overlapping == mf_value_cp_obj] = 1
            TP_cp_obj += sum(sum(img_blank))

            img_ones = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones2 = np.ones((img_cp.shape[0], img_cp.shape[1]))
            img_ones[img_blank > 0] = 0

            difference_cp_1 = (sum(sum(np.multiply(img_ones2, img_cp))) - sum(
                sum(np.multiply(img_ones, img_cp)))) / sum(sum(img_blank))
            img_blank_cp = np.zeros((img_cp.shape[0], img_cp.shape[1]))
            img_blank_cp[img_cp == difference_cp_1] = 1
            cp_match_mask += img_blank_cp
            FP_cp_obj += (sum(sum(img_blank_cp)) - sum(sum(img_blank)))


    img_blank = np.zeros((img_cp.shape[0], img_cp.shape[1]))
    img_blank[img_cp > 0] = 1
    img_cp_mask = img_blank

    cp_match_mask[cp_match_mask > 0] = 1

    FP_cp_obj = FP_cp_obj + sum(sum(img_cp_mask)) - sum(sum(cp_match_mask))
    FN_cp_obj = sum(sum(img_gt_CorNmask)) - TP_cp_obj

    F_cp_obj = (2 * TP_cp_obj) / (2 * TP_cp_obj + FN_cp_obj + FP_cp_obj)


    return F_cp_obj




