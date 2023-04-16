# DetectGPT: Distinguishing between Machine-Generated and Human-Written Text

This repository is an exrtension of the original work done on the detectGPT model by incorporating three datasets on new writing styles and verifying detectGPT's performance on them.  

## Original implementation of the experiments in the [DetectGPT paper](https://arxiv.org/abs/2301.11305v1).

An interactive demo of DetectGPT can be found [here](https://detectgpt.ericmitchell.ai).

## Instructions

First, install the Python dependencies:

```{python}
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
```

Second, execute `run.py` using `python run.py` and provide the appropriate command line arguments to the script.

If you have new dataset to include, add its inclusion in `custom_datasets.py` script and then execute `run.py` as instructed above.

Please refer to the script for more details on how each function is working and what CLI to give.

Here, we extend the original DetectGPT paper. We apply the method on new datasets and compare the results to the ones achieved by the original authors, verifying the algorithm works well on new datasets (especially ones that have a different style of text). Further, we document the original source code and provide a document outlining how we ran our code (and tuned associated hyperparameters).

### Future Work:

1. Improving GPT-2 model using ensemble methods
2. Further exploring the relationship between prompting and detection
3. Determing whether negative log likelihood curvature is present for generative models in other domains: audio, video and images.
