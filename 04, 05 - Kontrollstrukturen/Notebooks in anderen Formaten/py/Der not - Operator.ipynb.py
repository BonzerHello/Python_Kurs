# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.

# coding: utf-8

# ## Der `not` - Operator

# In[8]:


age = 25

if not age >= 30:
    print("ausgeführt")
    
if age < 30:
    print("ausgeführt")


# In[10]:


names = ["Max", "Nadine"]

if "Moritz" not in names:
    print("Moritz ist nicht in der Liste enthalten")
    
if not "Moritz" in names:
    print("Moritz ist nicht in der Liste enthalten")


