import numpy as np
import cv2
from skimage.filters import thresholding
np.set_printoptions(threshold = np.inf)


def is_outlier(value, p25, p75):
    """Check if value is an outlier
    """
    lower = p25 - 1.5 * (p75 - p25)
    upper = p75 + 1.5 * (p75 - p25)
    return value <= lower or value >= upper


def get_indices_of_outliers(values):
    """Get outlier indices (if any)
    """
    p25 = np.percentile(values, 25)
    p75 = np.percentile(values, 75)

    indices_of_outliers = []
    for ind, value in enumerate(values):
        if is_outlier(value, p25, p75):
            indices_of_outliers.append(ind)
    upper = p75 + 1.5 * (p75 - p25)
    return indices_of_outliers, upper


def keep_largest_component(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    largest_component = []

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] == 1:
                component = []
                dfs(grid, i, j, visited, component)
                if len(component) > len(largest_component):
                    largest_component = component

    largest_grid = [[0] * cols for _ in range(rows)]
    for i, j in largest_component:
        largest_grid[i][j] = 1

    return largest_grid


def dfs(grid, row, col, visited, component):
    rows = len(grid)
    cols = len(grid[0])
    stack = [(row, col)]

    while stack:
        curr_row, curr_col = stack.pop()
        if not visited[curr_row][curr_col] and grid[curr_row][curr_col] == 1:
            visited[curr_row][curr_col] = True
            component.append((curr_row, curr_col))

            # Explore neighbors in four directions (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_row = curr_row + dx
                new_col = curr_col + dy

                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    stack.append((new_row, new_col))

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
        if max_count < Hash[i]:
            res = i
            max_count = Hash[i]
    return res


def isodata(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_isodata(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl

def li(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_li(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl

def mean(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_mean(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl

def otsu(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_otsu(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl

def triangle(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_triangle(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl

def yen(file1, file2, k):

    img_ori = cv2.imread(file1, -1)
    segmented_cells = cv2.imread(file2, -1)

    rows = segmented_cells.shape[0]
    cols = segmented_cells.shape[1]

    s_c = segmented_cells.flatten()
    s_c = [x for x in s_c if x != 0]

    segmented_cells = np.uint8(segmented_cells)
    edge = cv2.Canny(segmented_cells, 0, max(s_c))

    img_contour = np.zeros((rows, cols))
    cell_num = np.amax(segmented_cells)
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour += edge

    img_blank1 = np.zeros((rows, cols))
    img_blank1[img_contour == 0] = 1
    img_blank2 = np.zeros((rows, cols))
    img_blank4 = np.zeros((rows, cols))
    img_blank5 = np.ones((rows, cols))

    img_blank2[segmented_cells > 0] = 1
    img_blank3 = np.multiply(img_ori, img_blank2)
    img_blank3 = np.multiply(img_blank3, img_blank1)
    img_blank6 = np.multiply(segmented_cells, img_blank1)

    threshold_list = img_blank3[img_blank3 != 0]
    indices_of_outliers, res = get_indices_of_outliers(threshold_list)
    if indices_of_outliers != []:
        thres1 = threshold_list[threshold_list > res][0]
    else:
        thres1 = res

    img_blank3[img_blank3 >= thres1] = 0
    thres2 = thresholding.threshold_yen(img_blank3[img_blank3 != 0])

    img_blank5[img_blank3 < thres2] = 0
    img_blank5[img_blank3 == 0] = 1
    img_blank4 = img_blank2 - img_blank5

    img_global_nucl = np.multiply(img_blank4, segmented_cells)

    img_blank6 = np.uint8(img_blank6)

    # Perform distance transform on the grayscale image
    dist_transform = cv2.distanceTransform(img_blank6, cv2.DIST_L2, 3)
    dist_transform2 = np.zeros((rows, cols))
    dist_transform2[dist_transform > 0] = 1

    dist_transform2 = np.multiply(dist_transform2, segmented_cells)

    img_contour2 = np.zeros((rows, cols))

    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[dist_transform2 == i + 1] = 1
        img_blank = np.uint8(img_blank)

        edge = cv2.Canny(img_blank, 0, 1)
        img_contour2 += edge

    img_contour2[img_contour2 > 0] = 1
    boundary_pixel = np.multiply(img_contour2, dist_transform)
    s_c2 = boundary_pixel.flatten()
    s_c2 = [x for x in s_c2 if x != 0]
    average_num = sum(s_c2) / len(s_c2)

    # Determine the distance threshold as the valley between the peaks
    distance_threshold = average_num + k

    # Create a mask by setting pixels with distance values below the threshold to 255 (nucleus regions) and others to 0
    nucleus_mask = np.zeros_like(img_global_nucl)
    nucleus_mask[dist_transform < distance_threshold] = 255

    # Display the resulting nucleus mask

    img_blank7 = np.ones((rows, cols))
    img_blank7[nucleus_mask == 255] = 0
    nucleus_mask = np.multiply(img_blank7, img_global_nucl)
    img_blank8 = np.zeros((rows, cols))

    for i in range(max(s_c)):
        img_blank = np.zeros((rows, cols))
        img_blank[segmented_cells == i + 1] = 1

        overlapping = np.multiply(nucleus_mask, img_blank)
        overlapping = np.uint8(overlapping)

        retval1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(overlapping)
        img_labels = labels1.flatten()
        img_labels = [x for x in img_labels if x != 0]
        n = len(img_labels)
        mf_num = mostFrequent(img_labels, n)

        img_blank8[labels1 == mf_num] = 1

    img_blank9 = np.zeros((rows, cols))
    img_blank9[segmented_cells > 0] = 1
    img_blank9 -= img_blank8
    result = np.multiply(img_blank9, segmented_cells)

    final_result = np.zeros((rows, cols))
    for i in range(cell_num):
        img_blank = np.zeros((rows, cols))
        img_blank[result == i + 1] = 1
        img_blank = np.uint8(img_blank)
        largest_grid = keep_largest_component(img_blank)
        final_result += largest_grid

    final_result_cyto = np.multiply(final_result, segmented_cells)
    final_result_nucl = segmented_cells - final_result_cyto
    return final_result_cyto, final_result_nucl


