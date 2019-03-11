from __future__ import print_function

import numpy as np
import gluoncv as gcv
from gluoncv.model_zoo.model_store import pretrained_model_list
from common import try_gpu

@try_gpu(0)
def test_export_model_zoo():
    for model in pretrained_model_list():
        print('exporting:', model)
        kwargs = {'data_shape':(480, 480, 3)} if 'deeplab' in model or 'psp' in model else {}
        if '_gn' in model:
            continue
        try:
            gcv.utils.export_block(model, gcv.model_zoo.get_model(model, pretrained=True), **kwargs)
        except ValueError:
            # ignore non defined model name
            pass
        except AttributeError:
            # deeplab model do not support it now, skip
            pass

def test_export_model_zoo_tvm():
    try:
        import tvm
    except ImportError:
        print("No tvm installed, skipping...")
        return
    for model in ['resnet18_v1']:
        gcv.utils.export_block(model, gcv.model_zoo.get_model(model, pretrained=True))

if __name__ == '__main__':
    import nose
    nose.runmodule()
