import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "Used Car Analysis",
    layout = "wide",
    page_icon = "🚗"
)

df = pd.read_csv('project/clean_vehicle_data.csv')
# st.dataframe(df)

with st.sidebar:

    opt = option_menu("Menu",['Home','Dataset','Preprocessing','Visualizations','About'],
    icons=['house','file-text','tools','bar-chart-line','info-circle'])
    selected_state=st.multiselect("Select State",options = df["State"].unique())


if selected_state :
    filtered = df[df['State'].isin(selected_state)]
else:
    filtered = df


if opt=='Home':
    st.title('🚗Used Car Dashboard')
    st.markdown('### Explore the cleaned used vehicle dataset with interactive analytics.')
    
    Vehicles = len(filtered)
    total_brand = filtered['Brand'].nunique()
    total_state = filtered['State'].nunique()
    avg_price = filtered['Price'].mean()
   
    st.markdown("""
    <style>
    .kpi-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 16px 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.1s;
        margin: 6px 0;
    }
    .kpi-card:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    .kpi-label {
        font-size: 1rem;
        color: #6c757d;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        line-height: 1.2;
        margin-top: 4px;
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
        <div class="kpi-icon">🏷️</div>
        <div class="kpi-title">Total Vehicles</div>
        <div class="kpi-value">{Vehicles:,}</div>
        </div>
        """, unsafe_allow_html=True)


    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🚗</div>
            <div class="kpi-title">Total Brands</div>
            <div class="kpi-value">{total_brand:,}</div>
        </div>
        """, unsafe_allow_html=True)


    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">🌍</div>
            <div class="kpi-title">Total State</div>
            <div class="kpi-value">{total_state:,}</div>
        </div>
        """, unsafe_allow_html=True)



    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">💰</div>
            <div class="kpi-title">Avg Price</div>
            <div class="kpi-value">${avg_price:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)





    # st.subheader("📖 About this Dashboard")
    # st.info("""
    # This dashboard provides interactive insights into the used car market.
    # Users can explore top transmission, avg vehicle age, fuel types,avg engine size,
    # and other important characteristics using dynamic filters.
    # """)

   
    
    col1, col2, col3, col4 = st.columns(4)
    # # Total kilometers

    with col1:
        avg_kilometers = filtered['Kilometres'].mean()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🛣️ </div>
            <div class="kpi-title">Average Kilometers</div>
            <div class="kpi-value">{avg_kilometers:.0f}</div>
            
        </div>
        """, unsafe_allow_html=True)

   

    # Average Vehicle Age
    with col2:
        avg_age = filtered['VehicleAge'].mean()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🚗</div>
            <div class="kpi-title">Average Vehicle Age</div>
            <div class="kpi-value">{avg_age:.1f} Years</div>
        </div>
        """, unsafe_allow_html=True)


    # Average Engine Size
    with col3:
        avg_engine = filtered['EngineSizeL'].mean()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🔧</div>
            <div class="kpi-title">Average Engine Size</div>
            <div class="kpi-value">{avg_engine:.1f} L</div>
        </div>
        """, unsafe_allow_html=True)




    # Fuel Types
    with col4:
        fuel_types = filtered['FuelType'].nunique()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">⛽</div>
            <div class="kpi-title">Fuel Types</div>
            <div class="kpi-value">{fuel_types}</div>
        </div>
        """, unsafe_allow_html=True)


    st.subheader("✨ Dashboard Features") 
    st.markdown(""" - 📈 Analyze vehicle prices. 
    - 🚗 Compare different brands and models. 
    - ⚙️ Explore transmission and fuel type distribution. 
    - 📍 Filter data by state. 
    - 📊 Interactive visualizations with Plotly. """)

#     st.subheader("✨ Dashboard Features")

#     st.markdown("""
#     <style>
#     .feature-card {
#         background: #ffffff;
#         padding: 22px;
#         border-radius: 15px;
#         text-align: center;
#         border: 1px solid #e5e7eb;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.06);
#         height: 190px;
#         transition: 0.3s;
#     }

#     .feature-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 8px 20px rgba(0,0,0,0.12);
#     }

#     .feature-icon {
#         font-size: 35px;
#         margin-bottom: 8px;
#     }

#    .feature-title {
#         font-size: 20px;
#         font-weight: 700;
#         color: #1f2937;
#         margin-bottom: 8px;
#     }

#     .feature-text {
#         font-size: 15px;
#         color: #6b7280;
#         line-height: 1.5;
#     }
#     </style>
#     """, unsafe_allow_html=True)


#     col1, col2, col3 = st.columns(3, gap="medium")


#     with col1:
#          st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">📊</div>
#             <div class="feature-title">Market Analytics</div>
#             <div class="feature-text">
#                 Analyze vehicle prices, brands, mileage,
#                 age and other important market statistics.
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


#     with col2:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">🔍</div>
#             <div class="feature-title">Smart Filtering</div>
#             <div class="feature-text">
#                 Filter vehicles by state and explore
#                 relevant data based on your selection.
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


#     with col3:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">📈</div>
#             <div class="feature-title">Interactive Charts</div>
#             <div class="feature-text">
#                 Explore interactive Plotly visualizations
#                 to discover trends and vehicle insights.
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

    
    st.subheader("🎯 Dashboard Purpose")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            padding:20px;
            border-radius:15px;
            color:white;
            text-align:center;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);
            height:180px;">
            <h2>🔍 Explore</h2>
            <p style="font-size:16px;">
            Analyze the used car market with interactive filters.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            padding:20px;
            border-radius:16px;
            color:white;
            text-align:center;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);
            height:180px;">
            <h2>📈 Compare</h2>
            <p style="font-size:16px;">
            Compare brands, prices, and vehicle characteristics.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fa709a, #fee140);
            padding:20px;
            border-radius:16px;
            color:white;
            text-align:center;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);
            height:180px;">
            <h2>💡 Discover</h2>
            <p style="font-size:16px;">
            Find valuable trends and market insights.
            </p>
        </div>
        """, unsafe_allow_html=True)
      




elif opt == "Dataset":

    st.title("🧾 Used Car Dataset")

    num_rows = filtered.shape[0]
    num_cols = filtered.shape[1]

    st.markdown("""
    <style>
    .dataset-info{
        background:#f8f9fa;
        padding:15px;
        border-radius:10px;
        border-left:5px solid #2c7be5;
        display:flex;
        gap:30px;
        flex-wrap:wrap;
        margin-bottom:20px;
    }

    .dataset-info-item{
        font-size:19px;
    }

    .dataset-info-item strong{
        color:#2c7be5;
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown(f"""
    <div class='dataset-info'>
    
    <span class='dataset-info-item'>📋<strong>Rows:</strong> {num_rows}</span>
    <span class='dataset-info-item'>📋<strong>Columns:</strong> {num_cols}</span>
    <span class='dataset-info-item'>🚗<strong>Brands:</strong> {filtered["Brand"].nunique()}</span>
    <span class='dataset-info-item'>🌍<strong>States:</strong> {filtered["State"].nunique()}</span>
    <span class='dataset-info-item'>🔖<strong>Models:</strong> {filtered["Model"].nunique()}</span>

    </div>
    """, unsafe_allow_html=True)

   
    # ---------- Tabs: Data preview | Columns information | Summary ----------
    tab1, tab2, tab3 = st.tabs(['Data Preview','Column Information','Summary'])  
    with tab1:
        #search button
        search = st.text_input(
        "🔍 Search Vehicle",
        placeholder="Search by Brand or Model...")

        if search:
            filtered = df[
                df["Brand"].str.contains(search, case=False, na=False) |
                df["Model"].str.contains(search, case=False, na=False)]

        else:
            filtered = df


        col1, col2 = st.columns([3,1])
        with col1:
            st.subheader("Preview Filtered Data")
        with col2:
            # Slider to choose number of rows to display
            num_rows = st.slider("Select number of rows to display",min_value=5,max_value=100,value=10,step=5)


        # Display the first n rows
        st.dataframe(filtered.head(num_rows),use_container_width=True)



        # Download button for the filtered data
        csv = filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download filtered data as CSV",
            data=csv,
            file_name="used_car_filtered.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with tab2:
        st.subheader("📋 Dataset Structure")

        structure = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Non-Null Values": df.notna().sum().values,
            "Missing Values": df.isna().sum().values,
            "Unique Values": df.nunique().values})

        st.dataframe(structure,use_container_width=True,hide_index=True)



    # with tab3:
    #     # ---------------- NUMERIC SUMMARY ----------------
    #     st.subheader("📈 Numerical Statistics")

    #     numeric_cols = df.select_dtypes(include="number").columns

    #     st.dataframe(
    #     df[numeric_cols].describe().T.round(2),
    #     use_container_width=True
    # )
    with tab3:
        st.subheader("Statistical Summary")

        # Separate numeric and categorical columns
        num_cols = filtered.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cat_cols = filtered.select_dtypes(include=['object', 'category']).columns.tolist()

        if num_cols:
            st.markdown("#### 📊 Numeric Columns")
            st.dataframe(filtered[num_cols].describe(), use_container_width=True)

        if cat_cols:
            st.markdown("#### 🏷️ Categorical Columns")
            # Show top 3 categories for each categorical column
            for col in cat_cols[:4]:  # Limit to first 4 to keep layout clean
                with st.expander(f"Top values in '{col}'"):
                    st.dataframe(
                        filtered[col].value_counts().reset_index().head(10),
                        use_container_width=True,
                        hide_index=True
                    )
            if len(cat_cols) > 4:
                st.info(f"Showing top 4 categorical columns. There are {len(cat_cols)} in total.")




elif opt == "Preprocessing":

    st.title("🧹 Data Preprocessing Pipeline")

    st.markdown("""
    This page shows how we clean the raw USED CAR data before visualisation.

    **We perform the following steps:**

    - 🗑️ Drop columns that are not needed for our analysis.
    - 🧹 Remove rows that contain missing values.
    - 🔄 Reset the index for a clean, sequential DataFrame.
    """)
    

    def get_missing_stats(df):
        missing_df = df.isna().sum().reset_index()
        missing_df.columns = ['Column Name', 'Missing Count']
        missing_df['Missing %'] = (missing_df['Missing Count'] / len(df) * 100).round(1)
        missing_df = missing_df[missing_df['Missing Count'] > 0] 
        return missing_df




      # ---------- Before Processing ----------
    st.subheader("🔍 Before Processing")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("**🔍 Missing Value Details**")
        missing_data = get_missing_stats(filtered)
   
        if missing_data.empty:
            st.markdown("**✅ Your dataset is completely clean!**")
        else:
            st.dataframe(
                missing_data.style.format({
                    "Missing Count": "{:,}",
                    "Missing %": "{:.1f}%"
                }),
                use_container_width=True,
                height=300
            )

    with col2:
        st.markdown("**📊 Dataset Status**")

        total_missing = int(missing_data["Missing Count"].sum()
        )if not missing_data.empty else 0

        affected_columns = len(missing_data)
        st.metric("📋 Affected Columns",affected_columns)
        st.metric("❌ Total Missing Values",f"{total_missing:,}")
        st.metric("📦 Total Records",f"{len(filtered):,}")  
        

    # if not missing_data.empty:
    #         # ---------- Missing Values Visualization ----------
           
    #     st.subheader("📊 Missing Values Visualization")

    #     fig = px.bar(
    #         missing_data,
    #         x="Column Name",
    #         y="Missing Count",
    #         text="Missing Count",
    #         color="Missing Count",
    #         color_continuous_scale="Oranges",
    #         title="Missing Values by Column"
    #     )

    #     # fig.update_traces(
    #     #         textposition="outside"
    #     #     )

    #     fig.update_layout(
    #             xaxis_title="Column Name",
    #             yaxis_title="Number of Missing Values",
    #             showlegend=False,
    #             template="plotly_white"
    # )
    #     st.plotly_chart(
    #         fig,
    #             use_container_width=True
    # )
    #     st.plotly_chart(fig, use_container_width=True)

    # else:
    #     st.success("✅ No missing values to visualize!")





    # ---------- After Processing ----------

    st.subheader("✅ After Processing")
    # ---------- Perform Preprocessing ----------

    rows_before = len(filtered)
    processed_data = filtered.dropna().reset_index(drop=True)
    rows_after = len(processed_data)
    rows_removed = rows_before - rows_after

    st.markdown(
        f"""
        **Data cleaning completed successfully!** 🎉

    The preprocessing removed **{rows_removed:,}** records containing
    missing values.
    The cleaned dataset now contains **{rows_after:,}**
    records ready for analysis.
    """)

    #  ---------- Cleaning Summary ----------

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Cleaned Records",f"{rows_after:,}",delta=f"{-rows_removed:,} removed")
    with col2:
        st.metric("📋 Available Columns",processed_data.shape[1])
    with col3:
        st.metric("🧹 Records Removed",f"{rows_removed:,}")



    # Show missing values again (should be all zeros)
    missing_after = get_missing_stats(processed_data)
    st.markdown("**Missing values after cleaning:**")
    if missing_after.empty:
        st.success("🎉 No missing values remaining!")
    else:
        st.dataframe(missing_after, use_container_width=True)



    # Preview of cleaned data
    st.subheader("👀 Clean Data Preview")
    with st.expander("Preview of Cleaned Data"):
        st.dataframe(processed_data.head(10), use_container_width=True)



    # ---------- Download Processed Dataset ----------

    st.markdown("---")
    st.subheader("📥 Export Cleaned Dataset")

    clean_csv = processed_data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Cleaned Vehicle Data",
        data=clean_csv,
        file_name="clean_vehicle_data.csv",
        mime="text/csv",
        use_container_width=True
    )
    df = pd.read_csv("project/clean_vehicle_data.csv")
    

    # ---------- Save Cleaned Data ----------

    st.session_state["cleaned_data"] = processed_data
    st.success("🚗 Cleaned vehicle data is ready for further analysis and visualisation!")



# elif opt == "Visualizations":
#     st.title("📊 Used Car Visualization")
#     st.markdown("""
#     Explore patterns and relationships in the used car dataset
#     through interactive charts and visual analytics.
#     """)


    
#     # ----- Load clean data (reuse from Processing if available) -----
#     if 'cleaned_data' in st.session_state:
#         plot_data = st.session_state['cleaned_data'].copy()
#     else:
#         # Fallback: clean filtered data on the fly
#         plot_data = filtered.copy()
#         cols_to_drop = ["InteriorColour"]
#         cols_exist = [c for c in cols_to_drop if c in plot_data.columns]
#         plot_data.drop(columns=cols_exist, inplace=True, errors='ignore')
#         plot_data.dropna(inplace=True)
#         plot_data.reset_index(drop=True, inplace=True)

#     if plot_data.empty:
#         st.warning("No data available after cleaning. Please check your filters or the Processing page.")
#     else:
#         # ----- Tabs for each library -----
#         tab1, tab2, tab3, tab4, tab5 = st.tabs(["💰 Price Analysis","🚗 Vehicle Analysis","⛽ Fuel & Transmission","🔧 Engine Analysis","🔥 Correlation"])

#         with tab1:
#             st.subheader("💰 Price Analysis")
#             st.markdown("**Explore vehicle pricing patterns, brand-wise prices, "
#             "vehicle age impact, and fuel-type pricing.**")

#             st.bar_chart(plot_data, x="Kilometres", y="Price", 
#                 x_label="Kilometers", y_label="Price")
#             st.caption("**Bar Chart** –  Vehicle price according to kilometres driven.")
            






elif opt == "Visualizations":
    st.title("📊 Used Car Analytics")
    st.markdown(
        "### Interactive high-fi visualization dashboard"
    )

    # ---------- Load clean data ----------
    if "cleaned_data" in st.session_state:
        plot_data = st.session_state["cleaned_data"].copy()
    else:
        plot_data = filtered.copy()
        plot_data = plot_data.dropna().reset_index(drop=True)

    if plot_data.empty:
        st.warning("No data available for visualization. Please check your filters.")
    else:
        # ---------- High-fi styling ----------
        st.markdown("""
        <style>
        .viz-header {
            padding: 18px 22px;
            border-radius: 16px;
            background: linear-gradient(135deg, #eef6ff, #f8fbff);
            border: 1px solid #dbeafe;
            margin-bottom: 18px;
        }
        .viz-header h3 {
            margin: 0 0 5px 0;
            color: #172554;
        }
        .viz-header p {
            margin: 0;
            color: #64748b;
        }
        .insight-card {
            padding: 15px 18px;
            border-radius: 14px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            margin-top: 8px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="viz-header">
            <h3>🚘 Market Intelligence</h3>
            <p>Explore pricing, vehicle characteristics and relationships using interactive charts.</p>
        </div>
        """, unsafe_allow_html=True)

        # ---------- KPI row ----------
        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.metric("🚗 Vehicles", f"{len(plot_data):,}")
        with k2:
            st.metric("💰 Average Price", f"${plot_data['Price'].mean():,.0f}")
        with k3:
            st.metric("🛣️ Avg Kilometres", f"{plot_data['Kilometres'].mean():,.0f}")
        with k4:
            st.metric("📅 Avg Vehicle Age", f"{plot_data['VehicleAge'].mean():.1f} yrs")

        st.markdown("---")

        # ---------- Chart controls ----------
        st.subheader("🎛️ Explore Visualizations")

        chart_choice = st.selectbox(
            "Choose an analysis",
            [
                "💰 Price Distribution",
                "🏷️ Average Price by Brand",
                "🛣️ Price vs Kilometres",
                "📅 Price vs Vehicle Age",
                "⛽ Average Price by Fuel Type",
                "⚙️ Average Price by Transmission",
                "🚙 Average Price by Body Type",
                "🔧 Engine Size vs Price",
                "🔥 Correlation Heatmap"
            ]
        )





        #  # ---------- Price Distribution ----------
        if chart_choice == "💰 Price Distribution":
            fig = px.histogram(
                plot_data,
                x="Price",
                nbins=30,
                title="Vehicle Price Distribution",
                labels={"Price": "Price"},
                template="plotly_white"
            )
            fig.update_layout(height=480, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)


            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> This chart shows how used-car prices are distributed and helps identify common price ranges and unusually expensive vehicles.</div>',
                unsafe_allow_html=True
            )





             # ---------- Brand ----------
        elif chart_choice == "🏷️ Average Price by Brand":
            brand_price = (
                plot_data.groupby("Brand", as_index=False)["Price"]
                .mean()
                .sort_values("Price", ascending=False)
                .head(15)
            )
            fig = px.bar(
                brand_price,
                x="Price",
                y="Brand",
                orientation="h",
                text_auto=".0f",
                title="Top 15 Brands by Average Price",
                labels={"Price": "Average Price", "Brand": "Brand"},
                template="plotly_white"
            )
            fig.update_layout(height=560, title_x=0.02, yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> Brand-level comparison highlights which manufacturers command higher average used-car prices.</div>',
                unsafe_allow_html=True
            )

        # ---------- Mileage ----------
        elif chart_choice == "🛣️ Price vs Kilometres":
            fig = px.scatter(
                plot_data,
                x="Kilometres",
                y="Price",
                hover_data=["Brand", "Model", "VehicleAge"],
                title="Price vs Kilometres",
                labels={"Kilometres": "Kilometres Driven", "Price": "Price"},
                template="plotly_white"
            )
            fig.update_layout(height=520, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> The scatter plot helps examine whether higher mileage is associated with lower vehicle prices.</div>',
                unsafe_allow_html=True
            )

        # ---------- Age ----------
        elif chart_choice == "📅 Price vs Vehicle Age":
            age_price = (
                plot_data.groupby("VehicleAge", as_index=False)["Price"]
                .mean()
                .sort_values("VehicleAge")
            )
            fig = px.line(
                age_price,
                x="VehicleAge",
                y="Price",
                markers=True,
                title="Average Price by Vehicle Age",
                labels={"VehicleAge": "Vehicle Age (Years)", "Price": "Average Price"},
                template="plotly_white"
            )
            fig.update_layout(height=500, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> This trend shows how average vehicle value changes as cars become older.</div>',
                unsafe_allow_html=True
            )

        # ---------- Fuel ----------
        elif chart_choice == "⛽ Average Price by Fuel Type":
            fuel_price = (
                plot_data.groupby("FuelType", as_index=False)["Price"]
                .mean()
                .sort_values("Price", ascending=False)
            )
            fig = px.bar(
                fuel_price,
                x="FuelType",
                y="Price",
                text_auto=".0f",
                title="Average Price by Fuel Type",
                labels={"FuelType": "Fuel Type", "Price": "Average Price"},
                template="plotly_white"
            )
            fig.update_layout(height=480, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> Fuel-type comparison reveals differences in average pricing across vehicle technologies.</div>',
                unsafe_allow_html=True
            )

        # ---------- Transmission ----------
        elif chart_choice == "⚙️ Average Price by Transmission":
            trans_price = (
                plot_data.groupby("Transmission", as_index=False)["Price"]
                .mean()
                .sort_values("Price", ascending=False)
            )
            fig = px.bar(
                trans_price,
                x="Transmission",
                y="Price",
                text_auto=".0f",
                title="Average Price by Transmission",
                labels={"Transmission": "Transmission", "Price": "Average Price"},
                template="plotly_white"
            )
            fig.update_layout(height=480, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> This comparison shows how average used-car prices differ between transmission types.</div>',
                unsafe_allow_html=True
            )

        # ---------- Body Type ----------
        elif chart_choice == "🚙 Average Price by Body Type":
            body_price = (
                plot_data.groupby("BodyType", as_index=False)["Price"]
                .mean()
                .sort_values("Price", ascending=False)
            )
            fig = px.bar(
                body_price,
                x="BodyType",
                y="Price",
                text_auto=".0f",
                title="Average Price by Body Type",
                labels={"BodyType": "Body Type", "Price": "Average Price"},
                template="plotly_white"
            )
            fig.update_layout(height=480, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> Body-type analysis helps compare pricing patterns across different vehicle categories.</div>',
                unsafe_allow_html=True
            )

        # ---------- Engine ----------
        elif chart_choice == "🔧 Engine Size vs Price":
            fig = px.scatter(
                plot_data,
                x="EngineSizeL",
                y="Price",
                hover_data=["Brand", "Model", "FuelType"],
                title="Engine Size vs Price",
                labels={"EngineSizeL": "Engine Size (L)", "Price": "Price"},
                template="plotly_white"
            )
            fig.update_layout(height=520, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> This relationship helps evaluate whether engine size is associated with vehicle price.</div>',
                unsafe_allow_html=True
            )

        # ---------- Correlation ----------
        elif chart_choice == "🔥 Correlation Heatmap":
            numeric_data = plot_data.select_dtypes(include="number")
            corr = numeric_data.corr()

            fig = px.imshow(
                corr,
                text_auto=".2f",
                aspect="auto",
                title="Numeric Feature Correlation Matrix",
                color_continuous_scale="RdBu_r",
                zmin=-1,
                zmax=1
            )
            fig.update_layout(height=620, title_x=0.02)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '<div class="insight-card">💡 <b>Insight:</b> Correlation values close to +1 or -1 indicate stronger positive or negative linear relationships between numeric features.</div>',
                unsafe_allow_html=True
            )














elif opt == "About":

    st.title("ℹ️ About Used Car Analysis")
    st.markdown("---")

    # ---------- Project Introduction ----------
    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("""
        ### 🚗 Used Car Analysis Dashboard

        This interactive dashboard is designed to explore and analyse
        used car data through **data preprocessing, statistics, and
        interactive visualisations**.

        ### ✨ What You Can Explore

        - 🧾 **Dataset Overview** – Explore the available vehicle data.
        - 🧹 **Data Preprocessing** – Understand how the data is cleaned.
        - 📊 **Visualisation** – Discover patterns and relationships.
        - 🔎 **Interactive Analysis** – Filter and explore vehicles easily.
        - 📈 **Statistical Insights** – Analyse prices, mileage, age,
          brands, fuel types, and other features.

        ### 🎯 Project Objectives

        - Understand used car market characteristics.
        - Analyse factors affecting vehicle prices.
        - Compare different brands, fuel types, and transmissions.
        - Identify useful patterns from vehicle age and kilometres.
        - Present data insights in an easy-to-understand dashboard.

        ---
        ### 🛠️ Technologies Used

        - 🐍 **Python** – Programming and data analysis
        - 🖥️ **Streamlit** – Interactive dashboard
        - 🐼 **Pandas** – Data cleaning and manipulation
        - 📊 **Plotly** – Interactive visualisations
        - 🔢 **NumPy** – Numerical operations
        """)

    with col2:

        st.markdown("""
        ### 📁 Dataset Information

        **Dataset:** Used Vehicle Dataset

        **Main information includes:**

        - 🚘 Brand & Model
        - 📅 Year & Vehicle Age
        - ⚙️ Transmission
        - ⛽ Fuel Type
        - 🔧 Engine Size
        - 🛣️ Kilometres
        - 🚙 Body Type
        - 📍 State
        - 💰 Price
        - 📈 Price Per Year Age
        """)

        st.info("""
        💡 **Dashboard Purpose**

        To transform raw used-car data into meaningful
        insights using data analytics and visualisation.
        """)

    st.markdown("---")

    # ---------- Project Workflow ----------

    st.subheader("🔄 Project Workflow")

    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.markdown("""
        ### 1️⃣ Dataset
        Explore the structure and contents of the vehicle dataset.
        """)

    with step2:
        st.markdown("""
        ### 2️⃣ Preprocessing
        Clean the data and prepare it for analysis.
        """)

    with step3:
        st.markdown("""
        ### 3️⃣ Analysis
        Find patterns and relationships between vehicle features.
        """)

    with step4:
        st.markdown("""
        ### 4️⃣ Visualisation
        Present insights using interactive charts.
        """)

    st.markdown("---")

    # ---------- Developer ----------

    st.markdown("""
    ### 👨‍💻 Project Developed By

    **Harteek**

    🎓 Data Analytics / Python Project

    *Built with Python, Pandas, Plotly and Streamlit.* 🚗📊
    """)