[![Install](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/actions/workflows/test.yml)
## Project #1: Continuous Integration using GitHub Actions of Python Data Science

## Youtube Video Link
[Youtube Link](https://www.youtube.com/watch?v=rPrHaqKwjWI)

### Directory Tree Structure 
```
Jeremy_Tan_IDS706_Week3_Individual/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.ipynb
├── main.py
├── Makefile
├── mylib/
│   ├── __init__.py
│   └── lib.py
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── test_lib.py
└── test_main.py
```
### Purpose of Project
The purpose of this project is to build upon the last three mini-projects to simulate best practices of continuous integration in Data Science projects. I use the Congress dataset provided by FiveThirtyEight to produce sample descriptive statistics and visualizations.

## Preparation 
1. Open codespaces 
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed 
3. If running locally, `git clone` the repository and use `make install`

## Check format and test errors
1. Format code `make format`
2. Lint code `make lint`

<img width="828" alt="Screenshot 2023-09-20 at 8 28 38 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/assets/36715338/78b644b0-12e4-48df-9026-5676e2f00111">

3. Test code `make test`

<img width="1374" alt="Screenshot 2023-09-20 at 8 28 51 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week3_Individual/assets/36715338/8f7c73fe-bf4c-47ae-80f1-c32ce35a9465">

## Descriptive statistics and vizualizations 
The descriptive statistics and vizualizations are generated whenever an individaul pushes to my repository via `actions-user` using `make generate_and_push`. You can find them here [descriptive statistics and vizualizations](/congress_summary.md)

## References 
https://github.com/nogibjj/python-ruff-template
