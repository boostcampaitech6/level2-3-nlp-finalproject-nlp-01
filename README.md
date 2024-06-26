# SNAP: Shortclip Navigator and Auto Producer

<a href=''><img src='https://img.shields.io/badge/Project-Demo-violet'></a>
<a href=''><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a>


## Introduction
SNAP은 멀티모달 정보를 활용해 긴 유튜브 영상에서 바이럴 숏츠를 뽑는 서비스입니다.



## Contents of Table
- [Demo](#demo)
- [Architecture](#architecture)
- [Install](#install)
- [Evaluation](#evaluation)
- [Examples](#examples)
- [Citation](#citation)
- [Acknowledgement](#acknowledgement)
- [License](#license)
- [Release](#release)

## Demo
The official demo service was closed as of March 21, 2024. If you want to check the detailed service code, please refer to the [production branch](https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer/tree/production).

Below is an image demonstrating the demo service.

![Image20240321174417](https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer/assets/71856506/519e4933-99fc-42d5-b419-60c0b385d2bc)

**Please note: This model comes with certain limitations:** <br>
- Allowed categories: `Comedy`, `Education`, `Entertainment`, `News & Politics`
    - More categories will be added soon <br>
- Language support: `English` <br>

[How can I check my youtube category?](https://techpostplus.com/how-to-find-youtube-video-category)

## Model Architecture

# ![image](https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer/assets/43094223/5df4ba49-b2d6-4e00-b687-b5e4e0edaa85)

## Service Architecture
# ![image](https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer/assets/43094223/a4bffdd1-d050-40af-98d0-95d3cd679891)

### Structure
The folder structure should be organized as follows before launching.

```shell
SNAP-Shortclip-Navigator-and-Auto-Producer
├── clip4clip
│   ├── models
│   │   └── models--openai-clip-vit-base-patch32
│   ├── Dockerfile
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── settings.py
│   └── visual_score.py
├── llm
│   ├── audio2text.py
│   ├── Dockerfile
│   ├── file
│   │   └── config.json
│   ├── models
│   │   ├── models--mistralai-Mistral-7B-Instruct-v0.2
│   │   └── models--openai-whisper-large-v3
│   ├── pipeline4eval.py
│   ├── pipeline.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── results
│   ├── settings.py
│   ├── text2summ.py
│   ├── timestamp.py
│   ├── utils
│   │   ├── audioUtils.py
│   │   ├── crawlers.py
│   │   ├── domainFlow.py
│   │   ├── get_src.py
│   │   ├── llmUtils.py
│   │   ├── preprocess.py
│   │   ├── prompts.py
│   │   ├── scores.py
│   │   └── videoUtils.py
│   └── youtube2audio.py
├── docker-compose.yml
└── snap.sh
```

## Install

Please follow the instructions below

Clone this repository
```shell
git clone https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer.git
```

Create a Docker Compose setup that builds two Docker images <br>
- One for the language model (LLM) and another for vision processing
- Automatically install dependencies using Poetry.

Run snap.sh <br>
- Put your youtube link and category in .env <br>



## Evaluation
- Will be released soon.

## Examples

![image](https://github.com/90stcamp/SNAP-Shortclip-Navigator-and-Auto-Producer/assets/71856506/a55e59d3-1e1b-4e31-9551-f81c921ee6c0)

`youtube_link`: https://www.youtube.com/watch?v=KOEfDvr4DcQ <br>
`category`: Entertainment

## Release
- `MAR, 23, 2024` Release the initial version of the SNAP model publicly.

