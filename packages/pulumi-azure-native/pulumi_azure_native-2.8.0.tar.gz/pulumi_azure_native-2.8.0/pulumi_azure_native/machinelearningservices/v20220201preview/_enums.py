# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BatchLoggingLevel',
    'BatchOutputAction',
    'ClassificationModels',
    'ClassificationMultilabelPrimaryMetrics',
    'ClassificationPrimaryMetrics',
    'CredentialsType',
    'DataType',
    'DatastoreType',
    'DistributionType',
    'EarlyTerminationPolicyType',
    'EgressPublicNetworkAccessType',
    'EndpointAuthMode',
    'EndpointComputeType',
    'FeatureLags',
    'FeaturizationMode',
    'ForecastHorizonMode',
    'ForecastingModels',
    'ForecastingPrimaryMetrics',
    'Goal',
    'IdentityConfigurationType',
    'InputDeliveryMode',
    'InstanceSegmentationPrimaryMetrics',
    'JobInputType',
    'JobLimitsType',
    'JobOutputType',
    'JobType',
    'LearningRateScheduler',
    'LogVerbosity',
    'ManagedServiceIdentityType',
    'ModelSize',
    'ModelType',
    'NCrossValidationsMode',
    'ObjectDetectionPrimaryMetrics',
    'OperatingSystemType',
    'OutputDeliveryMode',
    'PublicNetworkAccessType',
    'RandomSamplingAlgorithmRule',
    'RecurrenceFrequency',
    'ReferenceType',
    'RegressionModels',
    'RegressionPrimaryMetrics',
    'SamplingAlgorithmType',
    'ScaleType',
    'ScheduleStatus',
    'ScheduleType',
    'SeasonalityMode',
    'SecretsType',
    'ServiceDataAccessAuthIdentity',
    'ShortSeriesHandlingConfiguration',
    'SkuTier',
    'StackMetaLearnerType',
    'StochasticOptimizer',
    'TargetAggregationFunction',
    'TargetLagsMode',
    'TargetRollingWindowSizeMode',
    'TaskType',
    'UseStl',
    'ValidationMetricType',
    'ValueFormat',
    'Weekday',
]


class BatchLoggingLevel(str, Enum):
    """
    Logging level for batch inference operation.
    """
    INFO = "Info"
    WARNING = "Warning"
    DEBUG = "Debug"


class BatchOutputAction(str, Enum):
    """
    Indicates how the output will be organized.
    """
    SUMMARY_ONLY = "SummaryOnly"
    APPEND_ROW = "AppendRow"


class ClassificationModels(str, Enum):
    """
    Enum for all classification models supported by AutoML.
    """
    LOGISTIC_REGRESSION = "LogisticRegression"
    """
    Logistic regression is a fundamental classification technique.
    It belongs to the group of linear classifiers and is somewhat similar to polynomial and linear regression.
    Logistic regression is fast and relatively uncomplicated, and it's convenient for you to interpret the results.
    Although it's essentially a method for binary classification, it can also be applied to multiclass problems.
    """
    SGD = "SGD"
    """
    SGD: Stochastic gradient descent is an optimization algorithm often used in machine learning applications
    to find the model parameters that correspond to the best fit between predicted and actual outputs.
    """
    MULTINOMIAL_NAIVE_BAYES = "MultinomialNaiveBayes"
    """
    The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification).
    The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work.
    """
    BERNOULLI_NAIVE_BAYES = "BernoulliNaiveBayes"
    """
    Naive Bayes classifier for multivariate Bernoulli models.
    """
    SVM = "SVM"
    """
    A support vector machine (SVM) is a supervised machine learning model that uses classification algorithms for two-group classification problems.
    After giving an SVM model sets of labeled training data for each category, they're able to categorize new text.
    """
    LINEAR_SVM = "LinearSVM"
    """
    A support vector machine (SVM) is a supervised machine learning model that uses classification algorithms for two-group classification problems.
    After giving an SVM model sets of labeled training data for each category, they're able to categorize new text.
    Linear SVM performs best when input data is linear, i.e., data can be easily classified by drawing the straight line between classified values on a plotted graph.
    """
    KNN = "KNN"
    """
    K-nearest neighbors (KNN) algorithm uses 'feature similarity' to predict the values of new datapoints
    which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.
    """
    DECISION_TREE = "DecisionTree"
    """
    Decision Trees are a non-parametric supervised learning method used for both classification and regression tasks.
    The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
    """
    RANDOM_FOREST = "RandomForest"
    """
    Random forest is a supervised learning algorithm.
    The "forest" it builds, is an ensemble of decision trees, usually trained with the “bagging” method.
    The general idea of the bagging method is that a combination of learning models increases the overall result.
    """
    EXTREME_RANDOM_TREES = "ExtremeRandomTrees"
    """
    Extreme Trees is an ensemble machine learning algorithm that combines the predictions from many decision trees. It is related to the widely used random forest algorithm.
    """
    LIGHT_GBM = "LightGBM"
    """
    LightGBM is a gradient boosting framework that uses tree based learning algorithms.
    """
    GRADIENT_BOOSTING = "GradientBoosting"
    """
    The technique of transiting week learners into a strong learner is called Boosting. The gradient boosting algorithm process works on this theory of execution.
    """
    XG_BOOST_CLASSIFIER = "XGBoostClassifier"
    """
    XGBoost: Extreme Gradient Boosting Algorithm. This algorithm is used for structured data where target column values can be divided into distinct class values.
    """


class ClassificationMultilabelPrimaryMetrics(str, Enum):
    """
    Primary metric to optimize for this task.
    """
    AUC_WEIGHTED = "AUCWeighted"
    """
    AUC is the Area under the curve.
    This metric represents arithmetic mean of the score for each class,
    weighted by the number of true instances in each class.
    """
    ACCURACY = "Accuracy"
    """
    Accuracy is the ratio of predictions that exactly match the true class labels.
    """
    NORM_MACRO_RECALL = "NormMacroRecall"
    """
    Normalized macro recall is recall macro-averaged and normalized, so that random
    performance has a score of 0, and perfect performance has a score of 1.
    """
    AVERAGE_PRECISION_SCORE_WEIGHTED = "AveragePrecisionScoreWeighted"
    """
    The arithmetic mean of the average precision score for each class, weighted by
    the number of true instances in each class.
    """
    PRECISION_SCORE_WEIGHTED = "PrecisionScoreWeighted"
    """
    The arithmetic mean of precision for each class, weighted by number of true instances in each class.
    """
    IOU = "IOU"
    """
    Intersection Over Union. Intersection of predictions divided by union of predictions.
    """


class ClassificationPrimaryMetrics(str, Enum):
    """
    Primary metric for Text-Classification task.
    """
    AUC_WEIGHTED = "AUCWeighted"
    """
    AUC is the Area under the curve.
    This metric represents arithmetic mean of the score for each class,
    weighted by the number of true instances in each class.
    """
    ACCURACY = "Accuracy"
    """
    Accuracy is the ratio of predictions that exactly match the true class labels.
    """
    NORM_MACRO_RECALL = "NormMacroRecall"
    """
    Normalized macro recall is recall macro-averaged and normalized, so that random
    performance has a score of 0, and perfect performance has a score of 1.
    """
    AVERAGE_PRECISION_SCORE_WEIGHTED = "AveragePrecisionScoreWeighted"
    """
    The arithmetic mean of the average precision score for each class, weighted by
    the number of true instances in each class.
    """
    PRECISION_SCORE_WEIGHTED = "PrecisionScoreWeighted"
    """
    The arithmetic mean of precision for each class, weighted by number of true instances in each class.
    """


class CredentialsType(str, Enum):
    """
    [Required] Credential type used to authentication with storage.
    """
    ACCOUNT_KEY = "AccountKey"
    CERTIFICATE = "Certificate"
    NONE = "None"
    SAS = "Sas"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    KERBEROS_KEYTAB = "KerberosKeytab"
    KERBEROS_PASSWORD = "KerberosPassword"


class DataType(str, Enum):
    """
    [Required] Specifies the type of data.
    """
    URI_FILE = "UriFile"
    URI_FOLDER = "UriFolder"
    ML_TABLE = "MLTable"


class DatastoreType(str, Enum):
    """
    [Required] Storage type backing the datastore.
    """
    AZURE_BLOB = "AzureBlob"
    AZURE_DATA_LAKE_GEN1 = "AzureDataLakeGen1"
    AZURE_DATA_LAKE_GEN2 = "AzureDataLakeGen2"
    AZURE_FILE = "AzureFile"
    HDFS = "Hdfs"


class DistributionType(str, Enum):
    """
    [Required] Specifies the type of distribution framework.
    """
    PY_TORCH = "PyTorch"
    TENSOR_FLOW = "TensorFlow"
    MPI = "Mpi"


class EarlyTerminationPolicyType(str, Enum):
    """
    [Required] Name of policy configuration
    """
    BANDIT = "Bandit"
    MEDIAN_STOPPING = "MedianStopping"
    TRUNCATION_SELECTION = "TruncationSelection"


class EgressPublicNetworkAccessType(str, Enum):
    """
    If Enabled, allow egress public network access. If Disabled, this will create secure egress. Default: Enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EndpointAuthMode(str, Enum):
    """
    [Required] Use 'Key' for key based authentication and 'AMLToken' for Azure Machine Learning token-based authentication. 'Key' doesn't expire but 'AMLToken' does.
    """
    AML_TOKEN = "AMLToken"
    KEY = "Key"
    AAD_TOKEN = "AADToken"


class EndpointComputeType(str, Enum):
    """
    [Required] The compute type of the endpoint.
    """
    MANAGED = "Managed"
    KUBERNETES = "Kubernetes"
    AZURE_ML_COMPUTE = "AzureMLCompute"


class FeatureLags(str, Enum):
    """
    Flag for generating lags for the numeric features with 'auto' or null.
    """
    NONE = "None"
    """
    No feature lags generated.
    """
    AUTO = "Auto"
    """
    System auto-generates feature lags.
    """


class FeaturizationMode(str, Enum):
    """
    Featurization mode - User can keep the default 'Auto' mode and AutoML will take care of necessary transformation of the data in featurization phase.
    If 'Off' is selected then no featurization is done.
    If 'Custom' is selected then user can specify additional inputs to customize how featurization is done.
    """
    AUTO = "Auto"
    """
    Auto mode, system performs featurization without any custom featurization inputs.
    """
    CUSTOM = "Custom"
    """
    Custom featurization.
    """
    OFF = "Off"
    """
    Featurization off. 'Forecasting' task cannot use this value.
    """


class ForecastHorizonMode(str, Enum):
    """
    [Required] Set forecast horizon value selection mode.
    """
    AUTO = "Auto"
    """
    Forecast horizon to be determined automatically.
    """
    CUSTOM = "Custom"
    """
    Use the custom forecast horizon.
    """


class ForecastingModels(str, Enum):
    """
    Enum for all forecasting models supported by AutoML.
    """
    AUTO_ARIMA = "AutoArima"
    """
    Auto-Autoregressive Integrated Moving Average (ARIMA) model uses time-series data and statistical analysis to interpret the data and make future predictions.
    This model aims to explain data by using time series data on its past values and uses linear regression to make predictions.
    """
    PROPHET = "Prophet"
    """
    Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.
    It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.
    """
    NAIVE = "Naive"
    """
    The Naive forecasting model makes predictions by carrying forward the latest target value for each time-series in the training data.
    """
    SEASONAL_NAIVE = "SeasonalNaive"
    """
    The Seasonal Naive forecasting model makes predictions by carrying forward the latest season of target values for each time-series in the training data.
    """
    AVERAGE = "Average"
    """
    The Average forecasting model makes predictions by carrying forward the average of the target values for each time-series in the training data.
    """
    SEASONAL_AVERAGE = "SeasonalAverage"
    """
    The Seasonal Average forecasting model makes predictions by carrying forward the average value of the latest season of data for each time-series in the training data.
    """
    EXPONENTIAL_SMOOTHING = "ExponentialSmoothing"
    """
    Exponential smoothing is a time series forecasting method for univariate data that can be extended to support data with a systematic trend or seasonal component.
    """
    ARIMAX = "Arimax"
    """
    An Autoregressive Integrated Moving Average with Explanatory Variable (ARIMAX) model can be viewed as a multiple regression model with one or more autoregressive (AR) terms and/or one or more moving average (MA) terms.
    This method is suitable for forecasting when data is stationary/non stationary, and multivariate with any type of data pattern, i.e., level/trend /seasonality/cyclicity.
    """
    TCN_FORECASTER = "TCNForecaster"
    """
    TCNForecaster: Temporal Convolutional Networks Forecaster.
    """
    ELASTIC_NET = "ElasticNet"
    """
    Elastic net is a popular type of regularized linear regression that combines two popular penalties, specifically the L1 and L2 penalty functions.
    """
    GRADIENT_BOOSTING = "GradientBoosting"
    """
    The technique of transiting week learners into a strong learner is called Boosting. The gradient boosting algorithm process works on this theory of execution.
    """
    DECISION_TREE = "DecisionTree"
    """
    Decision Trees are a non-parametric supervised learning method used for both classification and regression tasks.
    The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
    """
    KNN = "KNN"
    """
    K-nearest neighbors (KNN) algorithm uses 'feature similarity' to predict the values of new datapoints
    which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.
    """
    LASSO_LARS = "LassoLars"
    """
    Lasso model fit with Least Angle Regression a.k.a. Lars. It is a Linear Model trained with an L1 prior as regularizer.
    """
    SGD = "SGD"
    """
    SGD: Stochastic gradient descent is an optimization algorithm often used in machine learning applications
    to find the model parameters that correspond to the best fit between predicted and actual outputs.
    It's an inexact but powerful technique.
    """
    RANDOM_FOREST = "RandomForest"
    """
    Random forest is a supervised learning algorithm.
    The "forest" it builds, is an ensemble of decision trees, usually trained with the “bagging” method.
    The general idea of the bagging method is that a combination of learning models increases the overall result.
    """
    EXTREME_RANDOM_TREES = "ExtremeRandomTrees"
    """
    Extreme Trees is an ensemble machine learning algorithm that combines the predictions from many decision trees. It is related to the widely used random forest algorithm.
    """
    LIGHT_GBM = "LightGBM"
    """
    LightGBM is a gradient boosting framework that uses tree based learning algorithms.
    """
    XG_BOOST_REGRESSOR = "XGBoostRegressor"
    """
    XGBoostRegressor: Extreme Gradient Boosting Regressor is a supervised machine learning model using ensemble of base learners.
    """


class ForecastingPrimaryMetrics(str, Enum):
    """
    Primary metric for forecasting task.
    """
    SPEARMAN_CORRELATION = "SpearmanCorrelation"
    """
    The Spearman's rank coefficient of correlation is a non-parametric measure of rank correlation.
    """
    NORMALIZED_ROOT_MEAN_SQUARED_ERROR = "NormalizedRootMeanSquaredError"
    """
    The Normalized Root Mean Squared Error (NRMSE) the RMSE facilitates the comparison between models with different scales.
    """
    R2_SCORE = "R2Score"
    """
    The R2 score is one of the performance evaluation measures for forecasting-based machine learning models.
    """
    NORMALIZED_MEAN_ABSOLUTE_ERROR = "NormalizedMeanAbsoluteError"
    """
    The Normalized Mean Absolute Error (NMAE) is a validation metric to compare the Mean Absolute Error (MAE) of (time) series with different scales.
    """


class Goal(str, Enum):
    """
    [Required] Defines supported metric goals for hyperparameter tuning
    """
    MINIMIZE = "Minimize"
    MAXIMIZE = "Maximize"


class IdentityConfigurationType(str, Enum):
    """
    [Required] Specifies the type of identity framework.
    """
    MANAGED = "Managed"
    AML_TOKEN = "AMLToken"
    USER_IDENTITY = "UserIdentity"


class InputDeliveryMode(str, Enum):
    """
    Input Asset Delivery Mode.
    """
    READ_ONLY_MOUNT = "ReadOnlyMount"
    READ_WRITE_MOUNT = "ReadWriteMount"
    DOWNLOAD = "Download"
    DIRECT = "Direct"
    EVAL_MOUNT = "EvalMount"
    EVAL_DOWNLOAD = "EvalDownload"


class InstanceSegmentationPrimaryMetrics(str, Enum):
    """
    Primary metric to optimize for this task.
    """
    MEAN_AVERAGE_PRECISION = "MeanAveragePrecision"
    """
    Mean Average Precision (MAP) is the average of AP (Average Precision).
    AP is calculated for each class and averaged to get the MAP.
    """


class JobInputType(str, Enum):
    """
    [Required] Specifies the type of job.
    """
    LITERAL = "Literal"
    URI_FILE = "UriFile"
    URI_FOLDER = "UriFolder"
    ML_TABLE = "MLTable"
    CUSTOM_MODEL = "CustomModel"
    ML_FLOW_MODEL = "MLFlowModel"
    TRITON_MODEL = "TritonModel"


class JobLimitsType(str, Enum):
    """
    [Required] JobLimit type.
    """
    COMMAND = "Command"
    SWEEP = "Sweep"


class JobOutputType(str, Enum):
    """
    [Required] Specifies the type of job.
    """
    URI_FILE = "UriFile"
    URI_FOLDER = "UriFolder"
    ML_TABLE = "MLTable"
    CUSTOM_MODEL = "CustomModel"
    ML_FLOW_MODEL = "MLFlowModel"
    TRITON_MODEL = "TritonModel"


class JobType(str, Enum):
    """
    [Required] Specifies the type of job.
    """
    AUTO_ML = "AutoML"
    COMMAND = "Command"
    SWEEP = "Sweep"
    PIPELINE = "Pipeline"


class LearningRateScheduler(str, Enum):
    """
    Type of learning rate scheduler. Must be 'warmup_cosine' or 'step'.
    """
    NONE = "None"
    """
    No learning rate scheduler selected.
    """
    WARMUP_COSINE = "WarmupCosine"
    """
    Cosine Annealing With Warmup.
    """
    STEP = "Step"
    """
    Step learning rate scheduler.
    """


class LogVerbosity(str, Enum):
    """
    Log verbosity for the job.
    """
    NOT_SET = "NotSet"
    """
    No logs emitted.
    """
    DEBUG = "Debug"
    """
    Debug and above log statements logged.
    """
    INFO = "Info"
    """
    Info and above log statements logged.
    """
    WARNING = "Warning"
    """
    Warning and above log statements logged.
    """
    ERROR = "Error"
    """
    Error and above log statements logged.
    """
    CRITICAL = "Critical"
    """
    Only critical statements logged.
    """


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class ModelSize(str, Enum):
    """
    Model size. Must be 'small', 'medium', 'large', or 'xlarge'.
    Note: training run may get into CUDA OOM if the model size is too big.
    Note: This settings is only supported for the 'yolov5' algorithm.
    """
    NONE = "None"
    """
    No value selected.
    """
    SMALL = "Small"
    """
    Small size.
    """
    MEDIUM = "Medium"
    """
    Medium size.
    """
    LARGE = "Large"
    """
    Large size.
    """
    EXTRA_LARGE = "ExtraLarge"
    """
    Extra large size.
    """


class ModelType(str, Enum):
    """
    The storage format for this entity. Used for NCD.
    """
    CUSTOM_MODEL = "CustomModel"
    ML_FLOW_MODEL = "MLFlowModel"
    TRITON_MODEL = "TritonModel"


class NCrossValidationsMode(str, Enum):
    """
    [Required] Mode for determining N-Cross validations.
    """
    AUTO = "Auto"
    """
    Determine N-Cross validations value automatically. Supported only for 'Forecasting' AutoML task.
    """
    CUSTOM = "Custom"
    """
    Use custom N-Cross validations value.
    """


class ObjectDetectionPrimaryMetrics(str, Enum):
    """
    Primary metric to optimize for this task.
    """
    MEAN_AVERAGE_PRECISION = "MeanAveragePrecision"
    """
    Mean Average Precision (MAP) is the average of AP (Average Precision).
    AP is calculated for each class and averaged to get the MAP.
    """


class OperatingSystemType(str, Enum):
    """
    The OS type of the environment.
    """
    LINUX = "Linux"
    WINDOWS = "Windows"


class OutputDeliveryMode(str, Enum):
    """
    Output Asset Delivery Mode.
    """
    READ_WRITE_MOUNT = "ReadWriteMount"
    UPLOAD = "Upload"


class PublicNetworkAccessType(str, Enum):
    """
    Set to "Enabled" for endpoints that should allow public access when Private Link is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RandomSamplingAlgorithmRule(str, Enum):
    """
    The specific type of random algorithm
    """
    RANDOM = "Random"
    SOBOL = "Sobol"


class RecurrenceFrequency(str, Enum):
    """
    [Required] Specifies frequency with with which to trigger schedule
    """
    MINUTE = "Minute"
    """
    Minute frequency
    """
    HOUR = "Hour"
    """
    Hour frequency
    """
    DAY = "Day"
    """
    Day frequency
    """
    WEEK = "Week"
    """
    Week frequency
    """
    MONTH = "Month"
    """
    Month frequency
    """


class ReferenceType(str, Enum):
    """
    [Required] Specifies the type of asset reference.
    """
    ID = "Id"
    DATA_PATH = "DataPath"
    OUTPUT_PATH = "OutputPath"


class RegressionModels(str, Enum):
    """
    Enum for all Regression models supported by AutoML.
    """
    ELASTIC_NET = "ElasticNet"
    """
    Elastic net is a popular type of regularized linear regression that combines two popular penalties, specifically the L1 and L2 penalty functions.
    """
    GRADIENT_BOOSTING = "GradientBoosting"
    """
    The technique of transiting week learners into a strong learner is called Boosting. The gradient boosting algorithm process works on this theory of execution.
    """
    DECISION_TREE = "DecisionTree"
    """
    Decision Trees are a non-parametric supervised learning method used for both classification and regression tasks.
    The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
    """
    KNN = "KNN"
    """
    K-nearest neighbors (KNN) algorithm uses 'feature similarity' to predict the values of new datapoints
    which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.
    """
    LASSO_LARS = "LassoLars"
    """
    Lasso model fit with Least Angle Regression a.k.a. Lars. It is a Linear Model trained with an L1 prior as regularizer.
    """
    SGD = "SGD"
    """
    SGD: Stochastic gradient descent is an optimization algorithm often used in machine learning applications
    to find the model parameters that correspond to the best fit between predicted and actual outputs.
    It's an inexact but powerful technique.
    """
    RANDOM_FOREST = "RandomForest"
    """
    Random forest is a supervised learning algorithm.
    The "forest" it builds, is an ensemble of decision trees, usually trained with the “bagging” method.
    The general idea of the bagging method is that a combination of learning models increases the overall result.
    """
    EXTREME_RANDOM_TREES = "ExtremeRandomTrees"
    """
    Extreme Trees is an ensemble machine learning algorithm that combines the predictions from many decision trees. It is related to the widely used random forest algorithm.
    """
    LIGHT_GBM = "LightGBM"
    """
    LightGBM is a gradient boosting framework that uses tree based learning algorithms.
    """
    XG_BOOST_REGRESSOR = "XGBoostRegressor"
    """
    XGBoostRegressor: Extreme Gradient Boosting Regressor is a supervised machine learning model using ensemble of base learners.
    """


class RegressionPrimaryMetrics(str, Enum):
    """
    Primary metric for regression task.
    """
    SPEARMAN_CORRELATION = "SpearmanCorrelation"
    """
    The Spearman's rank coefficient of correlation is a nonparametric measure of rank correlation.
    """
    NORMALIZED_ROOT_MEAN_SQUARED_ERROR = "NormalizedRootMeanSquaredError"
    """
    The Normalized Root Mean Squared Error (NRMSE) the RMSE facilitates the comparison between models with different scales.
    """
    R2_SCORE = "R2Score"
    """
    The R2 score is one of the performance evaluation measures for forecasting-based machine learning models.
    """
    NORMALIZED_MEAN_ABSOLUTE_ERROR = "NormalizedMeanAbsoluteError"
    """
    The Normalized Mean Absolute Error (NMAE) is a validation metric to compare the Mean Absolute Error (MAE) of (time) series with different scales.
    """


class SamplingAlgorithmType(str, Enum):
    """
    [Required] The algorithm used for generating hyperparameter values, along with configuration properties
    """
    GRID = "Grid"
    RANDOM = "Random"
    BAYESIAN = "Bayesian"


class ScaleType(str, Enum):
    """
    [Required] Type of deployment scaling algorithm
    """
    DEFAULT = "Default"
    TARGET_UTILIZATION = "TargetUtilization"


class ScheduleStatus(str, Enum):
    """
    Specifies the schedule's status
    """
    ENABLED = "Enabled"
    """
    Schedule is enabled
    """
    DISABLED = "Disabled"
    """
    Schedule is disabled
    """


class ScheduleType(str, Enum):
    """
    [Required] Specifies the schedule type
    """
    CRON = "Cron"
    """
    Cron schedule type
    """
    RECURRENCE = "Recurrence"
    """
    Recurrence schedule type
    """


class SeasonalityMode(str, Enum):
    """
    [Required] Seasonality mode.
    """
    AUTO = "Auto"
    """
    Seasonality to be determined automatically.
    """
    CUSTOM = "Custom"
    """
    Use the custom seasonality value.
    """


class SecretsType(str, Enum):
    """
    [Required] Credential type used to authentication with storage.
    """
    ACCOUNT_KEY = "AccountKey"
    CERTIFICATE = "Certificate"
    SAS = "Sas"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    KERBEROS_PASSWORD = "KerberosPassword"
    KERBEROS_KEYTAB = "KerberosKeytab"


class ServiceDataAccessAuthIdentity(str, Enum):
    """
    Indicates which identity to use to authenticate service data access to customer's storage.
    """
    NONE = "None"
    """
    Do not use any identity for service data access.
    """
    WORKSPACE_SYSTEM_ASSIGNED_IDENTITY = "WorkspaceSystemAssignedIdentity"
    """
    Use the system assigned managed identity of the Workspace to authenticate service data access.
    """
    WORKSPACE_USER_ASSIGNED_IDENTITY = "WorkspaceUserAssignedIdentity"
    """
    Use the user assigned managed identity of the Workspace to authenticate service data access.
    """


class ShortSeriesHandlingConfiguration(str, Enum):
    """
    The parameter defining how if AutoML should handle short time series.
    """
    NONE = "None"
    """
    Represents no/null value.
    """
    AUTO = "Auto"
    """
    Short series will be padded if there are no long series, otherwise short series will be dropped.
    """
    PAD = "Pad"
    """
    All the short series will be padded.
    """
    DROP = "Drop"
    """
    All the short series will be dropped.
    """


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class StackMetaLearnerType(str, Enum):
    """
    The meta-learner is a model trained on the output of the individual heterogeneous models.
    """
    NONE = "None"
    LOGISTIC_REGRESSION = "LogisticRegression"
    """
    Default meta-learners are LogisticRegression for classification tasks.
    """
    LOGISTIC_REGRESSION_CV = "LogisticRegressionCV"
    """
    Default meta-learners are LogisticRegression for classification task when CV is on.
    """
    LIGHT_GBM_CLASSIFIER = "LightGBMClassifier"
    ELASTIC_NET = "ElasticNet"
    """
    Default meta-learners are LogisticRegression for regression task.
    """
    ELASTIC_NET_CV = "ElasticNetCV"
    """
    Default meta-learners are LogisticRegression for regression task when CV is on.
    """
    LIGHT_GBM_REGRESSOR = "LightGBMRegressor"
    LINEAR_REGRESSION = "LinearRegression"


class StochasticOptimizer(str, Enum):
    """
    Type of optimizer.
    """
    NONE = "None"
    """
    No optimizer selected.
    """
    SGD = "Sgd"
    """
    Stochastic Gradient Descent optimizer.
    """
    ADAM = "Adam"
    """
    Adam is algorithm the optimizes stochastic objective functions based on adaptive estimates of moments
    """
    ADAMW = "Adamw"
    """
    AdamW is a variant of the optimizer Adam that has an improved implementation of weight decay.
    """


class TargetAggregationFunction(str, Enum):
    """
    The function to be used to aggregate the time series target column to conform to a user specified frequency.
    If the TargetAggregateFunction is set i.e. not 'None', but the freq parameter is not set, the error is raised. The possible target aggregation functions are: "sum", "max", "min" and "mean".
    """
    NONE = "None"
    """
    Represent no value set.
    """
    SUM = "Sum"
    MAX = "Max"
    MIN = "Min"
    MEAN = "Mean"


class TargetLagsMode(str, Enum):
    """
    [Required] Set target lags mode - Auto/Custom
    """
    AUTO = "Auto"
    """
    Target lags to be determined automatically.
    """
    CUSTOM = "Custom"
    """
    Use the custom target lags.
    """


class TargetRollingWindowSizeMode(str, Enum):
    """
    [Required] TargetRollingWindowSiz detection mode.
    """
    AUTO = "Auto"
    """
    Determine rolling windows size automatically.
    """
    CUSTOM = "Custom"
    """
    Use the specified rolling window size.
    """


class TaskType(str, Enum):
    """
    [Required] Task type for AutoMLJob.
    """
    CLASSIFICATION = "Classification"
    """
    Classification in machine learning and statistics is a supervised learning approach in which
    the computer program learns from the data given to it and make new observations or classifications.
    """
    REGRESSION = "Regression"
    """
    Regression means to predict the value using the input data. Regression models are used to predict a continuous value.
    """
    FORECASTING = "Forecasting"
    """
    Forecasting is a special kind of regression task that deals with time-series data and creates forecasting model
    that can be used to predict the near future values based on the inputs.
    """
    IMAGE_CLASSIFICATION = "ImageClassification"
    """
    Image Classification. Multi-class image classification is used when an image is classified with only a single label
    from a set of classes - e.g. each image is classified as either an image of a 'cat' or a 'dog' or a 'duck'.
    """
    IMAGE_CLASSIFICATION_MULTILABEL = "ImageClassificationMultilabel"
    """
    Image Classification Multilabel. Multi-label image classification is used when an image could have one or more labels
    from a set of labels - e.g. an image could be labeled with both 'cat' and 'dog'.
    """
    IMAGE_OBJECT_DETECTION = "ImageObjectDetection"
    """
    Image Object Detection. Object detection is used to identify objects in an image and locate each object with a
    bounding box e.g. locate all dogs and cats in an image and draw a bounding box around each.
    """
    IMAGE_INSTANCE_SEGMENTATION = "ImageInstanceSegmentation"
    """
    Image Instance Segmentation. Instance segmentation is used to identify objects in an image at the pixel level,
    drawing a polygon around each object in the image.
    """
    TEXT_CLASSIFICATION = "TextClassification"
    """
    Text classification (also known as text tagging or text categorization) is the process of sorting texts into categories.
    Categories are mutually exclusive.
    """
    TEXT_CLASSIFICATION_MULTILABEL = "TextClassificationMultilabel"
    """
    Multilabel classification task assigns each sample to a group (zero or more) of target labels.
    """
    TEXT_NER = "TextNER"
    """
    Text Named Entity Recognition a.k.a. TextNER.
    Named Entity Recognition (NER) is the ability to take free-form text and identify the occurrences of entities such as people, locations, organizations, and more.
    """


class UseStl(str, Enum):
    """
    Configure STL Decomposition of the time-series target column.
    """
    NONE = "None"
    """
    No stl decomposition.
    """
    SEASON = "Season"
    SEASON_TREND = "SeasonTrend"


class ValidationMetricType(str, Enum):
    """
    Metric computation method to use for validation metrics.
    """
    NONE = "None"
    """
    No metric.
    """
    COCO = "Coco"
    """
    Coco metric.
    """
    VOC = "Voc"
    """
    Voc metric.
    """
    COCO_VOC = "CocoVoc"
    """
    CocoVoc metric.
    """


class ValueFormat(str, Enum):
    """
    format for the workspace connection value
    """
    JSON = "JSON"


class Weekday(str, Enum):
    """
    Enum of weekdays
    """
    MONDAY = "Monday"
    """
    Monday weekday
    """
    TUESDAY = "Tuesday"
    """
    Tuesday weekday
    """
    WEDNESDAY = "Wednesday"
    """
    Wednesday weekday
    """
    THURSDAY = "Thursday"
    """
    Thursday weekday
    """
    FRIDAY = "Friday"
    """
    Friday weekday
    """
    SATURDAY = "Saturday"
    """
    Saturday weekday
    """
    SUNDAY = "Sunday"
    """
    Sunday weekday
    """
