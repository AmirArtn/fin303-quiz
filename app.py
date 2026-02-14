"""
FIN303 Exam Practice — Interactive Quiz App
A gamified Streamlit quiz with leaderboard, streaks, time bonuses, and explanations.
"""

import streamlit as st
import json
import os
import time
import random
from datetime import datetime
from questions import QUESTIONS, CHAPTERS, get_questions_by_chapter, get_random_questions

# ─────────────────────────── CONFIG ───────────────────────────
st.set_page_config(
    page_title="FIN303 Quiz Arena",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LEADERBOARD_FILE = os.path.join(os.path.dirname(__file__), "leaderboard.json")
POINTS_CORRECT = 100
STREAK_BONUS = 25
MAX_TIME_BONUS = 50
TIME_LIMIT = 30  # seconds per question for max time bonus


# ─────────────────────────── CSS ───────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ══════════════════════════════════════════════════
       APPLE-INSPIRED DARK MODE
       Clean, readable, warm, inviting
    ══════════════════════════════════════════════════ */

    /* ── Global ── */
    .stApp {
        background: #000000 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
    }
    [data-testid="stSidebar"] {
        background: rgba(28,28,30,0.98);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border-right: 1px solid rgba(255,255,255,0.06);
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #f5f5f7 !important;
    }

    /* Hide Streamlit default header & footer */
    header[data-testid="stHeader"] { background: transparent !important; }
    footer { display: none !important; }

    /* ── Hero Banner ── */
    .hero-banner {
        background: linear-gradient(160deg, #1c1c1e 0%, #2c2c2e 100%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 22px;
        padding: 3.5rem 2.5rem;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: '';
        position: absolute;
        top: -60%;
        left: -30%;
        width: 160%;
        height: 160%;
        background: radial-gradient(ellipse at 40% 50%, rgba(10,132,255,0.08) 0%, transparent 60%),
                    radial-gradient(ellipse at 70% 40%, rgba(94,92,230,0.06) 0%, transparent 50%);
        animation: glow 10s ease-in-out infinite;
    }
    @keyframes glow {
        0%, 100% { opacity: 0.6; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.05); }
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #f5f5f7, #d1d1d6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        position: relative;
        letter-spacing: -0.03em;
    }
    .hero-subtitle {
        color: #98989d;
        font-size: 1.05rem;
        font-weight: 400;
        position: relative;
        letter-spacing: -0.01em;
    }

    /* ── Glass Cards ── */
    .glass-card {
        background: #1c1c1e;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .glass-card:hover {
        border-color: rgba(10,132,255,0.3);
        box-shadow: 0 4px 20px rgba(10,132,255,0.08);
        transform: translateY(-1px);
    }

    /* ── Question Card ── */
    .question-card {
        background: #1c1c1e;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 18px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    .question-number {
        display: inline-block;
        background: #0a84ff;
        color: white;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 0.3rem 0.9rem;
        border-radius: 50px;
        margin-bottom: 1rem;
        letter-spacing: 0.03em;
    }
    .question-topic {
        display: inline-block;
        background: rgba(10,132,255,0.12);
        color: #64d2ff;
        font-weight: 500;
        font-size: 0.78rem;
        padding: 0.3rem 0.9rem;
        border-radius: 50px;
        margin-left: 0.5rem;
        margin-bottom: 1rem;
    }
    .question-text {
        color: #f5f5f7;
        font-size: 1.1rem;
        line-height: 1.75;
        font-weight: 400;
        letter-spacing: -0.01em;
        white-space: pre-line;
    }

    /* ── Stats Cards ── */
    .stat-card {
        background: #1c1c1e;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.1rem 0.8rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        border-color: rgba(255,255,255,0.15);
        transform: translateY(-1px);
    }
    .stat-value {
        font-size: 1.8rem;
        font-weight: 800;
        line-height: 1.2;
        letter-spacing: -0.02em;
    }
    .stat-label {
        color: #98989d;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-top: 0.25rem;
    }
    .gold { color: #ffd60a; }
    .cyan { color: #64d2ff; }
    .green { color: #30d158; }
    .pink { color: #ff375f; }
    .purple { color: #bf5af2; }

    /* ── Correct / Incorrect Feedback ── */
    .correct-box {
        background: rgba(48,209,88,0.1);
        border: 1px solid rgba(48,209,88,0.25);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        animation: slideIn 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .incorrect-box {
        background: rgba(255,55,95,0.08);
        border: 1px solid rgba(255,55,95,0.2);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        animation: shake 0.5s ease;
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20% { transform: translateX(-6px); }
        40% { transform: translateX(6px); }
        60% { transform: translateX(-3px); }
        80% { transform: translateX(3px); }
    }

    /* ── Explanation ── */
    .explanation-box {
        background: rgba(10,132,255,0.06);
        border: 1px solid rgba(10,132,255,0.15);
        border-radius: 14px;
        padding: 1.5rem 1.8rem;
        margin-top: 1rem;
        color: #e5e5ea;
        line-height: 1.75;
        font-size: 0.95rem;
    }
    .explanation-box strong {
        color: #64d2ff;
    }

    /* ── Leaderboard ── */
    .lb-row {
        display: flex;
        align-items: center;
        padding: 0.85rem 1.2rem;
        border-radius: 14px;
        margin-bottom: 0.4rem;
        transition: all 0.2s ease;
        background: #1c1c1e;
        border: 1px solid transparent;
    }
    .lb-row:hover {
        border-color: rgba(255,255,255,0.08);
        transform: translateY(-1px);
    }
    .lb-rank {
        font-weight: 800;
        font-size: 1.05rem;
        width: 48px;
        text-align: center;
    }
    .lb-name {
        flex: 1;
        color: #f5f5f7;
        font-weight: 600;
        font-size: 0.95rem;
    }
    .lb-score {
        font-weight: 700;
        font-size: 0.95rem;
        color: #ffd60a;
    }
    .lb-gold { background: rgba(255,214,10,0.06); border: 1px solid rgba(255,214,10,0.15) !important; }
    .lb-silver { background: rgba(174,174,178,0.06); border: 1px solid rgba(174,174,178,0.12) !important; }
    .lb-bronze { background: rgba(255,159,10,0.06); border: 1px solid rgba(255,159,10,0.12) !important; }

    /* ── Mode Select Cards ── */
    .mode-card {
        background: #1c1c1e;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 2rem 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        height: 100%;
    }
    .mode-card:hover {
        border-color: rgba(10,132,255,0.35);
        background: #2c2c2e;
        box-shadow: 0 8px 30px rgba(10,132,255,0.1);
        transform: translateY(-3px);
    }
    .mode-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
    .mode-title { color: #f5f5f7; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.4rem; }
    .mode-desc { color: #98989d; font-size: 0.85rem; line-height: 1.5; }

    /* ── Progress Bar ── */
    .progress-container {
        background: #2c2c2e;
        border-radius: 50px;
        height: 6px;
        margin: 1rem 0 1.5rem;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 50px;
        background: linear-gradient(90deg, #0a84ff, #5e5ce6, #bf5af2);
        transition: width 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    /* ── Achievement Badges ── */
    .badge {
        display: inline-block;
        background: #2c2c2e;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 0.6rem 1rem;
        margin: 0.3rem;
        font-size: 0.85rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .badge:hover { transform: scale(1.05); }
    .badge-gold { border-color: rgba(255,214,10,0.25); background: rgba(255,214,10,0.06); color: #ffd60a; }
    .badge-purple { border-color: rgba(191,90,242,0.25); background: rgba(191,90,242,0.06); color: #bf5af2; }
    .badge-cyan { border-color: rgba(100,210,255,0.25); background: rgba(100,210,255,0.06); color: #64d2ff; }
    .badge-green { border-color: rgba(48,209,88,0.25); background: rgba(48,209,88,0.06); color: #30d158; }
    .badge-pink { border-color: rgba(255,55,95,0.25); background: rgba(255,55,95,0.06); color: #ff375f; }

    /* ── Confetti ── */
    @keyframes confetti-fall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
    }
    .confetti-piece {
        position: fixed;
        top: -10px;
        z-index: 9999;
        animation: confetti-fall 3s ease-in forwards;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: #0a84ff !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        padding: 0.7rem 2rem !important;
        transition: all 0.25s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        font-size: 0.95rem !important;
        letter-spacing: -0.01em !important;
    }
    .stButton > button:hover {
        background: #409cff !important;
        box-shadow: 0 4px 16px rgba(10,132,255,0.35) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* ── Radio — THE FIX: bright white text on elevated cards ── */
    .stRadio > div {
        gap: 0.6rem !important;
    }
    .stRadio > div > label {
        background: #1c1c1e !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        border-radius: 14px !important;
        padding: 1rem 1.4rem !important;
        transition: all 0.25s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        cursor: pointer !important;
    }
    .stRadio > div > label:hover {
        border-color: rgba(10,132,255,0.5) !important;
        background: #2c2c2e !important;
        box-shadow: 0 2px 12px rgba(10,132,255,0.1) !important;
        transform: translateY(-1px) !important;
    }
    /* Force ALL text inside radio labels to be bright white */
    .stRadio > div > label,
    .stRadio > div > label span,
    .stRadio > div > label p,
    .stRadio > div > label div,
    .stRadio > div > label * {
        color: #f5f5f7 !important;
        font-size: 0.95rem !important;
        font-weight: 450 !important;
        letter-spacing: -0.01em !important;
    }
    /* Selected radio state */
    .stRadio > div > label[data-checked="true"],
    .stRadio > div > label:has(input:checked) {
        border-color: #0a84ff !important;
        background: rgba(10,132,255,0.1) !important;
        box-shadow: 0 0 0 1px rgba(10,132,255,0.3) !important;
    }

    /* ── Text Input ── */
    .stTextInput input {
        background: #1c1c1e !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        border-radius: 12px !important;
        color: #f5f5f7 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        transition: all 0.25s ease !important;
    }
    .stTextInput input:focus {
        border-color: #0a84ff !important;
        box-shadow: 0 0 0 3px rgba(10,132,255,0.15) !important;
    }
    .stTextInput input::placeholder {
        color: #636366 !important;
    }

    /* ── Select Box ── */
    .stSelectbox > div > div {
        background: #1c1c1e !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        border-radius: 12px !important;
        color: #f5f5f7 !important;
    }

    /* ── Misc ── */
    .chapter-badge {
        display: inline-block;
        background: rgba(10,132,255,0.1);
        border: 1px solid rgba(10,132,255,0.2);
        color: #64d2ff;
        border-radius: 10px;
        padding: 0.35rem 0.8rem;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .results-score {
        font-size: 4.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffd60a, #ff9f0a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        line-height: 1.1;
        letter-spacing: -0.03em;
    }
    .divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.06);
        margin: 2rem 0;
    }
    div[data-testid="stExpander"] {
        background: #1c1c1e !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 14px !important;
    }
    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] span {
        color: #e5e5ea !important;
    }

    /* ── Streamlit native overrides for dark consistency ── */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown li {
        color: #e5e5ea;
    }
    [data-testid="stWidgetLabel"] label,
    [data-testid="stWidgetLabel"] p {
        color: #98989d !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────── LEADERBOARD I/O ───────────────────────────
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []


def save_leaderboard(entries):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def add_to_leaderboard(name, score, accuracy, mode, time_taken):
    entries = load_leaderboard()
    entries.append({
        "name": name,
        "score": score,
        "accuracy": round(accuracy, 1),
        "mode": mode,
        "time": round(time_taken, 1),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    entries.sort(key=lambda x: x["score"], reverse=True)
    entries = entries[:50]  # keep top 50
    save_leaderboard(entries)


# ─────────────────────────── SESSION INIT ───────────────────────────
def init_session():
    defaults = {
        "screen": "welcome",
        "player_name": "",
        "quiz_mode": None,
        "questions": [],
        "current_q": 0,
        "score": 0,
        "streak": 0,
        "best_streak": 0,
        "correct_count": 0,
        "answers": [],
        "q_start_time": None,
        "quiz_start_time": None,
        "answered": False,
        "selected_answer": None,
        "chapter_filter": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────── WELCOME SCREEN ───────────────────────────
def show_welcome():
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🏆 FIN303 Quiz Arena</div>
        <div class="hero-subtitle">Master financial concepts. Compete with classmates. Top the leaderboard.</div>
    </div>
    """, unsafe_allow_html=True)

    # Name input
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input(
            "Enter your name to begin",
            placeholder="e.g. John Smith",
            key="name_input",
            label_visibility="collapsed",
        )
        st.markdown("<p style='text-align:center; color: rgba(255,255,255,0.35); font-size:0.85rem; margin-top:-0.5rem;'>Enter your name above to start</p>", unsafe_allow_html=True)

    if not name:
        # Show leaderboard preview even before name entry
        show_leaderboard_section()
        return

    st.markdown("<br>", unsafe_allow_html=True)

    # Mode selection
    st.markdown("<h3 style='text-align:center; color:#e2e8f0; font-weight:700; margin-bottom:1.5rem;'>Choose Your Challenge</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="mode-card">
            <div class="mode-icon">📋</div>
            <div class="mode-title">Full Exam</div>
            <div class="mode-desc">All 52 questions<br>Maximum points</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Full Exam", key="full", use_container_width=True):
            start_quiz(name, "Full Exam", QUESTIONS.copy())

    with col2:
        st.markdown("""
        <div class="mode-card">
            <div class="mode-icon">⚡</div>
            <div class="mode-title">Quick 10</div>
            <div class="mode-desc">10 random questions<br>Speed challenge</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Quick 10", key="quick", use_container_width=True):
            start_quiz(name, "Quick 10", get_random_questions(10))

    with col3:
        st.markdown("""
        <div class="mode-card">
            <div class="mode-icon">📚</div>
            <div class="mode-title">By Chapter</div>
            <div class="mode-desc">Focus on one chapter<br>Targeted studying</div>
        </div>
        """, unsafe_allow_html=True)

    # Chapter selector
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        ch = st.selectbox(
            "Select chapter",
            options=[1, 2, 3, 4],
            format_func=lambda x: f"Ch. {x}: {CHAPTERS[x]}",
            key="ch_select",
            label_visibility="collapsed",
        )
        if st.button(f"Start Chapter {ch}", key="ch_start", use_container_width=True):
            qs = get_questions_by_chapter(ch)
            random.shuffle(qs)
            start_quiz(name, f"Chapter {ch}", qs)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    show_leaderboard_section()


def start_quiz(name, mode, questions):
    random.shuffle(questions)
    st.session_state.player_name = name
    st.session_state.quiz_mode = mode
    st.session_state.questions = questions
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.correct_count = 0
    st.session_state.answers = []
    st.session_state.q_start_time = time.time()
    st.session_state.quiz_start_time = time.time()
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.screen = "quiz"
    st.rerun()


# ─────────────────────────── QUIZ SCREEN ───────────────────────────
def show_quiz():
    questions = st.session_state.questions
    idx = st.session_state.current_q
    total = len(questions)
    q = questions[idx]

    # ── Top Stats Bar ──
    cols = st.columns(5)
    stats = [
        ("🏆", f"{st.session_state.score:,}", "Score", "gold"),
        ("🎯", f"{idx + 1}/{total}", "Progress", "cyan"),
        ("✅", f"{round(st.session_state.correct_count / max(1, idx) * 100) if idx > 0 else 0}%", "Accuracy", "green"),
        ("🔥", str(st.session_state.streak), "Streak", "pink"),
        ("⭐", str(st.session_state.best_streak), "Best Streak", "purple"),
    ]
    for col, (icon, val, label, color) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:1.4rem;">{icon}</div>
                <div class="stat-value {color}">{val}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Progress Bar ──
    progress = (idx / total) * 100
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-fill" style="width: {progress}%"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Question Card ──
    st.markdown(f"""
    <div class="question-card">
        <span class="question-number">Q{idx + 1} of {total}</span>
        <span class="question-topic">📖 {q['topic']}</span>
        <span class="chapter-badge" style="margin-left:0.5rem;">Ch. {q['chapter']}</span>
        <div class="question-text" style="margin-top:1rem;">{q['question'].replace(chr(36), '&#36;')}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Answer Options ──
    if not st.session_state.answered:
        # Set start time for this question if not set
        if st.session_state.q_start_time is None:
            st.session_state.q_start_time = time.time()

        option_labels = [f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])]
        selected = st.radio(
            "Select your answer:",
            options=option_labels,
            key=f"q_{idx}_answer",
            label_visibility="collapsed",
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Submit Answer", key=f"submit_{idx}", use_container_width=True):
                selected_idx = option_labels.index(selected)
                process_answer(q, selected_idx)
                st.rerun()
    else:
        # Show feedback
        show_feedback(q)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if idx + 1 < total:
                if st.button("Next Question →", key=f"next_{idx}", use_container_width=True):
                    st.session_state.current_q += 1
                    st.session_state.answered = False
                    st.session_state.selected_answer = None
                    st.session_state.q_start_time = time.time()
                    st.rerun()
            else:
                if st.button("View Results 🏆", key="finish", use_container_width=True):
                    finish_quiz()
                    st.rerun()


def process_answer(q, selected_idx):
    elapsed = time.time() - (st.session_state.q_start_time or time.time())
    is_correct = selected_idx == q["correct"]

    points = 0
    if is_correct:
        points += POINTS_CORRECT
        # Streak bonus
        st.session_state.streak += 1
        streak_bonus = (st.session_state.streak - 1) * STREAK_BONUS
        points += streak_bonus
        # Time bonus
        if elapsed < TIME_LIMIT:
            time_bonus = int(MAX_TIME_BONUS * (1 - elapsed / TIME_LIMIT))
            points += max(0, time_bonus)
        st.session_state.correct_count += 1
        if st.session_state.streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.streak
    else:
        st.session_state.streak = 0

    st.session_state.score += points
    st.session_state.answered = True
    st.session_state.selected_answer = selected_idx
    st.session_state.answers.append({
        "question_id": q["id"],
        "selected": selected_idx,
        "correct": q["correct"],
        "is_correct": is_correct,
        "points": points,
        "time": round(elapsed, 1),
    })


def show_feedback(q):
    ans = st.session_state.answers[-1]
    selected_idx = ans["selected"]
    correct_idx = q["correct"]

    if ans["is_correct"]:
        points_detail = f"+{ans['points']} pts"
        if st.session_state.streak > 1:
            points_detail += f" (🔥 {st.session_state.streak}× streak!)"

        st.markdown(f"""
        <div class="correct-box">
            <div style="font-size:1.5rem; margin-bottom:0.5rem;">🎉 Correct!</div>
            <div style="color: #4ade80; font-weight:600; font-size:1.1rem;">{points_detail}</div>
            <div style="color: rgba(255,255,255,0.5); margin-top:0.5rem; font-size:0.9rem;">
                Answered in {ans['time']}s
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Show confetti
        confetti_html = ""
        colors = ["#fbbf24", "#4ade80", "#22d3ee", "#a78bfa", "#f472b6", "#6366f1"]
        for i in range(30):
            left = random.randint(0, 100)
            delay = random.random() * 2
            color = random.choice(colors)
            size = random.randint(6, 12)
            confetti_html += f'<div class="confetti-piece" style="left:{left}%; animation-delay:{delay}s; background:{color}; width:{size}px; height:{size}px; border-radius:2px;"></div>'
        st.markdown(confetti_html, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="incorrect-box">
            <div style="font-size:1.5rem; margin-bottom:0.5rem;">❌ Incorrect</div>
            <div style="color: rgba(255,255,255,0.7);">
                You selected: <span style="color:#f87171; font-weight:600;">{chr(65+selected_idx)}. {q['options'][selected_idx]}</span>
            </div>
            <div style="color: rgba(255,255,255,0.7); margin-top:0.3rem;">
                Correct answer: <span style="color:#4ade80; font-weight:600;">{chr(65+correct_idx)}. {q['options'][correct_idx]}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Always show explanation on incorrect
        st.markdown(f"""
        <div class="explanation-box">
            <div style="font-size:1rem; font-weight:700; color:#a5b4fc; margin-bottom:0.8rem;">📖 Concept Explanation</div>
            <div>{q['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Optional: show explanation on correct too (expandable)
    if ans["is_correct"]:
        with st.expander("📖 View explanation"):
            st.markdown(q["explanation"])


# ─────────────────────────── RESULTS SCREEN ───────────────────────────
def finish_quiz():
    total_time = time.time() - st.session_state.quiz_start_time
    accuracy = (st.session_state.correct_count / len(st.session_state.questions)) * 100

    add_to_leaderboard(
        st.session_state.player_name,
        st.session_state.score,
        accuracy,
        st.session_state.quiz_mode,
        total_time,
    )
    st.session_state.screen = "results"


def show_results():
    questions = st.session_state.questions
    total = len(questions)
    correct = st.session_state.correct_count
    accuracy = (correct / total) * 100
    total_time = time.time() - st.session_state.quiz_start_time

    # ── Hero Score ──
    st.markdown(f"""
    <div class="hero-banner" style="padding:2.5rem;">
        <div style="font-size:1.2rem; color:rgba(255,255,255,0.5); margin-bottom:0.5rem; position:relative;">🏆 Final Score</div>
        <div class="results-score">{st.session_state.score:,}</div>
        <div style="color:rgba(255,255,255,0.45); font-size:1rem; margin-top:0.5rem; position:relative;">
            {st.session_state.player_name} — {st.session_state.quiz_mode}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Summary Stats ──
    cols = st.columns(4)
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    summary = [
        ("✅", f"{correct}/{total}", "Correct", "green"),
        ("🎯", f"{accuracy:.1f}%", "Accuracy", "cyan"),
        ("⏱️", f"{minutes}:{seconds:02d}", "Time", "purple"),
        ("🔥", str(st.session_state.best_streak), "Best Streak", "pink"),
    ]
    for col, (icon, val, label, color) in zip(cols, summary):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:1.4rem;">{icon}</div>
                <div class="stat-value {color}">{val}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Achievement Badges ──
    st.markdown("<br>", unsafe_allow_html=True)
    badges = []
    if accuracy == 100:
        badges.append(("🏅 Perfect Score", "badge-gold"))
    if accuracy >= 90:
        badges.append(("🌟 Honor Roll", "badge-purple"))
    if accuracy >= 80:
        badges.append(("💪 Strong Performance", "badge-cyan"))
    if st.session_state.best_streak >= 10:
        badges.append(("🔥 Streak Master", "badge-pink"))
    elif st.session_state.best_streak >= 5:
        badges.append(("⚡ Streak Builder", "badge-pink"))
    if total_time < total * 15:
        badges.append(("⏱️ Speed Demon", "badge-cyan"))
    if correct >= 1:
        badges.append(("📚 Scholar", "badge-green"))

    if badges:
        badge_html = "<div style='text-align:center; margin:1rem 0;'>"
        badge_html += "<div style='color:rgba(255,255,255,0.5); font-size:0.85rem; margin-bottom:0.8rem; font-weight:600; text-transform:uppercase; letter-spacing:0.1em;'>Achievements Unlocked</div>"
        for text, cls in badges:
            badge_html += f'<span class="badge {cls}">{text}</span>'
        badge_html += "</div>"
        st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── Chapter Breakdown ──
    st.markdown("<h3 style='color:#e2e8f0; font-weight:700;'>📊 Chapter Breakdown</h3>", unsafe_allow_html=True)
    for ch_num in sorted(CHAPTERS.keys()):
        ch_answers = [a for a, q in zip(st.session_state.answers, questions) if q["chapter"] == ch_num]
        if not ch_answers:
            continue
        ch_correct = sum(1 for a in ch_answers if a["is_correct"])
        ch_total = len(ch_answers)
        ch_pct = (ch_correct / ch_total) * 100
        bar_color = "#4ade80" if ch_pct >= 80 else "#fbbf24" if ch_pct >= 60 else "#f87171"

        st.markdown(f"""
        <div class="glass-card" style="padding:1.2rem 1.5rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <span style="color:#a5b4fc; font-weight:600;">Ch. {ch_num}</span>
                    <span style="color:rgba(255,255,255,0.5); margin-left:0.5rem; font-size:0.9rem;">{CHAPTERS[ch_num]}</span>
                </div>
                <div style="color:{bar_color}; font-weight:700;">{ch_correct}/{ch_total} ({ch_pct:.0f}%)</div>
            </div>
            <div class="progress-container" style="margin:0.7rem 0 0;">
                <div class="progress-fill" style="width:{ch_pct}%; background:{bar_color};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Missed Questions Review ──
    missed = [(q, a) for q, a in zip(questions, st.session_state.answers) if not a["is_correct"]]
    if missed:
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#e2e8f0; font-weight:700;'>📝 Review Missed Questions</h3>", unsafe_allow_html=True)

        for q, a in missed:
            with st.expander(f"Q{q['id']}: {q['question'][:80]}..."):
                st.markdown(f"**Your answer:** {chr(65+a['selected'])}. {q['options'][a['selected']]}")
                st.markdown(f"**Correct answer:** {chr(65+a['correct'])}. {q['options'][a['correct']]}")
                st.markdown("---")
                st.markdown(f"**Explanation:** {q['explanation']}")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── Retry & Leaderboard ──
    col1, col2, col3 = st.columns(3)
    with col1:
        if missed:
            if st.button("🔄 Retry Missed Questions", use_container_width=True):
                missed_qs = [q for q, a in zip(questions, st.session_state.answers) if not a["is_correct"]]
                start_quiz(st.session_state.player_name, "Retry Missed", missed_qs)
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.screen = "welcome"
            st.rerun()
    with col3:
        if st.button("🔁 Play Again", use_container_width=True):
            st.session_state.screen = "welcome"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    show_leaderboard_section()


# ─────────────────────────── LEADERBOARD SECTION ───────────────────────────
def show_leaderboard_section():
    entries = load_leaderboard()

    st.markdown("<h3 style='text-align:center; color:#e2e8f0; font-weight:700; margin-bottom:1.5rem;'>🏆 Leaderboard</h3>", unsafe_allow_html=True)

    if not entries:
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:3rem;">
            <div style="font-size:2.5rem; margin-bottom:0.8rem;">🏆</div>
            <div style="color:rgba(255,255,255,0.5); font-size:1rem;">No scores yet — be the first to compete!</div>
        </div>
        """, unsafe_allow_html=True)
        return

    for i, entry in enumerate(entries[:10]):
        rank_icons = {0: "🥇", 1: "🥈", 2: "🥉"}
        rank_display = rank_icons.get(i, f"#{i+1}")
        row_class = "lb-gold" if i == 0 else "lb-silver" if i == 1 else "lb-bronze" if i == 2 else ""

        st.markdown(f"""
        <div class="lb-row {row_class}">
            <div class="lb-rank">{rank_display}</div>
            <div class="lb-name">
                {entry['name']}
                <span style="color:rgba(255,255,255,0.3); font-size:0.8rem; font-weight:400; margin-left:0.5rem;">{entry.get('mode', '')}</span>
            </div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.85rem; margin-right:1rem;">{entry.get('accuracy', 0):.0f}%</div>
            <div class="lb-score">{entry['score']:,} pts</div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────── MAIN ───────────────────────────
def main():
    inject_css()
    init_session()

    if st.session_state.screen == "welcome":
        show_welcome()
    elif st.session_state.screen == "quiz":
        show_quiz()
    elif st.session_state.screen == "results":
        show_results()


if __name__ == "__main__":
    main()
