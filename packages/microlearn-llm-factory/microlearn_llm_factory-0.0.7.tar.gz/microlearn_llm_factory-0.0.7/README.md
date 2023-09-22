# LLM Factory

This repo maintains the source code for python pip package `llm-factory`.

## Setup dev environment

1. Create virtual environment: `conda create -n llm_factory_test_env -y python=3.8`
1. Activate environment: `conda activate llm_factory_test_env`
1. Install dependencies: `pip install -r dev_requirements.txt`

## Run unit tests

1. Activate environment: `conda activate llm_factory_test_env`
1. Run: `pytest src/tests/test_llm_factory.py -v --log-cli-level INFO`

## Release new package

1. Push your changes
1. In GitHub:
