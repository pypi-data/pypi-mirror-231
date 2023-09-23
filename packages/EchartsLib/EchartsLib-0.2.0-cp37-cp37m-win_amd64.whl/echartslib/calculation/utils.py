import numpy as np
from typing import Union, Tuple, Dict, List
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler
from scipy.stats import wasserstein_distance
from scipy.stats import ks_2samp


def auto_type_classification(x, threshold=20):
    """Judge the type of variable and whether the value of variable contains string

    Parameters
    ----------
    x : list
        The list of some variable value
    threshold : int
        The unique value number threshold between numerical and categorical variables
    Returns
    -------
    type : tuple
        The type of the variable and whether the variable contains string
    """

    np.random.seed(0)
    if isinstance(x, pd.Series):
        n_samples = x.shape[0]
        auto_type = "categorical"
        try:
            x = x.astype(float)
        except:
            pass
        if np.issubdtype(x.dtype, np.number):
            # subsampling for big data
            if n_samples > 10000:
                idx = np.random.choice(np.arange(n_samples), size=10000, replace=False)
                xx = x.iloc[idx]
            else:
                xx = x
            uniq_vals = np.unique(xx).tolist()
            if len(uniq_vals) >= threshold:
                auto_type = "numerical"
    else:
        x = np.array(x.tolist())
        n_samples = x.shape[0]
        auto_type = "categorical"
        try:
            x = x.astype(float)
        except:
            pass
        if np.issubdtype(x.dtype, np.number):
            # subsampling for big data
            if n_samples > 10000:
                idx = np.random.choice(np.arange(n_samples), size=10000, replace=False)
                xx = x[idx]
            else:
                xx = x
            uniq_vals = set(xx)
            if len(uniq_vals) >= threshold:
                auto_type = "numerical"
    return auto_type

def calculate_distance(samples_1, samples_2, method='PSI', buckettype='uniform', buckets=10,
                       samples_type='numerical'):
    
    if samples_type == 'categorical':
        samples = np.concatenate([samples_1, samples_2], 0)
        os_ = OrdinalEncoder()
        os_.fit(samples.reshape(-1, 1))
        samples_1 = os_.transform(samples_1.reshape(-1,1)).ravel()
        samples_2 = os_.transform(samples_2.reshape(-1,1)).ravel()
    samples = np.concatenate([samples_1, samples_2], 0)
    mm = MinMaxScaler()
    mm.fit(samples.reshape(-1, 1))
    samples_1 = mm.transform(samples_1.reshape(-1,1)).ravel()
    samples_2 = mm.transform(samples_2.reshape(-1,1)).ravel()
    if method == "Euclidean":
        left_center = samples_1.mean()
        right_center = samples_2.mean()
        return np.sqrt(np.sum((left_center - right_center) ** 2))
    elif method == 'PSI':
        return calculate_psi(samples_1, samples_2, buckettype=buckettype, buckets=buckets)
    elif method == 'WD1':
        return wasserstein_distance(samples_1, samples_2)
    elif method == 'KS':
        return ks_2samp(samples_1, samples_2).statistic


def calculate_psi(expected, actual, buckettype='uniform', buckets=10, axis=0):
    '''Calculate the PSI (population stability index) across all variables
    Args:
    expected: numpy matrix of original values (Training)
    actual: numpy matrix of new values, same size as expected (Validation)
    buckettype: type of strategy for creating buckets, uniform splits into even splits, quantiles splits into quantile buckets
    buckets: number of quantiles to use in bucketing variables
    axis: axis by which variables are defined, 0 for vertical, 1 for horizontal
    Returns:
    psi_values: ndarray of psi values for each variable
    Author:
    Matthew Burke
    github.com/mwburke
    worksofchart.com
    '''

    def psi(expected_array, actual_array, buckets):
        '''Calculate the PSI for a single variable
        Args:
        expected_array: numpy array of original values
        actual_array: numpy array of new values, same size as expected
        buckets: number of percentile ranges to bucket the values into
        Returns:
        psi_value: calculated PSI value
        '''

        def scale_range(_input, _min, _max):
            _input += -(np.min(_input))
            _input /= np.max(_input) / (_max - _min)
            _input += _min
            return _input

        breakpoints = np.arange(0, buckets + 1) / (buckets) * 100

        if buckettype == 'uniform':
            breakpoints = scale_range(breakpoints, np.min(expected_array), np.max(expected_array))
        elif buckettype == 'quantile':
            breakpoints = np.stack([np.percentile(expected_array, b) for b in breakpoints])

        expected_percents = np.histogram(expected_array, breakpoints)[0] / len(expected_array)
        actual_percents = np.histogram(actual_array, breakpoints)[0] / len(actual_array)

        def sub_psi(e_perc, a_perc):
            '''Calculate the actual PSI value from comparing the values.
            Update the actual value to a very small number if equal to zero
            '''
            if a_perc == 0:
                a_perc = 0.0001
            if e_perc == 0:
                e_perc = 0.0001

            value = (e_perc - a_perc) * np.log(e_perc / a_perc)
            return value

        lis = []
        for i in range(0, len(expected_percents)):
            lis.append(sub_psi(expected_percents[i], actual_percents[i]))
        psi_value = np.sum(lis)

        return psi_value

    if len(expected.shape) == 1:
        psi_values = np.empty(len(expected.shape))
    else:
        psi_values = np.empty(expected.shape[axis])

    for i in range(0, len(psi_values)):
        if len(psi_values) == 1:
            psi_values = psi(expected, actual, buckets)
        elif axis == 0:
            psi_values[i] = psi(expected[:, i], actual[:, i], buckets)
        elif axis == 1:
            psi_values[i] = psi(expected[i, :], actual[i, :], buckets)

    return psi_values

def twosample_test(sample1: Union[np.array, pd.DataFrame], sample2: Union[np.array, pd.DataFrame],
                   feature_names: List[str] = None, feature_types: List[str] = None,
                   metric: str = 'PSI', psi_buckets: str = 'uniform', feature: Union[str, int] = None,
                   sample1_name: str = None, sample2_name: str = None,
                   return_data: bool = False, figsize: Tuple[int, int] = (8, 6),
                   silent=False) -> Dict:
    """Two sample test between two arbitrary datasets

    Parameters
    ----------
    sample1 : Union[np.array, pd.DataFrame]
        sample 1 dataset
    sample2 : Union[np.array, pd.DataFrame]
        sample 2 dataset, must have same dimensions as sample 1
    feature_names : List[str], optional
        feature names, by default None
    feature_types: List[str], optional
        feature types, can be 'numerical' or 'categorical'; if None or empty, the type of each feature will be determined by several samples
    metric : str, optional
        test metric, by default 'PSI'
    psi_buckets : str, optional
        buckets type for PSI metric calculation, by default 'uniform'.
    feature : Union[str, int], optional
        feature for distribution plot, can be string (feature's name) or int (feature's index)
        if not given, the plot would be metric scores against each feature, by default None
    sample1_name : str, optional
        sample 1 name for plot, by default None
    sample2_name : str, optional
        sample 2 name for plot, by default None
    return_data : bool, optional
        whether or not return result data, by default False
    figsize : Tuple[int, int], optional
        plot figure size, by default (8, 6)

    Returns
    -------
    Dict
        result data, including metric scores

    Raises
    ------
    ValueError
        Two samples must have same dimensions.
    ValueError
        Metric not supported.
    """
    if sample1.shape[1] != sample2.shape[1]:
        raise ValueError('Two samples must have same dimensions.')

    if feature_names is None:
        feature_names = [f'X{i}' for i in range(sample1.shape[1])]
    metric_scores = np.zeros(len(feature_names))

    if sample1_name is None:
        sample1_name = 'Sample 1'
    if sample2_name is None:
        sample2_name = 'Sample 2'

    TOP_N = 30
    if metric == 'PSI':
        metric_title = f'Population Stability Index (PSI) - Top {TOP_N}'
    elif metric == 'WD1':
        metric_title = f'Wasserstein distance-1D (WD1) - Top {TOP_N}'
    elif metric == 'KS':
        metric_title = f'Kolmogorov-Smirnov (KS) - Top {TOP_N}'
    else:
        raise ValueError(f'Metric `{metric}` is not supported.')

    for feature_idx in range(len(feature_names)):
        sample1_i = np.array(sample1)[:, feature_idx]
        sample2_i = np.array(sample2)[:, feature_idx]
        if feature_types:
            feature_dtype = feature_types[feature_idx]
        else:
            feature_dtype = auto_type_classification(sample1_i, threshold=5)
        if feature_dtype == 'categorical':  # for str type features
            oe = OrdinalEncoder()
            oe.fit(np.concatenate((sample1_i, sample2_i)).reshape(-1, 1))
            sample1_i = oe.transform(sample1_i.reshape(-1, 1)).ravel()
            sample2_i = oe.transform(sample2_i.reshape(-1, 1)).ravel()
        metric_scores[feature_idx] = calculate_distance(sample1_i, sample2_i, buckettype=psi_buckets,
                                                        method=metric)

    metric_sort_idx = np.argsort(-1 * metric_scores)
    feature_names_sorted = [feature_names[i] for i in metric_sort_idx]
    feature_types_sorted = [feature_types[i] for i in metric_sort_idx]

    df = pd.DataFrame()
    if feature is None:
        fig = plt.figure(figsize=figsize)
        plt.bar(feature_names_sorted[:TOP_N], metric_scores[metric_sort_idx][:TOP_N])
        plt.title(metric_title, fontsize=15)
        plt.ylabel(metric.upper(), fontsize=12)
        plt.xticks(rotation=90)
        plt.tight_layout()
        if not silent:
            plt.show()
        else:
            plt.ioff()
    else:
        fig = plt.figure(figsize=figsize)
        if isinstance(feature, int):
            feature_idx = feature
        else:
            feature_idx = feature_names_sorted.index(feature)
        feature_name = feature_names_sorted[feature_idx]
        metric_score = metric_scores[metric_sort_idx][feature_idx]
        x1_sorted = np.array(sample1[:, metric_sort_idx[feature_idx]])
        x2_sorted = np.array(sample2[:, metric_sort_idx[feature_idx]])
        xx = np.concatenate((x1_sorted, x2_sorted))
        df[feature_name] = xx
        s1 = np.array([sample1_name] * len(x1_sorted))
        s2 = np.array([sample2_name] * len(x2_sorted))
        df['sample'] = np.concatenate((s1, s2))

        if feature_types_sorted:
            feature_dtype = feature_types_sorted[feature_idx]
        else:
            feature_dtype = auto_type_classification(x1_sorted, threshold=5)
        if feature_dtype == 'categorical':
            df_ = df.copy()
            df_[feature_name] = df_[feature_name].astype(
                str)  # change categorical feature's actual data type to string for correct x-axis alignment
            # TODO: speed up for bins
            feature_unique_values = sorted(df_[feature_name].unique())  # get and sort feature's unique values
            df_[feature_name] = pd.Categorical(df_[feature_name], feature_unique_values)
            ax = sns.histplot(data=df_, x=feature_name, hue='sample',
                              multiple="dodge", stat='percent', bins=len(feature_unique_values), shrink=.8,
                              common_norm=False, fill=True, legend=True, palette='Blues', alpha=.5)
        else:
            ax = sns.kdeplot(data=df, x=feature_name, hue='sample',
                             common_norm=False, fill=True, legend=True, palette='Blues', alpha=.5)

        legend_title = f'sample: {metric.upper()}={metric_score:.4f}'
        ax.legend_.set_title(legend_title)
        sns.move_legend(ax, "upper right")
        plt.title('Distribution plot', fontsize=15)
        plt.tight_layout()
        if not silent:
            plt.show()
        else:
            plt.ioff()

    return {metric: metric_scores, 'figure': fig}