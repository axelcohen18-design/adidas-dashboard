# PROMPT FOR CLAUDE CODE — Adidas Financial Dashboard

## What to build

Create a **Streamlit + Plotly** financial analysis dashboard for Adidas from scratch. Single `app.py` file. The data source is `Easy-to-use simplified balance sheet Financial diagnosis_Adidas.xlsx` located in this project folder. The course reference material with all formulas, thresholds, and interpretations is in `course_material.md` in this folder — read it carefully before coding.

---

## Data source

The Excel file has one sheet called **"Balance Sheet"** with 24 rows × 4 years (2021–2024). Values are in **thousands of euros (€K)**. Display everything in **millions (€M)** in the dashboard.

The 24 balance sheet line items are:
Intangible assets, PP&E, Other non-current assets, Total non-current assets, Inventories, Accounts receivable, Other current assets, Cash and cash equivalents, Total current assets, Total assets, Issued share capital, Capital & Other reserves, Equity portion of convertible debt, Retained earnings, Total equity, Borrowings non-current, Other non-current liabilities, Total non-current liabilities, Accounts payable, Bank overdraft, Borrowings current, Other current liabilities, Total current liabilities, Total equity and liabilities.

**IMPORTANT**: Only compute and display ratios/metrics that are fully computable from this Balance Sheet data. Do NOT show any ratio that requires Income Statement data (Sales, COGS, EBIT, EBITDA, Net Income, Interest Expense), Cash Flow Statement data, or Market Data (share price, shares outstanding, dividends). If a ratio needs any of those, exclude it entirely.

---

## Computable metrics (exhaustive list — compute ALL of these)

### Structural Aggregates
- **Working Capital (WC)** = Total Equity + Total Non-Current Liabilities − Total Non-Current Assets
- **Working Capital Need (WCN)** = (Inventories + Accounts Receivable + Other Current Assets) − (Accounts Payable + Other Current Liabilities)
- **Net Cash (NC)** = WC − WCN (verify: Cash − Borrowings Current − Bank Overdraft)
- **Net Debt** = Borrowings Non-Current + Borrowings Current − Cash and Cash Equivalents
- **Capital Employed** = Total Non-Current Assets + WCN
- **Invested Capital** = Total Equity + Net Debt

### Liquidity Ratios (Short-Term)
- **Current Ratio** = Total Current Assets / Total Current Liabilities
- **Quick Ratio** = (Total Current Assets − Inventories) / Total Current Liabilities
- **Cash Ratio** = Cash and Cash Equivalents / Total Current Liabilities

### Solvency & Leverage Ratios (Long-Term)
- **Equity Multiplier** = Total Assets / Total Equity
- **Total Debt Ratio** = (Borrowings Non-Current + Borrowings Current) / Total Assets
- **Debt-to-Equity** = (Borrowings Non-Current + Borrowings Current) / Total Equity

### Structural Percentages
- Each balance sheet line item as a % of Total Assets (asset side) or % of Total Equity & Liabilities (liability side)
- Non-Current Assets % vs Current Assets %
- Equity % vs NCL % vs CL %

### Year-over-Year Growth
- YoY % change for every raw line item AND every computed aggregate (WC, WCN, NC, Net Debt, etc.)

---

## WC/WCN/NC Scenario Classification

For each year, classify Adidas into one of these 6 scenarios based on the signs of WC, WCN, and NC:

| Case | WC | WCN | NC | Label | Interpretation |
|------|-----|------|-----|-------|----------------|
| 1 | >0 | >0 | >0 | Ideal | Healthy cycle. Long-term resources cover fixed assets with extra cash for operations. |
| 2 | >0 | >0 | <0 | Risky but Common | Stable long-term, but short-term liquidity tension. Operating cycle too heavy, needs short-term bank loans. |
| 3 | >0 | <0 | >0 | Excellent | Perfect situation (common in retail). Negative WCN means operations generate cash. Solid long-term, excess liquidity. |
| 4 | <0 | <0 | >0 | Paradoxical | Risky structure (fixed assets financed by short-term debt), but business generates enough daily cash to survive. If activity slows, massive liquidity problem. |
| 5 | <0 | <0 | <0 | Risky | Bad structure + cash consumption. Extreme financial tension, over-reliant on short-term debt. |
| 6 | <0 | >0 | <0 | Dangerous | Worst situation. Weak structure, cash-consuming operating cycle, severe liquidity distress. High bankruptcy risk. |

Display which case Adidas falls into each year with a prominent visual indicator (color + icon + label + the full interpretation text from above).

---

## Interpretation thresholds (display these for EVERY ratio)

Each ratio must have a **dedicated interpretation panel** showing: the formula, the computed value, the threshold ranges from the course, and a plain-English verdict for Adidas. Use the exact thresholds below:

**Current Ratio**: <1 = Liquidity concern (🔴), 1.5–2 = Healthy (🟢), >3 = Inefficient (🟡)
**Quick Ratio**: <1 = Liquidity risk (🔴), 1–1.5 = Strong (🟢), >2 = Very conservative (🟡)
**Cash Ratio**: <0.5 = Reliance on inventory/receivables (🟡), 0.5–1 = Ideal (🟢), >1 = Extremely conservative (🟡)
**Equity Multiplier**: Show value + explain it measures financial leverage aggressiveness. Higher = more leveraged.
**Total Debt Ratio**: 0.2–0.4 = Low debt (🟢), 0.4–0.6 = Acceptable (🟡), >0.6 = High (🔴), >0.8 = Very high (🔴🔴)
**Debt-to-Equity**: 0.5–1 = Healthy (🟢), 1–1.5 = Acceptable (🟡), >1.5 = High leverage (🔴)

---

## Dashboard structure — Main Summary + Drill-Down Pages

Use `st.sidebar` with radio buttons or selectbox to navigate between pages:

### Page 1: Executive Summary (landing page)
- Top row: 4 columns, one per year, each showing a "health snapshot" card with the WC/WCN/NC scenario case label and color
- Second row: Key metrics at a glance for the most recent year (2024): WC, Net Cash, Current Ratio, D/E — each as a color-coded card with the traffic light verdict
- Third row: A single multi-line chart showing the evolution of WC, WCN, and Net Cash across all 4 years
- Fourth row: A summary table of ALL computed ratios across all years with color-coded cells

### Page 2: Balance Sheet Explorer
- Full balance sheet table in €M with conditional formatting
- Stacked bar charts: Asset composition + Equity & Liabilities composition across years
- Structural % breakdown (pie or stacked 100% bar)

### Page 3: Structural Aggregates (WC / WCN / NC)
- Detailed cards for WC, WCN, NC, Net Debt, Capital Employed, Invested Capital per year
- The scenario classification panel (which case each year, with full interpretation text)
- Grouped bar chart comparing all aggregates across years
- Formula box showing exactly how each aggregate is computed

### Page 4: Liquidity Analysis
- Current Ratio, Quick Ratio, Cash Ratio — each with:
  - A large metric card showing the value + color verdict
  - The interpretation panel (formula + thresholds + what it means for Adidas)
  - A line/bar chart showing evolution across years with threshold reference lines drawn on the chart (e.g., horizontal dashed lines at 1.0, 1.5, 2.0 for Current Ratio)
- Comparative chart of all three ratios together

### Page 5: Solvency & Leverage
- Same layout as Page 4 but for: Equity Multiplier, Total Debt Ratio, D/E
- Each with interpretation panel + threshold reference lines on charts

### Page 6: Interactive Comparison Tool
- **Year selector**: Multi-select checkboxes to pick which years to display (default: all 4)
- **Metric selector**: Dropdown or multi-select to pick specific ratios/aggregates to compare
- **Output**: A dynamic chart + table that updates based on selection
- Include YoY delta calculations between selected years (show as % change with green ↑ / red ↓ arrows)

### Page 7 (optional — include only if it looks good): Trend & Forecast
- Linear regression trend line on key metrics (WC, Net Cash, Current Ratio) using only the 4 data points
- Show R² value
- Project 1 year forward (2025 estimate) with a clear "projection" label
- If R² is too low (<0.5), show a note saying the trend is unreliable

---

## Visual design — Dark Adidas theme

- **Background**: Dark grey/black (#0d1117 or #1a1a2e)
- **Cards**: Slightly lighter dark (#161b22 or #1e1e2e) with subtle border
- **Text**: White (#ffffff) for primary, grey (#8b949e) for secondary
- **Accent colors**: Adidas blue (#004B87), green (#00A651) for good, orange (#FF6B00) for warning, red (#E31937) for danger
- **Charts**: Dark background, white gridlines, use the accent palette for data series
- **Font**: Clean sans-serif
- Apply consistent custom CSS via `st.markdown()` with `unsafe_allow_html=True`
- `st.set_page_config(layout="wide", page_title="Adidas Financial Dashboard", page_icon="👟")`

---

## Code quality requirements

- Single `app.py` file, well-commented with section headers
- Use `@st.cache_data` for data loading
- All values displayed in €M (divide by 1000), formatted as `€X.XM`
- Ratios formatted to 2 decimal places
- Percentages formatted with 1 decimal + % sign
- Every chart must have clear titles, axis labels, and legends
- Every Plotly chart should use `template="plotly_dark"` to match the dark theme
- Responsive layout using `st.columns()` throughout
- No hardcoded data — everything reads from the Excel file dynamically

---

## What NOT to include

Do NOT compute or display any of these (they require data we don't have):
- ROE, ROS, Net Profit Margin, Gross Margin, EBITDA Margin, Operating Margin (need Income Statement)
- DSO, DIO, DPO, CCC, Asset Turnover, PPE Turnover (need Sales/COGS)
- Interest Coverage Ratio, Net Debt/EBITDA (need EBIT/EBITDA)
- EPS, P/E, P/B, Dividend Payout, Dividend Yield (need market data)
- CFO, CFI, FCF, CFF, TCF (need Cash Flow Statement)
- Seasonal decomposition (need sub-annual data)
- DuPont decomposition (needs Net Income and Sales)
- Added Value, EBITDA, EBIT, EBT calculations (need Income Statement lines)

Do NOT include a tab or section listing "non-computable metrics." Just exclude them silently.
