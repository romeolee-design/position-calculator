import streamlit as st

st.title("Калькулятор позиции")

deposit = 100000

risk_percent = st.number_input("Риск (%)", value=1.0)
entry = st.number_input("Цена входа", value=0.0)
stop = st.number_input("Стоп", value=0.0)
rr = st.number_input("RR", value=2.0)

if st.button("Рассчитать"):

    if entry == stop:
        st.error("Ошибка: вход равен стопу")
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

        st.write(f"Тип сделки: {direction}")
        st.write(f"Риск: {risk_amount:g} $")
        st.write(f"% до стопа: {percent_move:g}")
        st.write(f"Объём позиции: {position_value:g} $")
        st.write(f"Тейк: {take_profit:g}")
