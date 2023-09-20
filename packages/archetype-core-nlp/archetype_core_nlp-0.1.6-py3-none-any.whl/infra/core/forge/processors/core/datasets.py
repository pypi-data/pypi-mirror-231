from pyspark.sql import DataFrame

from infra.core.forge.processors import io


def sklearn_ds(name: str, *args, **kwargs) -> DataFrame:
    """Load Scikit-learn dataset from function name.

    Parameters
    ----------
    name: Name of the function within :code:`sklearn.datasets`
    args: Arguments passed to the building function
    \**kwargs
        Key arguments passed to the building function

    Examples
    --------
    .. code-block:: python

        import yhbrasil.dna.core as C
        C.datasets.iris().limit(5).toPandas()

    """
    import pandas as pd
    from sklearn import datasets

    NUMBERS = ('um dois tres quatro cinco seis sete oito nove dez onze doze '
            'treze quatorze quinze dezesseis dezesete dezoito dezenove '
            'vinte trinta quarenta cinquenta sessenta setenta oitenta '
            'noventa cem duzentos trezentos quatrocentos quinhentos '
            'seiscentos setecentos oitocentos novecentos mil milhao'
            .split())    

    x = getattr(datasets, name)(*args, **kwargs)
    d = pd.DataFrame(x.data, columns=x.feature_names)

    d['target'] = (x.target_names[x.target].astype(str)
                   if hasattr(x, 'target_names')
                   else x.target)

    d = io.stream.read(d)
    d = io.stream.conform(d)
    d = io.stream.merge(d)

    return d


def wine() -> DataFrame:
    """Load the wine dataset from :code:`sklearn.datasets` as spark dataframe.

    Examples
    --------
    .. jupyter-execute::

        import yhbrasil.dna.core as C
        C.datasets.wine().limit(2).toPandas()

    """
    return sklearn_ds('load_wine')


def iris() -> DataFrame:
    """Load the iris dataset from :code:`sklearn.datasets` as spark dataframe.

    Examples
    --------
    .. jupyter-execute::

        import yhbrasil.dna.core as C
        C.datasets.iris().limit(2).toPandas()

    """
    return sklearn_ds('load_iris')


def digits() -> DataFrame:
    """Load the digits dataset from :code:`sklearn.datasets` as spark dataframe.

    Examples
    --------
    .. jupyter-execute::

        import yhbrasil.dna.core as C
        C.datasets.digits().limit(2).toPandas()

    """
    return sklearn_ds('load_digits')


def boston() -> DataFrame:
    """Load the iris dataset from :code:`sklearn.datasets` as spark dataframe.

    Examples
    --------
    .. jupyter-execute::

        import yhbrasil.dna.core as C
        C.datasets.boston().limit(2).toPandas()

    """
    return sklearn_ds('load_boston')
