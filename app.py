import streamlit as st

st.title("Калькулятор позиции")

# Ввод данных
deposit = st.number_input("Депозит ($)", min_value=1.0, value=100000.0)
risk_percent = st.number_input("Риск (%)", min_value=0.1, value=1.0)
entry = st.number_input("Цена входа", value=0.0)
stop = st.number_input("Стоп", value=0.0)
rr = st.number_input("RR (например 2)", min_value=0.1, value=2.0)

# Кнопка расчета
if st.button("Рассчитать"):

    if entry == stop:
        st.error("Ошибка: вход равен стопу")
    elif entry == 0:
        st.error("Ошибка: вход не может быть 0")
    else:
        risk_amount = deposit * (risk_percent / 100)
        stop_distance = abs(entry - stop)

        if entry > stop:
            direction = "LONG"
            take_profit = entry + (stop_distance * rr)
        else:
            direction = "SHORT"
            take_profit = entry - (stop_distance * rr)

        percent_move = (stop_distance / entry) * 100
        position_value = risk_amount / (percent_move / 100)

        st.subheader("Результат")

        st.write(f"Тип сделки: {direction}")
        st.write(f"Риск: {risk_amount:g} $")
        st.write(f"% до стопа: {percent_move:g}")
        st.write(f"Объём позиции: {position_value:g} $")
        st.write(f"Тейк профит: {take_profit:g}")
