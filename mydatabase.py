import streamlit as st

# Function to convert Bits to dollars
def convert_bits_to_dollars(bits):
  return bits * 0.01

# Add some formatting to the title

st.markdown("<h1 style='text-align: center; color: green;'>Twitch Bits to US Dollar Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: blue;'>Enter the number of Bits to convert</h3>", unsafe_allow_html=True)

# Get number of Bits from user
bits = st.number_input(" ",key='bits', min_value=0)

# Convert Bits to dollars
dollars = convert_bits_to_dollars(bits)

# Display result to user


# Add some formatting to make the display look nice
st.markdown("---")
st.markdown(f"<h1 style='text-align: center; color: green;'>{bits} Bits is equal to ${dollars:.2f}</h1>", unsafe_allow_html=True)

# Add some styling to the input area
st.markdown("<style>input {font-size: 20px; padding: 10px; border-radius: 5px;}</style>", unsafe_allow_html=True)


