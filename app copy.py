import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide", page_title="Adidas Financial Dashboard", page_icon="👟", initial_sidebar_state="expanded")

BG=     "#0d1117"; CARD="#161b22"; BORDER="#30363d"; TXT="#e6edf3"; TXT2="#8b949e"
BLUE=   "#004B87"; GREEN="#00A651"; ORANGE="#FF6B00"; RED="#E31937"; GOLD="#FFB800"
PAL=    [BLUE, GREEN, ORANGE, RED, GOLD, "#9B59B6"]

Y = [2021,2022,2023,2024,2025,"2026E"]
YH= [2021,2022,2023,2024,2025]

REVENUE   ={2021:21234,2022:22511,2023:21427,2024:23683,2025:24811}
GROSS_P   ={2021:10765,2022:10644,2023:10183,2024:12025,2025:12804}
EBITDA_V  ={2021: 3066,2022: 1874,2023: 1358,2024: 2465,2025: 3124}
DA_V      ={2021: -1115,2022:-1371,2023:-1170,2024:-1180,2025:-1135}
EBIT_V    ={2021: 1989,2022:  669,2023:  268,2024: 1337,2025: 2060}
NET_FIN   ={2021:  -96,2022: -115,2023:  -83,2024: -122,2025: -158}
EBT_V     ={2021: 1813,2022:  388,2023:   65,2024: 1121,2025: 1820}
TAX_V     ={2021: -471,2022: -134,2023: -124,2024: -297,2025: -443}
NET_INC   ={2021: 2116,2022:  612,2023:  -75,2024:  764,2025: 1340}
COGS_V    ={2021:10469,2022:11867,2023:11244,2024:11658,2025:12007}
MKTG_V    ={2021: 2082,2022: 2430,2023: 2528,2024: 2841,2025: 3079}
DISTR_V   ={2021: 3943,2022: 4384,2023: 4521,2024: 5002,2025: 4948}
GA_V      ={2021: 1474,2022: 1651,2023: 1839,2024: 2138,2025: 1885}
FIN_INC_V ={2021:   76,2022:  109,2023:  127,2024:  102,2025:  131}
FIN_EXP_V ={2021:  172,2022:  224,2023:  210,2024:  224,2025:  289}

BS = {
    "Intangible assets":   {2021:1581,2022:1689,2023:1680,2024:1701,2025:1646},
    "PP&E":                {2021:4825,2022:4943,2023:4405,2024:4912,2025:4578},
    "Other NCA":           {2021:1787,2022:1931,2023:2126,2024:2138,2025:2062},
    "Total NCA":           {2021:8193,2022:8563,2023:8211,2024:8751,2025:8286},
    "Inventories":         {2021:4009,2022:5973,2023:4525,2024:4989,2025:5832},
    "Accounts Receivable": {2021:3015,2022:1862,2023:2903,2024:3145,2025:2634},
    "Other CA":            {2021:3092,2022:3099,2023:1161,2024:1640,2025:1893},
    "Cash":                {2021:3828,2022: 798,2023:1220,2024:2130,2025:1617},
    "Total CA":            {2021:13944,2022:11732,2023:9809,2024:11904,2025:11976},
    "Total Assets":        {2021:22137,2022:20295,2023:18020,2024:20655,2025:20262},
    "Issued Share Capital":{2021: 192,2022: 179,2023: 179,2024: 179,2025: 179},
    "Capital & Reserves":  {2021: 785,2022: 825,2023: 601,2024: 914,2025: -161},
    "Retained Earnings":   {2021:6860,2022:4347,2023:4145,2024:4775,2025:5758},
    "Total Equity":        {2021:7837,2022:5351,2023:4925,2024:5868,2025:5776},
    "Borrowings NC":       {2021:4729,2022:5289,2023:4469,2024:4410,2025:4306},
    "Other NCL":           {2021: 606,2022: 399,2023: 583,2024: 784,2025: 737},
    "Total NCL":           {2021:5335,2022:5688,2023:5052,2024:5194,2025:5043},
    "Accounts Payable":    {2021:2294,2022:2908,2023:2276,2024:3096,2025:2910},
    "Borrowings Current":  {2021: 602,2022:1170,2023:1094,2024:1177,2025:1248},
    "Other CL":            {2021:6069,2022:5179,2023:4673,2024:5320,2025:4935},
    "Total CL":            {2021:8965,2022:9257,2023:8043,2024:9593,2025:9093},
    "Total E&L":           {2021:22137,2022:20296,2023:18020,2024:20655,2025:19912},
}

CF_OP  ={2021: 3192,2022: -479,2023: 2550,2024: 2910,2025:  751}
CF_INV ={2021: -424,2022:  495,2023: -451,2024: -356,2025: -404}
CF_FIN ={2021:-2991,2022:-2963,2023:-1425,2024:-1559,2025:-1103}
CF_FX  ={2021: -135,2022:  -56,2023:  -43,2024: -131,2025:  -81}
CAPEX  ={2021: -667,2022: -695,2023: -504,2024: -540,2025: -477}
CF_NET ={2021: 2633,2022:  -40,2023: 2056,2024: 2423,2025:  266}
FCF    ={yr: CF_OP[yr]+CAPEX[yr] for yr in YH}

CF_DET = {
    "Net Income":            {2021: 2116,2022:  612,2023:  -75,2024:  764,2025: 1340},
    "D&A":                   {2021: 1115,2022: 1371,2023: 1170,2024: 1180,2025: 1135},
    "Delta Inventories":     {2021: -738,2022:-1964,2023: 1497,2024:  627,2025: -470},
    "Delta Accts Receivable":{2021: -406,2022: 1153,2023: 1153,2024: -248,2025: -242},
    "Delta Payables & Other":{2021: 1136,2022:-2054,2023:-1148,2024:  640,2025:  100},
    "Income Tax Paid":       {2021: -555,2022: -423,2023: -297,2024: -394,2025: -352},
    "Other Adjustments":     {2021:  524,2022:-1224,2023:  250,2024:  341,2025:    0},
    "Net Operating CF":      {2021: 3192,2022: -479,2023: 2550,2024: 2910,2025:  751},
    "Capex":                 {2021: -667,2022: -695,2023: -504,2024: -540,2025: -477},
    "Other Investing":       {2021:  243,2022: 1190,2023:   53,2024:  184,2025:   73},
    "Net Investing CF":      {2021: -424,2022:  495,2023: -451,2024: -356,2025: -404},
    "Lease Repayments":      {2021: -916,2022: -944,2023: -842,2024: -880,2025:-1056},
    "Dividends Paid":        {2021: -400,2022: -486,2023:    0,2024: -100,2025: -140},
    "Share Buybacks":        {2021:-1032,2022:-2530,2023:  -29,2024:  -35,2025:  -43},
    "Other Financing":       {2021: -643,2022:    3,2023: -554,2024: -544,2025:  136},
    "Net Financing CF":      {2021:-2991,2022:-2963,2023:-1425,2024:-1559,2025:-1103},
    "FX Effects":            {2021: -135,2022:  -56,2023:  -43,2024: -131,2025:  -81},
    "Net Change in Cash":    {2021: 2633,2022:  -40,2023: 2056,2024: 2423,2025:  266},
}

ROE    ={2021:0.2700,2022:0.1144,2023:-0.0152,2024:0.1302,2025:0.2320}
ROS    ={2021:0.0997,2022:0.0272,2023:-0.0035,2024:0.0323,2025:0.0540}
AT_R   ={2021:0.9592,2022:1.1092,2023:1.1891,2024:1.1466,2025:1.2245}
EM_R   ={2021:2.8247,2022:3.7927,2023:3.6589,2024:3.5199,2025:3.5080}
GPM    ={2021:0.5070,2022:0.4728,2023:0.4752,2024:0.5077,2025:0.5161}
EBITDAM={2021:0.1444,2022:0.0832,2023:0.0634,2024:0.1041,2025:0.1259}
EBITM  ={2021:0.0937,2022:0.0297,2023:0.0125,2024:0.0565,2025:0.0830}
DSO    ={2021:51.83,2022:30.19,2023:49.45,2024:48.47,2025:38.75}
DIO    ={2021:139.77,2022:183.71,2023:146.89,2024:156.20,2025:177.29}
DPO    ={2021:79.98,2022:89.44,2023:73.88,2024:96.93,2025:88.46}
CCC    ={2021:111.62,2022:124.46,2023:122.46,2024:107.74,2025:127.58}
PPET   ={2021:4.40,2022:4.55,2023:4.86,2024:4.82,2025:5.42}
CR     ={2021:1.555,2022:1.267,2023:1.220,2024:1.241,2025:1.317}
QR     ={2021:1.108,2022:0.622,2023:0.657,2024:0.721,2025:0.676}
CASHR  ={2021:0.427,2022:0.086,2023:0.152,2024:0.222,2025:0.178}
DE     ={2021:0.758,2022:1.282,2023:1.248,2024:1.086,2025:1.089}
TDR    ={2021:0.268,2022:0.338,2023:0.341,2024:0.308,2025:0.310}
IC     ={2021:11.56,2022:2.99,2023:1.28,2024:5.97,2025:7.13}
NDEBITDA={2021:0.688,2022:3.234,2023:3.627,2024:1.720,2025:1.496}
EPS    ={2021:11.85,2022:3.43,2023:-0.42,2024:4.28,2025:7.50}
PE     ={2021:26.17,2022:37.04,2023:None,2024:56.07,2025:25.73}
PB     ={2021:7.065,2022:4.236,2023:6.705,2024:7.301,2025:5.968}
DIVPAY ={2021:0.249,2022:0.964,2023:None,2024:0.164,2025:0.266}
DIVYLD ={2021:0.00950,2022:0.02600,2023:0.00379,2024:0.00292,2025:0.01036}
DPS    ={2021:2.945,2022:3.305,2023:0.700,2024:0.700,2025:1.999}
PRICE  ={2021:310,2022:127,2023:185,2024:240,2025:193}
WC     ={2021:4979,2022:2476,2023:1766,2024:2311,2025:2533}
WCN    ={2021:1753,2022:2847,2023:1640,2024:1358,2025:2514}
NC_SFS ={2021:3226,2022:-371,2023:126,2024:953,2025:19}
NETDBT ={2021:2109,2022:6060,2023:4926,2024:4241,2025:4674}

# 2026E forecast
REV26   = round(REVENUE[2025]*1.076)
GP26    = round(REV26*0.520)
EBITDA26= round(REV26*0.135)
EBIT26  = EBITDA26-1135
NI26    = round((EBIT26-175)*0.75)
EPS26   = round(NI26/178.6,2)

for d,v in [(REVENUE,REV26),(GROSS_P,GP26),(EBITDA_V,EBITDA26),(EBIT_V,EBIT26),(NET_INC,NI26)]:
    d["2026E"]=v
ROE["2026E"]=round(NI26/6100,4); ROS["2026E"]=round(NI26/REV26,4)
GPM["2026E"]=0.520; EBITDAM["2026E"]=0.135; EBITM["2026E"]=round(EBIT26/REV26,4)
AT_R["2026E"]=1.28; EM_R["2026E"]=3.25
DSO["2026E"]=36.0; DIO["2026E"]=165.0; DPO["2026E"]=90.0; CCC["2026E"]=111.0
PPET["2026E"]=5.6; CR["2026E"]=1.35; QR["2026E"]=0.72; CASHR["2026E"]=0.19
DE["2026E"]=1.00; TDR["2026E"]=0.29; IC["2026E"]=8.5; NDEBITDA["2026E"]=1.2
EPS["2026E"]=EPS26; PE["2026E"]=None; PB["2026E"]=None
DIVPAY["2026E"]=0.25; DIVYLD["2026E"]=None; DPS["2026E"]=round(EPS26*0.25,2)
WC["2026E"]=2800; WCN["2026E"]=2300; NC_SFS["2026E"]=500; NETDBT["2026E"]=4000

# ── HELPERS ───────────────────────────────────────────────────────────────────
def fm(v):   return f"€{v:,.0f}M"
def fp(v):   return f"{v*100:.1f}%" if v is not None else "N/A"
def fx(v):   return f"{v:.2f}x" if v is not None else "N/A"
def fd(v):   return f"{v:.1f}d"

def color_roe(v):
    if v is None: return TXT2
    return GREEN if v>0.15 else ORANGE if v>0 else RED

def color_m(v,lo,hi):
    if v is None: return TXT2
    return GREEN if v>=hi else ORANGE if v>=lo else RED

def yoy(d,yr):
    avail=[y for y in Y if y in d]
    idx=avail.index(yr) if yr in avail else -1
    if idx<=0: return None
    p=d[avail[idx-1]]; c=d[yr]
    if not p or not c: return None
    return (c-p)/abs(p)

def dark_fig(fig,h=350):
    fig.update_layout(
        template="plotly_dark",paper_bgcolor=BG,plot_bgcolor=BG,
        font=dict(family="sans-serif",color=TXT,size=12),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        margin=dict(l=50,r=20,t=40,b=40),height=h,
    )
    fig.update_xaxes(gridcolor=BORDER,linecolor=BORDER)
    fig.update_yaxes(gridcolor=BORDER,linecolor=BORDER)
    return fig

def line_fig(data_dict,title,h=330,pres=False):
    fig=go.Figure()
    fh=h if not pres else 380
    for i,(lbl,d) in enumerate(data_dict.items()):
        xh=[str(yr) for yr in YH if yr in d and d[yr] is not None]
        yh=[d[yr] for yr in YH if yr in d and d[yr] is not None]
        xe=["2026E"] if "2026E" in d and d["2026E"] is not None else []
        ye=[d["2026E"]] if xe else []
        c=PAL[i%len(PAL)]
        if xh:
            fig.add_trace(go.Scatter(x=xh,y=yh,name=lbl,mode="lines+markers",
                line=dict(color=c,width=2.5),marker=dict(size=7)))
        if xe and xh:
            fig.add_trace(go.Scatter(x=[xh[-1],xe[0]],y=[yh[-1],ye[0]],
                name=f"{lbl} (est.)",line=dict(color=c,width=2,dash="dot"),
                marker=dict(size=8,symbol="diamond"),showlegend=True))
    fig.update_layout(title=dict(text=title,font=dict(size=13 if not pres else 16,color=TXT2)))
    return dark_fig(fig,fh)

def bar_fig(data_dict,title,h=300,stack=False,pres=False):
    fig=go.Figure()
    fh=h if not pres else 380
    for i,(lbl,d) in enumerate(data_dict.items()):
        xs=[str(yr) for yr in Y if yr in d and d[yr] is not None]
        ys=[d[yr] for yr in Y if yr in d and d[yr] is not None]
        fig.add_trace(go.Bar(name=lbl,x=xs,y=ys,marker_color=PAL[i%len(PAL)]))
    bm="stack" if stack else "group"
    fig.update_layout(barmode=bm,title=dict(text=title,font=dict(size=13 if not pres else 16,color=TXT2)))
    return dark_fig(fig,fh)

def waterfall_fig(yr):
    op=CF_OP[yr]; inv=CF_INV[yr]; fin=CF_FIN[yr]; fx_=CF_FX[yr]; net=CF_NET[yr]
    lbls=["Operating CF","Investing CF","Financing CF","FX Effects","Net Change"]
    vals=[op,inv,fin,fx_,net]
    clrs=[GREEN if v>=0 else RED for v in vals]
    fig=go.Figure(go.Bar(x=lbls,y=vals,marker_color=clrs,
        text=[fm(v) for v in vals],textposition="outside",textfont=dict(color=TXT,size=11)))
    fig.add_hline(y=0,line_dash="dash",line_color=TXT2,opacity=0.4)
    fig.update_layout(title=dict(text=f"Cash Flow Waterfall {yr}",font=dict(size=13,color=TXT2)),showlegend=False)
    return dark_fig(fig,350)

def kpi(title,value,color=TXT,sub="",pres=False):
    fv="2.4rem" if pres else "1.85rem"
    ft="0.95rem" if pres else "0.78rem"
    pd_="22px 24px" if pres else "14px 16px"
    return (f'<div style="background:{CARD};border:1px solid {BORDER};border-radius:12px;'
            f'padding:{pd_};margin-bottom:10px;border-top:3px solid {color};">'
            f'<div style="font-size:{ft};color:{TXT2};font-weight:500;margin-bottom:4px;">{title}</div>'
            f'<div style="font-size:{fv};font-weight:700;color:{color};line-height:1.2;">{value}</div>'
            f'<div style="font-size:0.75rem;color:{TXT2};margin-top:4px;">{sub}</div></div>')

def ibox(text,color=BLUE):
    return (f'<div style="background:{color}18;border-left:3px solid {color};border-radius:6px;'
            f'padding:12px 16px;margin:10px 0;font-size:0.88rem;line-height:1.6;">{text}</div>')

def sec(t):
    st.markdown(f'<div style="font-size:1.1rem;font-weight:700;margin:18px 0 8px;'
                f'padding-bottom:5px;border-bottom:2px solid {BLUE};color:{TXT};">{t}</div>',
                unsafe_allow_html=True)

SCENARIOS={
    1:("Ideal","✅",GREEN,"WC>0 · WCN>0 · NC>0","Long-term resources cover fixed assets with extra cash. Healthy cycle."),
    2:("Risky but Common","⚠️",ORANGE,"WC>0 · WCN>0 · NC<0","Stable long-term, short-term liquidity tension — relies on ST bank loans."),
    3:("Excellent","🌟","#00D4AA","WC>0 · WCN<0 · NC>0","Ops self-finance and generate cash. Common in strong retail brands."),
    4:("Paradoxical","🔄",GOLD,"WC<0 · WCN<0 · NC>0","Risky structure but daily cash generation compensates. Vulnerable if activity slows."),
    5:("Risky","🔴",RED,"WC<0 · WCN<0 · NC<0","Bad structure + cash consuming ops. Over-reliant on short-term debt."),
    6:("Dangerous","💀","#FF0000","WC<0 · WCN>0 · NC<0","Worst case: weak structure + cash-consuming cycle. High bankruptcy risk."),
}

def get_sc(wc,wcn,nc):
    if wc>0 and wcn>0 and nc>0: return 1
    if wc>0 and wcn>0 and nc<0: return 2
    if wc>0 and wcn<0 and nc>0: return 3
    if wc<0 and wcn<0 and nc>0: return 4
    if wc<0 and wcn<0 and nc<0: return 5
    return 6

def css():
    st.markdown(f"""<style>
    .stApp{{background:{BG};color:{TXT};}}
    [data-testid="stSidebar"]{{background:#0a0e14;border-right:1px solid {BORDER};}}
    [data-testid="stSidebar"] *{{color:{TXT}!important;}}
    .stTabs [data-baseweb="tab"]{{color:{TXT2};font-size:.84rem;}}
    .stTabs [aria-selected="true"]{{color:{TXT}!important;border-bottom:2px solid {BLUE}!important;}}
    footer{{visibility:hidden;}}
    </style>""",unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PRESENTATION SLIDES
# ══════════════════════════════════════════════════════════════════════════════
SLIDES=[
    {"id":"overview",     "title":"📊 Overview"},
    {"id":"profitability","title":"📈 Profitability"},
    {"id":"operating",    "title":"🏭 Operating Management"},
    {"id":"investment",   "title":"🔄 Investment Management"},
    {"id":"sfs",          "title":"🏗️ Financial Structure"},
    {"id":"finmgmt",      "title":"🛡️ Financial Management"},
    {"id":"investors",    "title":"💹 Investor Ratios"},
    {"id":"statements",      "title":"📋 Full Statements"},
    {"id":"recommendations", "title":"💡 Recommendations"},
]

def slide(sid,yr,pres=True):
    if sid=="overview":
        st.markdown(f"<h2 style='color:{TXT};margin-bottom:4px;'>Adidas — Financial Overview</h2>"
                    f"<p style='color:{TXT2};font-size:1rem;margin-bottom:16px;'>FY {yr} · Key Performance Indicators</p>",
                    unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        yoy_rev=yoy(REVENUE,yr); yoy_str=f"YoY {fp(yoy_rev)}" if yoy_rev is not None else "Forecast"
        c1.markdown(kpi("Revenue",fm(REVENUE[yr]),BLUE,yoy_str,pres),unsafe_allow_html=True)
        c2.markdown(kpi("EBITDA",fm(EBITDA_V[yr]),GREEN,f"Margin {fp(EBITDAM[yr])}",pres),unsafe_allow_html=True)
        c3.markdown(kpi("Net Income",fm(NET_INC[yr]),GREEN if NET_INC[yr]>0 else RED,f"ROS {fp(ROS[yr])}",pres),unsafe_allow_html=True)
        c4.markdown(kpi("ROE",fp(ROE[yr]),color_roe(ROE[yr]),"Return on Equity",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(bar_fig({"Revenue":REVENUE,"EBITDA":EBITDA_V},"Revenue & EBITDA (€M)",pres=pres),use_container_width=True)
        with c2b:
            st.plotly_chart(line_fig({"Net Income":NET_INC},"Net Income (€M)",pres=pres),use_container_width=True)
        st.markdown(ibox(f"<b>FY {yr}:</b> Revenue {fm(REVENUE[yr])}, EBITDA margin {fp(EBITDAM[yr])}, ROE {fp(ROE[yr])}. "
            f"Strong recovery from the 2022–2023 crisis driven by Yeezy wind-down and Russia exit. "
            f"2026E projects continued revenue growth (+7.6%) and margin expansion toward 13.5% EBITDA."),
            unsafe_allow_html=True)

    elif sid=="profitability":
        st.markdown(f"<h2 style='color:{TXT};'>Profitability Analysis — FY {yr}</h2>",unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        c1.markdown(kpi("ROE",fp(ROE[yr]),color_roe(ROE[yr]),"DuPont: ROS × AT × EM",pres),unsafe_allow_html=True)
        c2.markdown(kpi("ROS (Net Margin)",fp(ROS[yr]),color_m(ROS[yr],0.03,0.06),"Net Income / Revenue",pres),unsafe_allow_html=True)
        c3.markdown(kpi("Assets Turnover",fx(AT_R[yr]),color_m(AT_R[yr],0.8,1.1),"Revenue / Total Assets",pres),unsafe_allow_html=True)
        c4.markdown(kpi("Equity Multiplier",fx(EM_R[yr]),ORANGE if EM_R[yr]>3 else GREEN,"Assets / Equity",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(line_fig({"ROE":ROE,"ROS":ROS},"ROE & ROS",pres=pres),use_container_width=True)
        with c2b:
            st.plotly_chart(line_fig({"Gross Margin":GPM,"EBITDA Margin":EBITDAM,"EBIT Margin":EBITM},
                "Profit Margins",pres=pres),use_container_width=True)
        st.markdown(ibox(
            f"<b>ROE {fp(ROE[yr])}</b> = ROS {fp(ROS[yr])} × AT {fx(AT_R[yr])} × EM {fx(EM_R[yr])}. "
            f"ROE recovered strongly from -1.5% (2023 loss year) to {fp(ROE[yr])} ({yr}). "
            f"High Equity Multiplier (~3.5×) boosts ROE but signals elevated financial leverage. "
            f"EBITDA margin {fp(EBITDAM[yr])} reflects {'solid recovery' if yr in [2024,2025,'2026E'] else 'pressure'}.",color_roe(ROE[yr])),
            unsafe_allow_html=True)

    elif sid=="operating":
        st.markdown(f"<h2 style='color:{TXT};'>Operating Management — FY {yr}</h2>",unsafe_allow_html=True)
        c1,c2,c3=st.columns(3)
        c1.markdown(kpi("Gross Profit Margin",fp(GPM[yr]),color_m(GPM[yr],0.40,0.50),"Gross Profit / Revenue",pres),unsafe_allow_html=True)
        c2.markdown(kpi("EBITDA Margin",fp(EBITDAM[yr]),color_m(EBITDAM[yr],0.08,0.12),"EBITDA / Revenue",pres),unsafe_allow_html=True)
        c3.markdown(kpi("EBIT Margin",fp(EBITM[yr]),color_m(EBITM[yr],0.05,0.10),"EBIT / Revenue",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(line_fig({"Gross Margin":GPM,"EBITDA Margin":EBITDAM,"EBIT Margin":EBITM},
                "Profit Margins",pres=pres),use_container_width=True)
        with c2b:
            st.plotly_chart(bar_fig({"Revenue":REVENUE,"EBITDA":EBITDA_V,"EBIT":EBIT_V},"P&L Summary (€M)",pres=pres),use_container_width=True)
        st.markdown(ibox(
            f"<b>Gross Margin {fp(GPM[yr])}</b> — above 50%, reflecting strong brand pricing power. "
            f"EBITDA Margin {fp(EBITDAM[yr])} recovering from the 6.3% low in 2023. "
            f"EBIT Margin {fp(EBITM[yr])} shows {'operational recovery' if EBITM[yr]>0.05 else 'margin pressure'}. "
            f"Key cost drivers: Distribution ({fp(DISTR_V[yr]/REVENUE[yr])} of revenue) and Marketing ({fp(MKTG_V[yr]/REVENUE[yr])}).",GREEN),
            unsafe_allow_html=True)
        fs_body="0.9rem" if pres else "0.82rem"
        fs_ctx ="0.85rem" if pres else "0.78rem"
        st.markdown(f"<div style='font-size:{'1.1rem' if pres else '1.0rem'};font-weight:700;margin:24px 0 12px;padding-bottom:5px;border-bottom:2px solid {GOLD};color:{TXT};'>📝 Key Takeaways</div>",unsafe_allow_html=True)
        KT_OP=[
            (RED,"2023 Low Point",
             "The crisis year crystallised in two headline figures:",
             ["Revenue dip of −4.8% vs. 2022",
              "EBIT crashed 86.5% vs. 2021 — reflecting both volume and margin destruction"]),
            (GREEN,"Margin Restoration (FY 2025)",
             "All three margin lines recovered meaningfully:",
             ["Gross Margin: 51.6% — back above the 50% threshold, reflecting brand pricing power",
              "EBITDA Margin: 12.6% — significant recovery from ~6% in 2023",
              "EBIT Margin: 8.3% — up from ~1% in 2023"]),
        ]
        kt_cols=st.columns(2)
        for i,(color,title,context,bullets) in enumerate(KT_OP):
            with kt_cols[i%2]:
                bl="".join(f"<li style='margin-bottom:5px;'>{b}</li>" for b in bullets)
                ul=f"<ul style='margin:8px 0 0;padding-left:18px;font-size:{fs_body};color:{TXT};line-height:1.7;'>{bl}</ul>"
                st.markdown(f"<div style='background:{color}14;border:1px solid {color}45;border-left:4px solid {color};border-radius:10px;padding:18px 20px;margin-bottom:14px;'><div style='font-weight:700;color:{color};font-size:{fs_body};margin-bottom:6px;'>{title}</div><div style='font-size:{fs_ctx};color:{TXT2};line-height:1.6;'>{context}</div>{ul}</div>",unsafe_allow_html=True)
        st.markdown(
            f"<p style='font-size:{fs_body};color:{GOLD};font-weight:600;margin:14px 0 6px;'>🟡 Growth Outlook — </p>"
            f"<p style='font-size:{fs_ctx};color:{TXT2};margin:0 0 6px;'>Accelerating trajectory projected for 2026E, with revenue expected to grow ~7.6% and margin expansion continuing as operational leverage kicks in.</p>"
            f"<p style='font-size:{fs_body};color:{ORANGE};font-weight:600;margin:14px 0 6px;'>🟠 Key Challenge — </p>"
            f"<p style='font-size:{fs_ctx};color:{TXT2};margin:0;'>Profit margins remain thinner than the 2021 baseline (EBIT 8.3% vs. 9.4% pre-crisis). Continuous focus on profitability improvement — particularly below the gross line — is required.</p>",
            unsafe_allow_html=True)

    elif sid=="investment":
        st.markdown(f"<h2 style='color:{TXT};'>Investment Management — FY {yr}</h2>",unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        c1.markdown(kpi("DSO",fd(DSO[yr]),GREEN if DSO[yr]<45 else ORANGE,"Days Sales Outstanding",pres),unsafe_allow_html=True)
        c2.markdown(kpi("DIO",fd(DIO[yr]),RED if DIO[yr]>170 else ORANGE if DIO[yr]>140 else GREEN,"Days Inventory Outstanding",pres),unsafe_allow_html=True)
        c3.markdown(kpi("DPO",fd(DPO[yr]),GREEN if DPO[yr]>80 else ORANGE,"Days Payable Outstanding",pres),unsafe_allow_html=True)
        c4.markdown(kpi("CCC",fd(CCC[yr]),GREEN if CCC[yr]<110 else ORANGE if CCC[yr]<130 else RED,"Cash Conversion Cycle",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(line_fig({"DSO":DSO,"DIO":DIO,"DPO":DPO,"CCC":CCC},"WC Days",pres=pres),use_container_width=True)
        with c2b:
            st.plotly_chart(line_fig({"PP&E Turnover":PPET},"PP&E Turnover (×)",pres=pres),use_container_width=True)
        st.markdown(ibox(
            f"<b>CCC {fd(CCC[yr])}</b> — Adidas needs ~{CCC[yr]:.0f} days to convert ops into cash. "
            f"DIO {fd(DIO[yr])} is {'elevated — inventory risk' if DIO[yr]>160 else 'managed'}. "
            f"DSO {fd(DSO[yr])} — {'strong improvement in collections' if yr in [2025,'2026E'] else 'needs monitoring'}. "
            f"DPO {fd(DPO[yr])} — using supplier credit {'effectively' if DPO[yr]>85 else 'moderately'}. "
            f"PP&E Turnover {fx(PPET[yr])} shows {'excellent' if PPET[yr]>5 else 'good'} fixed asset efficiency.",ORANGE),
            unsafe_allow_html=True)

    elif sid=="sfs":
        st.markdown(f"<h2 style='color:{TXT};'>Financial Structure (SFS) — FY {yr}</h2>",unsafe_allow_html=True)
        wc_v=WC.get(yr,0); wcn_v=WCN.get(yr,0); nc_v=NC_SFS.get(yr,0)
        sc=get_sc(wc_v,wcn_v,nc_v)
        sname,sico,sc_c,ssigns,sinterp=SCENARIOS[sc]
        c1,c2,c3,c4=st.columns(4)
        c1.markdown(kpi("Working Capital (WC)",fm(wc_v),GREEN if wc_v>0 else RED,"Equity+NCL−NCA",pres),unsafe_allow_html=True)
        c2.markdown(kpi("WC Need (WCN)",fm(wcn_v),GREEN if wcn_v<0 else ORANGE,"Inv+AR+OCA−AP−OCL",pres),unsafe_allow_html=True)
        c3.markdown(kpi("Net Cash (NC)",fm(nc_v),GREEN if nc_v>0 else RED,"WC − WCN",pres),unsafe_allow_html=True)
        c4.markdown(kpi("Net Debt",fm(NETDBT.get(yr,0)),
            GREEN if NETDBT.get(yr,0)<2500 else ORANGE if NETDBT.get(yr,0)<5000 else RED,
            "NCL+Borr.C−Cash",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns([3,2])
        with c1b:
            st.plotly_chart(line_fig({"WC":WC,"WCN":WCN,"NC":NC_SFS},"SFS Indicators (€M)",pres=pres),use_container_width=True)
        with c2b:
            st.markdown(f"""<div style="background:{sc_c}18;border:2px solid {sc_c};border-radius:12px;
                padding:20px 16px;margin:8px 0;">
                <div style="font-size:2rem;">{sico}</div>
                <div style="font-size:1.3rem;font-weight:700;color:{sc_c};margin:4px 0;">Case {sc}: {sname}</div>
                <div style="font-size:0.82rem;color:{TXT2};margin:6px 0;">{ssigns}</div>
                <div style="font-size:0.9rem;color:{TXT};margin-top:8px;">{sinterp}</div>
            </div>""",unsafe_allow_html=True)
        st.markdown(ibox(
            f"<b>WC {fm(wc_v)}</b> {'positive — long-term resources exceed fixed assets' if wc_v>0 else 'negative — structural imbalance'}. "
            f"<b>WCN {fm(wcn_v)}</b> — operating cycle {'requires' if wcn_v>0 else 'generates'} {fm(abs(wcn_v))} of financing. "
            f"<b>NC {fm(nc_v)}</b> {'confirms liquidity surplus' if nc_v>0 else 'signals short-term credit reliance'}.",sc_c),
            unsafe_allow_html=True)

        # ── SFS Deep-Dive Key Takeaways ──────────────────────────────────────
        st.markdown(f"<div style='font-size:1rem;font-weight:700;color:{TXT};margin:22px 0 10px;border-bottom:2px solid {GOLD};padding-bottom:5px;'>🔍 Deep-Dive Analysis</div>",unsafe_allow_html=True)
        ka1,ka2=st.columns(2)
        with ka1:
            st.markdown(f"""<div style="background:{GREEN}12;border:1px solid {GREEN}44;border-left:4px solid {GREEN};border-radius:10px;padding:16px 18px;margin-bottom:10px;">
            <div style="font-weight:700;color:{GREEN};font-size:0.92rem;margin-bottom:8px;">📗 FY 2021 — Peak Liquidity</div>
            <div style="font-size:0.83rem;color:{TXT};line-height:1.7;">
            • WC <b>€4,979M</b> — massive structural safety cushion<br>
            • WCN <b>€1,753M</b> — efficient cycle, inventory well-controlled<br>
            • NC <b>€3,226M</b> — €3.2B cash surplus, no external reliance needed<br>
            • Net Debt <b>€2,109M</b> — fully manageable against reserves
            </div></div>""",unsafe_allow_html=True)

            st.markdown(f"""<div style="background:{RED}12;border:1px solid {RED}44;border-left:4px solid {RED};border-radius:10px;padding:16px 18px;">
            <div style="font-weight:700;color:{RED};font-size:0.92rem;margin-bottom:8px;">📕 FY 2025 — The Liquidity Crunch</div>
            <div style="font-size:0.83rem;color:{TXT};line-height:1.7;">
            • WC <b>€2,533M</b> — safety net cut in half vs 2021<br>
            • WCN <b>€2,514M</b> — ⚠️ inventory glut trapping billions in cash<br>
            • NC <b>€19M</b> — the €3.2B surplus has effectively evaporated<br>
            • Net Debt <b>€4,674M</b> — doubled; external debt now funds daily ops
            </div></div>""",unsafe_allow_html=True)

        with ka2:
            st.markdown(f"""<div style="background:{ORANGE}12;border:1px solid {ORANGE}44;border-left:4px solid {ORANGE};border-radius:10px;padding:16px 18px;margin-bottom:10px;">
            <div style="font-weight:700;color:{ORANGE};font-size:0.92rem;margin-bottom:8px;">✂️ The Scissor Effect (2021 → 2025)</div>
            <div style="font-size:0.83rem;color:{TXT};line-height:1.7;">
            • Working Capital: <b style="color:{RED};">−49.1%</b> — stable resources shrinking<br>
            • WC Need: <b style="color:{RED};">+43.4%</b> — operational requirements surging<br>
            • Net Cash: <b style="color:{RED};">−99.4%</b> — surplus effectively wiped out<br>
            • Net Debt: <b style="color:{RED};">+121.6%</b> — more than doubled in 4 years
            </div></div>""",unsafe_allow_html=True)

            st.markdown(f"""<div style="background:{GOLD}12;border:1px solid {GOLD}44;border-left:4px solid {GOLD};border-radius:10px;padding:16px 18px;">
            <div style="font-weight:700;color:{GOLD};font-size:0.92rem;margin-bottom:8px;">⚡ Strategic Takeaway</div>
            <div style="font-size:0.83rem;color:{TXT};line-height:1.7;">
            • Status: technically "Ideal" (Case 1) — but practically fragile<br>
            • WC ≈ WCN leaves zero buffer for any operational shock<br>
            • <b>Priority:</b> aggressively liquidate excess inventory to reduce WCN<br>
            • Only path to restore NC and begin paying down the €4.6B debt load
            </div></div>""",unsafe_allow_html=True)

    elif sid=="finmgmt":
        st.markdown(f"<h2 style='color:{TXT};'>Financial Management — FY {yr}</h2>",unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        c1.markdown(kpi("Current Ratio",fx(CR[yr]),GREEN if CR[yr]>=1.5 else ORANGE if CR[yr]>=1 else RED,"CA / CL",pres),unsafe_allow_html=True)
        c2.markdown(kpi("Quick Ratio",fx(QR[yr]),GREEN if QR[yr]>=1.0 else ORANGE if QR[yr]>=0.5 else RED,"(CA−Inv) / CL",pres),unsafe_allow_html=True)
        c3.markdown(kpi("Debt-to-Equity",fx(DE[yr]),GREEN if DE[yr]<=1 else ORANGE if DE[yr]<=1.5 else RED,"Total Debt / Equity",pres),unsafe_allow_html=True)
        c4.markdown(kpi("Interest Coverage",fx(IC[yr]),GREEN if IC[yr]>=5 else ORANGE if IC[yr]>=2 else RED,"EBIT / Fin. Expenses",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(line_fig({"Current Ratio":CR,"Quick Ratio":QR,"Cash Ratio":CASHR},"Liquidity Ratios",pres=pres),use_container_width=True)
        with c2b:
            st.plotly_chart(line_fig({"D/E":DE,"ND/EBITDA":NDEBITDA,"Interest Coverage":IC},"Solvency Ratios",pres=pres),use_container_width=True)
        st.markdown(ibox(
            f"<b>Liquidity:</b> CR {fx(CR[yr])} ({'adequate' if CR[yr]>=1.2 else 'tight'}) · QR {fx(QR[yr])} ({'above 1 — strong' if QR[yr]>=1 else 'below 1 — relies on inventory'}).<br>"
            f"<b>Solvency:</b> D/E {fx(DE[yr])} (improving deleverage trend from 1.28 in 2022) · "
            f"Interest Coverage {fx(IC[yr])}× ({'comfortable' if IC[yr]>=5 else 'tight — 2023 was 1.3×' if yr==2023 else 'recovering'}) · "
            f"ND/EBITDA {fx(NDEBITDA[yr])} ({'healthy' if NDEBITDA[yr]<2 else 'elevated'}).",BLUE),
            unsafe_allow_html=True)

    elif sid=="investors":
        st.markdown(f"<h2 style='color:{TXT};'>Investor & Shareholder Ratios — FY {yr}</h2>",unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        c1.markdown(kpi("EPS",f"€{EPS[yr]:.2f}" if EPS[yr] is not None else "N/A",
            GREEN if (EPS[yr] or 0)>5 else ORANGE if (EPS[yr] or 0)>0 else RED,"Earnings per Share",pres),unsafe_allow_html=True)
        c2.markdown(kpi("P/E Ratio",fx(PE[yr]),ORANGE if PE[yr] and PE[yr]>30 else GREEN,"Price / EPS",pres),unsafe_allow_html=True)
        c3.markdown(kpi("P/B Ratio",fx(PB[yr]),BLUE,"Price / Book",pres),unsafe_allow_html=True)
        c4.markdown(kpi("Dividend Yield",fp(DIVYLD[yr]) if DIVYLD[yr] else "N/A",GREEN,f"DPS €{DPS[yr]:.2f}",pres),unsafe_allow_html=True)
        c1b,c2b=st.columns(2)
        with c1b:
            st.plotly_chart(bar_fig({"EPS (€)":EPS},"Earnings Per Share",pres=pres),use_container_width=True)
        with c2b:
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=[str(y) for y in YH],y=[PRICE[y] for y in YH],
                mode="lines+markers",fill="tozeroy",line=dict(color=BLUE,width=2.5),marker=dict(size=8),name="Share Price"))
            fig.update_layout(title=dict(text="Share Price History (€)",font=dict(size=13 if not pres else 16,color=TXT2)))
            st.plotly_chart(dark_fig(fig,380 if pres else 330),use_container_width=True)
        st.markdown(ibox(
            f"<b>EPS €{EPS[yr]:.2f}</b> — recovered from -€0.42 loss in 2023. "
            f"P/E {fx(PE[yr])} {'signals market confidence in recovery' if PE[yr] and PE[yr]>20 else ''}. "
            f"P/B {fx(PB[yr])} reflects premium brand valuation above book. "
            f"Dividend €{DPS[yr]:.2f}/share (payout {fp(DIVPAY[yr])}) — cut in 2023 to preserve cash, now normalising.",GOLD),
            unsafe_allow_html=True)
        fs_body="0.9rem" if pres else "0.82rem"
        fs_ctx ="0.85rem" if pres else "0.78rem"
        st.markdown(f"<div style='font-size:{'1.1rem' if pres else '1.0rem'};font-weight:700;margin:24px 0 12px;padding-bottom:5px;border-bottom:2px solid {GOLD};color:{TXT};'>📝 Key Takeaways</div>",unsafe_allow_html=True)
        INV_KT=[
            (GREEN,"EPS (€7.50)",
             "Strong rebound in profitability following losses in 2023.",
             "Earnings per share turned sharply positive, confirming the operational recovery is translating into bottom-line results."),
            (ORANGE,"P/E (25.7×)",
             "High multiple → market expects strong future earnings growth and continued recovery.",
             "Investors are pricing in further margin expansion and revenue growth — the stock commands a premium over current earnings."),
            (BLUE,"P/B (5.97×)",
             "Premium valuation → reflects strong brand value but trading well above book value.",
             "The gap between market and book value signals market confidence in Adidas's intangible assets and brand equity."),
            (GOLD,"Dividend Yield (1.0%)",
             "Low yield — dividend policy remains conservative as the company prioritises reinvestment and balance sheet repair.",
             "The dividend was cut in 2023 to preserve cash; the current yield reflects a gradual, disciplined normalisation."),
        ]
        kt_cols=st.columns(2)
        for i,(color,title,subtitle,detail) in enumerate(INV_KT):
            with kt_cols[i%2]:
                st.markdown(f"<div style='background:{color}14;border:1px solid {color}45;border-left:4px solid {color};border-radius:10px;padding:18px 20px;margin-bottom:14px;'><div style='font-weight:700;color:{color};font-size:{fs_body};margin-bottom:4px;'>{title}</div><div style='font-size:{fs_body};color:{TXT};font-style:italic;margin-bottom:6px;'>{subtitle}</div><div style='font-size:{fs_ctx};color:{TXT2};line-height:1.6;'>{detail}</div></div>",unsafe_allow_html=True)

    elif sid=="statements":
        st.markdown(f"<h2 style='color:{TXT};'>Full Financial Statements</h2>",unsafe_allow_html=True)
        st.info("📋 Switch to the **Statements** tab (normal mode) or scroll down for the full P&L table and Cash Flow waterfall.")
        c1,c2=st.columns(2)
        with c1:
            sec("Key CF Metrics")
            c1a,c2a,c3a=st.columns(3)
            c1a.markdown(kpi("Op. CF 2025",fm(CF_OP[2025]),GREEN,"from operations",pres),unsafe_allow_html=True)
            c2a.markdown(kpi("Capex 2025",fm(CAPEX[2025]),ORANGE,"capital expenditure",pres),unsafe_allow_html=True)
            c3a.markdown(kpi("FCF 2025",fm(FCF[2025]),GREEN if FCF[2025]>0 else RED,"Free Cash Flow",pres),unsafe_allow_html=True)
        with c2:
            st.plotly_chart(waterfall_fig(2025),use_container_width=True)

    elif sid=="recommendations":
        st.markdown(f"<h2 style='color:{TXT};'>Strategic Recommendations</h2>",unsafe_allow_html=True)
        st.markdown(f"<p style='color:{TXT2};font-size:0.95rem;margin-bottom:20px;'>Based on the 2021–2025 financial analysis — four priority actions for Adidas leadership.</p>",unsafe_allow_html=True)
        RECS=[
            (RED,"1. Restore Working Capital Health",
             "WC fell 49% (€5.0bn → €2.5bn) · WCN rose 43% (€1.75bn → €2.5bn) · Net Cash near zero (€19M vs €3.2bn in 2021)",
             ["One bad year would force reliance on short-term bank loans",
              "Reinforce long-term resources and aggressively shorten the operating cycle",
              "Priority: reduce inventory glut — the core driver of WCN surge"]),
            (ORANGE,"2. Rebuild the Liquidity Buffer",
             "Cash ratio fell from 0.43 → 0.18 (−58%) · Quick ratio at 0.68 (below the critical 1.0 threshold)",
             ["Adidas cannot cover short-term liabilities without liquidating slow-moving inventory",
              "Target a cash buffer of €2.5–3bn to restore Quick Ratio above 1",
              "Maintain disciplined dividend policy · defer major share buybacks"]),
            (BLUE,"3. Gradually Deleverage",
             "D/E rose from 0.76 → 1.09 (+44%) · Equity Multiplier at 3.5× (high-leverage zone)",
             ["Interest coverage and ND/EBITDA are healthy, but capital mix has shifted structurally",
              "Prioritise debt repayment over shareholder returns for the next 2–3 years",
              "Goal: restore pre-crisis capital structure"]),
            (GREEN,"4. Continue Margin Recovery Below the Gross Line",
             "Gross margin stable (~51%) · EBIT margin 8.3% vs 9.4% in 2021 · EBITDA margin 12.6% vs 14.4% in 2021",
             ["Margin pressure comes from marketing, distribution and G&A — not COGS",
              "Restructure cost base to recover the 2021 margin profile",
              "Operational leverage should improve as revenue grows toward 2026E"]),
        ]
        cols=st.columns(2)
        for i,(color,title,context,bullets) in enumerate(RECS):
            with cols[i%2]:
                bl="".join(f"<li style='margin-bottom:6px;'>{b}</li>" for b in bullets)
                st.markdown(f"""<div style="background:{color}18;border:1px solid {color}50;
                    border-left:5px solid {color};border-radius:12px;padding:22px 24px;margin-bottom:18px;">
                    <div style="font-weight:700;color:{color};font-size:1.05rem;margin-bottom:8px;">{title}</div>
                    <div style="font-size:0.82rem;color:{TXT2};margin-bottom:12px;font-style:italic;">{context}</div>
                    <ul style="margin:0;padding-left:18px;font-size:0.88rem;color:{TXT};line-height:1.7;">{bl}</ul>
                </div>""",unsafe_allow_html=True)

# ── PRESENTATION MODE ─────────────────────────────────────────────────────────
def pres_mode():
    if "slide" not in st.session_state: st.session_state.slide=0
    if "pres_yr" not in st.session_state: st.session_state.pres_yr=2025

    with st.sidebar:
        st.markdown(f"<div style='color:{GOLD};font-weight:700;font-size:1.05rem;margin-bottom:10px;'>🎤 PRESENTATION MODE</div>",unsafe_allow_html=True)
        yr_opts=[2021,2022,2023,2024,2025,"2026E"]
        st.session_state.pres_yr=st.selectbox("Focus Year",yr_opts,index=4,key="yr_sel")
        st.markdown("---")
        for i,s in enumerate(SLIDES):
            active=i==st.session_state.slide
            if st.button(s["title"],key=f"sl_{i}",use_container_width=True,type="primary" if active else "secondary"):
                st.session_state.slide=i; st.rerun()
        st.markdown("---")
        st.markdown(f"<div style='color:{TXT2};font-size:0.75rem;'>Slide {st.session_state.slide+1}/{len(SLIDES)}</div>",unsafe_allow_html=True)

    cur=st.session_state.slide
    yr=st.session_state.pres_yr
    slide(SLIDES[cur]["id"],yr,pres=True)

    st.markdown("<br>",unsafe_allow_html=True)
    n1,n2,n3=st.columns([1,6,1])
    with n1:
        if st.button("◀ Prev",disabled=cur==0,use_container_width=True,key="prev"):
            st.session_state.slide=cur-1; st.rerun()
    with n2:
        st.markdown(f"<div style='text-align:center;color:{TXT2};font-size:0.82rem;padding-top:8px;'>"
                    f"{SLIDES[cur]['title']} · Slide {cur+1}/{len(SLIDES)}</div>",unsafe_allow_html=True)
    with n3:
        if st.button("Next ▶",disabled=cur==len(SLIDES)-1,use_container_width=True,key="nxt"):
            st.session_state.slide=cur+1; st.rerun()

# ── NORMAL TABS ───────────────────────────────────────────────────────────────
def tab_overview():
    sec("Key Performance Overview — All Years")
    c1,c2,c3,c4=st.columns(4)
    for col,yr2 in zip([c1,c2,c3,c4],[2022,2023,2024,2025]):
        col.markdown(kpi(f"Revenue {yr2}",fm(REVENUE[yr2]),BLUE,f"YoY {fp(yoy(REVENUE,yr2))}"),unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(bar_fig({"Revenue":REVENUE,"EBITDA":EBITDA_V},"Revenue vs EBITDA (€M)"),use_container_width=True)
    with c2: st.plotly_chart(line_fig({"Net Income":NET_INC,"EBIT":EBIT_V},"Income Trend (€M)"),use_container_width=True)
    sec("DuPont Decomposition")
    c1,c2,c3=st.columns(3)
    with c1: st.plotly_chart(line_fig({"ROE":ROE},"Return on Equity"),use_container_width=True)
    with c2: st.plotly_chart(line_fig({"ROS":ROS,"Asset Turnover":AT_R},"ROS & AT"),use_container_width=True)
    with c3: st.plotly_chart(line_fig({"Equity Multiplier":EM_R},"Equity Multiplier"),use_container_width=True)
    st.markdown(ibox("<b>2023 Crisis → Recovery:</b> ROE collapsed to -1.5% in 2023 (Yeezy writeoffs, Russia exit, inventory glut). "
        "By 2025, ROE recovered to 23.2% driven by margin expansion and improved asset efficiency. "
        "The Equity Multiplier (~3.5×) remains elevated — amplifies returns but also downside risk."),unsafe_allow_html=True)

def tab_profitability():
    sec("Profitability Ratios — FY 2025")
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(kpi("ROE",fp(ROE[2025]),color_roe(ROE[2025]),"DuPont: ROS×AT×EM"),unsafe_allow_html=True)
    c2.markdown(kpi("ROS",fp(ROS[2025]),color_m(ROS[2025],0.03,0.06),"Net Inc / Revenue"),unsafe_allow_html=True)
    c3.markdown(kpi("Asset Turnover",fx(AT_R[2025]),color_m(AT_R[2025],0.8,1.1),"Revenue / Assets"),unsafe_allow_html=True)
    c4.markdown(kpi("Equity Multiplier",fx(EM_R[2025]),ORANGE if EM_R[2025]>3 else GREEN,"Assets / Equity"),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"ROE":ROE,"ROS":ROS},"ROE & ROS"),use_container_width=True)
    with c2: st.plotly_chart(line_fig({"AT":AT_R,"EM":EM_R},"AT & Equity Multiplier"),use_container_width=True)
    sec("Profit Margins")
    c1,c2,c3=st.columns(3)
    for col,lbl,d,lo,hi in [(c1,"Gross Margin",GPM,0.40,0.50),(c2,"EBITDA Margin",EBITDAM,0.08,0.12),(c3,"EBIT Margin",EBITM,0.05,0.10)]:
        with col:
            xs=[str(yr) for yr in Y if yr in d and d[yr] is not None]
            ys=[d[yr] for yr in Y if yr in d and d[yr] is not None]
            fig=go.Figure(go.Bar(x=xs,y=ys,marker_color=[color_m(v,lo,hi) for v in ys],
                text=[fp(v) for v in ys],textposition="outside",textfont=dict(color=TXT,size=10)))
            fig.update_layout(title=dict(text=lbl,font=dict(size=12,color=TXT2)),showlegend=False,yaxis_tickformat=".0%")
            st.plotly_chart(dark_fig(fig,280),use_container_width=True)
    st.markdown(ibox("Gross Margin recovered above 50% in 2024–2025. "
        "EBITDA Margin dropped to 6.3% in 2023 due to Yeezy revenue loss and elevated opex, now recovering toward 13.5% (2026E). "
        "EBIT Margin at 8.3% (2025) signals operational normalisation."),unsafe_allow_html=True)

def tab_operating():
    sec("Profit Margins")
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"GPM":GPM,"EBITDA Margin":EBITDAM,"EBIT Margin":EBITM},"Margin Trends"),use_container_width=True)
    with c2:
        fig=go.Figure()
        for i,yr2 in enumerate(YH):
            fig.add_trace(go.Bar(name=str(yr2),
                x=["Revenue","Gross Profit","EBITDA","EBIT","Net Income"],
                y=[REVENUE[yr2],GROSS_P[yr2],EBITDA_V[yr2],EBIT_V[yr2],NET_INC[yr2]],
                marker_color=PAL[i%len(PAL)]))
        fig.update_layout(barmode="group",title=dict(text="P&L Breakdown (€M)",font=dict(size=13,color=TXT2)))
        st.plotly_chart(dark_fig(fig),use_container_width=True)
    sec("Cost Structure (% of Revenue)")
    c1,c2,c3=st.columns(3)
    for col,yr2 in zip([c1,c2,c3],[2023,2024,2025]):
        rev=REVENUE[yr2]
        lbls=["COGS","Marketing","Distribution","G&A","EBIT"]
        vals=[COGS_V[yr2]/rev,MKTG_V[yr2]/rev,DISTR_V[yr2]/rev,GA_V[yr2]/rev,EBIT_V[yr2]/rev]
        clrs=[RED,ORANGE,ORANGE,GOLD,GREEN]
        fig=go.Figure(go.Bar(x=lbls,y=vals,marker_color=clrs,
            text=[fp(v) for v in vals],textposition="outside",textfont=dict(color=TXT,size=10)))
        fig.update_layout(title=dict(text=f"Cost % Revenue {yr2}",font=dict(size=12,color=TXT2)),
            yaxis_tickformat=".0%",showlegend=False)
        col.plotly_chart(dark_fig(fig,280),use_container_width=True)
    st.markdown(ibox("COGS improved from 52.7% (2022) to 48.4% (2025) of revenue — richer product mix and fewer discounts. "
        "Marketing at 12.4% (2024) reflects Yeezy replacement spend. EBIT margin at 8.3% signals normalisation."),unsafe_allow_html=True)

    # ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────
    st.markdown(f"<div style='font-size:1.05rem;font-weight:700;margin:28px 0 14px;"
                f"padding-bottom:6px;border-bottom:2px solid {GOLD};color:{TXT};'>📝 Key Takeaways</div>",
                unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:0.95rem;color:{BLUE};font-weight:600;margin:0 0 6px;'>🔵 V-Shaped Recovery — </p>"
        f"<p style='font-size:0.82rem;color:{TXT2};margin:0 0 14px;'>Strong rebound following the 2023 performance trough — Adidas successfully navigated the post-Yeezy shock and returned to growth.</p>",
        unsafe_allow_html=True)
    KT=[
        (RED,"2023 Low Point",
         "The crisis year crystallised in two headline figures:",
         ["Revenue dip of −4.8% vs. 2022",
          "EBIT crashed 86.5% vs. 2021 — reflecting both volume and margin destruction"]),
        (GREEN,"Margin Restoration (FY 2025)",
         "All three margin lines recovered meaningfully:",
         ["Gross Margin: 51.6% — back above the 50% threshold, reflecting brand pricing power",
          "EBITDA Margin: 12.6% — significant recovery from ~6% in 2023",
          "EBIT Margin: 8.3% — up from ~1% in 2023"]),
    ]
    cols=st.columns(2)
    for i,(color,title,context,bullets) in enumerate(KT):
        with cols[i%2]:
            bl="".join(f"<li style='margin-bottom:5px;'>{b}</li>" for b in bullets)
            ul=f"<ul style='margin:8px 0 0;padding-left:18px;font-size:0.84rem;color:{TXT};line-height:1.7;'>{bl}</ul>"
            st.markdown(f"<div style='background:{color}14;border:1px solid {color}45;border-left:4px solid {color};border-radius:10px;padding:18px 20px;margin-bottom:14px;'><div style='font-weight:700;color:{color};font-size:0.95rem;margin-bottom:6px;'>{title}</div><div style='font-size:0.82rem;color:{TXT2};line-height:1.6;'>{context}</div>{ul}</div>",unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:0.95rem;color:{GOLD};font-weight:600;margin:14px 0 6px;'>🟡 Growth Outlook — </p>"
        f"<p style='font-size:0.82rem;color:{TXT2};margin:0 0 6px;'>Accelerating trajectory projected for 2026E, with revenue expected to grow ~7.6% and margin expansion continuing as operational leverage kicks in.</p>"
        f"<p style='font-size:0.95rem;color:{ORANGE};font-weight:600;margin:14px 0 6px;'>🟠 Key Challenge — </p>"
        f"<p style='font-size:0.82rem;color:{TXT2};margin:0;'>Profit margins remain thinner than the 2021 baseline (EBIT 8.3% vs. 9.4% pre-crisis). Continuous focus on profitability improvement — particularly below the gross line — is required.</p>",
        unsafe_allow_html=True)

def tab_investment():
    sec("Working Capital Days — FY 2025")
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(kpi("DSO",fd(DSO[2025]),GREEN if DSO[2025]<45 else ORANGE,"Days Sales Outstanding"),unsafe_allow_html=True)
    c2.markdown(kpi("DIO",fd(DIO[2025]),RED if DIO[2025]>170 else ORANGE,"Days Inventory Outstanding"),unsafe_allow_html=True)
    c3.markdown(kpi("DPO",fd(DPO[2025]),GREEN if DPO[2025]>80 else ORANGE,"Days Payable Outstanding"),unsafe_allow_html=True)
    c4.markdown(kpi("CCC",fd(CCC[2025]),GREEN if CCC[2025]<110 else ORANGE,"Cash Conversion Cycle"),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"DSO":DSO,"DIO":DIO,"DPO":DPO,"CCC":CCC},"WC Days Trend"),use_container_width=True)
    with c2:
        fig=go.Figure()
        for d2,lbl,c_ in [(DSO,"DSO",BLUE),(DIO,"DIO",RED),(DPO,"DPO",GREEN)]:
            xs=[str(yr) for yr in Y if yr in d2]; ys=[d2[yr] for yr in Y if yr in d2]
            fig.add_trace(go.Bar(name=lbl,x=xs,y=ys,marker_color=c_))
        fig.update_layout(barmode="stack",title=dict(text="DSO / DIO / DPO Stacked",font=dict(size=13,color=TXT2)))
        st.plotly_chart(dark_fig(fig),use_container_width=True)
    sec("Non-Current Asset Management")
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"PP&E Turnover":PPET},"PP&E Turnover (×)"),use_container_width=True)
    with c2:
        fig=go.Figure()
        for lbl,key in [("PP&E","PP&E"),("Intangibles","Intangible assets"),("Other NCA","Other NCA")]:
            fig.add_trace(go.Bar(name=lbl,x=[str(y) for y in YH],y=[BS[key][yr] for yr in YH]))
        fig.update_layout(barmode="stack",title=dict(text="NCA Composition (€M)",font=dict(size=13,color=TXT2)))
        st.plotly_chart(dark_fig(fig,300),use_container_width=True)
    st.markdown(ibox("DIO peaked at 183 days in 2022 (demand surge over-stocking). 2025: 177 days — still high. "
        "DSO improved from 52 → 39 days — faster collections. DPO 88 days — effective supplier credit use. "
        "PP&E Turnover 5.4× (2025) — increasing fixed asset efficiency."),unsafe_allow_html=True)

def tab_sfs():
    sec("Financial Structure Analysis")
    yr_sel=st.select_slider("Select Year",options=Y,value=2025,key="sfs_yr")
    wc_v=WC.get(yr_sel,0); wcn_v=WCN.get(yr_sel,0); nc_v=NC_SFS.get(yr_sel,0)
    sc=get_sc(wc_v,wcn_v,nc_v); sname,sico,sc_c,ssigns,sinterp=SCENARIOS[sc]
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(kpi("WC",fm(wc_v),GREEN if wc_v>0 else RED,"Equity+NCL−NCA"),unsafe_allow_html=True)
    c2.markdown(kpi("WCN",fm(wcn_v),GREEN if wcn_v<0 else ORANGE,"Inv+AR+OCA−AP−OCL"),unsafe_allow_html=True)
    c3.markdown(kpi("NC",fm(nc_v),GREEN if nc_v>0 else RED,"WC − WCN"),unsafe_allow_html=True)
    c4.markdown(kpi("Net Debt",fm(NETDBT.get(yr_sel,0)),
        GREEN if NETDBT.get(yr_sel,0)<2500 else ORANGE if NETDBT.get(yr_sel,0)<5000 else RED,
        "NCL+Borr.C−Cash"),unsafe_allow_html=True)
    c1b,c2b=st.columns([3,2])
    with c1b:
        st.plotly_chart(line_fig({"WC":WC,"WCN":WCN,"NC":NC_SFS},"SFS Indicators (€M)"),use_container_width=True)
    with c2b:
        st.markdown(f"""<div style="background:{sc_c}18;border:2px solid {sc_c};border-radius:12px;
            padding:20px;margin:8px 0;">
            <div style="font-size:1.8rem;">{sico}</div>
            <div style="font-size:1.2rem;font-weight:700;color:{sc_c};margin:6px 0;">Case {sc}: {sname}</div>
            <div style="font-size:0.8rem;color:{TXT2};margin:4px 0;">{ssigns}</div>
            <div style="font-size:0.88rem;color:{TXT};margin-top:8px;">{sinterp}</div>
        </div>""",unsafe_allow_html=True)
    sec("Scenario Journey Map")
    fig=go.Figure()
    for yr_p in YH:
        wc_p=WC[yr_p]; wcn_p=WCN[yr_p]; nc_p=NC_SFS[yr_p]
        sc_p=get_sc(wc_p,wcn_p,nc_p); _,_,c_p,_,_=SCENARIOS[sc_p]
        fig.add_trace(go.Scatter(x=[wcn_p],y=[wc_p],mode="markers+text",
            marker=dict(size=22,color=c_p,line=dict(color=TXT,width=1)),
            text=[str(yr_p)],textposition="top center",name=str(yr_p),
            hovertemplate=f"<b>{yr_p}</b><br>WC: €%{{y:,.0f}}M<br>WCN: €%{{x:,.0f}}M<extra></extra>"))
    fig.add_hline(y=0,line_dash="dash",line_color=TXT2,opacity=0.5)
    fig.add_vline(x=0,line_dash="dash",line_color=TXT2,opacity=0.5)
    fig.update_layout(xaxis_title="WCN (€M)",yaxis_title="WC (€M)",
        title=dict(text="WC vs WCN Scenario Map",font=dict(size=13,color=TXT2)),showlegend=True)
    st.plotly_chart(dark_fig(fig,400),use_container_width=True)

def tab_finmgmt():
    sec("Liquidity Analysis — FY 2025")
    c1,c2,c3=st.columns(3)
    c1.markdown(kpi("Current Ratio",fx(CR[2025]),GREEN if CR[2025]>=1.5 else ORANGE,"CA / CL"),unsafe_allow_html=True)
    c2.markdown(kpi("Quick Ratio",fx(QR[2025]),GREEN if QR[2025]>=1 else ORANGE,"(CA−Inv) / CL"),unsafe_allow_html=True)
    c3.markdown(kpi("Cash Ratio",fx(CASHR[2025]),GREEN if CASHR[2025]>=0.2 else ORANGE,"Cash / CL"),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"Current Ratio":CR,"Quick Ratio":QR,"Cash Ratio":CASHR},"Liquidity Ratios"),use_container_width=True)
    with c2:
        xs=[str(yr) for yr in YH]; ys=[BS["Cash"][yr] for yr in YH]
        fig=go.Figure(go.Bar(x=xs,y=ys,marker_color=[GREEN if v>1500 else ORANGE if v>800 else RED for v in ys],
            text=[fm(v) for v in ys],textposition="outside",textfont=dict(color=TXT,size=10)))
        fig.update_layout(title=dict(text="Cash Balance (€M)",font=dict(size=13,color=TXT2)),showlegend=False)
        st.plotly_chart(dark_fig(fig,300),use_container_width=True)
    sec("Solvency Analysis — FY 2025")
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(kpi("Debt-to-Equity",fx(DE[2025]),GREEN if DE[2025]<=1 else ORANGE,"Total Debt / Equity"),unsafe_allow_html=True)
    c2.markdown(kpi("Total Debt Ratio",fp(TDR[2025]),GREEN if TDR[2025]<=0.3 else ORANGE,"Total Debt / Assets"),unsafe_allow_html=True)
    c3.markdown(kpi("Interest Coverage",fx(IC[2025]),GREEN if IC[2025]>=5 else ORANGE,"EBIT / Fin. Exp."),unsafe_allow_html=True)
    c4.markdown(kpi("ND / EBITDA",fx(NDEBITDA[2025]),GREEN if NDEBITDA[2025]<2 else ORANGE,"Net Debt / EBITDA"),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(line_fig({"D/E":DE,"Total Debt Ratio":TDR},"Leverage Ratios"),use_container_width=True)
    with c2: st.plotly_chart(line_fig({"Interest Coverage":IC,"ND/EBITDA":NDEBITDA},"Coverage Ratios"),use_container_width=True)
    st.markdown(ibox("CR 1.32 (adequate, below 1.5 ideal). QR 0.68 — below 1 means reliance on inventory liquidation. "
        "D/E improved from 1.28 (2022) to 1.09 (2025) — clear deleveraging trend. "
        "Interest Coverage 7.1× vs critical 1.3× in 2023. ND/EBITDA 1.5 — within comfort zone (<3×)."),unsafe_allow_html=True)

def tab_investors():
    sec("Shareholder Value — FY 2025")
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(kpi("EPS",f"€{EPS[2025]:.2f}",GREEN,"vs -€0.42 in 2023"),unsafe_allow_html=True)
    c2.markdown(kpi("P/E",fx(PE[2025]),ORANGE,"Price / EPS"),unsafe_allow_html=True)
    c3.markdown(kpi("P/B",fx(PB[2025]),BLUE,"Price / Book"),unsafe_allow_html=True)
    c4.markdown(kpi("Div. Yield",fp(DIVYLD[2025]),GREEN,f"DPS €{DPS[2025]:.2f}"),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(bar_fig({"EPS (€)":EPS},"Earnings Per Share"),use_container_width=True)
    with c2:
        fig=go.Figure(go.Scatter(x=[str(y) for y in YH],y=[PRICE[y] for y in YH],
            mode="lines+markers",fill="tozeroy",line=dict(color=BLUE,width=2.5),marker=dict(size=8)))
        fig.update_layout(title=dict(text="Share Price History (€)",font=dict(size=13,color=TXT2)))
        st.plotly_chart(dark_fig(fig,300),use_container_width=True)
    c1,c2=st.columns(2)
    with c1:
        xs=[str(yr) for yr in Y if yr in PB and PB[yr]]; ys=[PB[yr] for yr in Y if yr in PB and PB[yr]]
        fig=go.Figure(go.Bar(x=xs,y=ys,marker_color=BLUE,text=[fx(v) for v in ys],textposition="outside",textfont=dict(color=TXT,size=10)))
        fig.update_layout(title=dict(text="P/B Ratio",font=dict(size=13,color=TXT2)),showlegend=False)
        st.plotly_chart(dark_fig(fig,280),use_container_width=True)
    with c2:
        xs=[str(yr) for yr in Y if yr in DPS]; ys=[DPS[yr] for yr in Y if yr in DPS]
        fig=go.Figure(go.Bar(x=xs,y=ys,marker_color=GOLD,text=[f"€{v:.2f}" for v in ys],textposition="outside",textfont=dict(color=TXT,size=10)))
        fig.update_layout(title=dict(text="Dividend Per Share (€)",font=dict(size=13,color=TXT2)),showlegend=False)
        st.plotly_chart(dark_fig(fig,280),use_container_width=True)
    st.markdown(ibox("EPS recovery: €11.85 (2021) → -€0.42 (2023) → €7.50 (2025). "
        "P/E 25.7× (2025) signals market confidence. P/B 5.97× reflects premium brand valuation. "
        "Dividend cut to €0.70 in 2023–2024 (cash preservation), rising to €2.00 in 2025."),unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:1.0rem;font-weight:700;margin:28px 0 14px;padding-bottom:5px;border-bottom:2px solid {GOLD};color:{TXT};'>📝 Key Takeaways</div>",unsafe_allow_html=True)
    INV_KT=[
        (GREEN,"EPS (€7.50)",
         "Strong rebound in profitability following losses in 2023.",
         "Earnings per share turned sharply positive, confirming the operational recovery is translating into bottom-line results."),
        (ORANGE,"P/E (25.7×)",
         "High multiple → market expects strong future earnings growth and continued recovery.",
         "Investors are pricing in further margin expansion and revenue growth — the stock commands a premium over current earnings."),
        (BLUE,"P/B (5.97×)",
         "Premium valuation → reflects strong brand value but trading well above book value.",
         "The gap between market and book value signals market confidence in Adidas's intangible assets and brand equity."),
        (GOLD,"Dividend Yield (1.0%)",
         "Low yield — dividend policy remains conservative as the company prioritises reinvestment and balance sheet repair.",
         "The dividend was cut in 2023 to preserve cash; the current yield reflects a gradual, disciplined normalisation."),
    ]
    cols=st.columns(2)
    for i,(color,title,subtitle,detail) in enumerate(INV_KT):
        with cols[i%2]:
            st.markdown(f"<div style='background:{color}14;border:1px solid {color}45;border-left:4px solid {color};border-radius:10px;padding:18px 20px;margin-bottom:14px;'><div style='font-weight:700;color:{color};font-size:0.95rem;margin-bottom:4px;'>{title}</div><div style='font-size:0.88rem;color:{TXT};font-style:italic;margin-bottom:6px;'>{subtitle}</div><div style='font-size:0.82rem;color:{TXT2};line-height:1.6;'>{detail}</div></div>",unsafe_allow_html=True)

def tab_statements():
    import pandas as pd
    st.markdown(f"<h3 style='color:{TXT};margin-bottom:4px;'>Full Financial Statements</h3>",unsafe_allow_html=True)
    t1,t2,t3=st.tabs(["📊 Income Statement","💸 Cash Flow","🏦 Balance Sheet"])

    with t1:
        sec("Income Statement (€M)")
        IS_ROWS=[("Revenue",REVENUE),("Cost of Sales",{y:-COGS_V[y] for y in YH}),
                 ("Gross Profit",GROSS_P),("Marketing Exp.",{y:-MKTG_V[y] for y in YH}),
                 ("Distribution Exp.",{y:-DISTR_V[y] for y in YH}),
                 ("G&A Expenses",{y:-GA_V[y] for y in YH}),
                 ("EBITDA",EBITDA_V),("D&A",DA_V),("EBIT",EBIT_V),
                 ("Financial Income",FIN_INC_V),("Financial Expenses",{y:-FIN_EXP_V[y] for y in YH}),
                 ("Net Financial Result",NET_FIN),("EBT",EBT_V),
                 ("Income Tax",TAX_V),("Net Income",NET_INC)]
        rows_dict={lbl:{str(yr):f"€{d[yr]:,.0f}M" for yr in YH} for lbl,d in IS_ROWS}
        df=pd.DataFrame(rows_dict).T; df.columns=[str(y) for y in YH]
        st.dataframe(df,use_container_width=True)
        st.plotly_chart(line_fig({"GPM":GPM,"EBITDA Margin":EBITDAM,"EBIT Margin":EBITM,"Net Margin":ROS},"Margin Analysis"),use_container_width=True)

    with t2:
        sec("Cash Flow Statement (€M)")
        yr_cf=st.selectbox("Year for Waterfall",YH,index=4,key="cf_yr_sel")
        c1,c2=st.columns([2,3])
        with c1:
            cf_dict={row:{str(yr):f"€{CF_DET[row][yr]:,.0f}M" for yr in YH} for row in CF_DET}
            df_cf=pd.DataFrame(cf_dict).T; df_cf.columns=[str(y) for y in YH]
            st.dataframe(df_cf,use_container_width=True)
        with c2:
            st.plotly_chart(waterfall_fig(yr_cf),use_container_width=True)
            sec("Free Cash Flow")
            xs=[str(yr) for yr in YH]; ys=[FCF[yr] for yr in YH]
            fig=go.Figure(go.Bar(x=xs,y=ys,marker_color=[GREEN if v>=0 else RED for v in ys],
                text=[fm(v) for v in ys],textposition="outside",textfont=dict(color=TXT,size=10)))
            fig.add_hline(y=0,line_dash="dash",line_color=TXT2,opacity=0.4)
            fig.update_layout(title=dict(text="Free Cash Flow (Op CF − Capex, €M)",font=dict(size=13,color=TXT2)),showlegend=False)
            st.plotly_chart(dark_fig(fig,280),use_container_width=True)

    with t3:
        sec("Balance Sheet (€M)")
        bs_dict={row:{str(yr):f"€{BS[row][yr]:,.0f}M" for yr in YH} for row in BS}
        df_bs=pd.DataFrame(bs_dict).T; df_bs.columns=[str(y) for y in YH]
        st.dataframe(df_bs,use_container_width=True)
        c1,c2=st.columns(2)
        with c1:
            fig=go.Figure()
            for lbl,key in [("NCA","Total NCA"),("CA","Total CA")]:
                fig.add_trace(go.Bar(name=lbl,x=[str(y) for y in YH],y=[BS[key][yr] for yr in YH]))
            fig.update_layout(barmode="stack",title=dict(text="Asset Structure (€M)",font=dict(size=13,color=TXT2)))
            st.plotly_chart(dark_fig(fig,300),use_container_width=True)
        with c2:
            fig2=go.Figure()
            for lbl,key in [("Equity","Total Equity"),("NCL","Total NCL"),("CL","Total CL")]:
                fig2.add_trace(go.Bar(name=lbl,x=[str(y) for y in YH],y=[BS[key][yr] for yr in YH]))
            fig2.update_layout(barmode="stack",title=dict(text="Equity & Liabilities Structure (€M)",font=dict(size=13,color=TXT2)))
            st.plotly_chart(dark_fig(fig2,300),use_container_width=True)

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    css()
    with st.sidebar:
        st.markdown(f"<div style='font-size:1.4rem;font-weight:700;color:{BLUE};margin-bottom:2px;'>👟 Adidas</div>"
                    f"<div style='font-size:0.82rem;color:{TXT2};margin-bottom:14px;'>Financial Dashboard 2021–2026E</div>",
                    unsafe_allow_html=True)
        pres=st.toggle("🎤 Presentation Mode",value=False)
        if not pres:
            st.markdown("---")
            st.markdown(f"<div style='color:{TXT2};font-size:0.76rem;'>All values in €M.<br>2026E = trend forecast.<br>Data: Adidas Annual Reports.</div>",unsafe_allow_html=True)

    if pres:
        pres_mode()
    else:
        st.markdown(f"<h2 style='color:{TXT};margin-bottom:2px;'>Adidas Financial Dashboard</h2>"
                    f"<p style='color:{TXT2};margin-bottom:12px;'>2021 – 2025 Historical · 2026E Forecast</p>",
                    unsafe_allow_html=True)
        tabs=st.tabs(["📊 Overview","📈 Profitability","🏭 Operating Mgmt",
                      "🔄 Investment Mgmt","🏗️ Financial Structure",
                      "🛡️ Financial Mgmt","💹 Investor Ratios","📋 Statements"])
        with tabs[0]: tab_overview()
        with tabs[1]: tab_profitability()
        with tabs[2]: tab_operating()
        with tabs[3]: tab_investment()
        with tabs[4]: tab_sfs()
        with tabs[5]: tab_finmgmt()
        with tabs[6]: tab_investors()
        with tabs[7]: tab_statements()

main()
