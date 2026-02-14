"""
FIN303 Exam Practice 1 — Question Bank
All 52 questions parsed from the exam practice DOCX.
Each question has: id, chapter, question text, options, correct answer index,
and a detailed explanation for learning when incorrect.
"""

QUESTIONS = [
    # ──────────────────────────── CHAPTER 1 ────────────────────────────
    {
        "id": 1,
        "chapter": 1,
        "topic": "Business Organization",
        "question": "Which of the following statements is most correct?",
        "options": [
            "One advantage of forming a corporation is that you have limited liability.",
            "Corporations face fewer regulations than sole proprietorships.",
            "One disadvantage of being a sole proprietor is that you have to pay corporate taxes, even though you don't realize the benefits of being a corporation.",
            "Statements b and c are correct."
        ],
        "correct": 0,
        "explanation": "A key advantage of the corporate form of business is **limited liability** — shareholders can only lose the amount they invested. Sole proprietors and partners, by contrast, have unlimited personal liability. Corporations actually face *more* regulations, not fewer, and sole proprietors do not pay corporate taxes."
    },
    {
        "id": 2,
        "chapter": 1,
        "topic": "Corporate Goals",
        "question": "The primary goal of a publicly-owned firm interested in serving its stockholders should be to",
        "options": [
            "Maximize expected total corporate profit.",
            "Maximize expected EPS.",
            "Minimize the chances of losses.",
            "Maximize the stock price per share."
        ],
        "correct": 3,
        "explanation": "The primary goal in financial management is to **maximize shareholder wealth**, which is reflected in the stock price. Maximizing profits or EPS alone ignores risk, timing of cash flows, and capital structure effects. Stock price captures all of these factors."
    },
    {
        "id": 3,
        "chapter": 1,
        "topic": "Agency Problems",
        "question": "Which of the following actions are likely to reduce agency conflicts between stockholders and managers?",
        "options": [
            "Paying managers a large fixed salary.",
            "Increasing the threat of corporate takeover.",
            "Placing restrictive covenants in debt agreements.",
            "All of the statements above are correct."
        ],
        "correct": 1,
        "explanation": "**Agency conflicts** arise when managers act in their own interest rather than shareholders'. The threat of a **corporate takeover** aligns manager and shareholder interests because poor performance makes the firm a takeover target, putting managers' jobs at risk. Fixed salaries don't incentivize value creation, and debt covenants address bondholder-stockholder conflicts, not stockholder-manager conflicts."
    },
    {
        "id": 4,
        "chapter": 1,
        "topic": "Agency Relationships",
        "question": "Which of the following statements is most correct?",
        "options": [
            "A good goal for a corporate manager is maximization of expected EPS.",
            "Most business in the U.S. is conducted by corporations; corporations' popularity results primarily from their favorable tax treatment.",
            "A good example of an agency relationship is the one between stockholders and managers.",
            "Corporations and partnerships have an advantage over proprietorships because a sole proprietor is subject to unlimited liability, but investors in the other types of businesses are not."
        ],
        "correct": 2,
        "explanation": "An **agency relationship** exists when one party (the principal) hires another (the agent) to act on their behalf. Stockholders (principals) hire managers (agents) to run the firm. This is the classic example. EPS maximization ignores risk; corporations face *double* taxation (not favorable); and *limited* partners have limited liability but *general* partners do not."
    },

    # ──────────────────────────── CHAPTER 2 ────────────────────────────
    {
        "id": 5,
        "chapter": 2,
        "topic": "Financial Markets",
        "question": "Which of the following statements is most correct?",
        "options": [
            "If an investor sells 100 shares of Microsoft to his brother-in-law, this is a primary market transaction.",
            "Private securities are generally less liquid than publicly traded securities.",
            "Money markets are where short-term, liquid securities are traded, whereas capital markets represent the markets for long-term debt and common stock.",
            "Statements b and c are correct."
        ],
        "correct": 3,
        "explanation": "Both (b) and (c) are correct. **Private securities** lack a public exchange, making them harder to buy/sell (less liquid). **Money markets** trade short-term instruments (< 1 year) like T-bills and commercial paper, while **capital markets** trade long-term instruments like stocks and bonds. Selling shares between individuals is a *secondary* market transaction, not primary."
    },
    {
        "id": 6,
        "chapter": 2,
        "topic": "Market Types",
        "question": "Which of the following statements is most correct?",
        "options": [
            "While the distinctions are blurring, investment banks generally specialize in lending money, whereas commercial banks generally help companies raise capital from other parties.",
            "Money market mutual funds usually invest their money in a well-diversified portfolio of liquid common stocks.",
            "The NYSE operates as an auction market, whereas NASDAQ is an example of a dealer market.",
            "Statements b and c are correct."
        ],
        "correct": 2,
        "explanation": "The **NYSE** is an **auction market** where buyers and sellers trade through a centralized system. **NASDAQ** is a **dealer market** where dealers (market makers) buy and sell from their own inventory. Investment banks help raise capital (not lend), and money market funds invest in short-term debt (not stocks)."
    },
    {
        "id": 7,
        "chapter": 2,
        "topic": "Capital Markets",
        "question": "Which of the following is an example of a capital market instrument?",
        "options": [
            "Commercial paper.",
            "Preferred stock.",
            "U.S. Treasury bills.",
            "Banker's acceptances."
        ],
        "correct": 1,
        "explanation": "**Capital market instruments** are long-term (> 1 year) securities. **Preferred stock** is a long-term equity instrument. Commercial paper, T-bills, and banker's acceptances are all *money market* instruments (short-term, < 1 year)."
    },
    {
        "id": 8,
        "chapter": 2,
        "topic": "Money Markets",
        "question": "Money markets are markets for",
        "options": [
            "Foreign currency exchange.",
            "Consumer automobile loans.",
            "Corporate stocks.",
            "Short-term debt securities."
        ],
        "correct": 3,
        "explanation": "**Money markets** deal in **short-term debt securities** with maturities of one year or less, such as Treasury bills, commercial paper, and certificates of deposit. Foreign exchange, auto loans, and stocks are traded in other markets."
    },
    {
        "id": 9,
        "chapter": 2,
        "topic": "Market Efficiency",
        "question": "Which of the following statements is most correct?",
        "options": [
            "Semistrong-form market efficiency means that stock prices reflect all public information.",
            "An individual who has information about past stock prices should be able to profit from this information in a weak-form efficient market.",
            "An individual who has inside information about a publicly traded company should be able to profit from this information in a strong-form efficient market.",
            "Statements a and c are correct."
        ],
        "correct": 0,
        "explanation": "The **Efficient Market Hypothesis (EMH)** has three forms:\n• **Weak form**: Prices reflect all *past* trading data → can't profit from historical prices.\n• **Semistrong form**: Prices reflect all *publicly available* information → can't profit from public info.\n• **Strong form**: Prices reflect *all* information (public + private) → can't profit even with insider info."
    },
    {
        "id": 10,
        "chapter": 2,
        "topic": "Market Efficiency",
        "question": "Which of the following statements is most correct?",
        "options": [
            "If the stock market is semistrong-form efficient, all stocks should have the same expected return.",
            "An individual who has information about past stock prices should be able to profit from this information in a weak-form efficient market.",
            "An individual who has inside information about a publicly traded company should be able to profit from this information in a strong-form efficient market.",
            "Semistrong-form market efficiency means that stock prices reflect all public information."
        ],
        "correct": 3,
        "explanation": "**Semistrong-form efficiency** means stock prices already incorporate all publicly available information — financial statements, news, analyst reports, etc. You cannot earn excess returns by trading on public info. It does NOT mean all stocks have the same return (risk varies). In weak-form efficient markets, past prices are already reflected, so technical analysis doesn't work."
    },

    # ──────────────────────────── CHAPTER 3 ────────────────────────────
    {
        "id": 11,
        "chapter": 3,
        "topic": "Balance Sheet",
        "question": "Which of the following statements is CORRECT?",
        "options": [
            "The balance sheet for a given year is designed to give us an idea of what happened to the firm during that year.",
            "The balance sheet for a given year tells us how much money the company earned during that year.",
            "If a company's statements were prepared in accordance with GAAP, the market value of the stock equals the book value of the stock as reported on the balance sheet.",
            "The assets section of a typical company's balance sheet begins with cash, then lists the assets in the order in which they will probably be converted to cash, with the longest lived assets listed last."
        ],
        "correct": 3,
        "explanation": "The balance sheet lists assets in order of **liquidity** — starting with cash (most liquid) and ending with fixed assets (least liquid). The balance sheet is a *snapshot* at a point in time, not a record of what happened during the year (that's the income statement). Book value rarely equals market value."
    },
    {
        "id": 13,
        "chapter": 3,
        "topic": "Book Value Per Share",
        "question": "Brown Fashions Inc.'s December 31, 2014 balance sheet showed total common equity of $4,050,000 and 290,000 shares of stock outstanding. During 2015, the firm had $450,000 of net income, and it paid out $100,000 as dividends. What was the book value per share at 12/31/15, assuming no common stock was either issued or retired during 2015?",
        "options": [
            "$11.53",
            "$18.51",
            "$14.11",
            "$15.17"
        ],
        "correct": 3,
        "explanation": "**Book Value Per Share = Total Common Equity ÷ Shares Outstanding**\n\n• 12/31/14 equity: $4,050,000\n• + Net income: $450,000\n• − Dividends: $100,000\n• = Addition to retained earnings: $350,000\n• 12/31/15 equity: $4,050,000 + $350,000 = **$4,400,000**\n• BVPS = $4,400,000 ÷ 290,000 = **$15.17**"
    },
    {
        "id": 14,
        "chapter": 3,
        "topic": "Net Operating Working Capital",
        "question": "Prezas Company's balance sheet showed total current assets of $3,250, all of which were required in operations. Its current liabilities consisted of $975 of accounts payable, $600 of short-term notes payable to the bank, and $250 of accrued wages and taxes. What was its net operating working capital?",
        "options": [
            "$1,620",
            "$1,701",
            "$2,309",
            "$2,025"
        ],
        "correct": 3,
        "explanation": "**NOWC = Current Assets − (Current Liabilities − Notes Payable)**\n\nNotes payable is an interest-bearing debt, not an operating liability, so we exclude it.\n• Current Liabilities = $975 + $600 + $250 = $1,825\n• Operating Current Liabilities = $1,825 − $600 = $1,225\n• NOWC = $3,250 − $1,225 = **$2,025**"
    },
    {
        "id": 15,
        "chapter": 3,
        "topic": "EBIT Calculation",
        "question": "Rao Construction recently reported $20.00 million of sales, $12.60 million of operating costs other than depreciation, and $3.00 million of depreciation. It had $8.50 million of bonds outstanding that carry a 7.0% interest rate, and its federal-plus-state income tax rate was 40%. What was Rao's operating income, or EBIT, in millions?",
        "options": [
            "$4.27",
            "$3.83",
            "$3.56",
            "$4.40"
        ],
        "correct": 3,
        "explanation": "**EBIT = Sales − Operating Costs − Depreciation**\n\n• Sales: $20.00M\n• Operating costs: $12.60M\n• Depreciation: $3.00M\n• EBIT = $20.00 − $12.60 − $3.00 = **$4.40M**\n\nNote: Interest expense and taxes are *below* EBIT on the income statement."
    },
    {
        "id": 16,
        "chapter": 3,
        "topic": "Free Cash Flow",
        "question": "Vasudevan Inc. recently reported operating income of $5.35 million, depreciation of $1.20 million, and had a tax rate of 40%. The firm's Capex and net operating working capital totaled $0.6 million. How much was its free cash flow, in millions?",
        "options": [
            "$3.54",
            "$3.05",
            "$3.81",
            "$3.39"
        ],
        "correct": 2,
        "explanation": "**FCF = EBIT(1 − T) + Depreciation − (CapEx + ΔNOWC)**\n\n• EBIT(1 − T) = $5.35 × 0.60 = $3.21M\n• + Depreciation: $1.20M\n• − (CapEx + ΔNOWC): $0.60M\n• FCF = $3.21 + $1.20 − $0.60 = **$3.81M**\n\nFree cash flow represents the cash available to all investors after the firm has made necessary investments."
    },
    {
        "id": 17,
        "chapter": 3,
        "topic": "Market Value Added (MVA)",
        "question": "Over the years, O'Brien Corporation's stockholders have provided $20,000,000 of capital, when they purchased new issues of stock and allowed management to retain some of the firm's earnings. The firm now has 1,000,000 shares of common stock outstanding, and it sells at a price of $33.00 per share. How much value has O'Brien's management added to stockholder wealth over the years, i.e., what is O'Brien's MVA?",
        "options": [
            "$11,050,000",
            "$12,350,000",
            "$9,750,000",
            "$13,000,000"
        ],
        "correct": 3,
        "explanation": "**MVA = Market Value of Equity − Book Value of Equity**\n\n• Market Value = 1,000,000 shares × $33.00 = $33,000,000\n• Book Value = $20,000,000\n• MVA = $33,000,000 − $20,000,000 = **$13,000,000**\n\nMVA measures the total value management has created above and beyond the capital invested by shareholders."
    },
    {
        "id": 18,
        "chapter": 3,
        "topic": "Net Operating Working Capital",
        "question": "Wu Systems has the following balance sheet. How much net operating working capital does the firm have?\n\nCash $100 | Accounts payable $200\nAccounts receivable $650 | Accruals $255\nInventory $550 | Notes payable $445\nCurrent assets $1,300 | Current liabilities $900\nNet fixed assets $1,000 | Long-term debt $600\n| Common equity $300\n| Retained earnings $500\nTotal assets $2,300 | Total liab. & equity $2,300",
        "options": [
            "$845",
            "$718",
            "$794",
            "$701"
        ],
        "correct": 0,
        "explanation": "**NOWC = Current Assets − (Current Liabilities − Notes Payable)**\n\n• Current Assets = $1,300\n• Current Liabilities = $900\n• Notes Payable = $445\n• Operating CL = $900 − $445 = $455\n• NOWC = $1,300 − $455 = **$845**\n\nWe exclude notes payable because it's interest-bearing debt, not an operating liability."
    },

    # ──────────────────────────── CHAPTER 4 ────────────────────────────
    {
        "id": 19,
        "chapter": 4,
        "topic": "Current Ratio",
        "question": "All else being equal, which of the following will increase a company's current ratio?",
        "options": [
            "An increase in accounts receivable.",
            "An increase in accounts payable.",
            "An increase in net fixed assets.",
            "Statements a and b are correct."
        ],
        "correct": 0,
        "explanation": "**Current Ratio = Current Assets ÷ Current Liabilities**\n\nAn increase in **accounts receivable** increases current assets, raising the current ratio. An increase in accounts payable raises current liabilities (lowers the ratio). Net fixed assets don't affect the current ratio at all."
    },
    {
        "id": 20,
        "chapter": 4,
        "topic": "Debt & Financial Ratios",
        "question": "Stennett Corp.'s CFO has proposed that the company issue new debt and use the proceeds to buy back common stock. Which of the following are likely to occur if this proposal is adopted? (Assume the proposal would have no effect on operating income.)",
        "options": [
            "Return on assets (ROA) will decline.",
            "The Depreciation will increase.",
            "Taxes paid will decline.",
            "Statements a and c are correct."
        ],
        "correct": 3,
        "explanation": "When a firm issues debt to buy back stock:\n• **ROA decreases** because interest expense reduces net income while total assets stay roughly the same.\n• **Taxes decline** because interest is tax-deductible, reducing taxable income.\n• Depreciation is unaffected since no new fixed assets are purchased."
    },
    {
        "id": 21,
        "chapter": 4,
        "topic": "ROE & Leverage",
        "question": "Bedford Hotels and Breezewood Hotels both have $100 million in total assets and a 10% return on assets (ROA). Each company has a 40% tax rate. However, one has a higher debt ratio and higher interest expense. Which of the following statements is most correct?",
        "options": [
            "The two companies have the same return on equity (ROE).",
            "The company with the higher debt ratio will have a lower return on equity (ROE).",
            "The company with the higher debt ratio will have a higher return on equity (ROE).",
            "The company with the higher interest expense will have a higher net income."
        ],
        "correct": 2,
        "explanation": "**ROE = Net Income ÷ Equity**. With higher debt (leverage), equity is smaller, so even though net income might be slightly lower due to interest, the **equity multiplier effect** dominates. The DuPont equation shows: ROE = ROA × Equity Multiplier. A higher debt ratio means a higher equity multiplier, which amplifies ROE — this is the concept of **financial leverage**."
    },
    {
        "id": 22,
        "chapter": 4,
        "topic": "Price/Earnings Ratio",
        "question": "Other things held constant, which of the following alternatives would increase a company's P/E ratio?",
        "options": [
            "The company's stock price increases.",
            "The company's expected growth rate increases.",
            "The company's notes payable increase.",
            "Statements a and b are correct."
        ],
        "correct": 3,
        "explanation": "The **P/E ratio = Stock Price ÷ Earnings Per Share**.\n\n• If stock price **increases** while EPS stays constant, P/E rises.\n• Higher **expected growth** makes investors willing to pay more per dollar of current earnings, increasing P/E.\n• Notes payable changes don't directly increase P/E."
    },
    {
        "id": 23,
        "chapter": 4,
        "topic": "Total Assets Turnover",
        "question": "Rappaport Corp.'s sales last year were $320,000, and its total assets were $160,000. What was its total assets turnover ratio (TATO)?",
        "options": [
            "2.0",
            "3.2",
            "1.6",
            "1.2"
        ],
        "correct": 0,
        "explanation": "**Total Assets Turnover (TATO) = Sales ÷ Total Assets**\n\n• TATO = $320,000 ÷ $160,000 = **2.0**\n\nThis means the company generates $2 in sales for every $1 of assets — a measure of asset efficiency."
    },
    {
        "id": 24,
        "chapter": 4,
        "topic": "Debt Ratio",
        "question": "Tapley Dental Associates has total assets of $400 million. Its balance sheet shows $50 million in current liabilities, $150 million in long-term debt, and $200 million in common equity. It has 800 outstanding shares of preferred stock, each with a par value of $100 and a market price of $110. What is its debt ratio, in millions?",
        "options": [
            "35.5%",
            "42.1%",
            "50.0%",
            "56.3%"
        ],
        "correct": 2,
        "explanation": "**Debt Ratio = Total Debt ÷ Total Assets**\n\n• Total Debt = Current Liabilities + Long-term Debt = $50M + $150M = $200M\n• Debt Ratio = $200M ÷ $400M = **50.0%**\n\nPreferred stock is treated as equity here. The debt ratio shows what percentage of assets is financed by debt."
    },
    {
        "id": 25,
        "chapter": 4,
        "topic": "Profit Margin",
        "question": "Faldo Corp. had the following data for the year. What was Faldo's profit margin? Net income: $250; Sales: $2,000; Total assets: $1,500; Debt ratio: 60%; TIE: 5.0×.",
        "options": [
            "12.5%",
            "14.7%",
            "9.9%",
            "16.2%"
        ],
        "correct": 0,
        "explanation": "**Profit Margin = Net Income ÷ Sales**\n\n• Profit Margin = $250 ÷ $2,000 = **12.5%**\n\nThe profit margin tells you what percentage of each dollar of revenue the company keeps as profit after all expenses."
    },
    {
        "id": 26,
        "chapter": 4,
        "topic": "DuPont ROE",
        "question": "A firm has a profit margin of 3% and an equity multiplier of 2.2. Its sales are $200 million and it has total assets of $100 million. What is its ROE?",
        "options": [
            "13.2%",
            "8.5%",
            "9.8%",
            "12.4%"
        ],
        "correct": 0,
        "explanation": "**DuPont Equation: ROE = Profit Margin × Total Assets Turnover × Equity Multiplier**\n\n• Profit Margin = 3%\n• TATO = Sales ÷ Assets = $200M ÷ $100M = 2.0\n• Equity Multiplier = 2.2\n• ROE = 0.03 × 2.0 × 2.2 = **13.2%**\n\nThe DuPont equation decomposes ROE into profitability, efficiency, and leverage."
    },
    {
        "id": 27,
        "chapter": 4,
        "topic": "ROE Calculation",
        "question": "Last year Urbana Corp. had $197,500 of assets, $307,500 of sales, $19,575 of net income, and a debt-to-total-assets ratio of 42.5%. The new CFO believes a new computer program will enable the firm to reduce costs and thus raise net income to $33,000. Assets, sales, and the debt ratio will not be affected. By how much would the cost reduction improve the ROE?",
        "options": [
            "9.01%",
            "11.82%",
            "10.41%",
            "12.94%"
        ],
        "correct": 1,
        "explanation": "**ROE = Net Income ÷ Equity**\n\n• Equity = Assets × (1 − Debt Ratio) = $197,500 × 0.575 = $113,562.50\n• Old ROE = $19,575 ÷ $113,562.50 = 17.24%\n• New ROE = $33,000 ÷ $113,562.50 = 29.06%\n• Change in ROE = 29.06% − 17.24% = **11.82%**"
    },
    {
        "id": 28,
        "chapter": 4,
        "topic": "Return on Equity",
        "question": "Garvin Enterprises' ROE last year was only 3%; management wants to raise it to 20%. The firm plans to use the DuPont system. Profit margin = 10%, TATO = 1.8. If the profit margin and total assets stay the same, the equity multiplier must be:",
        "options": [
            "0.88",
            "1.11",
            "0.56",
            "None of the above"
        ],
        "correct": 1,
        "explanation": "**DuPont: ROE = PM × TATO × Equity Multiplier**\n\n• Target ROE = 20%\n• 0.20 = 0.10 × 1.8 × EM\n• 0.20 = 0.18 × EM\n• EM = 0.20 ÷ 0.18 = **1.11**\n\nThe equity multiplier reflects how much leverage (debt) the firm uses."
    },
    {
        "id": 29,
        "chapter": 4,
        "topic": "Equity Multiplier & Debt Ratio",
        "question": "A firm that has an equity multiplier of 4.0 will have a debt ratio of",
        "options": [
            "4.00",
            "3.00",
            "1.00",
            "0.75"
        ],
        "correct": 3,
        "explanation": "**Equity Multiplier = Total Assets ÷ Equity = 1 ÷ (1 − Debt Ratio)**\n\n• 4.0 = 1 ÷ (1 − DR)\n• 1 − DR = 0.25\n• DR = **0.75**\n\nAn equity multiplier of 4 means only 25% of assets are financed with equity, so 75% is financed with debt."
    },
    {
        "id": 30,
        "chapter": 4,
        "topic": "DuPont Profit Margin",
        "question": "The Merriam Company has determined that its return on equity is 15 percent. Management is interested in the various components that went into this calculation. You are given: total liabilities/total assets = 0.35 and total assets turnover = 2.8. What is the profit margin?",
        "options": [
            "3.48%",
            "5.42%",
            "6.96%",
            "2.45%"
        ],
        "correct": 0,
        "explanation": "**DuPont: ROE = PM × TATO × Equity Multiplier**\n\n• Debt ratio = 0.35, so Equity ratio = 0.65\n• Equity Multiplier = 1 ÷ 0.65 = 1.5385\n• 0.15 = PM × 2.8 × 1.5385\n• PM = 0.15 ÷ 4.308 = **3.48%**"
    },
    {
        "id": 31,
        "chapter": 4,
        "topic": "Days Sales Outstanding",
        "question": "Calculate the DSO (days sales outstanding) ratio.",
        "options": [
            "7.83",
            "8.4",
            "55.1",
            "36.7"
        ],
        "correct": 0,
        "explanation": "**DSO = Accounts Receivable ÷ (Annual Sales ÷ 365)**\n\nDSO measures the average number of days it takes to collect payment after a sale. A lower DSO means faster collection. The calculated DSO here is **7.83 days**, indicating very efficient receivables collection."
    },
    {
        "id": 32,
        "chapter": 4,
        "topic": "Inventory Turnover",
        "question": "Calculate the inventory turnover ratio.",
        "options": [
            "27.23",
            "13.3",
            "55.43",
            "11.67"
        ],
        "correct": 3,
        "explanation": "**Inventory Turnover = COGS (or Sales) ÷ Inventory**\n\nThis ratio measures how many times inventory is sold and replaced over a period. A turnover of **11.67** means the company sells through its entire inventory roughly 11.67 times per year. Higher turnover generally indicates efficient inventory management."
    },
    {
        "id": 33,
        "chapter": 4,
        "topic": "Return on Equity",
        "question": "Calculate the return on equity (ROE) for MaxCorp.",
        "options": [
            "20.4%",
            "17.8%",
            "22.4%",
            "27.8%"
        ],
        "correct": 3,
        "explanation": "**ROE = Net Income ÷ Total Common Equity**\n\nROE measures the return generated on shareholders' investment. MaxCorp's ROE of **27.8%** indicates strong profitability relative to equity — meaning for every dollar shareholders have invested, the company generates about 28 cents in profit."
    },

    # ──── British Pub Corporation Questions (34-37) ────
    {
        "id": 34,
        "chapter": 4,
        "topic": "Current Ratio",
        "question": "The British Pub Corporation — What was British Pub's current ratio for 199X?\n\nIncome Statement: Net sales $1,025 | COGS $682 | EBITDA $343 | Depreciation $31 | Operating exp $103 | Admin exp $127 | EBIT $82 | Interest $27 | EBT $55 | Taxes $17 | Net income $38\n\nBalance Sheet: Cash $61 | AR $286 | Inventory $354 | Current assets $701 | Net fixed assets $802 | Total assets $1,503\nNotes payable $223 | AP $152 | Accruals $32 | Current liab $407 | LT debt $306 | Common stock $102 | RE $688 | Total L&E $1,503\n\n68,000 shares outstanding.",
        "options": [
            "0.55",
            "1.73",
            "1.02",
            "1.37"
        ],
        "correct": 1,
        "explanation": "**Current Ratio = Current Assets ÷ Current Liabilities**\n\n• Current Assets = $701K\n• Current Liabilities = $407K\n• Current Ratio = $701 ÷ $407 = **1.72 ≈ 1.73**\n\nA current ratio above 1 means the company has more current assets than current liabilities."
    },
    {
        "id": 35,
        "chapter": 4,
        "topic": "Return on Assets",
        "question": "What was British Pub's return on total assets for 199X?",
        "options": [
            "2.53%",
            "3.47%",
            "4.81%",
            "6.73%"
        ],
        "correct": 0,
        "explanation": "**ROA = Net Income ÷ Total Assets**\n\n• Net Income = $38K\n• Total Assets = $1,503K\n• ROA = $38 ÷ $1,503 = **2.53%**\n\nROA shows how efficiently a company uses its assets to generate profit."
    },
    {
        "id": 36,
        "chapter": 4,
        "topic": "Return on Equity",
        "question": "What was British Pub's return on owners' equity in 199X?",
        "options": [
            "4.81%",
            "5.93%",
            "6.75%",
            "8.37%"
        ],
        "correct": 0,
        "explanation": "**ROE = Net Income ÷ Total Common Equity**\n\n• Net Income = $38K\n• Common Equity = Common Stock + Retained Earnings = $102 + $688 = $790K\n• ROE = $38 ÷ $790 = **4.81%**"
    },
    {
        "id": 37,
        "chapter": 4,
        "topic": "Book Value Per Share",
        "question": "What was British Pub's book value per share at year-end 199X?",
        "options": [
            "$7.74",
            "$8.29",
            "$11.62",
            "$11.90"
        ],
        "correct": 2,
        "explanation": "**Book Value Per Share = Total Common Equity ÷ Shares Outstanding**\n\n• Common Equity = $102 + $688 = $790K = $790,000\n• Shares = 68,000\n• BVPS = $790,000 ÷ 68,000 = **$11.62**"
    },

    # ──── Sebring Corporation Questions (38-40) ────
    {
        "id": 38,
        "chapter": 3,
        "topic": "NOPAT",
        "question": "Sebring Corporation — What is Sebring's net operating profit after taxes (NOPAT) for 2013?\n\nIncome: Sales $3,600M | Op costs $3,060M | EBITDA $540M | D&A $90M | EBIT $450M | Interest $65M | EBT $385M | Taxes(40%) $154M | NI $231M\nBalance Sheet (2013): Current assets $1,116M | Net fixed assets $900M | Total assets $2,016M\nCL: AP $324M | Notes payable $201M | Accruals $216M | Total CL $741M | LT bonds $450M | Common stock $150M | RE $675M\nAfter-tax cost of capital: 10%",
        "options": [
            "$150,000,000",
            "$225,000,000",
            "$270,000,000",
            "$375,000,000"
        ],
        "correct": 2,
        "explanation": "**NOPAT = EBIT × (1 − Tax Rate)**\n\n• EBIT = $450M\n• Tax Rate = 40%\n• NOPAT = $450M × 0.60 = **$270M**\n\nNOPAT represents the profit generated from operations after taxes, ignoring the effects of financing (interest). It's a key component in calculating Economic Value Added (EVA)."
    },
    {
        "id": 39,
        "chapter": 3,
        "topic": "Net Operating Working Capital",
        "question": "What is Sebring's net operating working capital for 2013?",
        "options": [
            "$540,000,000",
            "$576,000,000",
            "$750,000,000",
            "$985,000,000"
        ],
        "correct": 1,
        "explanation": "**NOWC = Current Assets − (Current Liabilities − Notes Payable)**\n\n• Current Assets = $1,116M\n• Current Liabilities = $741M\n• Notes Payable = $201M (excluded — interest-bearing)\n• Operating CL = $741M − $201M = $540M\n• NOWC = $1,116M − $540M = **$576M**"
    },
    {
        "id": 40,
        "chapter": 3,
        "topic": "Free Cash Flow",
        "question": "What is Sebring's free cash flow for 2013?",
        "options": [
            "$85,000,000",
            "$146,000,000",
            "$249,000,000",
            "$255,000,000"
        ],
        "correct": 2,
        "explanation": "**FCF = NOPAT − Net Investment in Operating Capital**\n\n• NOPAT = $270M\n• NOWC 2013 = $576M, NOWC 2012 = $1,080M − ($605M − $155M) = $630M → ΔNOWC = −$54M\n• Net Fixed Assets: 2013 = $900M, 2012 = $825M → ΔFA = $75M, but gross = $990M − $825M = $165M → Net investment in op capital = ΔNOWC + ΔNet FA = −$54M + $75M = $21M\n• FCF = $270M − $21M = **$249M**\n\nFCF is the cash available to distribute to all investors."
    },
    {
        "id": 41,
        "chapter": 3,
        "topic": "Financial Statements",
        "question": "Which of the following statements is CORRECT?",
        "options": [
            "The four most important financial statements provided in the annual report are the balance sheet, income statement, cash budget, and the statement of stockholders' equity.",
            "The balance sheet gives us a picture of the firm's financial position at a point in time.",
            "The income statement gives us a picture of the firm's financial position at a point in time.",
            "The statement of cash flows tells us how much cash the firm must pay out in interest during the year."
        ],
        "correct": 1,
        "explanation": "The **balance sheet** is a **snapshot** of the firm's financial position at a specific point in time — it shows assets, liabilities, and equity on a given date. The income statement shows performance *over a period* (not at a point in time). The four key statements are: balance sheet, income statement, statement of cash flows, and statement of stockholders' equity (not cash budget)."
    },
    {
        "id": 42,
        "chapter": 3,
        "topic": "EVA & MVA",
        "question": "Which of the following statements is CORRECT?",
        "options": [
            "MVA stands for market value added, and it is defined as: MVA = (Shares outstanding)(Stock price) + Book value of common equity.",
            "The primary difference between EVA and accounting net income is that when net income is calculated, a deduction is made to account for the cost of common equity, whereas EVA represents net income before deducting the cost of the equity capital the firm uses.",
            "MVA gives us an idea about how much value a firm's management has added during the last year.",
            "EVA stands for economic value added, and it is defined as: EVA = NOPAT − (Investor-supplied oper. capital)(AT cost of capital %)"
        ],
        "correct": 3,
        "explanation": "**EVA = NOPAT − (Investor-Supplied Operating Capital × After-Tax Cost of Capital)**\n\nEVA measures whether a firm is earning more than its cost of capital. If EVA > 0, the firm is creating value. \n\n• MVA = Market Value − Book Value (not +)\n• EVA deducts capital costs; net income does not (statement b is backward)\n• MVA is cumulative, not just last year"
    },
    {
        "id": 43,
        "chapter": 3,
        "topic": "After-Tax Operating Income",
        "question": "Kwok Enterprises has the following income statement. How much after-tax operating income does the firm have?\n\nSales $2,250 | Costs $1,400 | Depreciation $250 | EBIT $600 | Interest $70 | EBT $530 | Taxes(40%) $212 | Net income $318",
        "options": [
            "$325",
            "$342",
            "$360",
            "$378"
        ],
        "correct": 2,
        "explanation": "**After-tax operating income = EBIT × (1 − Tax Rate)**\n\n• EBIT = $600\n• Tax Rate = 40%\n• EBIT(1 − T) = $600 × 0.60 = **$360**\n\nThis is the same as NOPAT. We apply the tax rate directly to EBIT (ignoring interest) to get the operating profit available if the firm had no debt."
    },
    {
        "id": 44,
        "chapter": 4,
        "topic": "Current Ratio",
        "question": "Considered alone, which of the following would increase a company's current ratio?",
        "options": [
            "An increase in net fixed assets.",
            "An increase in accrued liabilities.",
            "An increase in notes payable.",
            "An increase in accounts receivable."
        ],
        "correct": 3,
        "explanation": "**Current Ratio = Current Assets ÷ Current Liabilities**\n\nAn increase in **accounts receivable** increases current assets without changing current liabilities, so the ratio goes up. Fixed assets don't affect current ratio. Both accrued liabilities and notes payable increase current liabilities, which would *decrease* the ratio."
    },
    {
        "id": 45,
        "chapter": 4,
        "topic": "Total Assets Turnover",
        "question": "Ryngard Corp's sales last year were $38,000, and its total assets were $16,000. What was its total assets turnover ratio (TATO)?",
        "options": [
            "2.04",
            "2.14",
            "2.26",
            "2.38"
        ],
        "correct": 3,
        "explanation": "**TATO = Sales ÷ Total Assets**\n\n• TATO = $38,000 ÷ $16,000 = **2.375 ≈ 2.38**\n\nThis means the firm generates $2.38 in revenue for every $1 invested in assets."
    },
    {
        "id": 46,
        "chapter": 4,
        "topic": "Debt Ratio Target",
        "question": "Beranek Corp has $720,000 of assets, and it uses no debt — it is financed only with common equity. The new CFO wants to employ enough debt to raise the debt/assets ratio to 40%, using the proceeds from borrowing to buy back common stock at its book value. How much must the firm borrow to achieve the target debt ratio?",
        "options": [
            "$273,600",
            "$288,000",
            "$302,400",
            "$317,520"
        ],
        "correct": 1,
        "explanation": "**Amount Borrowed = Target Debt Ratio × Total Assets**\n\n• Target Debt Ratio = 40%\n• Total Assets = $720,000\n• Amount = 0.40 × $720,000 = **$288,000**\n\nSince the borrowed funds are used to buy back stock, total assets remain unchanged. The firm replaces equity with debt."
    },
    {
        "id": 47,
        "chapter": 4,
        "topic": "Basic Earning Power",
        "question": "X-1 Corp's total assets at the end of last year were $405,000 and its EBIT was $52,500. What was its basic earning power (BEP) ratio?",
        "options": [
            "11.70%",
            "12.31%",
            "12.96%",
            "13.61%"
        ],
        "correct": 2,
        "explanation": "**BEP = EBIT ÷ Total Assets**\n\n• BEP = $52,500 ÷ $405,000 = **12.96%**\n\nThe BEP ratio shows the raw earning power of the company's assets, before the effects of taxes and leverage. It's useful for comparing companies with different tax rates and debt levels."
    },
    {
        "id": 48,
        "chapter": 4,
        "topic": "Times Interest Earned",
        "question": "Ajax Corp's sales last year were $435,000, its operating costs were $362,500, and its interest charges were $12,500. What was the firm's times-interest-earned (TIE) ratio?",
        "options": [
            "4.72",
            "4.97",
            "5.51",
            "5.80"
        ],
        "correct": 3,
        "explanation": "**TIE = EBIT ÷ Interest Expense**\n\n• EBIT = Sales − Operating Costs = $435,000 − $362,500 = $72,500\n• TIE = $72,500 ÷ $12,500 = **5.80×**\n\nThe TIE ratio measures how many times a firm can cover its interest payments with its operating income. A higher ratio means less risk of default."
    },
    {
        "id": 49,
        "chapter": 4,
        "topic": "Market/Book Ratio",
        "question": "Hoagland Corp's stock price at the end of last year was $33.50, and its book value per share was $25.00. What was its market/book ratio?",
        "options": [
            "1.34",
            "1.41",
            "1.48",
            "1.55"
        ],
        "correct": 0,
        "explanation": "**Market/Book Ratio = Stock Price ÷ Book Value Per Share**\n\n• M/B = $33.50 ÷ $25.00 = **1.34**\n\nA M/B ratio > 1 means the market values the company at more than its accounting book value, often reflecting intangible assets, growth prospects, and investor confidence."
    },
    {
        "id": 50,
        "chapter": 4,
        "topic": "DuPont ROE",
        "question": "Precision Aviation had a profit margin of 6.25%, a total assets turnover of 1.5, and an equity multiplier of 1.8. What was the firm's ROE?",
        "options": [
            "15.23%",
            "16.03%",
            "16.88%",
            "17.72%"
        ],
        "correct": 2,
        "explanation": "**DuPont: ROE = Profit Margin × TATO × Equity Multiplier**\n\n• ROE = 6.25% × 1.5 × 1.8 = **16.875% ≈ 16.88%**\n\nThe three components break down ROE into:\n• Profit Margin → profitability\n• TATO → asset efficiency\n• Equity Multiplier → financial leverage"
    },
    {
        "id": 51,
        "chapter": 4,
        "topic": "Dividends Per Share",
        "question": "Helmuth Inc's latest net income was $1,250,000, and it had 225,000 shares outstanding. The company wants to pay out 45% of its income. What dividend per share should it declare?",
        "options": [
            "$2.14",
            "$2.26",
            "$2.38",
            "$2.50"
        ],
        "correct": 3,
        "explanation": "**DPS = EPS × Payout Ratio**\n\n• EPS = Net Income ÷ Shares = $1,250,000 ÷ 225,000 = $5.556\n• DPS = $5.556 × 0.45 = **$2.50**\n\nThe payout ratio determines what fraction of earnings goes to dividends vs. retained earnings."
    },
    {
        "id": 52,
        "chapter": 4,
        "topic": "DuPont Analysis",
        "question": "Last year Rennie Industries had sales of $305,000, assets of $175,000, a profit margin of 5.3%, and an equity multiplier of 1.2. The CFO believes the company could reduce its assets by $51,000 without affecting either sales or costs. Had it reduced its assets by this amount, and had the debt/assets ratio, sales, and costs remained constant, how much would the ROE have changed?",
        "options": [
            "4.10%",
            "4.56%",
            "5.01%",
            "5.52%"
        ],
        "correct": 1,
        "explanation": "**DuPont: ROE = PM × TATO × Equity Multiplier**\n\n**Old:**\n• TATO = $305,000 ÷ $175,000 = 1.743\n• ROE = 5.3% × 1.743 × 1.2 = 11.08%\n\n**New (assets reduced by $51,000):**\n• New Assets = $175,000 − $51,000 = $124,000\n• New TATO = $305,000 ÷ $124,000 = 2.460\n• New ROE = 5.3% × 2.460 × 1.2 = 15.64%\n\n• **Change = 15.64% − 11.08% = 4.56%**\n\nReducing assets while maintaining sales improves asset efficiency (TATO), which increases ROE."
    },
]

# Helper: get questions filtered by chapter
def get_questions_by_chapter(chapter: int):
    return [q for q in QUESTIONS if q["chapter"] == chapter]

# Helper: get random subset
def get_random_questions(n: int = 10):
    import random
    return random.sample(QUESTIONS, min(n, len(QUESTIONS)))

CHAPTERS = {
    1: "Overview of Financial Management",
    2: "Financial Markets and Institutions",
    3: "Financial Statements, Cash Flow, and Taxes",
    4: "Analysis of Financial Statements (Ratios)",
}
