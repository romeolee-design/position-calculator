import streamlit as st

st.title("Калькулятор позиции (через % до стопа)")

# Ввод
deposit = st.number_input("Депозит ($)", min_value=1.0, value=0.0, format="%g")
risk_percent = st.number_input("Риск (%)", min_value=0.1, value=1.0, format="%g")
stop_percent = st.number_input("% до стопа", min_value=0.01, value=0.0, format="%g")

# Кнопка
if st.button("Рассчитать"):

    if deposit == 0:
        st.error("Введите депозит")
    elif stop_percent == 0:
        st.error("Введите % до стопа")
    else:
        # расчёты
        risk_amount = deposit * (risk_percent / 100)
        position_value = risk_amount / (stop_percent / 100)

        st.subheader("Результат")

        st.write(f"Риск: {risk_amount:g} $")
        st.write(f"% до стопа: {stop_percent:g}")
        st.write(f"Объём позиции: {position_value:g} $")
