import torch
from torchinfo import summary
import prp_c3d
import vp_c3d


MODEL_PATHS = [
    "D:/Projects/ai-research-school/PRP-video-pace/PRP/outputs/ft_classify_default_UCF-101/05-20-15-00/60.pth.tar",
    "D:/Projects/ai-research-school/PRP-video-pace/video-pace/outputs/epoch-03.pth.tar"
]

MODEL_TYPES = [
    prp_c3d.C3D(with_classifier=False),
    # vp_c3d.C3D()
]


def get_model_summaries(models: list):
    for model in models:
        # print(model)
        # state_dict = torch.load(path)['model_state_dict']
        # state_dict = torch.load(model)
        # print(state_dict.keys())
        temp = model
        # summary(temp, input_size=(3, 16, 112, 112))
        # summary(temp)
        print(temp)


if __name__ == '__main__':
    get_model_summaries(MODEL_TYPES)
