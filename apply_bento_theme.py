import shutil
import re

src = '/Users/mint/Desktop/AI智能体/iOS App/积分联盟计划iOS版App_DribbbleLux.html'
dst = '/Users/mint/Desktop/AI智能体/iOS App/积分联盟计划iOS版App_AppleStore.html'

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

# The user wants a new UI color scheme/style. Let's create a "Bento Box / Warm Pastel (奶油便当盒风)"
new_css = """
      /* ========================================================= */
      /* WARM PASTEL BENTO BOX THEME (治愈系便当盒/高级奶油风)   */
      /* ========================================================= */
      :root {
        --bg: #F7F5F0 !important;
        --card: #FFFFFF !important;
        --text: #2C2A29 !important;
        --muted: #8A7D72 !important;
        --line: rgba(138, 125, 114, 0.1) !important;
        --radius: 28px !important;
        --radius-sm: 16px !important;
        --shadow-soft: 0 12px 40px rgba(138, 125, 114, 0.08) !important;
        --shadow-sm: 0 4px 16px rgba(138, 125, 114, 0.05) !important;
        --accent: #E87A5D !important; /* Warm Terracotta */
        --accent-hover: #D46A4F !important;
      }

      body {
        background-color: var(--bg) !important;
        background-image: none !important;
        color: var(--text) !important;
        font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", sans-serif !important;
      }
      .noise { display: none !important; }

      /* Cards & Layout (Bento Style) */
      .card, .product, .balance, .member-card, .mall-section, .modal, .card-block, .row {
        background: var(--card) !important;
        border-radius: var(--radius) !important;
        box-shadow: var(--shadow-soft) !important;
        border: none !important;
        transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.3s ease !important;
      }
      
      /* Balance Card */
      .balance {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFFDF9 100%) !important;
        padding: 32px 24px !important;
        border: 1px solid rgba(255,255,255,0.8) !important;
      }
      .balance-value {
        font-size: 52px !important;
        font-weight: 800 !important;
        color: var(--text) !important;
        background: none !important;
        -webkit-text-fill-color: var(--text) !important;
        letter-spacing: -1px !important;
      }
      .balance::after, .balance::before { display: none !important; }

      /* Product Grid */
      .product {
        padding: 16px !important;
      }
      .product:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 16px 40px rgba(138, 125, 114, 0.12) !important;
      }
      .product-thumb-new, .mall-cat-icon {
        background: #F2EFE9 !important;
        border-radius: 18px !important;
        border: none !important;
      }

      /* Buttons - Warm Accent */
      button#buyBtn, button#verifyBtn, button#viewOrderBtn, .btn-primary, .channels-actions button {
        background: var(--accent) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 20px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        box-shadow: 0 8px 24px rgba(232, 122, 93, 0.3) !important;
        transition: transform 0.2s ease, background 0.2s ease !important;
      }
      button#buyBtn:active, button#verifyBtn:active, button#viewOrderBtn:active {
        transform: scale(0.96) !important;
        background: var(--accent-hover) !important;
      }
      
      .mini-btn, .pill {
        background: #F7F5F0 !important;
        color: var(--text) !important;
        border: none !important;
        border-radius: 99px !important;
        font-weight: 600 !important;
        box-shadow: var(--shadow-sm) !important;
      }
      .pill.active {
        background: var(--text) !important;
        color: #FFFFFF !important;
      }

      /* Typography Overrides */
      .brand-title {
        font-size: 24px !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px !important;
        color: var(--text) !important;
      }
      .section-title h3 {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: var(--text) !important;
      }

      /* Header & Nav */
      header.top, .nav {
        background: rgba(247, 245, 240, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: none !important;
      }
      .nav-item { color: var(--muted) !important; }
      .nav-item.active { color: var(--accent) !important; font-weight: 700 !important; }
      .nav-item svg { opacity: 0.8 !important; fill: var(--muted) !important; }
      .nav-item.active svg { fill: var(--accent) !important; }

      /* Member Card - Soft Coffee */
      .member-card {
        background: linear-gradient(135deg, #4A4036 0%, #2C2A29 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 16px 40px rgba(44, 42, 41, 0.2) !important;
      }
      .member-card .title, .member-card .member-title {
        background: none !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-weight: 600 !important;
      }
      .member-card .text-muted, .member-card .member-hint {
        color: rgba(255,255,255,0.6) !important;
      }

      /* Channels Circle - Bento style */
      .channels-circle {
        background: #FFFFFF !important;
        border: none !important;
        box-shadow: inset 0 0 0 6px #F7F5F0, 0 12px 30px rgba(138, 125, 114, 0.1) !important;
        width: 170px !important;
        height: 170px !important;
        border-radius: 50% !important;
      }
      .channels-circle::after, .channels-circle::before { display: none !important; }
      .channels-circle-val {
        font-weight: 800 !important;
        font-size: 32px !important;
        color: var(--text) !important;
      }

      /* Modals & Inputs */
      .modal {
        border-radius: 32px 32px 0 0 !important;
        background: #FFFFFF !important;
        border: none !important;
      }
      .otp-input {
        background: #F7F5F0 !important;
        border: 2px solid transparent !important;
        border-radius: 18px !important;
        box-shadow: none !important;
        color: var(--text) !important;
        font-weight: 700 !important;
      }
      .otp-input:focus {
        border-color: var(--accent) !important;
        background: #FFFFFF !important;
        box-shadow: 0 8px 20px rgba(232, 122, 93, 0.15) !important;
        outline: none !important;
      }

      /* Inline color overrides */
      div[style*="background: #222"], div[style*="background: #222222"] { background: var(--text) !important; }
      div[style*="color: #222"], div[style*="color: #111"] { color: var(--text) !important; }
      div[style*="color: #555"], div[style*="color: #666"] { color: var(--muted) !important; }
      div[style*="background: #F8F8F8"], div[style*="background: #F4F4F4"], div[style*="background: #F5F5F7"] { background: #F7F5F0 !important; }
      
      .qty-btn, .spec-option {
        background: #F7F5F0 !important;
        color: var(--text) !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
      }
      .spec-option.active {
        background: var(--text) !important;
        color: #FFFFFF !important;
      }
"""

# Strip out old ACETERNITY UI / LIGHT LUXURY TECH overrides that were present in DribbbleLux (if any)
# or strip out any previously injected style overrides at the bottom
html = re.sub(r'/\* ========================================================= \*/\s*/\*.*?THEME OVERRIDES.*?</style>', '</style>', html, flags=re.DOTALL)

# Inject the new CSS before </style>
html = html.replace('</style>', new_css + '\n</style>')

# Also rename the <title> or <html data-theme="..."> if desired, but not strictly necessary.
html = html.replace('data-theme="dribbble"', 'data-theme="bento"')

with open(dst, 'w', encoding='utf-8') as f:
    f.write(html)
