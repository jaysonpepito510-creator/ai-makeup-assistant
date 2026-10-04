import streamlit as st
import random

# ----------------------
# AI Makeup Assistant — Clean Beauty-App Style
# Creator: Angelica S. Aniñon 💖
# No chatbot formatting — elegant guide layout only
# ----------------------
st.set_page_config(
    page_title="💄 AI Makeup Assistant",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------
# Session State
# ----------------------
if "active_view" not in st.session_state:
    st.session_state.active_view = "generate"
if "user_input" not in st.session_state:
    st.session_state.user_input = {}

# ----------------------
# Custom CSS — Elegant & Clean
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
    .confidence-banner {
        background: linear-gradient(90deg, rgba(255,94,140,0.2) 0%, rgba(168,85,247,0.2) 100%);
        border-radius: 20px;
        padding: clamp(1.5rem, 5vw, 2rem);
        margin: 1rem 0 2rem;
        text-align: center;
        border: 1px solid rgba(255,140,180,0.3);
    }
    .confidence-text {
        font-size: clamp(1.1rem, 4vw, 1.5rem);
        font-weight: 700;
        color: #ffd6e8;
        margin-top: 0.5rem;
    }
    .form-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: clamp(1.5rem, 5vw, 2rem);
        border: 1px solid rgba(255, 200, 220, 0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffd6e8;
        border-left: 4px solid #ff8fab;
        padding-left: 1rem;
        margin: 2rem 0 1rem;
    }
    .tutorial-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin: 0.8rem 0;
        border-left: 3px solid #ff8fab;
        transition: all 0.25s ease;
        line-height: 1.7;
    }
    .tutorial-card:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(4px);
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
        border-radius: 16px;
        padding: 1.2rem;
        margin: 1rem 0 2rem;
        border: 1px solid rgba(255, 140, 180, 0.25);
    }
    .catalog-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 0;
        margin: 0.8rem 0;
        border: 1px solid rgba(255, 180, 210, 0.2);
        transition: all 0.3s ease;
        overflow: hidden;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .catalog-card:hover {
        transform: translateY(-3px);
        border-color: #ff8fab;
        box-shadow: 0 8px 25px rgba(255, 94, 140, 0.15);
    }
    .card-image-container {
        width: 100%;
        height: 180px;
        overflow: hidden;
    }
    .card-image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    .catalog-card:hover .card-image-container img {
        transform: scale(1.05);
    }
    .card-content {
        padding: 1.2rem;
        flex-grow: 1;
    }
    .product-name {
        font-weight: 700;
        color: #ffd6e8;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .product-brand {
        color: #ffb3c1;
        font-size: 0.9rem;
    }
    .product-price {
        display: inline-block;
        background: rgba(255, 140, 180, 0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        color: #ff9abb;
        margin: 0.5rem 0;
    }
    .product-desc {
        color: #d4c4d8;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    .product-tag {
        display: inline-block;
        background: linear-gradient(135deg, #ff8fab 0%, #ffa8B5 100%);
        color: #2b1624;
        border-radius: 20px;
        padding: 0.3rem 0.7rem;
        margin: 0.25rem;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .tip-box {
        background: rgba(255, 200, 100, 0.12);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 200, 100, 0.3);
        margin: 2rem 0;
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
        transition: all 0.3s ease;
    }
    div.stButton > button:hover:first-child {
        transform: scale(1.02);
        box-shadow: 0 6px 25px rgba(255, 94, 140, 0.4);
    }
    div.stButton:nth-child(2) > button:first-child {
        background: linear-gradient(90deg, #7b2ffd 0%, #a855f7 100%);
    }
    div.stButton:nth-child(2) > button:hover:first-child {
        box-shadow: 0 6px 25px rgba(168, 85, 247, 0.4);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px 12px 0 0;
        padding: 0.7rem 1.1rem;
        border: 1px solid transparent;
        color: #d4c4d8;
        font-weight: 500;
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
        padding: 2rem;
        color: #b8a0b0;
        font-size: 0.9rem;
    }
    .back-note {
        text-align: center;
        color: #c8b8d0;
        margin: 1rem 0;
    }
    @media (min-width: 768px) {
        .catalog-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
    }
    @media (min-width: 1024px) {
        .catalog-grid {
            grid-template-columns: repeat(3, 1fr);
        }
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# Database — Clean & Structured
# ----------------------
SKIN_TYPES = ["oily", "dry", "combination", "normal", "sensitive"]
OCCASIONS = ["everyday", "work", "party", "date", "wedding/bridal", "graduation"]
LEVELS = ["beginner", "intermediate", "advanced"]
FACE_SHAPES = ["oval", "round", "square", "heart", "long", "diamond"]
UNDERTONES = ["warm (yellow/golden)", "cool (pink/red)", "neutral (balanced)"]

TUTORIALS = {
    "base": {
        "oily": [
            {"title": "Prep", "text": "Start with oil-free, non-comedogenic moisturizer — let it absorb fully, about 2 to 3 minutes."},
            {"title": "Prime", "text": "Apply mattifying primer only on your T-zone to control shine without drying your cheeks."},
            {"title": "Foundation", "text": "Use water-based or oil-free formula. Apply in thin layers using a damp beauty sponge."},
            {"title": "Conceal", "text": "Dab only on blemishes and under eyes. Blend outward gently — avoid building up too much product."},
            {"title": "Set", "text": "Press translucent powder onto T-zone. Leave cheeks powder-free for natural dimension."}
        ],
        "dry": [
            {"title": "Prep", "text": "Apply rich hydrating cream plus facial oil. Wait 5 to 8 minutes to let it sink in completely."},
            {"title": "Prime", "text": "Use hydrating, illuminating primer — creates a smooth, dewy canvas."},
            {"title": "Foundation", "text": "Choose cream or satin-finish formula. Apply with clean fingertips for warmth and seamless blend."},
            {"title": "Conceal", "text": "Use cream formula under eyes. Pat gently — never drag or pull at delicate skin."},
            {"title": "Set", "text": "Apply light powder only on T-zone. Finish with dewy setting spray to lock in moisture and glow."}
        ],
        "combination": [
            {"title": "Prep", "text": "Use lightweight lotion on T-zone and richer cream on dry cheek areas."},
            {"title": "Prime", "text": "Apply mattifying primer on forehead and nose; use hydrating primer on cheeks and jawline."},
            {"title": "Foundation", "text": "Medium-coverage works best. Blend well, especially along jawline and down onto your neck."},
            {"title": "Conceal", "text": "Spot-apply only where needed. Feather edges outward so there are no visible lines."},
            {"title": "Set", "text": "Lightly powder T-zone. Leave cheeks natural or finish with dewy setting spray."}
        ],
        "normal": [
            {"title": "Prep", "text": "Light moisturizer plus SPF. Let settle for 2 minutes before next step."},
            {"title": "Prime", "text": "Any primer works — choose based on your desired finish: dewy or matte."},
            {"title": "Foundation", "text": "Tinted moisturizer or light-to-medium coverage. Always match shade to your neck, not your face."},
            {"title": "Conceal", "text": "Brighten under eyes and cover any redness. Keep it light."},
            {"title": "Set", "text": "Setting spray or light powder — whichever you prefer!"}
        ],
        "sensitive": [
            {"title": "Prep", "text": "Fragrance-free, hypoallergenic moisturizer. Pat gently — do not rub hard."},
            {"title": "Prime", "text": "Skip if it causes irritation. Always choose sensitive-skin friendly base products."},
            {"title": "Foundation", "text": "Mineral or dermatologist-tested formula. Apply with clean sponge or fingertips."},
            {"title": "Conceal", "text": "Fragrance-free formula. Dab lightly only where needed."},
            {"title": "Set", "text": "Use talc-free gentle powder. Apply very sparingly."}
        ]
    },
    "eyes": {
        "beginner": [
            {"title": "Base", "text": "Sweep neutral beige or taupe shade all over eyelid up to brow bone."},
            {"title": "Depth", "text": "Blend soft warm brown into crease using back-and-forth windshield-wiper motion."},
            {"title": "Brighten", "text": "Pat champagne shimmer onto center of lid using your finger for best payoff."},
            {"title": "Define", "text": "Line upper lash line with brown pencil — softer and more forgiving than black."},
            {"title": "Finish", "text": "Curl lashes then apply mascara. Wiggle wand from roots upward. 1 to 2 coats only."}
        ],
        "intermediate": [
            {"title": "Prime", "text": "Apply eye primer all over lid — prevents creasing and helps color last longer."},
            {"title": "Transition", "text": "Blend soft warm shade into crease, deepen color gradually toward outer corner."},
            {"title": "Lid", "text": "Pat shimmer or satin shade onto lid. Add highlight to inner corner and brow bone."},
            {"title": "Line", "text": "Create thin winged liner OR tightline right between upper lashes."},
            {"title": "Finish", "text": "Curl lashes + mascara. Soft brown on lower lash line is optional."}
        ],
        "advanced": [
            {"title": "Prime", "text": "Use long-wear eye primer for maximum staying power all day."},
            {"title": "Dimension", "text": "Build gradient effect — lighter inner lid, medium middle, deepest shade outer corner."},
            {"title": "Definition", "text": "Complete your look with cut-crease, smokey, or metallic finish."},
            {"title": "Line", "text": "Sharp wing liner plus detailed soft smokey effect on lower lash line."},
            {"title": "Finish", "text": "Individual false lashes plus setting spray to seal everything in place."}
        ]
    },
    "lips": {
        "everyday": [
            {"title": "Prep", "text": "Gently exfoliate then apply lip balm. Let absorb fully before applying color."},
            {"title": "Color", "text": "Tinted balm, lip oil, or sheer lipstick. One thin layer is enough."},
            {"title": "Blend", "text": "Blot once. Soften edges with your fingertip for natural, lived-in look."}
        ],
        "work": [
            {"title": "Prep", "text": "Apply lip balm then blot away excess."},
            {"title": "Color", "text": "Creamy rose, mauve, or warm terracotta. Keep edges clean and defined."},
            {"title": "Finish", "text": "Professional and polished. Bring your lipstick for quick touch-ups after meals."}
        ],
        "party": [
            {"title": "Prep", "text": "Line entire lip with lip liner matching your lipstick — this acts as long-wearing base."},
            {"title": "Color", "text": "Apply lipstick with lip brush for clean, precise application."},
            {"title": "Define", "text": "Clean up edges with concealer brush for crisp, perfect outline."},
            {"title": "Glow", "text": "Dab a little gloss only in center of lips to create fuller effect."}
        ],
        "date": [
            {"title": "Prep", "text": "Hydrate well then blot completely dry."},
            {"title": "Color", "text": "Creamy rose, warm coral, or soft red. Buildable lip stain is perfect here."},
            {"title": "Finish", "text": "Blot once then apply thin final layer — more kiss-proof and long-lasting!"}
        ],
        "wedding/bridal": [
            {"title": "Prep", "text": "Use lip mask 10 minutes before starting makeup. Blot completely dry."},
            {"title": "Base", "text": "Line entire lip with long-wear lip liner — this is your secret to transfer-proof wear."},
            {"title": "Color", "text": "Apply lipstick, blot, reapply, blot again. This creates all-day staying power."},
            {"title": "Finish", "text": "Subtle gloss only on center of lips. Keep rest matte or satin for elegance."}
        ],
        "graduation": [
            {"title": "Prep", "text": "Light lip balm — matte formulas generally last longer through long events."},
            {"title": "Color", "text": "Rosewood, dusty rose, or warm berry — shades that look beautiful in photos."},
            {"title": "Finish", "text": "Blot well. Keep lipstick in your bag for touch-ups between photos."}
        ]
    },
    "contour_bronze": {
        "oval": [
            {"title": "Face Shape Guide", "text": "✨ Oval face — naturally balanced proportions."},
            {"title": "Contour", "text": "Under cheekbones from ears toward center — stop halfway. Light along jawline."},
            {"title": "Bronzer", "text": "Highest points of cheekbones, lightly across forehead, along jawline — sun-kissed pattern."},
            {"title": "Blush", "text": "Apply on apples of cheeks, blend upward toward temples."},
            {"title": "Pro Tip", "text": "Keep everything soft and blended — your shape is already perfect!"}
        ],
        "round": [
            {"title": "Face Shape Guide", "text": "✨ Round face — create definition and lift."},
            {"title": "Contour", "text": "At temples, sweep upward and outward under cheekbones, along jawline."},
            {"title": "Bronzer", "text": "Higher on cheekbones, across forehead, light on tip of chin."},
            {"title": "Blush", "text": "Slightly higher on cheeks to visually lift face."},
            {"title": "Pro Tip", "text": "Always blend upward and outward — avoid circular motions!"}
        ],
        "square": [
            {"title": "Face Shape Guide", "text": "✨ Square face — soften strong angles."},
            {"title": "Contour", "text": "Soften corners of jawline inward. Contour temples near hairline."},
            {"title": "Bronzer", "text": "Across cheekbones, center forehead, softly on chin."},
            {"title": "Blush", "text": "On apples, blend outward to add width to lower face."},
            {"title": "Pro Tip", "text": "Use gentle circular blending to soften sharp lines."}
        ],
        "heart": [
            {"title": "Face Shape Guide", "text": "✨ Heart face — balance forehead and chin."},
            {"title": "Contour", "text": "Sides of forehead, under cheekbones, light touch on tip of chin."},
            {"title": "Bronzer", "text": "Lower cheeks and jawline. Keep light on forehead."},
            {"title": "Blush", "text": "Mid-cheeks — not too high — adds softness and balance."},
            {"title": "Pro Tip", "text": "Gently contour temples to visually narrow forehead."}
        ],
        "long": [
            {"title": "Face Shape Guide", "text": "✨ Long face — shorten and widen visually."},
            {"title": "Contour", "text": "Across upper forehead and temples. Horizontal along jawline."},
            {"title": "Bronzer", "text": "Across cheekbones horizontally, across chin."},
            {"title": "Blush", "text": "Broad sweep across cheeks — keeps everything horizontal."},
            {"title": "Pro Tip", "text": "Keep all placement horizontal — never blend vertically."}
        ],
        "diamond": [
            {"title": "Face Shape Guide", "text": "✨ Diamond face — balance width at temples and cheekbones."},
            {"title": "Contour", "text": "Temples and upper cheekbones to soften widest points."},
            {"title": "Bronzer", "text": "Below cheekbones, across forehead and chin."},
            {"title": "Blush", "text": "On apples of cheeks — adds softness and warmth."},
            {"title": "Pro Tip", "text": "Soften temples to balance narrow forehead and chin."}
        ]
    },
    "undertone_guide": {
        "warm (yellow/golden)": "Best shades: golden, peach, orange, warm red, amber, bronze, honey. Shades to avoid: icy pinks and cool blues.",
        "cool (pink/red)": "Best shades: rose, berry, plum, cherry red, mauve, silver-pink. Shades to avoid: overly orange or earthy tones.",
        "neutral (balanced)": "You're so lucky! Most shades look beautiful on you. Warm golds and soft roses look especially lovely."
    },
    "catalog": [
        {
            "category": "Base & Prep",
            "name": "Hydrating Primer",
            "brand": "Sunnies Face",
            "price": "₱399",
            "image_url": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=300&fit=crop",
            "desc": "Lightweight, dewy finish — perfect for dry and normal skin. Makes foundation glide smoothly.",
            "best_for": ["Dry skin", "Dewy look", "Everyday"]
        },
        {
            "category": "Base & Prep",
            "name": "Mattifying Primer",
            "brand": "Maybelline",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f98?w=400&h=300&fit=crop",
            "desc": "Controls shine all day — minimizes appearance of large pores on T-zone.",
            "best_for": ["Oily skin", "Combination skin", "Long wear"]
        },
        {
            "category": "Base & Prep",
            "name": "Skin Tint",
            "brand": "Colourette",
            "price": "₱325",
            "image_url": "https://images.unsplash.com/photo-1608248597279-f3e0a1b925e0?w=400&h=300&fit=crop",
            "desc": "Sheer, natural coverage with skincare benefits — buildable, lightweight, comfortable.",
            "best_for": ["Everyday", "Beginner-friendly", "All skin types"]
        },
        {
            "category": "Base & Prep",
            "name": "Velvet Foundation",
            "brand": "Ever Bilena",
            "price": "₱295",
            "image_url": "https://images.unsplash.com/photo-1619451334792-150fd785ee74?w=400&h=300&fit=crop",
            "desc": "Medium-to-full matte coverage — affordable, long-lasting, great for oily skin.",
            "best_for": ["Oily skin", "Work & Party", "Budget-friendly"]
        },
        {
            "category": "Base & Prep",
            "name": "Conceal & Perfect Concealer",
            "brand": "Vice Cosmetics",
            "price": "₱249",
            "image_url": "https://images.unsplash.com/photo-1597225204655-99a93a2d18ea?w=400&h=300&fit=crop",
            "desc": "Covers dark circles and blemishes — crease-resistant, brightens under eyes.",
            "best_for": ["All skin types", "Brightening", "Budget pick"]
        },
        {
            "category": "Base & Prep",
            "name": "Translucent Setting Powder",
            "brand": "BYS",
            "price": "₱220",
            "image_url": "https://images.unsplash.com/photo-1571786410632-3b05c9a0d0d5?w=400&h=300&fit=crop",
            "desc": "Sets makeup without heaviness — blurs pores, extends wear time.",
            "best_for": ["All skin types", "Finishing touch", "Everyday"]
        },
        {
            "category": "Eyes",
            "name": "Everyday Neutrals Eyeshadow Palette",
            "brand": "blk Cosmetics",
            "price": "₱599",
            "image_url": "https://images.unsplash.com/photo-1583241800698-e8ab01830a9a?w=400&h=300&fit=crop",
            "desc": "Warm mattes and soft shimmers — perfectly curated for Filipina skin tones.",
            "best_for": ["Beginners", "Everyday", "Warm undertones"]
        },
        {
            "category": "Eyes",
            "name": "Lash Curler + Mascara Duo",
            "brand": "Maybelline",
            "price": "₱380",
            "image_url": "https://images.unsplash.com/photo-1600818586115-73d705bb0658?w=400&h=300&fit=crop",
            "desc": "Curls that hold plus volume and length in one. Waterproof option available.",
            "best_for": ["Beginners", "Everyday", "Date look"]
        },
        {
            "category": "Eyes",
            "name": "Precision Brown Eyeliner Pencil",
            "brand": "Sunnies Face",
            "price": "₱299",
            "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f98?w=400&h=300&fit=crop",
            "desc": "Softer than black — defines eyes gently, smudge-proof, easy to blend.",
            "best_for": ["Beginners", "Soft definition", "Everyday"]
        },
        {
            "category": "Eyes",
            "name": "Liquid Liner — Black Velvet",
            "brand": "Happy Skin",
            "price": "₱450",
            "image_url": "https://images.unsplash.com/photo-1599305090590-0d10c3a07a85?w=400&h=300&fit=crop",
            "desc": "Fine tip for sharp wings — quick-drying, long-wearing, no skipping.",
            "best_for": ["Intermediate+", "Party", "Date"]
        },
        {
            "category": "Eyes",
            "name": "Brow Gel & Pencil Set",
            "brand": "Ellana",
            "price": "₱680",
            "image_url": "https://images.unsplash.com/photo-1608579404353-4b49e0f43e3c?w=400&h=300&fit=crop",
            "desc": "Natural-looking fibers plus precise pencil — fills gaps, keeps brows neat all day.",
            "best_for": ["All levels", "Frame your face", "Sensitive skin"]
        },
        {
            "category": "Eyes",
            "name": "Champagne Highlighter Eyeshadow",
            "brand": "Sephora Collection",
            "price": "₱1,100",
            "image_url": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=300&fit=crop",
            "desc": "Silky metallic finish — brightens center of lid and inner corner instantly.",
            "best_for": ["Special occasions", "Glow", "Premium pick"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Multi-Use Cream Blush",
            "brand": "Colourette",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1608248597279-f3e0a1b925e0?w=400&h=300&fit=crop",
            "desc": "Lips and cheeks in one — dewy, blendable, universally flattering shades.",
            "best_for": ["Everyday", "Quick routine", "All skin types"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Sun-Kissed Bronzer",
            "brand": "BYS",
            "price": "₱250",
            "image_url": "https://images.unsplash.com/photo-1597225220465-99a93a2d18ea?w=400&h=300&fit=crop",
            "desc": "Warm golden-brown — creates instant warmth, perfect for Filipino skin.",
            "best_for": ["Warm undertones", "Dewy glow", "Everyday"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Sculpt Contour Stick",
            "brand": "Ever Bilena",
            "price": "₱265",
            "image_url": "https://images.unsplash.com/photo-1619451334792-150fd785ee74?w=400&h=300&fit=crop",
            "desc": "Cream-to-powder — easy to blend, defines cheekbones and jawline.",
            "best_for": ["Beginners", "All face shapes", "Budget-friendly"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Diamond Glow Highlighter",
            "brand": "MAC",
            "price": "₱1,850",
            "image_url": "https://images.unsplash.com/photo-1571786410632-3b05c9a0d0d5?w=400&h=300&fit=crop",
            "desc": "Radiant buildable shimmer — catches light beautifully, luxurious finish.",
            "best_for": ["Special events", "Premium glow", "Bridal"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Soft Blush Palette",
            "brand": "Vice Cosmetics",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1583241800698-e8ab01830a9a?w=400&h=300&fit=crop",
            "desc": "Four blendable shades — matte and satin finishes, mix and match daily.",
            "best_for": ["Versatile", "All undertones", "Great value"]
        },
        {
            "category": "Lips",
            "name": "Tinted Lip Oil — Rosy Glow",
            "brand": "Sunnies Face",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1599305090590-0d10c3a07a85?w=400&h=300&fit=crop",
            "desc": "Hydrating plus sheer color — comfortable, non-sticky, everyday essential.",
            "best_for": ["Everyday", "Dry lips", "Natural look"]
        },
        {
            "category": "Lips",
            "name": "Creamy Matte Lipstick — Rosewood",
            "brand": "Maybelline",
            "price": "₱399",
            "image_url": "https://images.unsplash.com/photo-1600818586115-73d705bb0658?w=400&h=300&fit=crop",
            "desc": "Rich, comfortable matte — long-lasting, doesn't dry out lips.",
            "best_for": ["Work", "Graduation", "Warm undertones"]
        },
        {
            "category": "Lips",
            "name": "Transfer-Proof Lip Stain",
            "brand": "Colourette",
            "price": "₱299",
            "image_url": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=300&fit=crop",
            "desc": "Lightweight, buildable color — kiss-proof, stays fresh through meals.",
            "best_for": ["Date", "Everyday", "Long wear"]
        },
        {
            "category": "Lips",
            "name": "Luxury Lipstick — Classic Red",
            "brand": "MAC",
            "price": "₱1,200",
            "image_url": "https://images.unsplash.com/photo-1585237017125-24bafd0c36f6?w=400&h=300&fit=crop",
            "desc": "Iconic satin finish — one swipe of confidence, timeless and elegant.",
            "best_for": ["Bridal", "Party", "Special occasions"]
        },
        {
            "category": "Finishing",
            "name": "Dewy Setting Spray",
            "brand": "Happy Skin",
            "price": "₱420",
            "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f98?w=400&h=300&fit=crop",
            "desc": "Locks makeup plus healthy glow — hydrating formula, fine mist.",
            "best_for": ["Dry & Normal skin", "All-day wear", "Dewy finish"]
        },
        {
            "category": "Finishing",
            "name": "Makeup Remover Balm",
            "brand": "Human Nature",
            "price": "₱380",
            "image_url": "https://images.unsplash.com/photo-1608579424134-b9a4d872d418?w=400&h=300&fit=crop",
            "desc": "Gentle, natural, zero-waste — melts away makeup without irritation.",
            "best_for": ["Sensitive skin", "Night routine", "Cruelty-free"]
        }
    ],
    "pro_tips": [
        "Always blend upward and outward — gives natural face-lift effect.",
        "Let each product absorb 1 to 2 minutes before next step = longer lasting look.",
        "Check makeup in natural window light — phone flash can be misleading!",
        "For Filipina skin: warm golden, peach, terracotta and coral shades are universally flattering.",
        "Cream products blend easier with fingertips; use brushes for powder precision.",
        "Apply bronzer where sun naturally hits: forehead, nose bridge, cheekbones, chin.",
        "When in doubt, blend longer — seamless is better than perfect.",
        "Remove makeup completely before bed — your skin will thank you!"
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

def generate_tutorial(skin_type, face_shape, undertone, occasion, level):
    lip_key = get_lip_key(occasion)
    return {
        "occasion": occasion,
        "skin_type": skin_type,
        "face_shape": face_shape,
        "undertone": undertone,
        "level": level,
        "base": TUTORIALS["base"][skin_type],
        "eyes": TUTORIALS["eyes"][level],
        "lips": TUTORIALS["lips"][lip_key],
        "contour": TUTORIALS["contour_bronze"][face_shape],
        "undertone_guide": TUTORIALS["undertone_guide"][undertone],
        "tip": random.choice(TUTORIALS["pro_tips"])
    }

# ----------------------
# Main App
# ----------------------
st.markdown("<h1>💄 AI Makeup Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Create your personalized makeup routine ✨</p>", unsafe_allow_html=True)

st.markdown("""
<div class='confidence-banner'>
    <div style='font-size: 3rem; margin-bottom: 0.5rem;'>✨💄✨</div>
    <p class='confidence-text'>The best makeup is your confidence!</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col_nav1, col_nav2 = st.columns(2)
with col_nav1:
    gen_btn = st.button("✨ Generate My Tutorial", use_container_width=True)
with col_nav2:
    cat_btn = st.button("📖 Makeup Catalog", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# View Switch
if gen_btn:
    st.session_state.active_view = "generate"
elif cat_btn:
    st.session_state.active_view = "catalog"
    st.markdown("<p class='back-note'>💡 Set your details below and click <strong>Generate My Tutorial</strong> for your custom routine!</p>", unsafe_allow_html=True)

# ==================================================
# VIEW 1: GENERATE — Clean Elegant Layout
# ==================================================
if st.session_state.active_view == "generate":
    with st.container():
        st.markdown("<div class='form-card'>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            skin_type = st.selectbox("🧴 Your Skin Type", SKIN_TYPES, 
                                     index=st.session_state.user_input.get("skin_idx", 0))
            face_shape = st.selectbox("✨ Your Face Shape", FACE_SHAPES,
                                      index=st.session_state.user_input.get("face_idx", 0))
            undertone = st.selectbox("🎨 Your Skin Undertone", UNDERTONES,
                                     index=st.session_state.user_input.get("tone_idx", 0))
        
        with col2:
            occasion = st.selectbox("💒 Occasion", OCCASIONS,
                                   index=st.session_state.user_input.get("occ_idx", 0))
            level = st.selectbox("📖 Experience Level", LEVELS,
                                index=st.session_state.user_input.get("level_idx", 0))
            product_tier = st.radio(
                "🛍️ Budget (Philippines)",
                ["Budget (₱150–₱600)", "Mid-Range (₱300–₱1,200)", "Premium (₱1,000+)"],
                index=st.session_state.user_input.get("tier_idx", 0),
                horizontal=True
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Save selections
        st.session_state.user_input = {
            "skin_idx": SKIN_TYPES.index(skin_type),
            "face_idx": FACE_SHAPES.index(face_shape),
            "tone_idx": UNDERTONES.index(undertone),
            "occ_idx": OCCASIONS.index(occasion),
            "level_idx": LEVELS.index(level),
            "tier_idx": ["Budget (₱150–₱600)", "Mid-Range (₱300–₱1,200)", "Premium (₱1,000+)"].index(product_tier),
        }
        
        # Generate routine
        tutorial = generate_tutorial(skin_type, face_shape, undertone, occasion, level)
        
        # Result Header — Clean & Clear
        st.markdown(f"""
        <div class='result-header'>
            <h3 style='margin:0; color:#ffd6e8;'>✨ Your {tutorial['occasion'].title()} Makeup Routine</h3>
            <p style='margin:0.5rem 0 0; color:#d4c4d8; font-size:0.95rem;'>
                {tutorial['skin_type'].title()} skin • {tutorial['face_shape']} face • {tutorial['undertone'].split()[0]} undertone • {tutorial['level']} level
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabs — Clean Layout
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🧴 Base & Complexion", 
            "👁️ Eye Makeup", 
            "💋 Lip Look", 
            "🎨 Contour & Bronze", 
            "🎨 Undertone Guide"
        ])
        
        with tab1:
            st.markdown("<p class='section-header'>Base & Complexion</p>", unsafe_allow_html=True)
            st.caption(f"Optimized for {tutorial['skin_type']} skin")
            for step in tutorial["base"]:
                st.markdown(f"""
                <div class='tutorial-card'>
                    <span class='step-title'>{step['title']}:</span>
                    <span class='step-text'>{step['text']}</span>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("<p class='section-header'>Eye Makeup</p>", unsafe_allow_html=True)
            st.caption(f"Skill Level: {tutorial['level']}")
            for step in tutorial["eyes"]:
                st.markdown(f"""
                <div class='tutorial-card'>
                    <span class='step-title'>{step['title']}:</span>
                    <span class='step-text'>{step['text']}</span>
                </div>
                """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("<p class='section-header'>Lip Look</p>", unsafe_allow_html=True)
            st.caption(f"Perfect for {tutorial['occasion']}")
            for step in tutorial["lips"]:
                st.markdown(f"""
                <div class='tutorial-card'>
                    <span class='step-title'>{step['title']}:</span>
                    <span class='step-text'>{step['text']}</span>
                </div>
                """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("<p class='section-header'>Contour & Bronzing</p>", unsafe_allow_html=True)
            st.caption(f"Face Shape: {tutorial['face_shape']}")
            for step in tutorial["contour"]:
                st.markdown(f"""
                <div class='tutorial-card'>
                    <span class='step-title'>{step['title']}:</span>
                    <span class='step-text'>{step['text']}</span>
                </div>
                """, unsafe_allow_html=True)
        
        with tab5:
            st.markdown("<p class='section-header'>Undertone Shade Guide</p>", unsafe_allow_html=True)
            st.caption(f"Your undertone: {tutorial['undertone']}")
            st.info(tutorial["undertone_guide"])
        
        # Daily Tip
        st.markdown(f"""
        <div class='tip-box'>
            <strong>💡 Daily Pro Tip:</strong> {tutorial['tip']}
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        st.markdown("💡 **Next:** Click **📖 Makeup Catalog** above to browse products that match your routine!")

# ==================================================
# VIEW 2: CATALOG — With Real Product Photos
# ==================================================
else:
    st.markdown("<h2 style='text-align:center; font-size:1.5rem; margin-bottom:0.5rem;'>📖 Makeup Catalog</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#d4c4d8; margin-bottom:2rem;'>Curated products available in the Philippines 🇵🇭</p>", unsafe_allow_html=True)
    
    cat_filter = st.selectbox("Filter by Category:", ["All"] + sorted(list({item["category"] for item in TUTORIALS["catalog"]})))
    
    filtered = TUTORIALS["catalog"] if cat_filter == "All" else [i for i in TUTORIALS["catalog"] if i["category"] == cat_filter]
    
    st.markdown("<div class='catalog-grid'>", unsafe_allow_html=True)
    for item in filtered:
        st.markdown(f"""
        <div class='catalog-card'>
            <div class='card-image-container'>
                <img src='{item["image_url"]}' alt='{item["name"]}' loading='lazy'>
            </div>
            <div class='card-content'>
                <span style='font-size:0.8rem; color:#a890a0;'>{item['category']}</span>
                <div class='product-name'>{item['name']}</div>
                <div class='product-brand'>by {item['brand']}</div>
                <div class='product-price'>{item['price']}</div>
                <div class='product-desc'>{item['desc']}</div>
                <div style='margin-top:0.8rem;'>
                    {''.join([f"<span class='product-tag'>{tag}</span>" for tag in item['best_for']])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='tip-box'>
        <strong>🛍️ Where to Buy:</strong> Lazada • Shopee • Watsons • The SM Store • Sephora.ph • BeautyMNL • Rustan's
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin-top:2rem; opacity:0.2;'>", unsafe_allow_html=True)
    st.markdown("<p class='back-note'>✨ Ready for your custom routine? Click <strong>✨ Generate My Tutorial</strong> above & I'll craft one just for you!</p>", unsafe_allow_html=True)

# ----------
