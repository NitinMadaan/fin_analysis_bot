def analyze_margins(df):
    results = {}
    if 'Revenue' in df.columns and 'Cost' in df.columns:
        df['Margin'] = df['Revenue'] - df['Cost']
        results['Avg Margin'] = df['Margin'].mean()
        results['Bleeding Count'] = (df['Margin'] < 0).sum()
    return results