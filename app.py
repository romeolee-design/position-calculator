import streamlit as st

st.title("Калькулятор позиции (через % до стопа)")

# Ввод
deposit = st.number_input("Депозит ($)", min_value=1.0, value=100000.0, format="%g")
risk_percent = st.number_input("Риск (%)", min_value=0.1, value=1.0, format="%g")
stop_percent = st.number_input("% до стопа", min_value=0.01, value=10.0, format="%g")
rr = st.number_input("RR (например 2 = 1:2)", min_value=0.1, value=2.0, format="%g")

# Кнопка
if st.button("Рассчитать"):

    # расчёты
    risk_amount = deposit * (risk_percent / 100)
    position_value = risk_amount / (stop_percent / 100)

    profit_amount = risk_amount * rr
    take_percent = stop_percent * rr

    st.subheader("Результат")

    st.write(f"Риск: {risk_amount:g} $")
    st.write(f"% до стопа: {stop_percent:g}")
    st.write(f"Объём позиции: {position_value:g} $")

    st.write("---")

    st.write(f"RR: 1:{rr:g}")
    st.write(f"Тейк (%): {take_percent:g}")
    st.write(f"Прибыль ($): {profit_amount:g}")
