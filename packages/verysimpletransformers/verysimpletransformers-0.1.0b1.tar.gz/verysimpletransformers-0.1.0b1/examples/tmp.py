import zlib
from pathlib import Path

import torch.cuda
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import dill

from verysimpletransformers.core import from_vst, to_vst, write_bundle
from verysimpletransformers.versioning import get_version
from verysimpletransformers.metadata_schema import MetaHeader, Metadata
from verysimpletransformers.types import DummyModel


def example_bundle():
    # Optional model configuration
    FAST = 1

    if FAST == 2:
        model = DummyModel()
    elif FAST == 1:
        model_args = ClassificationArgs(
            num_train_epochs=1,
            overwrite_output_dir=True,
            save_model_every_epoch=False,
        )

        # Create a ClassificationModel
        model = ClassificationModel(
            "bert", "./outputs", args=model_args,
            use_cuda=torch.cuda.is_available()
        )
    else:
        # Preparing train data
        train_data = [
            ["Aragorn was the heir of Isildur", 1],
            ["Frodo was the heir of Isildur", 0],
        ]
        train_df = pd.DataFrame(train_data)
        train_df.columns = ["text", "labels"]

        # Preparing eval data
        eval_data = [
            ["Theoden was the king of Rohan", 1],
            ["Merry was the king of Rohan", 0],
        ]
        eval_df = pd.DataFrame(eval_data)
        eval_df.columns = ["text", "labels"]

        model_args = ClassificationArgs(
            num_train_epochs=1,
            overwrite_output_dir=True,
            save_model_every_epoch=False,
        )

        # Create a ClassificationModel
        model = ClassificationModel(
            "bert", "prajjwal1/bert-small", args=model_args,
            use_cuda=torch.cuda.is_available()
        )

        # Train the model
        model.train_model(train_df)

    fp = Path("pytest1.vst")
    to_vst(model, fp, compression=5)

    new_model = from_vst(fp)

    # assert hasattr(model, 'predict')
    # assert not hasattr(model, 'predictx')
    assert hasattr(new_model, 'predict')
    assert not hasattr(new_model, 'predictx')


if __name__ == '__main__':
    example_bundle()
