from rich.console import Console
from rich.table import Table

console = Console()

def print_revenue_report(summary: dict):
    console.print("\n[bold green]📊 Revenue Report[/bold green]\n")

    console.print(f"Total Revenue: [bold yellow]{summary['total_revenue']}[/bold yellow]\n")

    table = Table(title="Revenue by Product")
    table.add_column("Product")
    table.add_column("Revenue", justify="right")

    for product, revenue in summary["revenue_by_product"].items():
        table.add_row(product, str(revenue))

    console.print(table)


def print_top_products(df):
    console.print("\n[bold cyan]🏆 Top Products[/bold cyan]\n")

    table = Table(title="Top Selling Products")
    table.add_column("Product")
    table.add_column("Total Sales", justify="right")
    table.add_column("Count", justify="right")

    for idx, row in df.iterrows():
        table.add_row(idx, str(row["total_sales"]), str(row["count"]))

    console.print(table)
