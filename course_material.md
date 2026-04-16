# Course Reference Material — Financial Diagnosis (Balance Sheet Only)

This file contains the formulas, thresholds, and interpretations from the course that are applicable to Balance Sheet data only.

---

## 1. Structural Balances (WC / WCN / NC)

### Formulas
- Working Capital (WC) = Shareholders' Equity + Long-Term Liabilities – Fixed Assets (Total Non-Current Assets)
- Working Capital Need (WCN) = Current Assets (excluding Cash) – Current Liabilities (excluding short-term bank loans and overdraft)
  - Specifically: (Inventories + Accounts Receivable + Other Current Assets) – (Accounts Payable + Other Current Liabilities)
- Net Cash (NC) = WC – WCN
  - Verification: Cash and Cash Equivalents – Borrowings Current – Bank Overdraft
- Net Debt = Long-Term Debt + Short-Term Financial Debt – Cash and Cash Equivalents
- Capital Employed = Fixed Assets + WCN
- Invested Capital = Shareholders' Equity + Net Debt
- Note: Capital Employed should equal Invested Capital (any gap comes from Other Non-Current Liabilities)

### Scenario Classification (6 Cases)

Case 1 — Ideal Situation: WC > 0, WCN > 0, NC > 0
Interpretation: Healthy manufacturing cycle. Long-term resources safely cover fixed assets, and the firm still has extra cash left over to fund day-to-day operations.

Case 2 — Risky but Common: WC > 0, WCN > 0, NC < 0
Interpretation: Financially stable long-term, but facing short-term liquidity tension. The operating cycle is too heavy and creates cash pressure (needs short-term bank loans).

Case 3 — Excellent / Comfortable: WC > 0, WCN < 0, NC > 0
Interpretation: Perfect situation (often seen in retail). The company generates cash through its daily operations (negative WCN), is solid long-term, and holds excess liquidity.

Case 4 — Paradoxical: WC < 0, WCN < 0, NC > 0
Interpretation: Risky financial structure (fixed assets financed by short-term debt), but the business model generates so much daily cash that it survives. If activity slows, liquidity becomes a massive problem.

Case 5 — Risky: WC < 0, WCN < 0, NC < 0
Interpretation: Bad financial structure combined with cash consumption. The firm is under extreme financial tension and relies too heavily on short-term debt.

Case 6 — Dangerous / Strong Risks: WC < 0, WCN > 0, NC < 0
Interpretation: The absolute worst situation. Weak financial structure, a cash-consuming operating cycle, and severe liquidity distress. High risk of bankruptcy.

---

## 2. Liquidity Ratios (Short-Term)

Current Ratio = Current Assets / Current Liabilities
- < 1: Potential liquidity concern (risk of not paying short-term debt)
- 1.5 to 2: Healthy and safe
- > 3: Inefficiency (too much working capital tied up in unused cash or inventory)

Quick Ratio = (Current Assets - Inventory) / Current Liabilities
- < 1: Possible liquidity risk (heavily dependent on selling inventory)
- 1 to 1.5: Strong, safe liquidity
- > 2: Very conservative (could mean under-investing in growth)

Cash Ratio = Cash and Cash Equivalents / Current Liabilities
- < 0.5: Not necessarily bad, but shows reliance on inventory/receivables to pay debts
- 0.5 to 1: Considered ideal
- > 1: Extremely conservative

---

## 3. Solvency & Leverage Ratios (Long-Term)

Equity Multiplier (EM) = Total Assets / Shareholders' Equity
- Measures financial leverage aggressiveness. Higher EM = more leveraged.

Total Debt Ratio (TDR) = Total Debt / Total Assets
- 0.2 to 0.4: Good / Low debt
- 0.4 to 0.6: Acceptable for most industries
- > 0.6: High debt load
- > 0.8: Very high leverage (warning signal)

Debt-to-Equity (D/E) = Total Debt / Total Shareholders' Equity
- 0.5 to 1: Healthy, balanced structure
- 1 to 1.5: Acceptable leverage
- > 1.5: High leverage (solvency problems)

---

## 4. Trend Forecasting

When projecting financial data, use linear regression: y_hat = a*t + b
- Coefficient of Determination (R²): Measures how well the trend line explains the data
- If R² is near 1, the trend line is reliable for forecasting
- If R² is low, data is heavily influenced by other factors and the projection is unreliable
- With only 4 annual data points, treat any projection as indicative only
