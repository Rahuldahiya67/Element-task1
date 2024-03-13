import streamlit as st
import re
import csv

def find_year(input_text):
    pattern1 = r'\.\s*(\d{4})\s*,'  # Pattern for year between full stop and comma
    pattern2 = r'\(\s*(\d{4})\s*\)'  # Pattern for year within parentheses
    pattern3 = r'\s*(\d{4})\s*,'      # Pattern for year followed by a comma without a preceding full stop
    match1 = re.search(pattern1, input_text)
    match2 = re.search(pattern2, input_text)
    match3 = re.search(pattern3, input_text)
    if match1:
        return match1.group(1)
    elif match2:
        return match2.group(1)
    elif match3:
        return match3.group(1)
    else:
        return None

# Input and output filenames
input_file = 'final_dataset.csv'  # Change to your input file name

# Streamlit UI
st.title('Year Finder App')

uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('**Input Data:**')
    st.write(df)

    st.write('**Extracted Years:**')
    extracted_years = []
    for index, row in df.iterrows():
        year = find_year(row['Input'])
        extracted_years.append(year)
    df['Extracted Year'] = extracted_years
    st.write(df)

    # Save the extracted years to a new CSV file
    st.write('**Save Extracted Years:**')
    if st.button('Save Extracted Years as CSV'):
        save_filename = 'extracted_years.csv'
        df.to_csv(save_filename, index=False)
        st.success(f'Extracted years saved to {save_filename}')
