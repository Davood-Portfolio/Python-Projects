import argparse
from engine.loaders import load_from_sqlite
from engine.analytics import revenue_summary, top_products, filter_by_date
from engine.reports import print_revenue_report, print_top_products

def main():
    parser = argparse.ArgumentParser(description="DataInsight Engine CLI")
    parser.add_argument("--report", required=True, help="Type of report: revenue | top-products")
    parser.add_argument("--from", dest="start_date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--to", dest="end_date", help="End date (YYYY-MM-DD)")

    args = parser.parse_args()

    df = load_from_sqlite("SELECT * FROM orders")

    if args.start_date or args.end_date:
        df = filter_by_date(df, args.start_date, args.end_date)

    if args.report == "revenue":
        summary = revenue_summary(df)
        print_revenue_report(summary)

    elif args.report == "top-products":
        result = top_products(df)
        print_top_products(result)

    else:
        print("Unknown report type")


if __name__ == "__main__":
    main()
