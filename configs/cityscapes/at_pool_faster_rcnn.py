_base_ = [
    "./faster_rcnn_r50_fpn_1x_cityscapes.py",
]

load_from = ""

model = dict(
    roi_head=dict(
        bbox_roi_extractor=dict(
            roi_layer=dict(
                type="DeformAttnRoIPool", output_size=(7, 7), num_features=256
            ),
        )
    )
)

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=8,
)
