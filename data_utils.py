def validate_data(df):
    report = {}
    report['Missing Values'] = df.isnull().sum().to_dict()
    report['Zeros'] = (df == 0).sum().to_dict()
    report['Outliers'] = {
        col: ((df[col] < df[col].quantile(0.05)) | (df[col] > df[col].quantile(0.95))).sum()
        for col in df.select_dtypes(include='number').columns
    }
    return report