_base_ = [
    "./faster_rcnn_r50_fpn_1x_cityscapes.py",
]

model = dict(
    roi_head=dict(
        bbox_roi_extractor=dict(
            roi_layer=dict(type="GpsaRoIPool", output_size=7, num_features=256),
        )
    )
)
