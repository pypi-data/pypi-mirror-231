import cv2
import numpy as np

from game_tools.recognition.imageutls import extract_color_regions


def read_text_file(file_path):
    try:
        # with open(file_path, 'r', encoding='utf-8') as file:
        with open(file_path, 'r', encoding='gbk') as file:
            text = file.read()
        return text
    except IOError:
        print(f"无法读取文件: {file_path}")
        return None


def parse_text(text, target_string):
    lines = text.splitlines()
    datas = []
    for line in lines:
        words = line.strip().split("$")
        if words and target_string == words[1]:
            datas.append(words)
    return datas


def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    return img.astype(np.float32)


def get_binary_array(des):
    bin_str = ''
    for c in des:
        byte = int(c, 16)
        byte_bin = bin(byte)[2:].zfill(4)
        bin_str += byte_bin
    m = len(bin_str) // 11
    if m % 4:
        bin_str = bin_str[:-(m % 4)]
    arr = np.array([list(bin_str[i:i + 11]) for i in range(0, len(bin_str), 11)], dtype=np.float32)
    arr = arr.transpose()
    return arr


# 单个点阵识别
def find_lattice(target_image, region, target_string, color_ranges, threshold, txt):
    threshold = 1 - threshold

    text = read_text_file(txt)
    if text is None:
        return -1, -1

    des = parse_text(text, target_string)

    if des is None:
        return -1, -1

    if region is None:
        _, w, h = target_image.shape
        x1, y1, x2, y2 = (0, 0, w, h)
        img = target_image
    else:
        x1, y1, x2, y2 = region
        img = extract_color_regions(target_image[y1:y2, x1:x2], color_ranges)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    img = preprocess_image(img)
    # cv2.imshow('1233', img)
    # cv2.waitKey(0)
    for d in des:
        # print(d)
        arr = get_binary_array(d[0])


        result = cv2.matchTemplate(arr, img, cv2.TM_SQDIFF_NORMED)
        min_val, _, min_loc, _ = cv2.minMaxLoc(result)
        w, h = arr.shape

        # print('min_val', min_val, 'threshold', threshold)
        if min_val < threshold:
            print('找到了', target_string, 'min_val', min_val, 'threshold', threshold)
            # logger.debug(f'找到了, {target_string}, min_val, {min_val}, threshold, {threshold}')
            return int(min_loc[0] + h / 2 + x1), int(min_loc[1] + w / 2 + y1)

    # print("没找到", target_string, 'min_val', min_val, 'threshold', threshold)
    # logger.debug(f'没找到, {target_string}, min_val, {min_val}, threshold, {threshold}')
    return -1, -1


# 找到所有符合的点阵
def find_lattices(target_image, region, target_string, color_ranges, threshold, txt):
    threshold = 1 - threshold
    text = read_text_file(txt)
    if text is None:
        return []

    words = parse_text(text, target_string)

    if words is None:
        return []

    if region is not None:
        x1, y1, x2, y2 = region
        target_image = target_image[y1:y2, x1:x2]
    else:
        h, w, _ = target_image.shape
        x1, y1, x2, y2 = 0, 0, w, h

    target_image = extract_color_regions(target_image, color_ranges)

    target_image = preprocess_image(target_image)

    matched_points = []

    for word in words:
        arr = get_binary_array(word[0])
        result = cv2.matchTemplate(arr, target_image, cv2.TM_SQDIFF_NORMED)

        min_val, max_val, min_loc, _ = cv2.minMaxLoc(result)
        print(word[1], 'min_val', min_val, 'threshold', threshold)
        # 检查最小值是否小于阈值
        if min_val <= threshold:
            # 找到满足条件的索引
            indices = np.where(result <= threshold)

            # 提取满足条件的值和对应的位置
            filtered_values = result[indices]
            filtered_locations = np.transpose(indices)

            w, h = arr.shape
            # 打印满足条件的值和对应的位置
            for value, loc in zip(filtered_values, filtered_locations):
                # print('words', words[1], "Value:", value, 'Location', loc)
                # print("Location:", loc)
                point_x = loc[1] + h / 2 + x1
                point_y = loc[0] + w / 2 + y1
                matched_points.append([int(point_x), int(point_y)])
    #             color = (0, 0, 255)  # BGR颜色，表示红色
    #             cv2.circle(showimage, (int(point_x), int(point_y)), 2, color, -1)
    #
    # cv2.imshow("Image with Point", showimage)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return [list(x) for x in set(tuple(x) for x in matched_points)]
