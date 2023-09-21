# mlsuite

## Install

```
pip install mlsuite==2.1.7
pip install https://github.com/JamesRitchie/scikit-rvm/archive/master.zip
```

## Usage

Notice: used pyhton3, not python2

usage: mlsuite.py [-h] [-V] {Fitting,Predict,Auto} ...

The traditional machine learning analysis based on sklearn package:

positional arguments:
  {Fitting,Predict,Auto}
                        machine learning models help.
    Fitting             Fitting and predicting the training and testing set from estimators.
    Predict             predict new data from fittting process model.
    Auto                the auto-processing for all: Fitting and/or Prediction.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit

Example:

1. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -p data.predict.txt -o testdt/ -m DT -pn 0.9 (The cumulative contribution ratio of PCA is 0.9.)
2. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -p data.predict.txt -o testdt/ -m DT -pn 0.9 -f (10 times sample grouping and 10 models)
3. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -o testdt/ -m DT -pn 0.9
4. python mlsuite.py Fitting -i data.traintest.txt -g group.new.txt -o testdt/ -m DT -pn 0.9
5. python mlsuite.py Fitting -i data.traintest.txt -g group.new.txt -o testdt/ -m DT -pn 0.9 -f (10 times sample grouping and 10 models)
6. python mlsuite.py Predict -p data.predict.txt   -g group.new.txt -x modelpath/ -y predictdt/ -m DT -pn 0.9.

## Update log
### v2.1.7
1. Fixed a bug in "MLSupervising.py" script.

### v2.1.6
1. Remove sklearn PCA modula, PCA analysis by self-written script in SVD method
2. "Fitting" module has been added "-pc|--pc_center" and "-ps|--pc__scale" arguments, indicate data should to be center or scale before PCA analysis. default data center is open, data scale is closed.

### v2.1.5
1. "Fitting" module has been added "-pn|--pc_number" arguments, which the spliting training data was reduced dimensions by PCA, and assign the number of PCs (integer, [1,Inf)) or the cumulative contribution ratio (float, (0, 1)).

### v2.1.4
1. "Fitting" module has been added "-f|--fit_10" arguments, which the input training dataset was splited into 10 train/test groups, and got 10 models.

### v2.1.3
1. pandas's parameter "line_terminator" had changed into "lineterminator" in the 2.0.0 version, so drop "line_terminator" in "MLOpenWrite.py" script.
2. fixed same packages' version:
```
    lightgbm == 3.3.3,
    joblib == 1.2.0,
    numpy == 1.21.4,
    pandas == 1.1.5,
    scikit-learn == 1.2.0,
    sklearn_pandas == 2.2.0,
    xgboost == 1.7.2
```

### v2.1.2
1. revised same packages' version:
```
    lightgbm == 3.3.3,
    joblib == 1.2.0,
    numpy >= 1.16.4,
    pandas >= 0.24.2,
    scikit-learn == 1.2.0,
    sklearn_pandas == 2.2.0,
    xgboost == 1.7.2
```

### v2.1.1
 1. fixed same packages' version:
```
    lightgbm == 3.3.3,
    joblib == 1.2.0,
    numpy == 1.23.5,
    pandas == 1.5.2,
    scikit-learn == 1.2.0,
    sklearn_pandas == 2.2.0,
    xgboost == 1.7.2
```

### v2.1.0
    1. LinearSVM parameter: LinearSVC(dual=False) report error: "unsupported set of arguments:  The combination of penalty='l2' and loss='hinge' are not supported when dual=False, Parameters: penalty='l2', loss='hinge', dual=False". So go back LinearSVC(dual=True).
    2. modified version information in MLArguments.py.

### v2.0.9

    1. refixed return value of program.

    2. change float data type into integer type.  max_iter parameter in LinearSVM model.

### v2.0.8

    1. modified LinearSVM parameter: LinearSVC(dual=False)

### v2.0.7

    1. repaired same bugs of predict module

### v2.0.6

    1. add RVMrbf and RVMpoly module in MLEstimators.py

### v2.0.2

    1. add SVMpoly module in MLEstimators.py
    2. add calculate MAD function in MLSupervising.py

### v2.0.0

    1. 删除数据预处理、特征筛选、画图等步骤，保留模型构建和模型预测两个步骤。
    2. 13个模型构建，改为并行，缩短分析时间。

### v1.0.0
