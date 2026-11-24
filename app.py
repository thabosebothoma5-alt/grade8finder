import streamlit as st
import urllib.parse

st.set_page_config(page_title="Grade 8 Finder - Gauteng", page_icon="🎓")

st.title("🎓 Grade 8 Finder - Gauteng")
st.write("Find a Grade 8 school near you. Search, filter, share on WhatsApp.")

if "favourites" not in st.session_state:
    st.session_state.favourites = []

# --- SCHOOLS DATABASE ---
schools = [
    # Soweto
    {"name": "Morris Isaacson High School", "area": "Soweto", "fees": "No fees", "pass": 87, "phone": "011 980 1234"},
    {"name": "Orlando High School", "area": "Soweto", "fees": "No fees", "pass": 82, "phone": "011 933 5678"},
    {"name": "Moletsane Secondary", "area": "Soweto", "fees": "No fees", "pass": 78, "phone": "011 985 4321"},
    # Daveyton / Benoni
    {"name": "Daveyton Secondary School", "area": "Daveyton", "fees": "No fees", "pass": 75, "phone": "011 420 1111"},
    {"name": "Mabuya Secondary School", "area": "Daveyton", "fees": "No fees", "pass": 73, "phone": "011 420 2222"},
    {"name": "Benoni High School", "area": "Benoni", "fees": "Fees", "pass": 92, "phone": "011 422 2230"},
    {"name": "Willowmoore High School", "area": "Benoni", "fees": "Fees", "pass": 94, "phone": "011 422 3001"},
    {"name": "Thomas Nhlapo Secondary", "area": "Wattville", "fees": "No fees", "pass": 71, "phone": "011 425 1234"},
    # Tembisa
    {"name": "Tembisa High School", "area": "Tembisa", "fees": "No fees", "pass": 80, "phone": "011 924 1001"},
    {"name": "Boitumelo Secondary School", "area": "Tembisa", "fees": "No fees", "pass": 77, "phone": "011 924 2002"},
    {"name": "Masiqhakaze Secondary", "area": "Tembisa", "fees": "No fees", "pass": 74, "phone": "011 924 3003"},
    # Katlehong
    {"name": "Katlehong High School", "area": "Katlehong", "fees": "No fees", "pass": 79, "phone": "011 905 1111"},
    {"name": "Thoko Thaba Secondary", "area": "Katlehong", "fees": "No fees", "pass": 76, "phone": "011 905 2222"},
    # Vosloorus
    {"name": "Vosloorus Comprehensive", "area": "Vosloorus", "fees": "No fees", "pass": 81, "phone": "011 906 1111"},
    {"name": "Kgotso Secondary", "area": "Vosloorus", "fees": "No fees", "pass": 72, "phone": "011 906 2222"},
    # Pretoria
    {"name": "Pretoria High School for Girls", "area": "Pretoria", "fees": "Fees", "pass": 98, "phone": "012 344 1234"},
    {"name": "Mamelodi High School", "area": "Mamelodi", "fees": "No fees", "pass": 83, "phone": "012 801 5678"},
    {"name": "Soshanguve High School", "area": "Soshanguve", "fees": "No fees", "pass": 78, "phone": "012 799 4321"},
]

# --- 1. SEARCH + 2. FILTERS ---
st.subheader("🔍 Search & Filter")

search = st.text_input("Search school name, e.g. Morris, Tembisa, Pretoria")

col1, col2, col3 = st.columns(3)
with col1:
    area_filter = st.selectbox("Area", ["All Areas"] + sorted(list(set([s["area"] for s in schools]))))
with col2:
    fee_filter = st.selectbox("Fees", ["All", "No fees", "Fees"])
with col3:
    pass_filter = st.selectbox("Pass Rate", ["All", "80%+", "70%+", "90%+"])

results = schools
if search:
    results = [s for s in results if search.lower() in s["name"].lower() or search.lower() in s["area"].lower()]
if area_filter != "All Areas":
    results = [s for s in results if s["area"] == area_filter]
if fee_filter != "All":
    results = [s for s in results if s["fees"] == fee_filter]
if pass_filter == "80%+":
    results = [s for s in results if s["pass"] >= 80]
if pass_filter == "70%+":
    results = [s for s in results if s["pass"] >= 70]
if pass_filter == "90%+":
    results = [s for s in results if s["pass"] >= 90]

# --- RESULTS ---
st.success(f"Found {len(results)} school(s)")

for s in results:
    st.write(f"### {s['name']}")
    st.write(f"📍 {s['area']} | 💰 {s['fees']} | 📊 {s['pass']}% Pass | 📞 {s['phone']}")

    # 3. WHATSAPP SHARE
    msg = f"Check this Grade 8 school: {s['name']} in {s['area']} - {s['fees']}, {s['pass']}% pass rate. Phone: {s['phone']}. Found on Grade 8 Finder!"
    wa_link = "https://wa.me/?text=" + urllib.parse.quote(msg)
    st.markdown(f"[📲 Share on WhatsApp]({wa_link})")

    if st.button(f"⭐ Save {s['name']}", key=s["name"]):
        if s["name"] not in st.session_state.favourites:
            st.session_state.favourites.append(s["name"])
            st.success(f"Saved {s['name']}")
    st.write("---")

if not results:
    st.warning("No school found. Try clearing search or filters.")

# Favourites
st.header("⭐ My Favourite Schools")
if st.session_state.favourites:
    for fav in st.session_state.favourites:
        st.write(f"⭐ {fav}")
    if st.button("Clear favourites"):
        st.session_state.favourites = []
        st.rerun()
else:
    st.write("No favourites yet.")

st.info("💡 Tip: Grade 8 applications open in May on GDE Admissions. Apply early!")
st.markdown("[👉 Apply on GDE Website](https://www.gdeadmissions.gov.za/)")
