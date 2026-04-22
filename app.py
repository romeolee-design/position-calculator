import streamlit as st

st.title("Калькулятор позиции")

# Ввод
deposit = st.number_input("Депозит ($)", min_value=1.0, value=100000.0, format="%g")
risk_percent = st.number_input("Риск (%)", min_value=0.1, value=1.0, format="%g")
entry = st.number_input("Цена входа", value=0.0, format="%g")
stop = st.number_input("Стоп", value=0.0, format="%g")
rr = st.number_input("RR (например 2)", min_value=0.1, value=2.0, format="%g")

# Кнопка
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

        # округление (чтобы не было мусора)
        risk_amount = round(risk_amount, 2)
        percent_move = round(percent_move, 4)
        position_value = round(position_value, 2)
        take_profit = round(take_profit, 6)

        st.subheader("Результат")

        st.write(f"Тип сделки: {direction}")
        st.write(f"Риск: {risk_amount:g} $")
        st.write(f"% до стопа: {percent_move:g}")
        st.write(f"Объём позиции: {position_value:g} $")
        st.write(f"Тейк профит: {take_profit:g}")
