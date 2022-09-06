from models import encoder
from models import losses
from models import resnet
from models import ssl

REGISTERED_MODELS = {
    'sim-clr': ssl.SimCLR,
    'eval': ssl.SSLEval,
    'eval-channel_mean': ssl.SSLEvalChannelMean,
    'semi-supervised-eval': ssl.SemiSupervisedEval,
}
