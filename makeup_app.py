import streamlit as st
import random

# ----------------------
# AI Makeup Assistant — Fully Working & Polished
# ----------------------
st.set_page_config(
    page_title="💄 AI Makeup Assistant",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------
# Custom CSS — Fixed & Responsive
# ----------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1025 0%, #2e1a3c 50%, #1f172b 100%);
        color: #f8e6f0;
    }
    h1 {
        background: linear-gradient(90deg, #ff9a9e 0%, #fad0c4 50%, #fbc2eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: clamp(1.8rem, 5vw, 3rem);
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #e0c8d5;
        font-size: clamp(1rem, 2.5vw, 1.2rem);
        margin-bottom: 2rem;
    }
    .form-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 200, 220, 0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffd6e8;
        border-left: 4px solid #ff8fab;
        padding-left: 0.8rem;
        margin: 1.5rem 0 1rem;
    }
    .step-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: 1rem 1.2rem;
        margin: 0.6rem 0;
        border-left: 3px solid #ff8fab;
        transition: transform 0.2s ease;
    }
    .step-card:hover {
        transform: translateX(6px);
        background: rgba(255, 255, 255, 0.08);
    }
    .product-tag {
        display: inline-block;
        background: linear-gradient(135deg, #ff8fab 0%, #ffa8B5 100%);
        color: #2b1624;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.4rem;
        font-weight: 600;
    }
    .tip-box {
        background: rgba(255, 200, 100, 0.12);
        border-radius: 14px;
        padding: 1.2rem;
        border: 1px solid rgba(255, 200, 100, 0.3);
        margin: 1.5rem 0;
    }
    .success-banner {
        background: linear-gradient(90deg, #4a2f5c 0%, #5a3b6e 100%);
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 700;
        margin: 1rem 0;
        border: 1px solid #ffc8dd;
        color: #fff;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff5e8c 0%, #ff8fab 100%);
        color: white !important;
        font-weight: 700;
        border-radius: 12px;
        padding: 0.7rem 2rem;
        border: none;
        width: 100%;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover:first-child {
        transform: scale(1.03);
        box-shadow: 0 6px 25px rgba(255, 94, 140, 0.4);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px 12px 0 0;
        padding: 0.7rem 1.2rem;
        border: 1px solid transparent;
        color: #d4c4d8;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(255, 140, 180, 0.2);
        border-color: #ff8fab;
        color: #fff;
        font-weight: 600;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        color: #b8a0b0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# Database — Complete
# ----------------------
SKIN_TYPES = ["oily", "dry", "combination", "normal", "sensitive"]
OCCASIONS = ["everyday", "work", "party", "date", "wedding/bridal", "graduation"]
LEVELS = ["beginner", "intermediate", "advanced"]
FACE_SHAPES = ["oval", "round", "square", "heart", "long", "diamond"]
UNDERTONES = ["warm (yellow/golden)", "cool (pink/red)", "neutral (balanced)"]

TUTORIALS = {
    "base": {
        "oily": [
            "**Prep:** Start with oil-free, non-comedogenic moisturizer — let it absorb fully (2–3 mins).",
            "**Prime:** Apply mattifying primer only on T-zone to control shine without drying cheeks.",
            "**Foundation:** Use water-based or oil-free formula — apply in thin layers with damp sponge.",
            "**Conceal:** Dab only on blemishes & under eyes; blend outward — avoid heavy buildup.",
            "**Set:** Press translucent powder on T-zone; leave cheeks powder-free for dimension."
        ],
        "dry": [
            "**Prep:** Apply hydrating cream + facial oil; wait 5–8 mins to sink in completely.",
            "**Prime:** Use hydrating, illuminating primer — creates smooth, dewy canvas.",
            "**Foundation:** Cream or satin-finish liquid — apply with fingers for warmth & better blend.",
            "**Conceal:** Cream formula under eyes — pat gently, never drag.",
            "**Set:** Light powder only on T-zone; use setting spray to lock in dewy finish."
        ],
        "combination": [
            "**Prep:** Lightweight lotion on T-zone; richer cream on dry cheek areas.",
            "**Prime:** Mattifying on forehead/nose; hydrating on cheeks & jawline.",
            "**Foundation:** Medium-coverage — blend well, especially along jaw & neck.",
            "**Conceal:** Spot-apply only where needed; feather edges outward.",
            "**Set:** T-zone lightly powdered; cheeks left natural or set with dewy spray."
        ],
        "normal": [
            "**Prep:** Light moisturizer + SPF — let settle 2 mins.",
            "**Prime:** Any type — match your desired finish (dewy/matte).",
            "**Foundation:** Tinted moisturizer or light-medium coverage — match to neck.",
            "**Conceal:** Brighten under eyes; cover any redness.",
            "**Set:** Setting spray or light powder — your preference!"
        ],
        "sensitive": [
            "**Prep:** Fragrance-free, hypoallergenic moisturizer — pat gently, no rubbing.",
            "**Prime:** Skip if irritation occurs; choose sensitive-skin base products.",
            "**Foundation:** Mineral or dermatologist-tested — apply with clean sponge.",
            "**Conceal:** Fragrance-free formula — dab lightly.",
            "**Set:** Talc-free gentle powder — apply sparingly."
        ]
    },
    "eyes": {
        "beginner": [
            "**Base:** Neutral beige or taupe all over lid up to brow bone.",
            "**Depth:** Soft warm brown in crease — blend back-and-forth like a wiper.",
            "**Brighten:** Champagne shimmer on center of lid with finger.",
            "**Define:** Brown pencil liner along upper lash line — softer than black.",
            "**Finish:** Curl lashes + mascara — wiggle from roots up, 1–2 coats."
        ],
        "intermediate": [
            "**Prime:** Eye primer all over lid — prevents creasing.",
            "**Transition:** Soft warm shade in crease, darker toward outer corner.",
            "**Lid:** Shimmer or satin shade; highlight inner corner & brow bone.",
            "**Line:** Thin winged liner OR tightline between lashes.",
            "**Finish:** Curl lashes + mascara; soft brown on lower lash line optional."
        ],
        "advanced": [
            "**Prime:** Long-wear base for max staying power.",
            "**Dimension:** Gradient blend — light inner, medium middle, deep outer.",
            "**Definition:** Cut-crease, smokey, or metallic finish.",
            "**Line:** Sharp wing + detailed lower lash smokey.",
            "**Finish:** Individual lashes + setting spray to seal."
        ]
    },
    "lips": {
        "everyday": [
            "**Prep:** Exfoliate gently then apply lip balm — let absorb.",
            "**Color:** Tinted balm, lip oil, or sheer lipstick — one thin layer.",
            "**Blend:** Blot; soften edges with finger for natural look."
        ],
        "work": [
            "**Prep:** Balm — blot excess.",
            "**Color:** Creamy rose, mauve, or terracotta — clean edges.",
            "**Finish:** Professional & long-lasting — reapply after meals."
        ],
        "party": [
            "**Prep:** Line entire lip with matching liner — acts as base.",
            "**Color:** Apply lipstick with brush for precision.",
            "**Define:** Clean edges with concealer brush.",
            "**Glow:** Dot gloss only in center for fuller effect."
        ],
        "date": [
            "**Prep:** Hydrate well; blot dry.",
            "**Color:** Creamy rose, warm coral, or soft red — buildable stain.",
            "**Finish:** Blot once then thin layer — kiss-proof friendly!"
        ],
        "wedding/bridal": [
            "**Prep:** Lip mask 10 mins before; blot completely dry.",
            "**Base:** Long-wear liner all over lips.",
            "**Color:** Apply, blot, reapply, blot — transfer-proof finish.",
            "**Finish:** Subtle gloss on center only."
        ],
        "graduation": [
            "**Prep:** Light balm — matte formulas last longer all day.",
            "**Color:** Rosewood, dusty rose, or warm berry — photogenic shades.",
            "**Finish:** Blot well; bring lipstick for photo touch-ups."
        ]
    },
    "contour_bronze": {
        "oval": [
            "✨ **Oval Face — Naturally Balanced**",
            "• **Contour:** Under cheekbones from ears toward center (stop halfway); light along jawline.",
            "• **Bronzer:** Highest cheekbones, across forehead lightly, along jaw — sun-kissed pattern.",
            "• **Blush:** Apples of cheeks, blended upward toward temples.",
            "• **Tip:** Keep it soft — your shape is already perfect!"
        ],
        "round": [
            "✨ **Round Face — Create Definition**",
            "• **Contour:** Temples, sweep upward & outward under cheekbones, along jaw.",
            "• **Bronzer:** Higher on cheekbones, across forehead, light on chin tip.",
            "• **Blush:** Slightly higher on cheeks to lift face.",
            "• **Tip:** Upward angles — avoid circular blending!"
        ],
        "square": [
            "✨ **Square Face — Soften Angles**",
            "• **Contour:** Soften jaw corners inward; temples near hairline.",
            "• **Bronzer:** On cheekbones, center forehead, softly on chin.",
            "• **Blush:** On apples, blend outward to widen.",
            "• **Tip:** Gentle circles to soften sharp lines."
        ],
        "heart": [
            "✨ **Heart Face — Balance Proportions**",
            "• **Contour:** Sides of forehead; under cheekbones; touch on chin tip.",
            "• **Bronzer:** Lower cheeks & jaw; light on forehead.",
            "• **Blush:** Mid-cheeks — not too high.",
            "• **Tip:** Contour temples gently to narrow forehead."
        ],
        "long": [
            "✨ **Long Face — Shorten & Widen**",
            "• **Contour:** Across upper forehead/temples; horizontal along jaw.",
            "• **Bronzer:** Cheekbones horizontally, across chin.",
            "• **Blush:** Broad sweep across cheeks.",
            "• **Tip:** Keep all placement horizontal!"
        ],
        "diamond": [
            "✨ **Diamond Face — Balance Width**",
            "• **Contour:** Temples & upper cheekbones to soften width.",
            "• **Bronzer:** Below cheekbones, across forehead & chin.",
            "• **Blush:** Apples of cheeks — adds softness.",
            "• **Tip:** Soften temples to balance narrow forehead/chin."
        ]
    },
    "undertone_guide": {
        "warm (yellow/golden)": "Best: golden, peach, orange, warm red, amber, bronze, honey. Avoid: icy pinks & cool blues.",
        "cool (pink/red)": "Best: rose, berry, plum, cherry red, mauve, silver-pink. Avoid: overly orange/earthy shades.",
        "neutral (balanced)": "Lucky you! Most shades work — experiment freely. Warm golds & soft roses look especially lovely."
    },
    "ph_products": {
        "budget": [
            "Maybelline — Watsons/SM, ₱200–₱600",
            "Ever Bilena — Local drugstore, ₱150–₱400",
            "BYS — SM Department Store, ₱199–₱500",
            "Sunnies Face — Shopee/Lazada, ₱349–₱690",
            "Vice Cosmetics — Nationwide, ₱199–₱500"
        ],
        "mid-range": [
            "Colourette — Multi-use, ₱299–₱799",
            "blk Cosmetics — Clean & elegant, ₱399–₱899",
            "Happy Skin — Skincare-infused, ₱499–₱999",
            "Ellana — Mineral & gentle, ₱500–₱1,200",
            "Human Nature — Natural & cruelty-free, ₱300–₱800"
        ],
        "premium": [
            "Sephora Collection — Sephora.ph, ₱1,000–₱3,000+",
            "Rare Beauty — Sephora PH, ₱1,500–₱2,500+",
            "MAC — Rustan's/SM, ₱1,200–₱3,500+",
            "Benefit — Sephora/Rustan's, ₱1,500–₱3,000+"
        ]
    },
    "pro_tips": [
        "💡 Always blend upward & outward — gives natural face-lift effect.",
        "💡 Let each product absorb 1–2 mins before next step = longer lasting look.",
        "💡 Check makeup in natural window light — phone flash can deceive!",
        "💡 For Filipina skin: Warm golden, peach, terracotta & coral are universally flattering.",
        "💡 Cream products blend easier with fingers; use brushes for powder precision.",
        "💡 Apply bronzer where sun naturally hits: forehead, nose bridge, cheekbones, chin.",
        "💡 When in doubt, blend longer — seamless > perfect.",
        "💡 Remove makeup completely before bed — your skin will thank you!"
    ]
}

# ----------------------
# Helper Functions
# ----------------------
def get_lip_key(occasion):
    return {
        "everyday": "everyday",
        "work": "work",
        "party": "party",
        "date": "date",
        "wedding/bridal": "wedding/bridal",
        "graduation": "graduation"
    }.get(occasion, "everyday")

def get_product_key(selection):
    sel = selection.lower()
    if "budget" in sel: return "budget"
    if "mid-range" in sel: return "mid-range"
    if "premium" in sel: return "premium"
    return "budget"

# ----------------------
# Main App
# ----------------------
st.markdown("<h1>💄 AI Makeup Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Create your personalized makeup routine ✨</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='form-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        skin_type = st.selectbox("🧴 Your Skin Type", SKIN_TYPES)
        face_shape = st.selectbox("✨ Your Face Shape", FACE_SHAPES)
        undertone = st.selectbox("🎨 Your Skin Undertone", UNDERTONES)
    
    with col2:
        occasion = st.selectbox("💒 Occasion", OCCASIONS)
        level = st.selectbox("📖 Experience Level", LEVELS)
        product_tier = st.radio(
            "🛍️ Budget (Philippines)",
            ["Budget (₱150–₱600)", "Mid-Range (₱300–₱1,200)", "Premium (₱1,000+)"],
            index=0,
            horizontal=True
        )
    
    generate = st.button("✨ Generate My Tutorial")
    
    st.markdown("</div>", unsafe_allow_html=True)

if generate:
    lip_key = get_lip_key(occasion)
    tier_key = get_product_key(product_tier)
    
    base_steps = TUTORIALS["base"][skin_type]
    eye_steps = TUTORIALS["eyes"][level]
    lip_steps = TUTORIALS["lips"][lip_key]
    contour_steps = TUTORIALS["contour_bronze"][face_shape]
    undertone_guide = TUTORIALS["undertone_guide"][undertone]
    products = TUTORIALS["ph_products"][tier_key]
    tip = random.choice(TUTORIALS["pro_tips"])

    st.markdown(f"""
    <div class='success-banner'>
        ✨ Your {occasion.upper()} Tutorial is Ready!<br>
        <small>{skin_type.title()} skin • {face_shape} face • {undertone.split()[0]} undertone • {level} level</small>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🧴 Base", "👁️ Eyes", "💋 Lips", "🎨 Contour", "🎨 Undertone", "🛍️ Products"
    ])

    with tab1:
        st.markdown("<p class='section-header'>Base & Complexion</p>", unsafe_allow_html=True)
        st.caption(f"Optimized for {skin_type} skin")
        for step in base_steps:
            st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<p class='section-header'>Eye Makeup</p>", unsafe_allow_html=True)
        st.caption(f"Skill Level: {level}")
        for step in eye_steps:
            st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<p class='section-header'>Lip Look</p>", unsafe_allow_html=True)
        st.caption(f"Perfect for {occasion}")
        for step in lip_steps:
            st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown("<p class='section-header'>Contour & Bronzing</p>", unsafe_allow_html=True)
        st.caption(f"Face Shape: {face_shape}")
        for line in contour_steps:
            st.markdown(line)

    with tab5:
        st.markdown("<p class='section-header'>Undertone Shade Guide</p>", unsafe_allow_html=True)
        st.caption(f"Your undertone: {undertone}")
        st.info(undertone_guide)

    with tab6:
        st.markdown("<p class='section-header'>Recommended Products — Philippines 🇵🇭</p>", unsafe_allow_html=True)
        st.caption(f"Category: {product_tier}")
        for prod in products:
            brand, desc = prod.split(" — ", 1)
            st.markdown(f"<span class='product-tag'>✅ {brand}</span><br><small>{desc}</small><br>", unsafe_allow_html=True)
        
        st.markdown("<div class='tip-box'>", unsafe_allow_html=True)
        st.markdown(f"**💡 Daily Pro Tip:** {tip}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("**Where to shop:** Lazada • Shopee • Watsons • The SM Store • Sephora.ph • Rustan's • BeautyMNL")
        st.markdown("*Shade tip: For warm undertones — look for 'warm', 'golden', or 'tan' on labels*")

st.markdown("""
<div class='footer'>
💖 Made with love for Cagayan de Oro & across the Philippines 💖<br>
Always remember: The best makeup is your confidence! ✨
</div>
""", unsafe_allow_html=True)