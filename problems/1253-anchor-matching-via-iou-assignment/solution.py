import numpy as np

def match_anchors(anchors, gt_boxes, pos_threshold=0.5, neg_threshold=0.4):
    anchors = np.asarray(anchors, dtype=float).reshape(-1, 4)
    gt_boxes = np.asarray(gt_boxes, dtype=float).reshape(-1, 4)

    n = anchors.shape[0]
    m = gt_boxes.shape[0]

    labels = np.full(n, -1, dtype=int)
    matched_gt = np.full(n, -1, dtype=int)

    # No anchors
    if n == 0:
        return labels, matched_gt

    # No ground truth: all anchors are negatives
    if m == 0:
        labels[:] = 0
        return labels, matched_gt

    # Pairwise intersection
    inter_x1 = np.maximum(anchors[:, None, 0], gt_boxes[None, :, 0])
    inter_y1 = np.maximum(anchors[:, None, 1], gt_boxes[None, :, 1])
    inter_x2 = np.minimum(anchors[:, None, 2], gt_boxes[None, :, 2])
    inter_y2 = np.minimum(anchors[:, None, 3], gt_boxes[None, :, 3])

    inter_w = np.maximum(0.0, inter_x2 - inter_x1)
    inter_h = np.maximum(0.0, inter_y2 - inter_y1)
    intersection = inter_w * inter_h

    # Areas; invalid/zero-area boxes get area 0
    anchor_w = np.maximum(0.0, anchors[:, 2] - anchors[:, 0])
    anchor_h = np.maximum(0.0, anchors[:, 3] - anchors[:, 1])
    gt_w = np.maximum(0.0, gt_boxes[:, 2] - gt_boxes[:, 0])
    gt_h = np.maximum(0.0, gt_boxes[:, 3] - gt_boxes[:, 1])

    anchor_area = anchor_w * anchor_h
    gt_area = gt_w * gt_h

    union = (
        anchor_area[:, None]
        + gt_area[None, :]
        - intersection
    )

    # IoU is 0 whenever union is zero
    iou = np.divide(
        intersection,
        union,
        out=np.zeros_like(intersection),
        where=union > 0,
    )

    # Best GT for each anchor
    best_gt = np.argmax(iou, axis=1)
    best_iou = iou[np.arange(n), best_gt]

    # Threshold assignment
    positive = best_iou >= pos_threshold
    negative = best_iou < neg_threshold

    labels[negative] = 0
    labels[positive] = 1
    matched_gt[positive] = best_gt[positive]

    # Force at least one positive anchor for every GT.
    # Iterating in GT-index order means a later GT wins if
    # multiple GTs select the same anchor.
    for j in range(m):
        anchor_idx = np.argmax(iou[:, j])
        labels[anchor_idx] = 1
        matched_gt[anchor_idx] = j

    return labels, matched_gt