# 🚀 QUICK START GUIDE

## Your Project is Ready!

You now have a complete, portfolio-ready data visualization project using a **single CSV file** with 2,560 participants.

---

## 📦 What's Included

```
gambling-analysis-project/
├── index.html                    ← Main dashboard (DEPLOY THIS)
├── visualizations/               ← 5 JSON files (DEPLOY THIS)
│   ├── age_distribution.json
│   ├── gambling_prevalence.json
│   ├── mental_health.json
│   ├── geographic.json
│   └── risk_factors.json
├── data/
│   ├── combined-scoring.csv      ← Original data
│   └── gambling_research.db      ← SQLite database
├── scripts/
│   ├── 01_create_database.py     ← Database creation
│   └── 02_analysis.py            ← Analysis code
└── README.md                     ← Full documentation
```

---

## 🎯 Where to Place Files in Your Website

### Your Current Structure:
```
cooper-sharp.github.io/
├── index.html
├── projects.html
├── resume.html
└── data/
```

### Add Your Project Here:
```
cooper-sharp.github.io/
├── index.html
├── projects.html
├── resume.html
├── data/
└── projects/                     ← CREATE THIS
    └── gambling-analysis/        ← PUT PROJECT HERE
        ├── index.html            ← The dashboard
        ├── visualizations/       ← The 5 JSON files
        │   ├── age_distribution.json
        │   ├── gambling_prevalence.json
        │   ├── mental_health.json
        │   ├── geographic.json
        │   └── risk_factors.json
        └── README.md             ← (optional)
```

---

## 📋 Step-by-Step Deployment

### Step 1: Create Folder Structure
```bash
cd /Users/coopersharp/Documents/GitHub/cooper-sharp.github.io
mkdir -p projects/gambling-analysis
```

### Step 2: Copy Essential Files

**From the project folder you downloaded, copy ONLY these to your repo:**
- `index.html` → `projects/gambling-analysis/index.html`
- `visualizations/` folder → `projects/gambling-analysis/visualizations/`
- `README.md` (optional) → `projects/gambling-analysis/README.md`

**You do NOT need to deploy:**
- `data/` folder (unless you want to show the raw data)
- `scripts/` folder (keep for your reference, but not needed online)

### Step 3: Update Your projects.html

Add this to your `projects.html`:

```html
<div class="project-card">
    <h3>Gambling & Mental Health Analysis</h3>
    <p>SQL + Python data visualization project analyzing 2,560 survey participants. 
       Demonstrates complex queries, CTEs, and interactive Plotly visualizations.</p>
    
    <div class="tech-stack">
        <span class="tech">SQL</span>
        <span class="tech">Python</span>
        <span class="tech">Plotly</span>
        <span class="tech">Pandas</span>
    </div>
    
    <div class="project-links">
        <a href="projects/gambling-analysis/" class="btn-primary">View Project →</a>
        <a href="https://github.com/cooper-sharp/gambling-analysis" class="btn-secondary">GitHub</a>
    </div>
</div>
```

### Step 4: Update GitHub Link in Dashboard

Open `projects/gambling-analysis/index.html` and find line ~750:

Change:
```html
<a href="https://github.com/cooper-sharp/gambling-analysis" target="_blank">GitHub</a>
```

To your actual GitHub repository URL.

### Step 5: Test Locally

```bash
cd /Users/coopersharp/Documents/GitHub/cooper-sharp.github.io
python3 -m http.server 8000
```

Then visit: `http://localhost:8000/projects/gambling-analysis/`

### Step 6: Deploy

```bash
git add .
git commit -m "Add gambling analysis data visualization project"
git push origin main
```

Wait 1-2 minutes, then visit:
`https://cooper-sharp.github.io/projects/gambling-analysis/`

---

## ✅ Deployment Checklist

- [ ] Created `projects/gambling-analysis/` folder
- [ ] Copied `index.html` 
- [ ] Copied `visualizations/` folder with all 5 JSON files
- [ ] Updated GitHub link in `index.html`
- [ ] Added project card to `projects.html`
- [ ] Tested locally
- [ ] Committed and pushed to GitHub
- [ ] Verified live site works

---

## 🎨 Customization (Optional)

### Change Colors
In `index.html`, find:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
Replace with your brand colors.

### Add "Back to Projects" Button
Add to top of `index.html` hero section:
```html
<a href="../../projects.html" style="display: inline-block; margin-bottom: 20px; color: #667eea;">
    ← Back to Projects
</a>
```

---

## 🎯 Key SQL Techniques Showcased

Your project demonstrates:

1. **CASE Statements** - Data categorization and transformation
2. **Conditional Aggregation** - CASE within SUM/AVG functions
3. **Common Table Expressions (CTEs)** - Readable, modular queries
4. **GROUP BY with HAVING** - Statistical filtering
5. **Complex Joins** - Multi-condition aggregations
6. **Type Casting** - CAST for numeric operations
7. **String Operations** - Data cleaning and formatting

---

## 💡 For Your Resume

**Project Description:**

> "Developed a data visualization dashboard analyzing 2,560 survey responses on gambling behavior and mental health. Created a SQLite database, wrote 5 complex SQL queries featuring CTEs and conditional aggregation, and built interactive Plotly visualizations. Deployed responsive HTML5 dashboard showcasing data analysis and SQL proficiency."

**Technologies:** Python, SQL, SQLite, Pandas, Plotly, HTML5, CSS3

---

## 📊 The 5 Analyses

1. **Age Distribution** - Comparing populations with GROUP BY
2. **Gambling Prevalence** - Conditional aggregation by demographics  
3. **Mental Health Correlation** - CTE-based comparative analysis
4. **Geographic Patterns** - State-level aggregation with HAVING
5. **Risk Factors** - Nested CASE with age categorization

---

## 🆘 Troubleshooting

**Visualizations not loading?**
- Check browser console (F12) for errors
- Ensure `visualizations/` folder is in the same directory as `index.html`
- Try hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

**404 errors on GitHub Pages?**
- Wait 1-2 minutes after pushing
- Check repository Settings → Pages is enabled
- Verify file paths are relative (no hardcoded paths)

**Need help?**
- Check the full README.md for detailed documentation
- Test locally first before deploying

---

## 🎉 You're Done!

Your project is now live and ready to share with employers and on LinkedIn!

**Next Steps:**
1. Add to your resume under "Projects"
2. Share on LinkedIn with #DataAnalysis #SQL #Python
3. Add to your portfolio site
4. Prepare talking points for interviews

---

**Great work! You now have a professional data visualization portfolio piece!** 🚀
