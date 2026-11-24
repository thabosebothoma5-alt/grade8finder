import streamlit as st

st.set_page_config(page_title="Grade 8 Finder", page_icon="🎓")
st.title("🎓 Grade 8 Finder - Gauteng")
st.write("Find a Grade 8 school near you. No stress, no running around.")

if "favourites" not in st.session_state:
    st.session_state.favourites = []

area = st.text_input("Type your area, e.g. Soweto, Wattville, Daveyton, Farrarmere")
fee_choice = st.selectbox("Choose fees", ["All", "No fees", "Fees"])
pass_choice = st.selectbox("Matric Pass Rate", ["All", "80% and up", "70% and up"])

schools = [
    {"name": "Morris Isaacson High School", "area": "Soweto", "fees": "No fees", "pass": 87, "phone": "011 984 1234"},
    {"name": "Orlando High School", "area": "Soweto", "fees": "No fees", "pass": 82, "phone": "011 932 5678"},
    {"name": "Selelekela Secondary", "area": "Soweto", "fees": "No fees", "pass": 78, "phone": "011 935 1111"},
    {"name": "Phefeni Secondary", "area": "Soweto", "fees": "No fees", "pass": 75, "phone": "011 934 2222"},
    {"name": "Benoni High School", "area": "Farrarmere", "fees": "Fees", "pass": 92, "phone": "011 422 2230"},
    {"name": "Willowmoore High School", "area": "Farrarmere", "fees": "Fees", "pass": 94, "phone": "011 422 3001"},
    {"name": "Thomas Nhlapo Secondary", "area": "Wattville", "fees": "No fees", "pass": 81, "phone": "011 425 1234"},
    {"name": "Mqhawe Secondary School", "area": "Wattville", "fees": "No fees", "pass": 79, "phone": "011 425 5678"},
    {"name": "Actonville Secondary", "area": "Actonville", "fees": "No fees", "pass": 76, "phone": "011 422 9876"},
    {"name": "Daveyton Secondary School", "area": "Daveyton", "fees": "No fees", "pass": 80, "phone": "011 420 1111"},
    {"name": "Mabuya Secondary School", "area": "Daveyton", "fees": "No fees", "pass": 84, "phone": "011 420 2222"},
    {"name": "Lesiba Secondary School", "area": "Daveyton", "fees": "No fees", "pass": 77, "phone": "011 420 3333"},
]

results = schools
if area:
    results = [s for s in results if area.lower() in s["area"].lower() or area.lower() in s["name"].lower()]
if fee_choice != "All":
    results = [s for s in results if s["fees"] == fee_choice]
if pass_choice == "80% and up":
    results = [s for s in results if s["pass"] >= 80]
if pass_choice == "70% and up":
    results = [s for s in results if s["pass"] >= 70]

if results:
    st.success(f"Found {len(results)} school(s)")
    for s in results:
        st.write(f"### {s['name']}")
        st.write(f"Area: {s['area']} | Fees: {s['fees']} | Pass Rate: {s['pass']}% | Phone: {s['phone']}")
        if st.button(f"Save {s['name']}", key=f"save-{s['name']}"):
            if s["name"] not in st.session_state.favourites:
                st.session_state.favourites.append(s["name"])
                st.success(f"Saved {s['name']}")
            else:
                st.info("Already saved")
        st.write("---")
else:
    st.warning("No school found. Try another area or change fees to All")

st.header("My Favourite Schools")
if st.session_state.favourites:
    for fav in st.session_state.favourites:
        st.write(f"⭐ {fav}")
    if st.button("Clear favourites"):
        st.session_state.favourites = []
else:
    st.write("You have no favourites yet. Click Save on a school.")

st.info("Tip: Grade 8 applications usually open in May. Apply early! | Made by Kappie RSA")