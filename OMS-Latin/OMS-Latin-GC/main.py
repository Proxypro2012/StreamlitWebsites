import streamlit as st
import streamlit_extras.let_it_rain
from streamlit_extras.card import card
import streamlit_extras.theme
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac
import os
import random
import json
import base64

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])


nav_pages = ["Notes", "PMAQ", "Contribute!"]
notification_txts = ["Website Updated Daily!", "Check out the PMAQ!", "Check out the Notes section!", "Please consider contributing!"]
selected_page = st.sidebar.radio("Navigation", nav_pages)


notificationMessage = random.choice(notification_txts)
st.toast(notificationMessage)


class Chapter4Vocabulary:
    def display_vocabulary(self):
        st.write("molestus, -a, -um: bothersome, troublesome, annoying")
        st.write("semper: always")
        st.write("vexāre: to annoy, to bother [vexat, vexant]")
        st.write("igitur: therefore")
        st.write("amāre: to like, to love [amat, amant]")
        st.write("dormīre: to sleep [dormit, dormiunt]")
        st.write("cōnspicere: to catch sight of, notice, see [cōnspicit, cōnspiciunt]")
        st.write("fūrtim: stealthily, sneakily")
        st.write("appropinquāre: to approach [appropinquat, appropinquant]")
        st.write("ascendere: to climb [ascendit, ascendunt]")
        st.write("magnus, -a, -um: great, big")
        st.write("magnā vōce: in a big (loud) voice")
        st.write("audīre: to hear, to listen (to) [audit, audiunt]")
        st.write("vidēre: to see [videt, vident]")
        st.write("vōx / vōcem: voice")
        st.write("terrēre: to scare, frighten [terret, terrent]")
        st.write("sollicitus, -a, -um: anxious, worried")
        st.write("tum: then")
        st.write("“Dēscende, Sexte!”: Climb down, Sextus!")
        st.write("tū: you (subject)")
        st.write("nihil: nothing")
        st.write("tē: you (direct object)")
        st.write("“Cāvē!”: Be careful! Beware!")
        st.write("rāmus: branch")
        st.write("infirmus, -a, -um: weak, shaky")
        st.write("fragor / fragōrem: loud noise, crash")



class LatinPMAQ():
    def display_pmaq(self):
        st.write("Notā bene — Note well")
        st.write("Et cetera (etc.) — And the rest")
        st.write("Et alia (et al.) — And the others")
        st.write("Ante meridiem (a.m.) — Before mid day")
        st.write("Post meridiem (p.m.) — After midday")
        st.write("Senatus Populusque Romanus (SPQR) — The Senate and People of Rome")
        st.write("Ab urbe conditā (A.U.C.) — From the founding of the city (Rome, 753 BCE)")
        st.write("Ex nihilō nihil fit — Nothing comes from nothing")
        st.write("Id est (i.e.) — That is")
        st.write("Modus operandī (M.O.) — Way of operating")
        st.write("Circa (c. or c.a.) — Around")
        st.write("Pro tempore (pro tem.) — For the time being")
        st.write("Nihil per os (n.p.o.) — Nothing through the mouth")
        st.write("Veritas — Truth (Harvard)")
        st.write("Lux et veritas — Light and truth (Yale)")
        st.write("Nil sine magnō labore — Nothing without great labor (Brooklyn)")
        st.write("Vox clamantis in desertō — The voice of one calling out in the desert (Motto of Dartmouth)")
        st.write("Esse quam viderī — To be rather than to seem (Motto of North Carolina)")
        st.write("Ad astra per aspera — To the stars through difficulties (Motto of Kansas)")
        st.write("Labor omnia vincit — Work conquers all (Motto of Oklahoma)")
        st.write("Dirigō — I lead (Maine)")
        st.write("Excelsior — Ever Upward (New York)")
        st.write("Veritas Vos liberabit — The truth will set you free (John Hopkins University)")
        st.write("Sapientia et suā et docendī causā — Knowledge for both its own sake and for teaching (University of Albany)")
        st.write("Labor omnia vincit — Work conquers all (Motto of Oklahoma)")
        st.write("Lo Saturnalia! — Hey Saturnalia!")
        st.write("Diēs festus — Holiday")
        st.write("Saturnalibus optimō dierum — …on Saturnalia, the best of days")
        st.write("Dum Spiro Spero — While I breathe I hope (Motto of South Carolina)")
        st.write("Ditat Deus — God Enriches (Motto of Arizona)")
        st.write("Deo Gratias habeamus — Let have thanks to God (Motto of Kentucky)")
        st.write("Sine Quā nōn — Not Without Which / The Necessities (English Grammar)")
        st.write("Crescit Eundo — It Grows By Going (Motto of New Mexico)")
        st.write("Eureka — I found it! (Motto of California)")
        st.write("Esto perpetua — May it last forever (Motto of Idaho)")
        st.write("Ensemble Petit Placidam Sub Libertate Quietem — With a Sword She Seeks Peaceful Quiet Under The Liberty (Motto of Massachusetts)")
        st.write("Ē Pluribus Unum — One Out Of Many (United States)")
        st.write("Annuit Coeptīs — He Has Favored Our Undertaking (Motto of United States)")
        st.write("Ordo seclōrum — a new order (United States)")
        st.write("Novus ordo seclōrum — a new order of the ages (United States)")
        st.write("Alīs volat propriīs — she flies by her own wings (Motto of Oregon)")
        st.write("Cedant arma togae — Let arms (weapons) yield to the toga (Let war give way to peace) (Motto of Wyoming)")
        st.write("Q isra nostra defendere — We dare to defend our rights (Motto of Alabama)")
        st.write("Justitia omnibus — Justice for all (Motto of Washington D.C)")
        st.write("Io Saturnalia! — Hey, Saturnalia! (Festive Holidays)")
        st.write("Optimō diērm— on the best of days (Catullus, writing about Saturnalia)")
        st.write("Opalia — the festival for Ops (Saturnalia)")
        st.write("Annus novus — New Year (Felicam annus novus— Happy New Year)")
        st.write("Imperium in imperio — An empire in an empire (Motto of Ohio)")
        st.write("Motanī simper liberī — Mountain people (are) always free (Motto of West Virginia)")
        st.write("Nil sine nominee — Nothing without good (Motto of Colorado)")
        st.write("Qui transtulit sustinet — He who transplate (us) sustains (us) (Motto of Connecticut)")
        st.write("Regnat populus — The people rule (Motto of Arkansas)")
        st.write("Salus populi supermen lex esto — Let the welfare of the people be the highest law (Motto of Missouri)")
        st.write("Scutō bones voluntatius tube coronatsi nōs — You have crowned us with the shield of your good will (Motto of Maryland)")
        st.write("Si quaeris peninsulam amoenam, circumspice — If you seek a pleasant peninsula look around (Motto of Michigan)")
        st.write("Aic simper tyranis — Thus always to tyrants (Motto of Virginia)")
        st.write("Virtute et armīs — By courage and arms")
        st.write("Aut I am inveniam aut faciam — I’ll either find a way or I’ll make one (Hannibal, the enemy of Rome)")
        st.write("Aut Caesar aut nihil — It’s Caesar or its nothing")
        st.write("Gerit — wears")
        st.write("Gerunt — they wear")
        st.write("Velocius quam asparagi coquantur — Faster than boiled asparagus! — Favorite saying of Augustus")
        st.write("Vox populī — The Voice Of The People")
        st.write("Semper paratus — Always Prepared")
        st.write("Semper fidelis — Always Faithful")
        st.write("Errare humanum est — Error is human (mistakes are human/ mistakes are good)")
        st.write("Ex nihilo nihil fit — Nothing comes from nothing (Lucretiu)")
        st.write("Ex Librīs - From the Library")
        
    



class EdPuzzleNotes():
    def display_edpuzzle_notes(self):
        text = """
        **Noun:**  
        A person, place or thing  
        Intangible concepts/ideas (virtue, courage)  
        Essential for all sentences in English (at least as the subject)
        
        **Verb:**  
        A necessity for all grammatically correct sentences  
        Verbs are actions (caught) or states of being (exists)  
        Don’t forget the common linking verb is (am, are)
        
        **Adjective:**  
        A word “attached” to the noun  
        Adjectives describe nouns  
        Colors are adjectives and so are numbers
        
        **Adverb:**  
        Words like soon and quickly  
        Adverbs describe verbs (and other things)
        
        **Prepositional Phrase:**  
        Short phrases like in the house  
        Consist of a preposition (e.g, in, on, under, with) followed by a noun
        """
        
        # Display the text in Streamlit using markdown
        st.markdown(text)






if selected_page == nav_pages[0]:
    st.subheader("Welcome to the OMS Latin Website!")
    st.write("Nil sine magnō labore — Nothing without great labor (Brooklyn)")
    st.write("Developed and Managed by Kabir Tiwari")

    for i in range(10):
        st.write("")
    
    st.header("Ecce Romani")
    card(title="Chapter 4", text="Ecce Romani")

    st.subheader("Chapter 4 Vocabulary:")

    for i in range(5):
        st.write("")  # Add some spacing

    # Instantiate and display the Chapter 4 Vocabulary after the content
    c4v = Chapter4Vocabulary()
    c4v.display_vocabulary()

    
    for i in range(10):
        st.write("")
    st.image("edpuzzle-logo.png")
    st.header("EdPuzzle Notes")
    for i in range(5):
        st.write("")  # Add some spacing

    edpn = EdPuzzleNotes()
    edpn.display_edpuzzle_notes()




        
    


if selected_page == nav_pages[1]:
        st.title("Latin PMAQ")
        st.write("Daily Phrase or Quote")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        latinpmaq = LatinPMAQ()
        latinpmaq.display_pmaq()


    
        

if selected_page == nav_pages[2]:
    st.title("Contribute!")
    st.write("It takes a lot of hard work to do well in school and manage a website at the same time!")
    st.write("Please consider supporting development by contributing to the PMAQ or Notes! (or just pay me ;)")

    


streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")
