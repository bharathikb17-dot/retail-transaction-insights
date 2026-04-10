from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import (
    basic_exploration,
    customer_behavior,
    promotion_analysis,
    seasonality_analysis
)
from src.visualization import (
    plot_transactions_by_city,
    plot_payment_distribution,
    plot_monthly_revenue,
    plot_heatmap
)


def display_menu():
    """Display main menu options"""
    print("\n" + "="*60)
    print("     RETAIL TRANSACTION INSIGHTS - ANALYSIS DASHBOARD")
    print("="*60)
    print("\nSelect an analysis task:")
    print("1. Task 1 - Data Preparation (Show preprocessing summary)")
    print("2. Task 2 - Basic Exploration (Transactions, Customers, Products)")
    print("3. Task 3 - Customer Behavior Analysis")
    print("4. Task 4 - Promotion & Discount Impact")
    print("5. Task 5 - Seasonality Trends")
    print("6. Task 6 - Generate All Visualizations")
    print("7. Show All Results (Run all tasks)")
    print("0. Exit")
    print("-"*60)


def show_task1_preparation(df):
    """Task 1: Data Preparation"""
    print("\n" + "="*60)
    print("TASK 1: DATA PREPARATION")
    print("="*60)
    print(f"✓ CSV file loaded successfully")
    print(f"✓ Date column parsed and converted to datetime format")
    print(f"✓ Additional columns extracted: Year, Month, DayOfWeek")
    print(f"✓ Data cleaned: Duplicates removed, missing values handled")
    print(f"\nDataset Info:")
    print(f"  - Total rows: {len(df)}")
    print(f"  - Total columns: {len(df.columns)}")
    print(f"  - Columns: {', '.join(df.columns.tolist())}")
    print(f"  - Date range: {df['Date'].min()} to {df['Date'].max()}")


def show_task2_exploration(df, basic):
    """Task 2: Basic Exploration"""
    print("\n" + "="*60)
    print("TASK 2: BASIC EXPLORATION")
    print("="*60)
    print(f"\n1. Total Transactions: {basic['total_transactions']:,}")
    print(f"2. Unique Customers: {basic['unique_customers']:,}")
    
    print(f"\n3. Top 5 Most Common Products:")
    for rank, (product, count) in enumerate(basic['top_products'].items(), 1):
        print(f"   {rank}. {product}: {count} transactions")
    
    print(f"\n4. Top 5 Cities by Transaction Count:")
    for rank, (city, count) in enumerate(basic['top_cities'].items(), 1):
        print(f"   {rank}. {city}: {count} transactions")


def show_task3_customer_behavior(df, customer):
    """Task 3: Customer Behavior Analysis"""
    print("\n" + "="*60)
    print("TASK 3: CUSTOMER BEHAVIOR ANALYSIS")
    print("="*60)
    
    print(f"\n1. Average Spending by Customer Category:")
    for category, avg_spend in customer['avg_spend_category'].items():
        print(f"   - {category}: ${avg_spend:.2f}")
    
    print(f"\n2. Payment Method Preferences by Customer Category (Highest):")
    payment_prefs = customer['payment_pref']
    # Group by category and find max for each
    category_max = {}
    for (category, method), count in payment_prefs.items():
        if category not in category_max or count > category_max[category][1]:
            category_max[category] = (method, count)
    
    for category, (method, count) in sorted(category_max.items()):
        print(f"   - {category}: {method} ({count} transactions)")
    
    print(f"\n3. Average Items Purchased per Store Type:")
    for store_type, avg_items in customer['avg_items_store'].items():
        print(f"   - {store_type}: {avg_items:.2f} items per transaction")


def show_task4_promotion(df, promo):
    """Task 4: Promotion & Discount Impact"""
    print("\n" + "="*60)
    print("TASK 4: PROMOTION & DISCOUNT IMPACT")
    print("="*60)
    
    print(f"\n1. Average Transaction Cost (Discount Impact):")
    for discount_status, avg_cost in promo['discount_impact'].items():
        status = "With Discount" if discount_status == True else "Without Discount"
        print(f"   - {status}: ${avg_cost:.2f}")
    
    print(f"\n2. Average Items Purchased by Promotion Type:")
    for promo_type, avg_items in promo['promo_items'].items():
        print(f"   - {promo_type}: {avg_items:.2f} items")
    
    print(f"\n3. Most Effective Promotion (by Average Cost):")
    for rank, (promo_type, avg_cost) in enumerate(promo['promo_effectiveness'].items(), 1):
        print(f"   {rank}. {promo_type}: ${avg_cost:.2f}")


def show_task5_seasonality(df, season):
    """Task 5: Seasonality Trends"""
    print("\n" + "="*60)
    print("TASK 5: SEASONALITY TRENDS")
    print("="*60)
    
    print(f"\n1. Total Revenue by Season:")
    for season_name, revenue in season['season_revenue'].items():
        print(f"   - {season_name}: ${revenue:,.2f}")
    
    highest_season = season['season_revenue'].idxmax()
    print(f"\n   ★ Highest Revenue Season: {highest_season}")
    
    print(f"\n2. Average Spending per Season:")
    for season_name, avg_spend in season['avg_spend_season'].items():
        print(f"   - {season_name}: ${avg_spend:.2f}")
    
    print(f"\n3. Store Type Preferences by Season:")
    for (season_name, store_type), count in season['season_store'].items():
        print(f"   - {season_name} / {store_type}: {count} transactions")


def show_task6_visualizations(df):
    """Task 6: Generate All Visualizations"""
    print("\n" + "="*60)
    print("TASK 6: GENERATING VISUALIZATIONS")
    print("="*60)
    print("\nGenerating plots...")
    
    plot_transactions_by_city(df)
    print("✓ Bar plot: Transactions per City")
    
    plot_payment_distribution(df)
    print("✓ Pie chart: Payment Method Distribution")
    
    plot_monthly_revenue(df)
    print("✓ Line chart: Monthly Revenue Trends")
    
    plot_heatmap(df)
    print("✓ Heatmap: Revenue by Season & Customer Category")
    
    print("\n✓ All visualizations saved to: outputs/plots/")


def main():
    # Load and preprocess data once
    df = load_data("data/Retail_Transactions_Dataset.csv")
    df = preprocess_data(df)
    
    # Run all analyses once
    basic = basic_exploration(df)
    customer = customer_behavior(df)
    promo = promotion_analysis(df)
    season = seasonality_analysis(df)

    while True:
        display_menu()
        choice = input("Enter your choice (0-7): ").strip()
        
        if choice == "1":
            show_task1_preparation(df)
        elif choice == "2":
            show_task2_exploration(df, basic)
        elif choice == "3":
            show_task3_customer_behavior(df, customer)
        elif choice == "4":
            show_task4_promotion(df, promo)
        elif choice == "5":
            show_task5_seasonality(df, season)
        elif choice == "6":
            show_task6_visualizations(df)
        elif choice == "7":
            print("\n" + "="*60)
            print("GENERATING ALL REPORTS...")
            print("="*60)
            show_task1_preparation(df)
            show_task2_exploration(df, basic)
            show_task3_customer_behavior(df, customer)
            show_task4_promotion(df, promo)
            show_task5_seasonality(df, season)
            show_task6_visualizations(df)
        elif choice == "0":
            print("\nThank you for using Retail Transaction Insights!")
            break
        else:
            print("\n✗ Invalid choice. Please select a valid option.")
        
        if choice != "0":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()