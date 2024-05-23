import streamlit as st

# Define tax slabs and rates for FY 2024-25 (Individual)
# New Tax Regime slabs
new_tax_slabs = {
    "Up to ₹3 lakhs": 0.0,
    "₹3 lakhs to ₹6 lakhs": 0.05,
    "₹6 lakhs to ₹9 lakhs": 0.1,
    "₹9 lakhs to ₹12 lakhs": 0.2,
    "₹12 lakhs to ₹15 lakhs": 0.3,
    "Above ₹15 lakhs": 0.3
}
capital_gains_tax_rates = {
    "Short-term capital gains (< 1 year)": 0.1,  # Placeholder, update with actual rate
    "Long-term capital gains (> 1 year)": 0.2,  # Placeholder, update with actual rate
}


# Old Tax Regime slabs (replace placeholders with actual rates if available)
old_tax_slabs = {
    "Up to ₹2.5 lakhs": 0.0,
    "₹2.5 lakhs to ₹5 lakhs": 0.05,
    "₹5 lakhs to ₹10 lakhs": 0.20,  # Placeholder, update with actual rates
    "Above ₹10 lakhs": 0.30,  # Placeholder, update with actual rates
}

# Define tax surcharge for income above ₹5 crore
tax_surcharge = {
    "Above ₹5 crore": 0.37
}

# Define standard deduction for different categories
standard_deductions = {
    "Salaried (Resident)": 50000,
    "Senior Citizen (Resident, 60+ years)": 75000,
    "Very Senior Citizen (Resident, 80+ years)": 100000,
    "NRI (Resident but not ordinarily resident)": 0,  # Placeholder, update with actual deduction
    "NRI (Non-resident)": 0,  # Placeholder, update with actual deduction
}

# Define other optional deductions (replace placeholders with actual values/calculation logic)
optional_deductions = {
    "HRA (House Rent Allowance)": 0,
    "Section 80C (Investments)": 0,
    "Section 80D (Medical Insurance)": 0,
    "Section 24 (Home Loan Interest)": 0,
    # Add more deductions as needed
}

# Capital gains tax rates (replace placeholders with actual rates for different asset types)
capital_gains_tax_rates = {
    "Short-term capital gains (< 1 year)": 0.1,  # Placeholder, update with actual rate
    "Long-term capital gains (> 1 year)": 0.2,  # Placeholder, update with actual rate
}

# Streamlit app title
st.set_page_config(page_title="India Income Tax Calculator (FY 2024-25)")

# App header with formatted title
st.header("Calculate Your Income Tax in India")

# User selection for residency status (with clear descriptions)
resident_status = st.selectbox(
    "Residency Status",
    [
        "Resident (Salaried, Business, etc.)",
        "NRI (Resident but not ordinarily resident)",
        "NRI (Non-resident)",
    ],
)

# User input for annual income
annual_income = st.number_input("Enter your annual income (₹)", min_value=0.00)

# User selection for tax filing category based on residency
if resident_status in ["Resident (Salaried, Business, etc.)", "NRI (Resident but not ordinarily resident)"]:
    selected_category = st.selectbox("Tax Filing Category", list(standard_deductions.keys()))
else:
    selected_category = "NRI (Non-resident)"  # Preset for non-resident

# User selection for tax regime (New or Old)
selected_regime = st.selectbox("Select Tax Regime", ["New Tax Regime", "Old Tax Regime"])

# User selection for optional deductions (checkboxes with descriptions)
selected_deductions = {}
for deduction_name, _ in optional_deductions.items():
    deduction_description = f"{deduction_name} (Details)"  # Replace with brief explanation for each deduction
    selected_deductions[deduction_name] = st.checkbox(deduction_description)

# User input for short-term capital gains (optional)
short_term_capital_gains = st.number_input("Enter Short-Term Capital Gains (₹)", min_value=0.00)

# User input for long-term capital gains (optional)
# User input for F&O income (optional)
fno_income = st.number_input("Enter F&O Income (₹)", min_value=0.00)

# Calculate taxable income
taxable_income = annual_income - standard_deductions[selected_category]

# Apply selected deductions (replace placeholders with actual calculation logic)
for deduction_name, value in selected_deductions.items():
    if value:
        taxable_income -= value  # Replace with actual deduction calculation
# F&O tax treatment (replace with actual logic)

  #fno_tax_rate = 0.0  # Placeholder

if fno_income > 0:
    # Check for specific F&O contract types (e.g., equity options, currency futures)
    # Apply relevant tax rates based on holding period (short-term/long-term)
    # You might need additional user inputs or calculations here

    # Example (replace with actual rates based on your research):
    fno_tax_rate = 0.1  # Placeholder for short-term F&O gains
    if holding_period > 1 year:
        fno_tax_rate = 0.05 
        
# Add capital gains and F&O income (placeholder for F&O)
#taxable_income += short_term_capital_gains * capital_gains_tax_rates["Short-term capital gains"]
taxable_income += fno_income * fno_tax_rate  # Placeholder, update with actual F&O tax treatment

# Calculate tax based on selected regime (replace placeholders with actual slabs and rates)
tax_amount = 0
if selected_regime == "New Tax Regime":
    for slab, rate in new_tax_slabs.items():
        if taxable_income <= float(slab.split()[0].replace("₹", "")):
            tax_amount += (taxable_income * rate)
            break
        else:
            taxable_income -= float(slab.split()[0].replace("₹", ""))
            tax_amount += (float(slab.split()[0].replace("₹", "")) * rate)
else:
    # Similar logic for Old Tax Regime (update with actual slabs and rates)
    pass

# Apply tax surcharge if applicable
if taxable_income > 50000000:
    tax_amount += tax_amount * tax_surcharge["Above ₹5 crore"]

# Display final tax payable
st.subheader("Your Estimated Tax Payable (₹)")
st.write(f"{tax_amount:.2f}")

# Disclaimer (add details as needed)
st.info(
    "Disclaimer: This is an estimated tax calculation tool. Please consult a tax professional for accurate tax advice."
)
