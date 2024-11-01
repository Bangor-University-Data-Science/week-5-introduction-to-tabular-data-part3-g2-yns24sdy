import pandas as pd

def import_data(filename):
    if filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    elif filename.endswith('.csv'):
        return pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format")

def filter_data(df):
    return df.dropna(subset=['CustomerID']).loc[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

def loyalty_customers(df, min_purchases):
    customer_counts = df.groupby('CustomerID').size()
    loyal_customers = customer_counts[customer_counts >= min_purchases].reset_index()
    loyal_customers.columns = ['CustomerID', 'PurchaseCount']
    return loyal_customers

def quarterly_revenue(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['quarter'] = df['InvoiceDate'].dt.quarter
    df['revenue'] = df['Quantity'] * df['UnitPrice']
    quarterly_revenue = df.groupby('quarter')['revenue'].sum().reset_index()
    quarterly_revenue.columns = ['quarter', 'total_revenue']
    return quarterly_revenue

def high_demand_products(df, top_n):
    product_quantity = df.groupby('StockCode')['Quantity'].sum().reset_index()
    top_products = product_quantity.nlargest(top_n, 'Quantity')
    return top_products

def purchase_patterns(df):
    patterns = df.groupby('StockCode').agg({'Quantity': 'mean', 'UnitPrice': 'mean'}).reset_index()
    patterns.columns = ['product', 'avg_quantity', 'avg_unit_price']
    return patterns

def answer_conceptual_questions():
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A", "B", "C"},
        "Q5": {"A"}
    }
    return answers
