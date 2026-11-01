from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load exported data on startup
sim_df = pd.read_json("app_data/sim_results.json")
product_master = pd.read_json("app_data/product_master.json")
sim_df["month"] = pd.to_datetime(sim_df["month"]).dt.strftime('%Y-%m')

@app.route('/api/locations')
def get_locations():
    """Returns available business locations."""
    locations = sorted(sim_df["Location_ID"].unique().tolist())
    return jsonify(locations)

@app.route('/api/replenishment/<location_id>')
def get_replenishment(location_id):
    """Returns the latest replenishment recommendations for a specific location."""
    loc_data = sim_df[sim_df["Location_ID"] == location_id].copy()
    latest_month = loc_data["month"].max()
    latest_data = loc_data[loc_data["month"] == latest_month].copy()
    
    # Merge with product names
    merged = latest_data.merge(product_master[["Product_ID", "Product_Name"]], on="Product_ID", how="left")
    actions = merged[merged["Order_Placed"] > 0].copy()
    
    items = []
    for _, row in actions.iterrows():
        items.append({
            "product_name": row.get("Product_Name", row["Product_ID"]),
            "ending_stock": round(float(row["Ending_Stock"]), 1),
            "order_units": int(round(float(row["Order_Placed"]))),
            "action": "Replenish Now"
        })
        
    return jsonify({
        "location_id": location_id,
        "latest_month": latest_month,
        "total_items": len(items),
        "total_units": sum([i["order_units"] for i in items]),
        "items": items
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)