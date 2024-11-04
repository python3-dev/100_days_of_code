# 100 Days of Code

The objective of this project is to code everyday, each code independent from each other, solving interesting and small problems.

## Generate requirements (dev)

Export the requirements.

```shell
poetry export -f requirements.txt --without-hashes --output requirements.txt
```

## Installing

If the requirement files have something in it.

Install the dependencies using.

```shell
pip install -r requirements.txt
```

To run the tests, you will have install pytest.

```shell
pip install pytest pytest-cov
```
