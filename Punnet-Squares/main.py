import streamlit as st
import streamlit_extras
import streamlit_extras.let_it_rain
from streamlit_extras.card import card
import streamlit_extras.theme
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac



if 'show_card' not in st.session_state:
    st.session_state.show_card = False
if 'box1type' not in st.session_state:
    st.session_state.box1type = False
if 'box2type' not in st.session_state:
    st.session_state.box2type = False
if 'box3type' not in st.session_state:
    st.session_state.box3type = False
if 'box4type' not in st.session_state:
    st.session_state.box4type = False
if 'valueshelper' not in st.session_state:
    st.session_state.valueshelper = []


r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 0.25, 1])


###############
# #####################################

def remove_duplicates(input_list):
    seen = set()  # A set to track seen items
    result = []  # A list to store the final result with only original occurrences

    for item in input_list:
        if item not in seen:
            result.append(item)  # Add the first occurrence of the item to result
            seen.add(item)  # Mark the item as seen (only the first occurrence)

    return result  # Return the list with the original items only




           



def get_percent(type, list):
    if type == "both":                
        boxchance = list.count("Homozygous Dominant") * 25
        boxchance2 = list.count("Heterozygous") * 25
        return boxchance + boxchance2
    else:

        boxchance = list.count("Homozygous Recessive") * 25        
        return boxchance
    














def get_phenotype(type, gene):
   output = ""
   if gene == "Color": 
        if type == "Homozygous Recessive":
            output = "Purple"
            

        if type == "Homozygous Dominant":
            output = "Red"


        if type == "Heterozygous":
            output = "Red"
   if gene == "Sweetness": 
        if type == "Homozygous Recessive":
            output = "Very Sweet"
            

        if type == "Homozygous Dominant":
            output = "Slightly Sweet"


        if type == "Heterozygous":
            output = "Slightly Sweet"
  
   if gene == "Spice level": 
        if type == "Homozygous Recessive":
            output = "Not spicy"
            

        if type == "Homozygous Dominant":
            output = "Very spicy"


        if type == "Heterozygous":
            output = "Very spicy"
   return output        
    
    

















def cross_genotypes(palleles1, palleles2, gene):
    if palleles1 == "" and palleles2 == "": 
      st.info("Please provide an input") 
    else:      
        box1 = palleles1[0] + palleles2[0]
        box2 = palleles1[1] + palleles2[0]
        box3 = palleles1[0] + palleles2[1]
        box4 = palleles1[1] + palleles2[1]
        if "C" in palleles1 or "c" in palleles1:
            genotype = "Color"
        if "S" in palleles1 or "s" in palleles1:
            genotype = "Sweetness"
        if "P" in palleles1 or "p" in palleles1:
            genotype = "Spice Level"
        if box1[0] == box1[1].lower():
                box1 = box1[::-1]
        else:
            box1 = box1        
        if box2[0] == box2[1].lower():
                box2 = box2[::-1]
        else:
            box2 = box2        
        if box3[0] == box3[1].lower():
                box3 = box3[::-1]
        else:
            box3 = box3
        if box4[0] == box4[1].lower():
                box4 = box4[::-1]
        else:
            box4 = box4        
        col1, col2 = st.columns([0.25, 0.25])
        r2col1, r2col2 = st.columns([0.25, 0.25])
        values = [st.session_state.box1type, st.session_state.box2type, st.session_state.box3type, st.session_state.box4type]
        valueshelper = []        
        with col1:
            with st.popover(box1): #key=f'betn_{box3}'):
                if str(box1)[0] == str(box1)[1]:
                    contains_upper = any(c.isupper() for c in box1)
                    if contains_upper == True:
                        st.write("This offspring's genotype will be Homozygous Dominant")
                        st.session_state.box1type = "Homozygous Dominant"
                        phenotype = get_phenotype(st.session_state.box1type, gene=gene)
                        percent1 = get_percent(type="both", list=values) 
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent1)
                        valueshelper.append(phenotype)                        
                    else:
                        st.write("This offspring's genotype will be Homozygous Recessive")
                        st.session_state.box1type = "Homozygous Recessive"
                        phenotype = get_phenotype(st.session_state.box1type, gene=gene)
                        percent1 = get_percent(type="single", list=values)
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent1)
                        valueshelper.append(phenotype)                    
                else:
                    st.write("This offspring's genotype will be Heterozygous")
                    st.session_state.box1type = "Heterozygous"
                    phenotype = get_phenotype(st.session_state.box1type, gene=gene)
                    percent1 = get_percent(type="both", list=values)
                    st.write("This offspring will be " + phenotype)
                    valueshelper.append(percent1)
                    valueshelper.append(phenotype)        
        with col2:
            with st.popover(box2): #key=f'betn_{box3}')
                if str(box2)[0] == str(box2)[1]:
                    contains_upper = any(c.isupper() for c in box2)
                    if contains_upper == True:
                        st.write("This offspring's genotype will be Homozygous Dominant")
                        st.session_state.box2type = "Homozygous Dominant"
                        phenotype = get_phenotype(st.session_state.box2type, gene=gene)
                        percent2 = get_percent(type="both", list=values)   
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent2)  
                        valueshelper.append(phenotype)
                    else:
                        st.write("This offspring's genotype will be Homozygous Recessive")
                        st.session_state.box2type = "Homozygous Recessive"
                        phenotype = get_phenotype(st.session_state.box2type, gene=gene)
                        percent2 = get_percent(type="single", list=values)
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent2)
                        valueshelper.append(phenotype)          
                else:
                    st.write("This offspring's genotype will be Heterozygous")
                    st.session_state.box2type = "Heterozygous"
                    phenotype = get_phenotype(st.session_state.box2type, gene=gene)
                    percent2 = get_percent(type="both", list=values)    
                    st.write("This offspring will be " + phenotype)
                    valueshelper.append(percent2)
                    valueshelper.append(phenotype)
        with r2col1:
            with st.popover(box3): #key=f'betn_{box3}'):
                if str(box3)[0] == str(box3)[1]:
                    contains_upper = any(c.isupper() for c in box3)
                    if contains_upper == True:
                        st.write("This offspring's genotype will be Homozygous Dominant")
                        st.session_state.box3type = "Homozygous Dominant"
                        phenotype = get_phenotype(st.session_state.box3type, gene=gene)
                        percent3 = get_percent(type="both", list=values) 
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent3)
                        valueshelper.append(phenotype)                  
                    else:
                        st.write("This offspring's genotype will be Homozygous Recessive")
                        st.session_state.box3type = "Homozygous Recessive"
                        phenotype = get_phenotype(st.session_state.box3type, gene=gene)
                        percent3 = get_percent(type="single", list=values)    
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent3)
                        valueshelper.append(phenotype)                  
                else:
                    st.write("This offspring's genotype will be Heterozygous")
                    st.session_state.box3type = "Heterozygous"
                    phenotype = get_phenotype(st.session_state.box3type, gene=gene)
                    percent3 = get_percent(type="both", list=values)     
                    st.write("This offspring will be " + phenotype)
                    valueshelper.append(percent3)
                    valueshelper.append(phenotype)        
        with r2col2:
            with st.popover(box4): #key=f'betn_{box3}'):
                if str(box4)[0] == str(box4)[1]:
                    contains_upper = any(c.isupper() for c in box4)
                    if contains_upper == True:
                        st.write("This offspring's genotype will be Homozygous Dominant")
                        st.session_state.box4type = "Homozygous Dominant"
                        phenotype = get_phenotype(st.session_state.box4type, gene=gene)
                        percent4 = get_percent(type="both", list=values) 
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent4)
                        valueshelper.append(phenotype)                    
                    else:
                        st.write("This offspring's genotype will be Homozygous Recessive")
                        st.session_state.box4type = "Homozygous Recessive"
                        phenotype = get_phenotype(st.session_state.box4type, gene=gene)
                        percent4 = get_percent(type="single", list=values)  
                        st.write("This offspring will be " + phenotype)
                        valueshelper.append(percent4)
                        valueshelper.append(phenotype)
                                                                  
                else:
                    st.write("This offspring's genotype will be Heterozygous")
                    st.session_state.box4type = "Heterozygous"
                    phenotype = get_phenotype(st.session_state.box4type, gene=gene)
                    percent4 = get_percent(type="both", list=values)
                    st.write("This offspring will be " + phenotype)
                    valueshelper.append(percent4)
                    valueshelper.append(phenotype)
        r4col1, r4col2 = st.columns(2)
        editedvalues = remove_duplicates(valueshelper)
        if len(editedvalues) > 0:
            percent = editedvalues[0]  
            with r4col1:
                if len(editedvalues) > 1: 
                    card("Percent:", "The probability of offspring being " + editedvalues[1] + " is " + str(percent) + " percent")
            if len(editedvalues) > 3:  
                percent = editedvalues[2]  
                with r4col2:
                    card("Percent:", "The probability of offspring being " + editedvalues[3] + " is " + str(percent) + " percent")




####################################################                  
                        








with r2col2:  
      gene = st.selectbox("Enter the Phenotype: ", ["Color", "Sweetness", "Spice Level"])
      alleles1 = st.text_input("Enter the first parents alleles. (Eg: 'Ss')").lstrip().rstrip()
      alleles2 = st.text_input("Enter the second parents alleles. (Eg: 'Ss')").lstrip().rstrip()


with r1col2:
    st.title("Punnett Squares",)

with r2col1:
    st.image('whiteapple.png', "Apple 1")

with r3col2:
    if st.button("Cross"):
        st.session_state.show_card = True

if st.session_state.show_card:
    card(title="Punnett Square", text="Box will be generated below")
    cross_genotypes(alleles1, alleles2, gene)

with r2col3:
    st.image('whiteapple.png', "Apple 2")


streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")

