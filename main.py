import streamlit as st
from game import simple_calculator

def main():
    st.title('Simple Calculator')
    num1 = st.number_input("Input first number")
    num2 = st.number_input("Input second number")
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    if st.button("Calculate"):
        result = simple_calculator(num1, num2, operation)
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()