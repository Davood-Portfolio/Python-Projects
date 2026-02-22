import pandas as pd

def revenue_summary(df: pd.DataFrame) -> dict:
    """Return total revenue and revenue by product."""
    total_revenue = df["price"].sum()

    revenue_by_product = (
        df.groupby("product")["price"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    return {
        "total_revenue": total_revenue,
        "revenue_by_product": revenue_by_product
    }


def top_products(df: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    """Return top-selling products."""
    return (
        df.groupby("product")
        .agg(total_sales=("price", "sum"), count=("product", "count"))
        .sort_values("total_sales", ascending=False)
        .head(limit)
    )


def filter_by_date(df: pd.DataFrame, start=None, end=None) -> pd.DataFrame:
    """Filter orders by date range."""
    df["date"] = pd.to_datetime(df["date"])

    if start:
        df = df[df["date"] >= pd.to_datetime(start)]
    if end:
        df = df[df["date"] <= pd.to_datetime(end)]

    return df
