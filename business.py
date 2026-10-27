import streamlit as st

# 1. Set up the layout and style of the dashboard app window (MUST BE FIRST)
st.set_page_config(page_title="IbraBeast Production Framework", layout="centered")

st.title("🐑 IbraBeast Eid Market Calculator")
st.markdown("Business Production & Inventory Optimization Framework for Qatar Markets")
st.markdown("---")

# 2. Set up baseline operating constants (Feed, overhead, and maintenance costs per beast in QAR)
COST_SHEEP = 450.0   # Feed and processing overhead until sold
COST_GOAT = 350.0    # Local goat maintenance overhead
COST_CHICKEN = 15.0  # Artisanal poultry production cost

# 3. Create Interactive Sliders for Sales Inventory
st.subheader("🚜 Adjust Eid Al-Adha Production Supply")

# Livestock inventory allocations
u_sheep = st.slider("Syrian Sheep Inventory (Heads)", min_value=0, max_value=500, value=120, step=5)
u_goat = st.slider("Local Goat Inventory (Heads)", min_value=0, max_value=300, value=50, step=5)
u_chicken = st.slider("Artisanal Chicken Quantity (Birds)", min_value=0, max_value=2000, value=500, step=25)

st.markdown("---")

# 4. Interactive Sliders for Market Pricing (Set to typical QAR market benchmarks)
st.subheader("💰 Eid Retail Price Configuration (QAR)")

price_sheep = st.slider("Syrian Sheep Market Price (per head)", min_value=800, max_value=2000, value=1250, step=50)
price_goat = st.slider("Local Goat Market Price (per head)", min_value=700, max_value=1800, value=1100, step=50)
price_chicken = st.slider("Artisanal Chicken Price (per bird)", min_value=20, max_value=80, value=45, step=5)

st.markdown("---")

# 5. Business Production Engines & Algebra Matrix
total_revenue = (u_sheep * price_sheep) + (u_goat * price_goat) + (u_chicken * price_chicken)
total_costs = (u_sheep * COST_SHEEP) + (u_goat * COST_GOAT) + (u_chicken * COST_CHICKEN)
net_profit = total_revenue - total_costs
total_beasts = u_sheep + u_goat + u_chicken

# 6. Display Calculations and Financial Forecasts
st.subheader("📊 Projected Eid Production Metrics")

# Visual data cards
col1, col2, col3 = st.columns(3)
col1.metric(label="Total Projected Revenue", value=f"{total_revenue:,} QAR")
col2.metric(label="Total Operating Costs", value=f"{total_costs:,} QAR")

if total_revenue > 0:
    profit_pct = (net_profit / total_revenue) * 100
else:
    profit_pct = 0.0

col3.metric(label="Net Profit Margin", value=f"{net_profit:,} QAR", delta=f"{profit_pct:.1f}% Profit")

st.markdown("---")

# 7. Strategic Deployment Decision Engine
st.subheader("🔮 Inventory Command Evaluation")

if net_profit >= 50000:
    st.success("🚀 PRODUCTION DECISION: MAXIMUM EXPANSION")
    st.info(f"Targeting {total_beasts} animals yields high margins. Secure additional Syrian stock and finalize delivery logistics across Qatar immediately.")
elif net_profit > 0:
    st.warning("⚠️ PRODUCTION DECISION: CONSERVATIVE STOCKING")
    st.info("The production margins are thin due to high feed/overhead costs. Avoid scaling stock up unless retail prices rise or subsidies apply.")
else:
    st.error("🛑 PRODUCTION DECISION: HALT ACQUISITION")
    st.error("Operating expenditures exceed projected revenue. Recalibrate retail prices or downscale stock volumes immediately to prevent capital loss.")
