import streamlit as st
import time

# ----------------------
# Page Configuration
# ----------------------
st.set_page_config(
    page_title="💄 AI Makeup Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------
# Custom CSS Styling
# ----------------------
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
* { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp {
    background: linear-gradient(135deg, #1a1025 0%, #2e1a3c 50%, #1f172b 100%);
    color: #f8e6f0;
}
.gradient-title {
    background: linear-gradient(90deg, #ff9a9e 0%, #fad0c4 50%, #fbc2eb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 2.5rem;
}
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    border: 1px solid rgba(255, 200, 220, 0.15);
    padding: 2rem;
    backdrop-filter: blur(14px);
    margin-bottom: 1.5rem;
}
.tutorial-card {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 12px;
    border-left: 4px solid #ff8fab;
    padding: 1rem 1.25rem;
    margin: 0.75rem 0;
    transition: all 0.25s ease;
}
.tutorial-card:hover {
    background: rgba(255, 255, 255, 0.08);
    transform: translateX(4px);
}
.step-title {
    font-weight: 700;
    color: #ffb3c1;
    font-size: 1rem;
}
.step-text {
    color: #f8e6f0;
    opacity: 0.9;
    font-size: 0.9rem;
    margin-top: 0.25rem;
}
.section-header {
    color: #ffc8dd;
    font-weight: 700;
    font-size: 1.1rem;
    border-bottom: 1px solid rgba(255, 183, 197, 0.2);
    padding-bottom: 0.5rem;
    margin: 1.5rem 0 1rem;
}
.banner-amber {
    background: rgba(255, 209, 102, 0.1);
    border: 1px solid rgba(255, 209, 102, 0.3);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
}
.banner-purple {
    background: rgba(167, 139, 250, 0.1);
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
}
.product-chip {
    background: rgba(255, 94, 140, 0.1);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin: 0.5rem;
    display: inline-block;
}
div.stButton > button:first-child {
    background: linear-gradient(90deg, #ff5e8c 0%, #ff8fab 100%);
    border: none;
    font-weight: 700;
    padding: 0.75rem 2rem;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(255, 94, 140, 0.4);
    width: 100%;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(255, 94, 140, 0.6);
}
</style>
""", unsafe_allow_html=True)

# ----------------------
# Tutorial Data
# ----------------------
TUTORIALS = {
    "undertone_guide": {
        "warm (yellow/golden)": "Go for golden, peach, coral, warm reds, and amber shades — avoid icy tones.",
        "cool (pink/red)": "Choose rose, berry, plum, cherry red, and pink-based nudes — avoid orange tones.",
        "neutral (balanced)": "You can pull off almost any shade! From soft nudes to bold reds — experiment freely ✨"
    },
    "face_shape_guide": {
        "oval": "Apply contour lightly under cheekbones. Highlight forehead center and chin for balanced radiance.",
        "round": "Contour along sides of jawline and temples to add soft definition and structure.",
        "square": "Soften angles by applying contour to corners of forehead and jawline. Keep blush rounded on apples.",
        "heart": "Contour the sides of forehead and point of chin. Highlight cheekbones to enhance heart shape.",
        "long": "Sweep bronzer horizontally across cheekbones and top of forehead to balance length softly.",
        "diamond": "Contour lower cheekbones to soften angular high cheeks; highlight chin and center of forehead."
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
    },
    "products": {
        "oily": ["Niacinamide Matte Primer", "Oil-Free Liquid Foundation", "Translucent Loose Setting Powder"],
        "dry": ["Hyaluronic Hydrating Primer", "Dewy Satin Cream Foundation", "Nourishing Peptide Lip Oil"],
        "combination": ["Dual-Action Balance Primer", "Medium Satin Finish Cushion", "Hydrating Tinted Balm"],
        "normal": ["Radiance SPF Glow Primer", "Sheer Tinted Skin Hydrator", "Velvet Cream Blush"],
        "sensitive": ["Calming Centella Mineral Primer", "Hypoallergenic Serum Foundation", "Soothing Peptide Lip Treatment"]
    }
}

# ----------------------
# Main UI
# ----------------------
st.markdown('<h1 class="gradient-title" style="text-align:center;">💄 AI Makeup Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#ffc8dd; opacity:0.8;">Your personalized makeup studio guide — step by step ✨</p>', unsafe_allow_html=True)

st.markdown("---")

# Input Form
col1, col2, col3 = st.columns(3)
with col1:
    skin_type = st.selectbox("🧴 Skin Type", list(TUTORIALS["base"].keys()))
with col2:
    occasion = st.selectbox("📅 Occasion", list(TUTORIALS["lips"].keys()))
with col3:
    level = st.selectbox("🎓 Skill Level", list(TUTORIALS["eyes"].keys()))

col4, col5 = st.columns(2)
with col4:
    face_shape = st.selectbox("✨ Face Shape", list(TUTORIALS["face_shape_guide"].keys()))
with col5:
    undertone = st.selectbox("🎨 Skin Undertone", list(TUTORIALS["undertone_guide"].keys()))

st.markdown("<br>", unsafe_allow_html=True)

# Generate Button
if st.button("✨ Generate My AI Tutorial", type="primary"):
    with st.spinner("Curating your personalized makeup routine..."):
        time.sleep(1.8)  # Simulate loading animation
        
    # Selection Summary
    st.markdown(f"""
    <div class="glass-card">
        <strong>Selection:</strong> {skin_type} skin • {occasion} • {level} • {face_shape} face • {undertone} undertone
    </div>
    """, unsafe_allow_html=True)
    
    # Undertone Banner
    undertone_text = TUTORIALS["undertone_guide"][undertone]
    st.markdown(f"""
    <div class="banner-amber">
        <strong style="color:#ffd166;">🎨 Color Tip — {undertone.split('(')[0].strip().upper()} Undertone</strong><br>
        {undertone_text}
    </div>
    """, unsafe_allow_html=True)
    
    # Face Shape Banner
    face_text = TUTORIALS["face_shape_guide"][face_shape]
    st.markdown(f"""
    <div class="banner-purple">
        <strong style="color:#a78bfa;">📐 Contour Tip — {face_shape.upper()} Face</strong><br>
        {face_text}
    </div>
    """, unsafe_allow_html=True)
    
    # Base & Skin Prep
    st.markdown('<p class="section-header">🧴 Base & Skin Prep</p>', unsafe_allow_html=True)
    for step in TUTORIALS["base"][skin_type]:
        st.markdown(f"""
        <div class="tutorial-card">
            <span class="step-title">{step['title']}</span>
            <span class="step-text">{step['text']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Eye Makeup
    st.markdown('<p class="section-header">👁️ Eye Makeup</p>', unsafe_allow_html=True)
    for step in TUTORIALS["eyes"][level]:
        st.markdown(f"""
        <div class="tutorial-card">
            <span class="step-title">{step['title']}</span>
            <span class="step-text">{step['text']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Lip Color
    st.markdown('<p class="section-header">💋 Lip Color</p>', unsafe_allow_html=True)
    for step in TUTORIALS["lips"][occasion]:
        st.markdown(f"""
        <div class="tutorial-card">
            <span class="step-title">{step['title']}</span>
            <span class="step-text">{step['text']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Product Recommendations
    st.markdown('<p class="section-header">🛍️ Recommended Products</p>', unsafe_allow_html=True)
    products = TUTORIALS["products"][skin_type]
    prod_cols = st.columns(len(products))
    for i, prod in enumerate(products):
        with prod_cols[i]:
            st.markdown(f"""
            <div class="product-chip" style="text-align:center;">
                <i class="fa-solid fa-sparkles" style="color:#ff8fab;"></i> {prod}
            </div>
            """, unsafe_allow_html=True)
    
    # Export text area
    st.markdown("<br>", unsafe_allow_html=True)
    export_text = f"""💄 MY AI MAKEUP ROUTINE
Selection: {skin_type} skin • {occasion} • {level} • {face_shape} face • {undertone}

🎨 Undertone Tip: {undertone_text}
📐 Contour Tip: {face_text}

--- 🧴 BASE & SKIN PREP ---
"""
    for s in TUTORIALS["base"][skin_type]:
        export_text += f"• {s['title']}: {s['text']}\n"
    export_text += "\n--- 👁️ EYE MAKEUP ---\n"
    for s in TUTORIALS["eyes"][level]:
        export_text += f"• {s['title']}: {s['text']}\n"
    export_text += "\n--- 💋 LIP COLOR ---\n"
    for s in TUTORIALS["lips"][occasion]:
        export_text += f"• {s['title']}: {s['text']}\n"
    
    st.text_area("📋 Your Routine (Copy & Save)", export_text, height=250)
