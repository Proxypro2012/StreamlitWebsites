import random
import streamlit as st
choices = ["rock", "paper", "scissors"]

st.title("Rock, Paper, Scissors")

if 'score' not in st.session_state:
    st.session_state.score = 0





choice = str(st.text_input("Rock, paper, or scissors?")).lower().strip()
aichoice = random.choice(choices)





# Decision Taking RPS AI



if choice == aichoice:
    st.info("You tied!")
if choice == "rock":
    if aichoice == "paper":
     st.info("You Lost! Paper beats Rock.")
    if aichoice == "scissors":
        st.info("You won! Rock beats scissors.")
        st.session_state.score = st.session_state.score + 1
        st.toast("Score: " + str(st.session_state.score), icon='👍')
if choice == "paper": 
    if aichoice == "scissors":
        st.info("You Lost! scissors beats paper.")
    if aichoice == "rock":
        st.info("You won! Paper beats rock.")
        st.session_state.score = st.session_state.score + 1
        st.toast("Score: " + str(st.session_state.score), icon='👍')
if choice == "scissors":
    if aichoice == "rock":
        st.info("You Lost! Rock beats scissors.")
    if aichoice == "paper":
        st.info("You won! Scissors beats paper.")
        st.session_state.score = st.session_state.score + 1
        st.toast("Score: " + str(st.session_state.score), icon='👍')







 

