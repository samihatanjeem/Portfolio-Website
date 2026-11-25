"""
Central place for all your portfolio content.
Edit the values below - the pages read from here, so you never
need to touch page layout code just to update your info.
"""

PROFILE = {
    "name": "Samiha Tanjeem",
    "title": "Data Analyst",
    "tagline": "Small talk isn't my thing, but data storytelling is!<br>I run on milk tea and curiosity to get there.",
    "bio": (
        "I am a MSc Business Analytics graduate from East Texas A&M University "
        "(GPA 3.90) who enjoys exploring data, connecting the dots, and "
        "solving real-world business problems.\n\n"
        "My professional journey began in the Textile industry, where working "
        "with inventory data and business operations sparked my interest in "
        "analytics. I then worked as a Marketing Data Analyst Intern at a "
        "healthcare tech company, analyzing patient CRM data, evaluating "
        "campaign performance, and assisting in tracking marketing KPIs while "
        "contributing to an increase in brand recognition. Most recently, I "
        "worked as a Data Research Analyst Intern at a real estate tech company, "
        "transforming customer data into actionable recommendations to support "
        "its AI-powered app development.\n\n"
        "My curiosity for data goes beyond work. I recently built an Agentic "
        "AI Stock Analyst web application combining LLMs, live financial data, "
        "RAG, and predictive modeling.\n\n"
        "I primarily work with SQL, Python, R, and BI tools. I'm currently "
        "exploring opportunities in Data Analytics, Business Intelligence, "
        "Data Engineering, and Data Science. I'm always excited to learn, "
        "experiment with technology, and turn ideas into something useful."
    ),
    "location": "Austin, TX",
    "email": "samihatanjeem@gmail.com",
    "phone": "(737) 288-4846",
    "resume_path": "assets/resume.pdf",
    "profile_image": "assets/profile.jpg",
    "profile_cutout_image": "assets/samiha.png",
}

SOCIAL_LINKS = {
    "GitHub": "https://github.com/samihatanjeem",
    "LinkedIn": "https://linkedin.com/in/samihatanjeem/",
    "Email": f"https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}",
}

PROJECTS = [
    {
        "title": "AI Stock Analyst Agent",
        "date": "Sep 2026",
        "description": (
            "Built and deployed a LangGraph agent powered by Gemini that "
            "autonomously selects among 5 tools per question (live financial "
            "statements, market quotes, news search, RAG over my capstone paper "
            "in MongoDB Atlas, and my fitted OLS model predicting next-year ROA "
            "from 7 financial ratios) to generate grounded stock analyses in a "
            "live Streamlit app, with multi-model fallback for reliability and "
            "automatic flags when a company falls outside the regression's "
            "training range."
        ),
        "image": "assets/projects/stock-analyst-agent.png",
        "bullets": [
            "Designed an LLM agent on the Gemini API that decides per question "
            "which of 5 tools to call (Yahoo Finance statements, Finnhub API "
            "quotes and analyst trends, DuckDuckGo news, a RAG search of my "
            "capstone paper, and my OLS model), with a three-model fallback "
            "chain and 15-second timeouts for reliability.",
            "Built the RAG pipeline end to end: chunked my capstone paper "
            "(800-character chunks, 120 overlap), embedded it with Gemini API "
            "embeddings at 768 dimensions, and indexed it in MongoDB Atlas "
            "Vector Search so the LLM answers from retrieved passages.",
            "Turned my fitted OLS regression (279 firm-year observations, 182 "
            "U.S. public companies) into a live ROA prediction tool that flags "
            "out-of-sample extrapolation, and deployed the app publicly on "
            "Streamlit Community Cloud with streaming answers and a live "
            "TradingView chart.",
        ],
        "tags": [
            "LLM", "RAG", "Gemini API", "Finnhub API", "MongoDB Atlas",
            "Python", "LangGraph", "LangChain", "Vector Search",
            "OLS Regression", "Tool Calling", "Streamlit", "yfinance",
        ],
        "demo_url": "https://stock-analyst-ai-agent.streamlit.app/",
        "repo_url": "https://github.com/samihatanjeem/Stock-Analyst-AI-Agent",
    },
    {
        "title": "US Stocks Predictive Analysis",
        "date": "Feb 2026",
        "description": (
            "Built and compared 5 regression models in R: pooled OLS with HC3 "
            "robust standard errors, a single-variable ROA baseline, and three "
            "firm-size-stratified models on a self-engineered panel dataset "
            "restructured from 1M+ raw SEC XBRL rows, with 7 engineered financial "
            "ratios and full multicollinearity, heteroskedasticity, and "
            "autocorrelation diagnostics."
        ),
        "image": "https://github.com/user-attachments/assets/d1a35682-e939-4262-ae06-9ef85e9afb87",
        "bullets": [
            "Cleaned SEC XBRL filings from 12,129 companies down to a validated "
            "panel of 279 firm-year observations across 182 firms, engineering "
            "7 financial ratios (ROA, ROE, debt ratio, asset turnover, and more).",
            "Built OLS regression models reaching R² = 0.673, finding current-year "
            "ROA the strongest predictor of next-year performance (β = 1.261) and "
            "debt ratio a consistent drag on it (β = −0.619) across firm sizes.",
            "Ran full diagnostics (multicollinearity, heteroskedasticity, "
            "autocorrelation) and found the simpler single-variable baseline "
            "actually beat the full 7-predictor model on holdout data — a real "
            "lesson in not over-fitting with limited observations.",
        ],
        "tags": ["R", "dplyr", "tidyr", "ggplot2", "sandwich", "lmtest", "corrplot"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/U.S-Stocks-Predictive-Analysis",
    },
    {
        "title": "Fast Food Giants EDA & Sales Regression",
        "date": "Jan 2025",
        "description": (
            "Performed exploratory data analysis and multivariate regression on "
            "U.S. fast-food market data to predict total sales and find key "
            "relationships among store count, unit sales, and revenue."
        ),
        "image": "https://github.com/user-attachments/assets/bd953db6-cb6b-4a80-86ce-7adf7ff65576",
        "bullets": [
            "Analyzed systemwide sales across the top 50 U.S. fast-food chains, "
            "finding store count and systemwide sales correlated at r ≈ 0.71.",
            "Built a multivariate regression (store count + avg. unit sales → "
            "total sales) reaching R² = 0.64, using backward elimination to "
            "select features and correlation heatmaps to guide the analysis.",
            "Flagged Chick-fil-A as a standout outlier — high systemwide revenue "
            "despite running far fewer locations than its closest competitors.",
        ],
        "tags": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/Fast-Food_served_with_Regression",
    },
    {
        "title": "Python ML Analytics Workspace",
        "date": "May 2024",
        "description": (
            "Built a menu-driven Python and machine learning workspace for data "
            "cleaning, visualization, exploratory analysis, and predictive "
            "modeling with linear regression and feature engineering."
        ),
        "image": "https://github.com/user-attachments/assets/ee080062-b646-42eb-9e55-193cd7892347",
        "bullets": [
            "Built a 15-notebook Python workspace spanning the full workflow: "
            "data cleaning, EDA, visualization, and regression modeling.",
            "Ran a salary-prediction exercise testing technical, communication, "
            "and leadership scores as predictors — a hands-on lesson in reading "
            "regression output honestly when a feature doesn't explain the "
            "outcome, rather than forcing a fit.",
            "Built a second mini-project covering outlier detection and a full "
            "data-cleaning pipeline end to end.",
        ],
        "tags": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/Python-ML-Analytics-Workspace",
    },
    {
        "title": "MTCars-Titanic-R-Linear-Regression",
        "date": "May 2024",
        "description": (
            "Built multiple linear and logistic regression models in R with "
            "diagnostics, performance evaluation, and visualization to interpret "
            "predictors of car fuel efficiency and Titanic passenger survival "
            "across genders and classes."
        ),
        "image": "https://github.com/user-attachments/assets/bf676880-17db-4fa3-9822-99eeea0e9eef",
        "bullets": [
            "Modeled car fuel efficiency in R, finding vehicle weight the "
            "dominant factor (−4.36 mpg per unit, p < 0.001) while horsepower "
            "and quarter-mile time weren't statistically significant — the "
            "model explained 83% of variance (Adj. R² = 0.8171).",
            "Built a logistic regression on Titanic survival: sex was the "
            "strongest predictor (women had ~11x higher odds of survival), with "
            "class and age also shaping outcomes.",
            "Evaluated the classifier with a confusion matrix and ROC curve, "
            "reaching ~77% accuracy with good discrimination.",
        ],
        "tags": ["R", "ggplot2", "caret", "lm", "glm", "pROC"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/MTCars-Titanic-R-Linear-Regression",
    },
]

SKILLS = {
    "Programming Languages": ["Python", "R", "Spark", "SQL", "Java"],
    "Data Analysis & Visualization": [
        "Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Plotly", "PySpark",
        "Excel", "IBM SPSS", "STATA", "Power BI", "Tableau", "Looker Studio"
    ],
    "Developer Tools & Platforms": [
        "MS Visual Studio", "MS SQL Server", "Git", "GitHub", "Snowflake", "Azure" "Docker", "VS Code",
        "Jupyter", "SQL Workbench", "AWS", "Azure", "GCP", "Microsoft 365", "ETL"
    ],
}

CERTIFICATIONS = [
    {
        "title": "AI Foundations – Machine Learning",
        "image": "assets/certifications/ai-foundations-ml.png",
    },
    {
        "title": "Machine Learning with Python",
        "image": "assets/certifications/ml-with-python.png",
    },
    {
        "title": "Business Analysis – Essential Tools and Techniques",
        "image": "assets/certifications/business-analysis-tools.png",
    },
    {
        "title": "Learning Data Analytics – Foundations",
        "image": "assets/certifications/data-analytics-foundations.png",
    },
    {
        "title": "Machine Learning and AI Foundations",
        "image": "assets/certifications/ml-and-ai-foundations.png",
    },
]

EXPERIENCE = [
    {
        "role": "Data Research Analyst Intern",
        "organization": "PRYPCO",
        "logo": "assets/prypco.png",
        "period": "May 2025 – Jul 2025",
        "impact": "13 prioritized feature recommendations helped the product team decide what to build first for PRYPCO's AI-enabled agent app.",
        "bullets": [
            "Supported the development of the company's AI-powered real estate "
            "agent app by conducting customer research across 5 real estate "
            "product lines (PRYPCO Mint, Blocks, Mortgage, One, and Golden Visa), "
            "analyzing 13 interviews with property buyers, sellers, and investors.",
            "Cleaned and structured 150 qualitative and quantitative data points, "
            "performed exploratory data analysis (EDA) using Python, Pandas, "
            "Excel, and Scikit-learn, created 13 customer journey flows using "
            "Plotly and Matplotlib, and visualized customer pain points and gain "
            "points using Seaborn.",
            "Translated analytical findings into 13 prioritized feature "
            "recommendations, ranking customer pain points by frequency, severity, "
            "and customer segment to inform the product roadmap and guide "
            "application feature development.",
        ],
    },
    {
        "role": "Marketing Data Analyst Intern",
        "organization": "Praava Health",
        "logo": "assets/praava.jpg",
        "period": "Sep 2022 – Jan 2023",
        "impact": "Drove a 27% increase in brand recognition and helped launch the company's first TikTok channel.",
        "bullets": [
            "Analyzed healthcare marketing campaign performance using Excel, pivot "
            "tables, regression analysis, and ANOVA; assisted in tracking marketing "
            "KPIs through Looker Studio and analyzing patient CRM data using Power "
            "BI to support data-driven marketing decisions.",
            "Analyzed competitor strategies and audience engagement data to identify "
            "growth opportunities, launched the company's first TikTok channel, and "
            "contributed to a 27% increase in brand recognition.",
            "Collected and structured patient feedback data using Qualtrics and "
            "SurveyMonkey, assisted in evaluating Customer Satisfaction Scores "
            "(CSAT) and Customer Acquisition Cost (CAC), and trained frontline "
            "healthcare staff on standardized data collection practices to improve "
            "data quality and consistency.",
            "Achievement: Awarded Best Intern at Praava Health for outstanding "
            "performance during the internship among 12 multicultural interns.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "Master of Science in Business Analytics (MSBA)",
        "institution": "East Texas A&M University",
        "logo": "assets/etamu.png",
        "period": "Aug 2026",
        "email": "stanjeem@lemail.tamuc.edu",
        "description": "GPA: 3.90",
        "courses": [
            "Database Management",
            "Business Analytics Programming",
            "Data Warehousing",
            "Business Data Science",
            "Applied Decision Modeling",
            "Analytics for Managers",
            "Project Management",
            "Marketing & Management Analytics",
        ],
    },
    {
        "degree": "Bachelor of Business Administration (BBA) in Marketing",
        "institution": "North South University",
        "logo": "assets/nsu.png",
        "period": "Dec 2022",
        "email": "samiha.tanjeem@northsouth.edu",
        "description": "",
        "courses": [
            "Computer Information Systems",
            "Applied Business Mathematics",
            "Applied Statistics",
            "Marketing Analytics",
            "Marketing Research",
            "E-Business",
            "Digital Marketing & Social Networks for Business",
            "Operations and Supply Chain Management",
            "Financial Accounting",
            "Managerial Accounting",
        ],
    },
]
