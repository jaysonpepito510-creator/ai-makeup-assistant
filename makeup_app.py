import streamlit as st
import random

# ----------------------
# AI Makeup Assistant — With Real Product Images
# Creator: Angelica S. Aniñon 💖
# + Generate-first flow
# + Real product photos on all catalog cards
# ----------------------
st.set_page_config(
    page_title="💄 AI Makeup Assistant",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------
# Session State — Remember Flow State
# ----------------------
if "active_view" not in st.session_state:
    st.session_state.active_view = "generate"
if "user_input" not in st.session_state:
    st.session_state.user_input = {}

# ----------------------
# Custom CSS — Fully Responsive + Image Cards
# ----------------------
st.markdown("""
<style>
    * {
        box-sizing: border-box;
    }
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
        line-height: 1.2;
    }
    .subtitle {
        text-align: center;
        color: #e0c8d5;
        font-size: clamp(0.9rem, 3vw, 1.2rem);
        margin-bottom: 1.5rem;
        padding: 0 0.5rem;
    }
    .confidence-banner {
        background: linear-gradient(90deg, rgba(255,94,140,0.2) 0%, rgba(168,85,247,0.2) 100%);
        border-radius: 16px;
        padding: clamp(1.2rem, 5vw, 2rem);
        margin: 2rem 0;
        text-align: center;
        border: 1px solid rgba(255,140,180,0.3);
    }
    .confidence-text {
        font-size: clamp(1.1rem, 4vw, 1.5rem);
        font-weight: 700;
        color: #ffd6e8;
        margin-top: 1rem;
    }
    .form-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: clamp(1rem, 5vw, 2rem);
        border: 1px solid rgba(255, 200, 220, 0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 1.5rem;
        max-width: 100%;
    }
    .section-header {
        font-size: clamp(1.1rem, 3vw, 1.4rem);
        font-weight: 700;
        color: #ffd6e8;
        border-left: 4px solid #ff8fab;
        padding-left: 0.8rem;
        margin: 1.5rem 0 1rem;
    }
    .step-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: clamp(0.8rem, 3vw, 1.2rem);
        margin: 0.6rem 0;
        border-left: 3px solid #ff8fab;
        transition: transform 0.2s ease;
        font-size: clamp(0.9rem, 2.5vw, 1rem);
        line-height: 1.6;
    }
    .step-card:hover {
        transform: translateX(4px);
        background: rgba(255, 255, 255, 0.08);
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
        background: linear-gradient(135deg, #ff8fab33 0%, #a855f733 100%);
        display: flex;
        align-items: center;
        justify-content: center;
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
        display: flex;
        flex-direction: column;
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
        flex-grow: 1;
    }
    .product-tag {
        display: inline-block;
        background: linear-gradient(135deg, #ff8fab 0%, #ffa8B5 100%);
        color: #2b1624;
        border-radius: 20px;
        padding: 0.4rem 0.8rem;
        margin: 0.3rem;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .tip-box {
        background: rgba(255, 200, 100, 0.12);
        border-radius: 14px;
        padding: clamp(1rem, 4vw, 1.2rem);
        border: 1px solid rgba(255, 200, 100, 0.3);
        margin: 1.5rem 0;
    }
    .success-banner {
        background: linear-gradient(90deg, #4a2f5c 0%, #5a3b6e 100%);
        border-radius: 14px;
        padding: clamp(1rem, 4vw, 1.2rem);
        text-align: center;
        font-size: clamp(1rem, 3vw, 1.1rem);
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
        padding: 0.8rem 2rem;
        border: none;
        width: 100%;
        font-size: clamp(1rem, 3vw, 1.1rem);
        transition: all 0.3s ease;
        min-height: 48px;
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
        gap: 0.3rem;
        background: transparent;
        flex-wrap: wrap;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px 12px 0 0;
        padding: 0.6rem 0.9rem;
        border: 1px solid transparent;
        color: #d4c4d8;
        font-size: clamp(0.8rem, 2.5vw, 0.95rem);
        white-space: nowrap;
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
        font-size: clamp(0.8rem, 2.5vw, 0.9rem);
        line-height: 1.6;
    }
    .back-note {
        text-align: center;
        color: #c8b8d0;
        font-size: 0.9rem;
        margin: 0.5rem 0 1rem;
    }
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 280px;
    }
    @media (min-width: 768px) {
        [data-testid="column"] {
            width: 50% !important;
            flex: 1 !important;
        }
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
    .block-container {
        padding-left: max(1rem, 3vw) !important;
        padding-right: max(1rem, 3vw) !important;
        max-width: 100% !important;
        overflow-x: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# Database — With Real Product Images
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
    "catalog": [
        {
            "category": "Base & Prep",
            "name": "Hydrating Primer",
            "brand": "Sunnies Face",
            "price": "₱399",
            "image_url": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=300&fit=crop",
            "desc": "Lightweight, dewy finish — perfect for dry & normal skin. Makes foundation glide smoothly.",
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
            "best_for": ["Oily skin", "Work/Party", "Budget-friendly"]
        },
        {
            "category": "Base & Prep",
            "name": "Conceal & Perfect Concealer",
            "brand": "Vice Cosmetics",
            "price": "₱249",
            "image_url": "https://images.unsplash.com/photo-1597225204655-99a93a2d18ea?w=400&h=300&fit=crop",
            "desc": "Covers dark circles & blemishes — crease-resistant, brightens under eyes.",
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
            "desc": "Warm mattes & soft shimmers — perfectly curated for Filipina skin tones.",
            "best_for": ["Beginners", "Everyday", "Warm undertones"]
        },
        {
            "category": "Eyes",
            "name": "Lash Curler + Mascara Duo",
            "brand": "Maybelline",
            "price": "₱380",
            "image_url": "https://images.unsplash.com/photo-1600818586115-73d705bb0658?w=400&h=300&fit=crop",
            "desc": "Curls that hold + volume & length in one. Waterproof option available.",
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
            "desc": "Natural-looking fibers + precise pencil — fills gaps, keeps brows neat all day.",
            "best_for": ["All levels", "Frame your face", "Sensitive skin"]
        },
        {
            "category": "Eyes",
            "name": "Champagne Highlighter Eyeshadow",
            "brand": "Sephora Collection",
            "price": "₱1,100",
            "image_url": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=300&fit=crop",
            "desc": "Silky metallic finish — brightens center of lid & inner corner instantly.",
            "best_for": ["Special occasions", "Glow", "Premium pick"]
        },
        {
            "category": "Cheeks & Contour",
            "name": "Multi-Use Cream Blush",
            "brand": "Colourette",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1608248597279-f3e0a1b925e0?w=400&h=300&fit=crop",
            "desc": "Lips + cheeks in one — dewy, blendable, universally flattering shades.",
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
            "desc": "Cream-to-powder — easy to blend, defines cheekbones & jawline.",
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
            "desc": "Four blendable shades — matte & satin finishes, mix & match daily.",
            "best_for": ["Versatile", "All undertones", "Great value"]
        },
        {
            "category": "Lips",
            "name": "Tinted Lip Oil — Rosy Glow",
            "brand": "Sunnies Face",
            "price": "₱349",
            "image_url": "https://images.unsplash.com/photo-1599305090590-0d10c3a07a85?w=400&h=300&fit=crop",
            "desc": "Hydrating + sheer color — comfortable, non-sticky, everyday essential.",
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
            "desc": "Iconic satin finish — one swipe of confidence, timeless & elegant.",
            "best_for": ["Bridal", "Party", "Special occasions"]
        },
        {
            "category": "Finishing",
            "name": "Dewy Setting Spray",
            "brand": "Happy Skin",
            "price": "₱420",
            "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f98?w=400&h=300&fit=crop",
            "desc": "Locks makeup + adds healthy glow — hydrating formula, fine mist.",
            "best_for": ["Dry/Normal skin", "All-day wear", "Dewy finish"]
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
    <div style='font-size: 3rem;'>✨💄✨</div>
    <p class='confidence-text'>The best makeup is your confidence!</p>
</div>
""", unsafe_allow_html=True)

# ---------- NAVIGATION BUTTONS ----------
col_nav1, col_nav2 = st.columns(2)
with col_nav1:
    gen_btn = st.button("✨ Generate My Tutorial", use_container_width=True)
with col_nav2:
    cat_btn = st.button("📖 Make-up Catalog", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- FLOW CONTROL ----------
if gen_btn:
    st.session_state.active_view = "generate"
elif cat_btn:
    st.session_state.active_view = "catalog"
    st.markdown("<p class='back-note'>💡 Tip: Set your details below & click <strong>Generate My Tutorial</strong> for a personalized routine!</p>", unsafe_allow_html=True)

# ==================================================
# VIEW 1: GENERATE — Default / First Flow
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
        
        tutorial = generate_tutorial(skin_type, face_shape, undertone, occasion, level)
        
        st.markdown(f"""
        <div class='success-banner'>
            ✨ Your {tutorial['occasion'].upper()} Tutorial is Ready!<br>
            <small>{tutorial['skin_type'].title()} skin • {tutorial['face_shape']} face • {tutorial['undertone'].split()[0]} undertone • {tutorial['level']} level</small>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🧴 Base", "👁️ Eyes", "💋 Lips", "🎨 Contour", "🎨 Undertone"
        ])
        
        with tab1:
            st.markdown("<p class='section-header'>Base & Complexion</p>", unsafe_allow_html=True)
            st.caption(f"Optimized for {tutorial['skin_type']} skin")
            for step in tutorial["base"]:
                st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)
        
        with tab2:
            st.markdown("<p class='section-header'>Eye Makeup</p>", unsafe_allow_html=True)
            st.caption(f"Skill Level: {tutorial['level']}")
            for step in tutorial["eyes"]:
                st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)
        
        with tab3:
            st.markdown("<p class='section-header'>Lip Look</p>", unsafe_allow_html=True)
            st.caption(f"Perfect for {tutorial['occasion']}")
            for step in tutorial["lips"]:
                st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)
        
        with tab4:
            st.markdown("<p class='section-header'>Contour & Bronzing</p>", unsafe_allow_html=True)
            st.caption(f"Face Shape: {tutorial['face_shape']}")
            for line in tutorial["contour"]:
                st.markdown(line)
        
        with tab5:
            st.markdown("<p class='section-header'>Undertone Shade Guide</p>", unsafe_allow_html=True)
            st.caption(f"Your undertone: {tutorial['undertone']}")
            st.info(tutorial["undertone_guide"])
        
        st.markdown("<div class='tip-box'>", unsafe_allow_html=True)
        st.markdown(f"**💡 Daily Pro Tip:** {tutorial['tip']}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("💡 **Next:** Click **📖 Make-up Catalog** above to browse recommended products that match your routine!")

# ==================================================
# VIEW 2: CATALOG — With Real Product Photos
# ==================================================
else:
    st.markdown("<h2 class='section-header' style='border:none; padding-left:0; text-align:center;'>📖 Make-up Catalog — 22 Curated Items</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#d4c4d8;'>Handpicked products available in the Philippines 🇵🇭</p>", unsafe_allow_html=True)
    
    cat_filter = st.selectbox("Filter by Category:", ["All"] + sorted(list({item["category"] for item in TUTORIALS["catalog"]})))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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
    <div class='tip-box' style='margin-top:2rem;'>
        <strong>🛍️ Where to Buy:</strong> Lazada • Shopee • Watsons • The SM Store • Sephora.ph • BeautyMNL • Rustan's
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin-top:2rem; opacity:0.2;'>", unsafe_allow_html=True)
    st.markdown("<p class='back-note'>✨ Ready for your custom routine? Click <strong>✨ Generate My Tutorial</strong> above & I'll craft one just for you!</p>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
💖 Made with love for You By: Angelica S. Aniñon 💖<br>
Always remember: The best makeup is your confidence! ✨
</div>
""", unsafe_allow_html=True)
