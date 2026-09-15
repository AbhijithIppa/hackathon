"""Demo data for StatGrow AI POC — India's Official Statistical System."""

from __future__ import annotations

COMPETENCIES = [
    "Statistical Methods",
    "Data Collection",
    "Data Analysis",
    "Survey Methodology",
    "Sampling Techniques",
    "Data Visualization",
    "Statistical Software",
    "Data Quality",
    "Official Statistics",
    "Census & Surveys",
    "Economic Statistics",
    "Social Statistics",
    "Data Governance",
    "AI & Machine Learning",
]

# Default user competency profile (percentages)
DEFAULT_PROFILE = {
    "Statistical Methods": 82,
    "Data Analysis": 71,
    "Data Visualization": 48,
    "Sampling Techniques": 38,
    "Data Quality": 64,
    "Data Governance": 55,
    "Survey Methodology": 60,
    "Official Statistics": 70,
    "Census & Surveys": 58,
    "Economic Statistics": 65,
    "Social Statistics": 62,
    "Statistical Software": 52,
    "Data Collection": 68,
    "AI & Machine Learning": 40,
}

LEARNING_MATERIALS = [
    {
        "id": "mat_sampling",
        "title": "Survey Sampling Fundamentals",
        "topics": [
            "Probability Sampling",
            "Stratified Sampling",
            "Cluster Sampling",
            "Sampling Error",
        ],
        "competencies": ["Sampling Techniques", "Survey Methodology", "Statistical Methods"],
        "difficulty": "Intermediate",
        "summary": (
            "Core principles of survey sampling for official statistics, including "
            "stratified and cluster designs used in NSS and Census operations."
        ),
    },
    {
        "id": "mat_official",
        "title": "Introduction to Official Statistics",
        "topics": ["UN Fundamental Principles", "NSO Role", "SDG Indicators", "Data Stewardship"],
        "competencies": ["Official Statistics", "Data Governance"],
        "difficulty": "Beginner",
        "summary": "Foundations of India's official statistical system and international standards.",
    },
    {
        "id": "mat_quality",
        "title": "Data Quality Frameworks",
        "topics": ["Accuracy", "Timeliness", "Coherence", "Accessibility", "DQAF"],
        "competencies": ["Data Quality", "Data Governance"],
        "difficulty": "Intermediate",
        "summary": "IMF DQAF-aligned quality dimensions for statistical products.",
    },
    {
        "id": "mat_econ",
        "title": "Economic Statistics Essentials",
        "topics": ["National Accounts", "CPI/WPI", "IIP", "Trade Statistics"],
        "competencies": ["Economic Statistics", "Statistical Methods"],
        "difficulty": "Intermediate",
        "summary": "Key economic indicators produced by MoSPI and related agencies.",
    },
    {
        "id": "mat_viz",
        "title": "Government Data Visualization",
        "topics": ["Dashboard Design", "Chart Selection", "Accessibility", "Storytelling"],
        "competencies": ["Data Visualization", "Data Analysis"],
        "difficulty": "Beginner",
        "summary": "Visual communication of official statistics for policy audiences.",
    },
    {
        "id": "mat_census",
        "title": "Census Methodology",
        "topics": ["Enumeration", "House Listing", "Post-Enumeration Survey", "Coverage"],
        "competencies": ["Census & Surveys", "Survey Methodology", "Sampling Techniques"],
        "difficulty": "Advanced",
        "summary": "Methodology underpinning India's Population Census operations.",
    },
]

QUIZ_BANK = {
    "Sampling Techniques": [
        {
            "question": "Which sampling method divides a population into homogeneous subgroups before selecting samples?",
            "options": [
                "Cluster Sampling",
                "Stratified Sampling",
                "Convenience Sampling",
                "Systematic Sampling",
            ],
            "correct": 1,
            "explanation": (
                "Stratified sampling divides a population into homogeneous subgroups (strata) "
                "and samples from each subgroup to improve precision."
            ),
            "competency": "Sampling Techniques",
            "difficulty": "Medium",
            "type": "MCQ",
        },
        {
            "question": "In NSS household surveys, Primary Sampling Units (PSUs) are typically selected at which stage?",
            "options": [
                "First stage of multi-stage sampling",
                "Only after census enumeration",
                "After non-response adjustment",
                "During data tabulation",
            ],
            "correct": 0,
            "explanation": (
                "Multi-stage designs used in NSS typically select villages/urban blocks as PSUs "
                "in the first stage, then households within selected PSUs."
            ),
            "competency": "Sampling Techniques",
            "difficulty": "Medium",
            "type": "MCQ",
        },
        {
            "question": "Sampling error decreases when sample size increases, all else equal.",
            "options": ["True", "False", "Only for cluster samples", "Only for census"],
            "correct": 0,
            "explanation": "Larger samples generally reduce sampling variance and therefore sampling error.",
            "competency": "Sampling Techniques",
            "difficulty": "Easy",
            "type": "True/False",
        },
        {
            "question": "A state statistical office needs district-level estimates with equal precision. Which approach is most appropriate?",
            "options": [
                "Simple random sample of the entire state",
                "Stratified design with allocation by district",
                "Convenience sampling of accessible districts",
                "Only use census microdata",
            ],
            "correct": 1,
            "explanation": (
                "Stratification by district with appropriate allocation supports reliable "
                "district-level estimates with controlled precision."
            ),
            "competency": "Sampling Techniques",
            "difficulty": "Hard",
            "type": "Scenario Based",
        },
        {
            "question": "Cluster sampling usually increases sampling variance compared to SRS of the same size because:",
            "options": [
                "Clusters are always larger than strata",
                "Units within clusters tend to be similar (intra-cluster correlation)",
                "Clusters cannot be selected randomly",
                "Weights cannot be computed for clusters",
            ],
            "correct": 1,
            "explanation": (
                "Positive intra-cluster correlation reduces effective sample size, "
                "increasing design effect and variance."
            ),
            "competency": "Sampling Techniques",
            "difficulty": "Hard",
            "type": "MCQ",
        },
        {
            "question": "Systematic sampling selects every k-th unit after a random start.",
            "options": ["True", "False", "Only in urban areas", "Only for rare events"],
            "correct": 0,
            "explanation": "Systematic sampling uses a fixed interval after a random starting point.",
            "competency": "Sampling Techniques",
            "difficulty": "Easy",
            "type": "True/False",
        },
        {
            "question": "Design weights in official surveys primarily adjust for:",
            "options": [
                "Software version differences",
                "Unequal selection probabilities",
                "Chart colour palettes",
                "Publication schedules",
            ],
            "correct": 1,
            "explanation": "Design weights compensate for unequal probabilities of selection across units.",
            "competency": "Sampling Techniques",
            "difficulty": "Medium",
            "type": "MCQ",
        },
        {
            "question": "Non-response bias is a form of sampling error.",
            "options": ["True", "False", "Only in panel surveys", "Only in online surveys"],
            "correct": 1,
            "explanation": (
                "Non-response bias is a non-sampling error arising from differences between "
                "respondents and non-respondents."
            ),
            "competency": "Sampling Techniques",
            "difficulty": "Medium",
            "type": "True/False",
        },
    ],
    "Data Analysis": [
        {
            "question": "Which measure is most robust to extreme outliers in income survey data?",
            "options": ["Mean", "Median", "Range", "Maximum"],
            "correct": 1,
            "explanation": "The median is less sensitive to extreme values than the mean.",
            "competency": "Data Analysis",
            "difficulty": "Easy",
            "type": "MCQ",
        },
        {
            "question": "A confidence interval for a survey estimate reflects:",
            "options": [
                "Only non-sampling error",
                "Uncertainty due to sampling variability (and design)",
                "Guaranteed true parameter coverage every time",
                "Data entry accuracy only",
            ],
            "correct": 1,
            "explanation": "Confidence intervals quantify sampling uncertainty under the survey design.",
            "competency": "Data Analysis",
            "difficulty": "Medium",
            "type": "MCQ",
        },
        {
            "question": "You observe a sudden spike in CPI for one month. First analytical check should include:",
            "options": [
                "Publishing without review",
                "Validating source data and seasonal factors",
                "Deleting the observation permanently",
                "Ignoring methodological notes",
            ],
            "correct": 1,
            "explanation": "Official statistics require validation of inputs and methodology before release.",
            "competency": "Data Analysis",
            "difficulty": "Medium",
            "type": "Scenario Based",
        },
    ],
    "Survey Methodology": [
        {
            "question": "A well-designed questionnaire should primarily minimise:",
            "options": [
                "Measurement error and respondent burden",
                "Sample frame size",
                "Use of pilot testing",
                "Training of enumerators",
            ],
            "correct": 0,
            "explanation": "Good questionnaire design reduces measurement error and respondent burden.",
            "competency": "Survey Methodology",
            "difficulty": "Easy",
            "type": "MCQ",
        },
        {
            "question": "Pilot testing is optional for large-scale national surveys.",
            "options": ["True", "False", "Only for CAPI surveys", "Only for opinion polls"],
            "correct": 1,
            "explanation": "Pilot testing is essential to refine instruments and field procedures.",
            "competency": "Survey Methodology",
            "difficulty": "Easy",
            "type": "True/False",
        },
    ],
    "Data Quality": [
        {
            "question": "Which is a core dimension in statistical data quality frameworks?",
            "options": ["Colourfulness", "Timeliness", "Font size", "Slide count"],
            "correct": 1,
            "explanation": "Timeliness is a standard quality dimension alongside accuracy, accessibility, etc.",
            "competency": "Data Quality",
            "difficulty": "Easy",
            "type": "MCQ",
        },
        {
            "question": "Coherence in official statistics means:",
            "options": [
                "All charts use the same colour",
                "Statistics are consistent across sources and over time where expected",
                "Only one agency produces data",
                "Raw microdata is never shared",
            ],
            "correct": 1,
            "explanation": "Coherence concerns consistency across datasets and over time.",
            "competency": "Data Quality",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
    "Data Visualization": [
        {
            "question": "For comparing magnitudes across categories, the most appropriate chart is usually a:",
            "options": ["Pie chart with 20 slices", "Bar chart", "3D exploded pie", "Word cloud"],
            "correct": 1,
            "explanation": "Bar charts make category comparisons clear and precise.",
            "competency": "Data Visualization",
            "difficulty": "Easy",
            "type": "MCQ",
        },
        {
            "question": "Dual-axis charts should be used cautiously because they can mislead interpretation.",
            "options": ["True", "False", "Never true for government data", "Only for maps"],
            "correct": 0,
            "explanation": "Dual axes can distort perceived relationships between series.",
            "competency": "Data Visualization",
            "difficulty": "Medium",
            "type": "True/False",
        },
    ],
    "Official Statistics": [
        {
            "question": "India's nodal agency for official statistics is:",
            "options": [
                "Ministry of Finance only",
                "Ministry of Statistics and Programme Implementation (MoSPI)",
                "RBI exclusively",
                "NITI Aayog only",
            ],
            "correct": 1,
            "explanation": "MoSPI is the nodal ministry for the national statistical system.",
            "competency": "Official Statistics",
            "difficulty": "Easy",
            "type": "MCQ",
        },
    ],
    "Data Governance": [
        {
            "question": "Data stewardship in official statistics emphasises:",
            "options": [
                "Unrestricted public release of all microdata",
                "Responsible management, privacy, and quality of statistical data",
                "Eliminating all metadata",
                "Using only proprietary formats",
            ],
            "correct": 1,
            "explanation": "Stewardship balances access, confidentiality, quality, and accountability.",
            "competency": "Data Governance",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
    "Census & Surveys": [
        {
            "question": "A Post-Enumeration Survey (PES) primarily helps assess:",
            "options": [
                "Printing quality of schedules",
                "Coverage and content errors in census enumeration",
                "Stock market volatility",
                "Website uptime",
            ],
            "correct": 1,
            "explanation": "PES evaluates census coverage and content error.",
            "competency": "Census & Surveys",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
    "Statistical Methods": [
        {
            "question": "In hypothesis testing, a Type I error is:",
            "options": [
                "Failing to reject a false null",
                "Rejecting a true null hypothesis",
                "Using the wrong software",
                "Missing metadata",
            ],
            "correct": 1,
            "explanation": "Type I error is incorrectly rejecting a true null hypothesis.",
            "competency": "Statistical Methods",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
    "Economic Statistics": [
        {
            "question": "CPI primarily measures:",
            "options": [
                "Changes in consumer prices over time",
                "Corporate tax collections",
                "Foreign exchange reserves only",
                "Literacy rates",
            ],
            "correct": 0,
            "explanation": "The Consumer Price Index tracks changes in prices of a consumer basket.",
            "competency": "Economic Statistics",
            "difficulty": "Easy",
            "type": "MCQ",
        },
    ],
    "Social Statistics": [
        {
            "question": "Labour force participation rate is typically calculated as:",
            "options": [
                "Employed / Total population",
                "Labour force / Working-age population",
                "Unemployed / Employed",
                "Households / Villages",
            ],
            "correct": 1,
            "explanation": "LFPR = labour force divided by the working-age (or reference) population.",
            "competency": "Social Statistics",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
    "Statistical Software": [
        {
            "question": "Which practice improves reproducibility of statistical analysis?",
            "options": [
                "Hard-coding undocumented steps in a GUI only",
                "Scripted analysis with versioned code and documented inputs",
                "Deleting intermediate datasets",
                "Avoiding metadata",
            ],
            "correct": 1,
            "explanation": "Scripts, version control, and documentation support reproducible workflows.",
            "competency": "Statistical Software",
            "difficulty": "Easy",
            "type": "MCQ",
        },
    ],
    "Data Collection": [
        {
            "question": "CAPI stands for:",
            "options": [
                "Computer-Assisted Personal Interviewing",
                "Central Agency Public Index",
                "Census Administrative Paper Input",
                "Cluster Analysis Primary Indicator",
            ],
            "correct": 0,
            "explanation": "CAPI is Computer-Assisted Personal Interviewing used in modern field surveys.",
            "competency": "Data Collection",
            "difficulty": "Easy",
            "type": "MCQ",
        },
    ],
    "AI & Machine Learning": [
        {
            "question": "In official statistics, ML models should be used with attention to:",
            "options": [
                "Explainability, bias, and quality assurance",
                "Maximising model complexity only",
                "Hiding methodology notes",
                "Replacing all surveys immediately",
            ],
            "correct": 0,
            "explanation": "Responsible use requires transparency, fairness checks, and QA.",
            "competency": "AI & Machine Learning",
            "difficulty": "Medium",
            "type": "MCQ",
        },
    ],
}

# Mock iGOT courses keyed loosely by competency
IGOT_COURSES = [
    {
        "id": "igot_sampling",
        "title": "Survey Sampling for Official Statistics",
        "competency": "Sampling Techniques",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "6 hours",
        "level": "Beginner–Intermediate",
        "description": (
            "Practical introduction to probability sampling, stratification, and design "
            "effects for government survey programmes."
        ),
    },
    {
        "id": "igot_viz",
        "title": "Data Visualization for Government Decision Making",
        "competency": "Data Visualization",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "4 hours",
        "level": "Beginner",
        "description": (
            "Design clear, accessible visualisations of official statistics for policy "
            "and public communication."
        ),
    },
    {
        "id": "igot_gov",
        "title": "Data Governance and Stewardship in Public Sector",
        "competency": "Data Governance",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "5 hours",
        "level": "Intermediate",
        "description": "Principles of stewardship, confidentiality, and quality management.",
    },
    {
        "id": "igot_quality",
        "title": "Statistical Data Quality Assurance",
        "competency": "Data Quality",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "5 hours",
        "level": "Intermediate",
        "description": "Apply quality dimensions and validation checks to statistical products.",
    },
    {
        "id": "igot_soft",
        "title": "R and Python for Statistical Officers",
        "competency": "Statistical Software",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "8 hours",
        "level": "Beginner–Intermediate",
        "description": "Hands-on scripting for reproducible analysis in government settings.",
    },
    {
        "id": "igot_survey",
        "title": "Survey Design and Field Operations",
        "competency": "Survey Methodology",
        "provider": "iGOT Karmayogi (Mock)",
        "duration": "7 hours",
        "level": "Intermediate",
        "description": "Questionnaire design, pilot testing, and field quality control.",
    },
]

LEARNING_MODULES = {
    "Sampling Techniques": [
        {
            "title": "Introduction to Sampling",
            "overview": "Why sampling matters in large-scale official statistics.",
            "objectives": ["Distinguish census vs sample", "Define target population and frame"],
            "duration": "45 min",
            "resources": ["Survey Sampling Fundamentals — Ch.1", "MoSPI sampling overview (demo)"],
        },
        {
            "title": "Probability Sampling",
            "overview": "SRS, systematic, and probability proportional to size.",
            "objectives": ["Compute selection probabilities", "Explain design weights"],
            "duration": "60 min",
            "resources": ["Probability sampling notes (demo)", "Worked NSS examples"],
        },
        {
            "title": "Stratified Sampling",
            "overview": "Forming strata and allocation strategies.",
            "objectives": ["Design strata", "Compare equal vs proportional allocation"],
            "duration": "60 min",
            "resources": ["Stratified sampling module", "District-level estimate case"],
        },
        {
            "title": "Cluster Sampling",
            "overview": "Clusters, stages, and design effect.",
            "objectives": ["Explain intra-cluster correlation", "Interpret design effect"],
            "duration": "50 min",
            "resources": ["Cluster sampling guide", "PSU selection walkthrough"],
        },
        {
            "title": "Sampling Error",
            "overview": "Variance estimation and reporting uncertainty.",
            "objectives": ["Interpret SE and CV", "Communicate uncertainty to users"],
            "duration": "45 min",
            "resources": ["Sampling error primer", "Quality report template"],
        },
    ],
    "Data Visualization": [
        {
            "title": "Chart Selection Essentials",
            "overview": "Matching chart types to statistical messages.",
            "objectives": ["Choose appropriate charts", "Avoid common misleading visuals"],
            "duration": "40 min",
            "resources": ["Government Data Visualization — Module 1"],
        },
        {
            "title": "Dashboard Design for Policy",
            "overview": "Clarity, hierarchy, and accessibility.",
            "objectives": ["Structure a policy dashboard", "Apply accessibility checks"],
            "duration": "50 min",
            "resources": ["Dashboard patterns (demo)"],
        },
        {
            "title": "Visual Storytelling with Official Data",
            "overview": "Narratives that respect statistical integrity.",
            "objectives": ["Build a data story", "Cite sources and caveats"],
            "duration": "45 min",
            "resources": ["Storytelling checklist"],
        },
    ],
    "Data Governance": [
        {
            "title": "Principles of Data Stewardship",
            "overview": "Roles, accountability, and lifecycle.",
            "objectives": ["Map stewardship roles", "Identify risk points"],
            "duration": "40 min",
            "resources": ["Data Governance primer"],
        },
        {
            "title": "Confidentiality and Access",
            "overview": "Balancing openness and privacy.",
            "objectives": ["Apply disclosure control basics", "Document access policies"],
            "duration": "55 min",
            "resources": ["Confidentiality guidelines (demo)"],
        },
        {
            "title": "Metadata and Lineage",
            "overview": "Making statistics discoverable and traceable.",
            "objectives": ["Document lineage", "Use standard metadata fields"],
            "duration": "40 min",
            "resources": ["Metadata template"],
        },
    ],
}

# Organization-level demo analytics rows
ORG_ANALYTICS_ROWS = [
    {"department": "NSS", "designation": "Statistical Officer", "competency": "Sampling Techniques", "score": 42, "experience_years": 2, "quizzes_taken": 3, "learning_progress": 35},
    {"department": "NSS", "designation": "Senior SO", "competency": "Sampling Techniques", "score": 58, "experience_years": 8, "quizzes_taken": 5, "learning_progress": 60},
    {"department": "CSO", "designation": "Deputy Director", "competency": "Sampling Techniques", "score": 65, "experience_years": 12, "quizzes_taken": 4, "learning_progress": 55},
    {"department": "State DES", "designation": "Investigator", "competency": "Sampling Techniques", "score": 35, "experience_years": 1, "quizzes_taken": 2, "learning_progress": 20},
    {"department": "NSS", "designation": "Statistical Officer", "competency": "Data Visualization", "score": 45, "experience_years": 3, "quizzes_taken": 2, "learning_progress": 40},
    {"department": "CSO", "designation": "Director", "competency": "Data Visualization", "score": 70, "experience_years": 15, "quizzes_taken": 3, "learning_progress": 65},
    {"department": "State DES", "designation": "Statistical Officer", "competency": "Data Visualization", "score": 38, "experience_years": 2, "quizzes_taken": 1, "learning_progress": 25},
    {"department": "NSS", "designation": "Investigator", "competency": "Data Governance", "score": 40, "experience_years": 2, "quizzes_taken": 2, "learning_progress": 30},
    {"department": "CSO", "designation": "Deputy Director", "competency": "Data Governance", "score": 72, "experience_years": 10, "quizzes_taken": 4, "learning_progress": 70},
    {"department": "State DES", "designation": "Senior SO", "competency": "Data Governance", "score": 55, "experience_years": 7, "quizzes_taken": 3, "learning_progress": 50},
    {"department": "NSS", "designation": "Statistical Officer", "competency": "Statistical Software", "score": 48, "experience_years": 4, "quizzes_taken": 3, "learning_progress": 45},
    {"department": "CSO", "designation": "Statistical Officer", "competency": "Statistical Software", "score": 60, "experience_years": 6, "quizzes_taken": 4, "learning_progress": 58},
    {"department": "State DES", "designation": "Investigator", "competency": "Statistical Software", "score": 30, "experience_years": 1, "quizzes_taken": 1, "learning_progress": 15},
    {"department": "NSS", "designation": "Senior SO", "competency": "Data Quality", "score": 68, "experience_years": 9, "quizzes_taken": 5, "learning_progress": 72},
    {"department": "CSO", "designation": "Deputy Director", "competency": "Data Quality", "score": 75, "experience_years": 11, "quizzes_taken": 6, "learning_progress": 80},
    {"department": "State DES", "designation": "Statistical Officer", "competency": "Survey Methodology", "score": 52, "experience_years": 5, "quizzes_taken": 3, "learning_progress": 48},
    {"department": "NSS", "designation": "Investigator", "competency": "Survey Methodology", "score": 44, "experience_years": 2, "quizzes_taken": 2, "learning_progress": 33},
    {"department": "CSO", "designation": "Director", "competency": "Official Statistics", "score": 85, "experience_years": 18, "quizzes_taken": 4, "learning_progress": 90},
    {"department": "NSS", "designation": "Statistical Officer", "competency": "Data Analysis", "score": 62, "experience_years": 5, "quizzes_taken": 4, "learning_progress": 58},
    {"department": "State DES", "designation": "Senior SO", "competency": "Economic Statistics", "score": 70, "experience_years": 8, "quizzes_taken": 3, "learning_progress": 65},
]

ASSISTANT_RESPONSES = {
    "stratified": (
        "**Stratified sampling** divides the population into homogeneous groups (strata)—for example, "
        "rural/urban or districts—then draws samples from each stratum.\n\n"
        "Why it helps official statistics: it improves precision for important subgroups and supports "
        "reliable domain estimates (e.g., state or district indicators)."
    ),
    "example": (
        "Example: To estimate average household expenditure in a state, form strata by district and "
        "sector (rural/urban). Draw households within each stratum. This ensures every district is "
        "represented and reduces variance compared with an unstratified sample of the same size."
    ),
    "test": (
        "Quick check: Which method samples from homogeneous subgroups?\n"
        "A) Cluster  B) Stratified  C) Convenience  D) Snowball\n\n"
        "Answer: **B) Stratified**. Clusters are often heterogeneous geographic units selected together."
    ),
    "mcq": (
        "Here are 3 practice MCQs on sampling:\n\n"
        "1. Design weights adjust for? → Unequal selection probabilities\n"
        "2. PES assesses? → Census coverage/content error\n"
        "3. Intra-cluster correlation tends to? → Increase design effect\n\n"
        "Say **Create 5 MCQs** for a fuller set on a specific competency."
    ),
    "wrong": (
        "When an answer is wrong, StatGrow AI compares your choice to the correct concept, "
        "highlights the misconception (e.g., confusing cluster vs stratified sampling), and "
        "links a short learning module. Open **My Learning Path** for targeted practice."
    ),
    "default": (
        "I can help you with statistical concepts, competency gaps, practice questions, and "
        "learning recommendations for India’s Official Statistical System.\n\n"
        "Try: *Explain stratified sampling simply*, *Give me an example*, *Test my knowledge*, "
        "or *Create 5 MCQs*."
    ),
}
