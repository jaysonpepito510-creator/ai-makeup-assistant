import streamlit as st
import time

st.set_page_config(
    page_title="💄 AI Makeup Assistant",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------
# Custom CSS
# ----------------------
st.markdown("""
<style>
    * {box-sizing: border-box;}
    .stApp {
        background: linear-gradient(135deg, #1a1025 0%, #2e1a3c 50%, #1f172b 100%);
        color: #f8e6f0;
    }
    h1 {
        background: linear-gradient(90deg, #ff9a9e 0%, #fad0c4 50%, #fbc2eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: clamp(1.6rem, 6vw, 3rem);
        text-align: center;
        margin: 0.5rem 0;
    }
    .subtitle {
        text-align: center;
        color: #e0c8d5;
        font-size: clamp(0.9rem, 3vw, 1.2rem);
        margin-bottom: 2rem;
    }
    .form-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: clamp(1.5rem, 5vw, 2rem);
        border: 1px solid rgba(255, 200, 220, 0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
    }
    .user-bubble {
        background: linear-gradient(90deg, #ff5e8c 0%, #ff8fab 100%);
        color: white;
        border-radius: 18px 18px 4px 18px;
        padding: 0.9rem 1.2rem;
        margin: 0.8rem 0;
        margin-left: auto;
        max-width: 80%;
    }
    .assistant-bubble {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 140, 180, 0.2);
        border-radius: 18px 18px 18px 4px;
        padding: 1.2rem 1.5rem;
        margin: 0.8rem 0;
        margin-right: auto;
        max-width: 90%;
    }
    .tutorial-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 0.6rem 0;
        border-left: 3px solid #ff8fab;
        line-height: 1.7;
    }
    .step-title {
        font-weight: 700;
        color: #ffb3c1;
        display: block;
        margin-bottom: 0.25rem;
    }
    .step-text {
        color: #e4d4dc;
    }
    .result-header {
        text-align: center;
        background: rgba(255, 140, 180, 0.15);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 140, 180, 0.25);
    }
    .skeleton-line {
        background: linear-gradient(90deg, rgba(255,255,255,0.06) 25%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.06) 75%);
        background-size: 200% 100%;
        animation: skeleton-loading 1.5s infinite;
        border-radius: 6px;
        height: 16px;
        margin: 0.6rem 0;
    }
    @keyframes skeleton-loading {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff5e8c 0%, #ff8fab 100%);
        color: white !important;
        font-weight: 700;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        border: none;
        width: 100%;
        font-size: 1rem;
        margin-top: 1rem;
        cursor: pointer;
    }
    div.stButton > button:first-child:hover {
        opacity: 0.95;
        transform: scale(1.01);
        transition: all 0.2s ease;
    }
    .tip-box {
        background: rgba(255, 200, 100, 0.12);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        border: 1px solid rgba(255, 200, 100, 0.3);
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# Tutorial Data
# ----------------------
SKIN_TYPES = ["oily", "dry", "combination", "normal", "sensitive"]
OCCASIONS = ["everyday", "work", "party", "date", "wedding/bridal", "graduation"]
LEVELS = ["beginner", "intermediate", "advanced"]
FACE_SHAPES = ["oval", "round", "square", "heart", "long", "diamond"]
UNDERTONES = ["warm (yellow/golden)", "cool (pink/red)", "neutral (balanced)"]

TUTORIALS = {
    "undertone_guide": {
        "warm (yellow/golden)": "Go for golden, peach, coral, warm reds, and amber shades — avoid icy tones.",
        "cool (pink/red)": "Choose rose, berry, plum, cherry red, and pink-based nudes — avoid orange tones.",
        "neutral (balanced)": "You can pull off almost any shade! From soft nudes to bold reds — experiment freely ✨"
    },
    "base": {
        "oily": [
            {"title": "Prep", "text": "Start with oil-free, non-comedogenic moisturizer — let it absorb fully, about 2–3 minutes."},
            {"title": "Prime", "text": "Apply mattifying primer only on your T-zone to control shine without drying cheeks."},
            {"title": "Foundation", "text": "Use water-based or oil-free formula. Apply in thin layers with a damp beauty sponge."},
            {"title": "Conceal", "text": "Dab only on blemishes and under eyes. Blend outward gently — avoid too much product."},
            {"title": "Set", "text": "Press translucent powder onto T-zone. Leave cheeks powder-free for natural glow."}
        ],
        "dry": [
            {"title": "Prep", "text": "Apply rich hydrating cream + facial oil. Wait 5–8 minutes to let it sink in fully."},
            {"title": "Prime", "text": "Use hydrating, illuminating primer — creates a smooth, dewy base."},
            {"title": "Foundation", "text": "Choose cream or satin formula. Apply with fingertips for warmth and seamless blend."},
            {"title": "Conceal", "text": "Use cream concealer under eyes. Pat gently — never drag or pull."},
            {"title": "Set", "text": "Light powder only on T-zone. Finish with dewy setting spray to lock in moisture."}
        ],
        "combination": [
            {"title": "Prep", "text": "Lightweight lotion on T-zone, richer cream on dry cheek areas."},
            {"title": "Prime", "text": "Mattifying primer on forehead/nose; hydrating primer on cheeks/jawline."},
            {"title": "Foundation", "text": "Medium-coverage works best. Blend well along jawline and onto neck."},
            {"title": "Conceal", "text": "Spot-apply only where needed. Feather edges so no visible lines."},
            {"title": "Set", "text": "Light powder on T-zone. Keep cheeks natural or use dewy spray."}
        ],
        "normal": [
            {"title": "Prep", "text": "Light moisturizer + SPF. Let settle 2 minutes before next step."},
            {"title": "Prime", "text": "Any primer works — choose dewy or matte finish as you like."},
            {"title": "Foundation", "text": "Tinted moisturizer or light-medium coverage. Match to your neck, not your face."},
            {"title": "Conceal", "text": "Brighten under eyes, cover redness. Keep it light."},
            {"title": "Set", "text": "Setting spray or light powder — whichever you prefer!"}
        ],
        "sensitive": [
            {"title": "Prep", "text": "Fragrance-free, hypoallergenic moisturizer. Pat gently — do not rub hard."},
            {"title": "Prime", "text": "Skip if it irritates. Always pick sensitive-skin friendly products."},
            {"title": "Foundation", "text": "Mineral or dermatologist-tested formula. Apply with clean sponge or fingertips."},
            {"title": "Conceal", "text": "Fragrance-free concealer. Dab lightly only where needed."},
            {"title": "Set", "text": "Talc-free gentle powder. Apply very sparingly."}
        ]
    },
    "eyes": {
        "beginner": [
            {"title": "Base", "text": "Sweep neutral beige/taupe all over lid up to brow bone."},
            {"title": "Depth", "text": "Blend soft warm brown into crease with back-and-forth motion."},
            {"title": "Brighten", "text": "Pat champagne shimmer on center of lid — your finger works best."},
            {"title": "Define", "text": "Line upper lash line with brown pencil — softer than black."},
            {"title": "Finish", "text": "Curl lashes + mascara. Wiggle from roots up. 1–2 coats only."}
        ],
        "intermediate": [
            {"title": "Prime", "text": "Eye primer all over lid — prevents creasing, helps color last."},
            {"title": "Transition", "text": "Blend soft warm shade into crease, deepen toward outer corner."},
            {"title": "Lid", "text": "Pat shimmer/satin on lid. Add highlight to inner corner & brow bone."},
            {"title": "Line", "text": "Thin wing liner OR tightline between upper lashes."},
            {"title": "Finish", "text": "Curl lashes + mascara. Soft brown on lower lash line is optional."}
        ],
        "advanced": [
            {"title": "Prime", "text": "Long-wear primer for all-day hold."},
            {"title": "Dimension", "text": "Gradient effect — lighter inner, medium middle, deepest outer corner."},
            {"title": "Definition", "text": "Complete look with cut-crease, smokey, or metallic finish."},
            {"title": "Line", "text": "Sharp wing liner + soft smokey detail on lower lash line."},
            {"title": "Finish", "text": "Individual lashes + setting spray to seal everything."}
        ]
    },
    "lips": {
        "everyday": [
            {"title": "Prep", "text": "Exfoliate gently + lip balm. Let absorb before applying color."},
            {"title": "Color", "text": "Tinted balm, lip oil, or sheer lipstick. One thin layer."},
            {"title": "Blend", "text": "Blot once. Soften edges with fingertip for natural look."}
        ],
        "work": [
            {"title": "Prep", "text": "Lip balm then blot excess."},
            {"title": "Color", "text": "Creamy rose, mauve, or warm terracotta. Keep edges clean."},
            {"title": "Finish", "text": "Polished look. Bring lipstick for touch-ups after meals."}
        ],
        "party": [
            {"title": "Prep", "text": "Line entire lip with matching lip liner — acts as long-wear base."},
            {"title": "Color", "text": "Apply lipstick with lip brush for precise application."},
            {"title": "Define", "text": "Clean edges with concealer brush for crisp outline."},
            {"title": "Glow", "text": "Dab gloss only in center of lips for fuller effect."}
        ],
        "date": [
            {"title": "Prep", "text": "Hydrate well then blot completely dry."},
            {"title": "Color", "text": "Creamy rose, warm coral, or soft red. Lip stain works great here."},
            {"title": "Finish", "text": "Blot once then thin final layer — more kiss-proof!"}
        ],
        "wedding/bridal": [
            {"title": "Prep", "text": "Lip mask 10 mins before starting. Blot fully dry."},
            {"title": "Base", "text": "Line entire lip with long-wear liner — secret to transfer-proof wear."},
            {"title": "Color", "text": "Apply lipstick, blot, reapply, blot again — all-day staying power."},
            {"title": "Finish", "text": "Subtle gloss only on center. Keep rest matte or satin."}
        ],
        "graduation": [
            {"title": "Prep", "text": "Light lip balm — matte formulas last longer through events."},
            {"title": "Color", "text": "Rosewood, dusty rose, or warm berry — shades that photo beautifully."},
            {"title": "Finish", "text": "Blot well. Keep lipstick in bag for touch-ups between photos."}
        ]
    }
}

def get_tutorial(skin_type, occasion, level, undertone):
    base = TUTORIALS["base"][skin_type]
    eyes = TUTORIALS["eyes"][level]
    lips = TUTORIALS["lips"][occasion]
    undertone_tip = TUTORIALS["undertone_guide"][undertone]
    return base, eyes, lips, undertone_tip

# ----------------------
# Main UI
# ----------------------
st.markdown("<h1>💄 AI Makeup Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your personalized makeup guide — step by step ✨</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='form-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        skin_type = st.selectbox("🧴 Skin Type", SKIN_TYPES)
        face_shape = st.selectbox("✨ Face Shape", FACE_SHAPES)
    with col2:
        occasion = st.selectbox("📅 Occasion", OCCASIONS)
        level = st.selectbox("🎓 Skill Level", LEVELS)
    undertone = st.selectbox("🎨 Skin Undertone", UNDERTONES)
    generate_btn = st.button("✨ Generate My Tutorial")
    st.markdown("</div>", unsafe_allow_html=True)

if generate_btn:
    user_msg = f"**Selection:** {skin_type} skin • {occasion} • {level} • {face_shape} • {undertone}"
    st.markdown(f"<div class='user-bubble'>{user_msg}</div>", unsafe_allow_html=True)

    skeleton_placeholder = st.empty()
    skeleton_html = """
    <div class='assistant-bubble'>
        <div style='width: 60%;' class='skeleton-line'></div>
        <div style='width: 85%;' class='skeleton-line'></div>
        <div style='width: 90%;' class='skeleton-line'></div>
        <div style='width: 75%;' class='skeleton-line'></div>
        <div style='width: 100%; height: 40px;' class='skeleton-line'></div>
        <div style='width: 65%;' class='skeleton-line'></div>
        <div style='width: 80%;' class='skeleton-line'></div>
        <div style='width: 95%;' class='skeleton-line'></div>
    </div>
    """
    skeleton_placeholder.markdown(skeleton_html, unsafe_allow_html=True)
    time.sleep(2.5)

    base_steps, eye_steps, lip_steps, undertone_tip = get_tutorial(skin_type, occasion, level, undertone)

    result_html = f"""
    <div class='assistant-bubble'>
        <div class='result-header'>
            ✨ Your Personalized Makeup Tutorial ✨<br>
            <small>{occasion.title()} • {level} • {skin_type} skin</small>
        </div>
        <h4 style='color:#ffd6e8; margin:0.5rem 0;'>🧴 Base & Skin Prep</h4>
    """
    for step in base_steps:
        result_html += f"""
        <div class='tutorial-card'>
            <span class='step-title'>{step['title']}</span>
            <span class='step-text'>{step['text']}</span>
        </div>
        """
    result_html += "<h4 style='color:#ffd6e8; margin:1rem 0 0.5rem;'>👁️ Eye Makeup</h4>"
    for step in eye_steps:
        result_html += f"""
        <div class='tutorial-card'>
            <span class='step-title'>{step['title']}</span>
            <span class='step-text'>{step['text']}</span>
        </div>
        """
    result_html += "<h4 style='color:#ffd6e8; margin:1rem 0 0.5rem;'>💋 Lip Color</h4>"
    for step in lip_steps:
        result_html += f"""
        <div class='tutorial-card'>
            <span class='step-title'>{step['title']}</span>
            <span class='step-text'>{step['text']}</span>
        </div>
        """
    result_html += f"""
        <div class='tip-box'>
            💡 <strong>Color Tip — {undertone.split('(')[0].strip()} Undertone:</strong> {undertone_tip}
        </div>
    </div>
    """

    # ✅ THIS IS THE CRITICAL LINE — unsafe_allow_html=True MUST BE HERE
    skeleton_placeholder.markdown(result_html, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "user", "content": f"<div class='user-bubble'>{user_msg}</div>"})
    st.session_state.messages.append({"role": "assistant", "content": result_html})

else:
    if st.session_state.messages:
        for msg in st.session_state.messages:
            # ✅ Also required here for history to render properly
            st.markdown(msg["content"], unsafe_allow_html=True)
