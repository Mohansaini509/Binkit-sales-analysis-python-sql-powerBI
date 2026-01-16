import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_blinkit_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s -%(levelname)s -%(message)s",
    filemode="a"
)
conn=sqlite3.connect('inventory.db')
def create_blinkit_summary(conn):
    '''this function will marge the different table to get the overall summary and adding new columns in the resultant data '''
    blinkit_sales_summary=pd.read_sql_query("""WITH orders AS(
            SELECT
                o.customer_id,
                oI.product_id,
                o.order_id,
                oI.quantity,
                o.order_date,
                o.order_total,
                o.payment_method,
                d.delivery_status,
                cf.rating,
                cf.feedback_category,
                cf.sentiment
                FROM blinkit_orders o
                LEFT JOIN blinkit_order_items oI
                    ON o.order_id = oI.order_id
                LEFT JOIN blinkit_delivery_performance d
                    ON oI.order_id = d.order_id
                LEFT JOIN blinkit_customer_feedback cf
                    ON d.order_id = cf.order_id

),

customers AS(
        SELECT
                customer_id,
                customer_name,
                customer_segment,
                registration_date,
                total_orders,
                avg_order_value
        FROM blinkit_customers
),

inventory AS(
    SELECT
        product_id,
        SUM(stock_received) AS Total_stock_received,
        SUM(damaged_stock) AS Total_damaged_received
    FROM (
        SELECT product_id, stock_received, damaged_stock FROM blinkit_inventory
        UNION ALL
        SELECT product_id, stock_received, damaged_stock FROM blinkit_inventoryNew
    ) t
    GROUP BY product_id
),

products AS(
         SELECT
            product_id,
            product_name,
            category,
            brand,
            mrp,
            price,
            shelf_life_days,
            min_stock_level,
            max_stock_level
            FROM blinkit_products
)

        SELECT
                o.product_id,
                o.order_id,
                o.customer_id,
                c.customer_name,
                p.product_name,
                c.registration_date,
                o.order_date,
                o.quantity,
                o.order_total,
                p.category,
                p.brand,
                p.mrp,
                p.price,
                o.payment_method,
                o.delivery_status,
                o.rating,
                o.feedback_category,
                o.sentiment,
                c.customer_segment,
                c.total_orders,
                c.avg_order_value,   
                p.shelf_life_days,
                p.min_stock_level,
                p.max_stock_level,
                I.Total_stock_received,
                I.Total_damaged_received
        FROM orders o
        LEFT JOIN customers c
            ON o.customer_id = c.customer_id
        LEFT JOIN products p
            ON o.product_id = p.product_id
        LEFT JOIN inventory I
            ON o.product_id = I.product_id
        ORDER BY c.customer_id ASC
        """,conn)
    return blinkit_sales_summary

def clean_data(df):
    '''this function will remove all the consistencies from the data and adding new features'''
   
    # changing data format
    df['order_date'] = (pd.to_datetime(df['order_date'], errors='coerce').dt.strftime('%Y-%m-%d'))
    df['registration_date'] = (pd.to_datetime(df['registration_date']))

    # adding new features
    df['ProfitMargin'] = (df['mrp']-df['price'])
    df['stockDamagRatio'] = (df['Total_damaged_received']/df['Total_stock_received'])
    
    return df

if __name__ == '__main__':
    #creating database connection
    conn = sqlite3.connect('inventory.db')

    logging.info("creating order table ")
    summary_df = create_blinkit_summary(conn)
    logging.info(summary_df.head())

    #cleaning data
    logging.info("cleaning data table")
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())

    #Again ingest in database
    logging.info("ingesting table")
    ingest_db(clean_df,'blinkit_sales_summary',conn)
    logging.info("complete")

    