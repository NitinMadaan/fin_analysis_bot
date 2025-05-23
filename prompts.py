dashboard_prompt = """
You are a BI dashboard assistant. Given this summary of validated data:
{data_summary}

Suggest:
1. 5 key KPIs to highlight
2. Chart types for each KPI
3. Visual layout (page structure)
4. Any data issues that must be fixed
"""