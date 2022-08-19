#code pkg
import streamlit as st
from PIL import Image



col1, col2 = st.columns(2)
img=Image.open('images/arpan.jpg')
col1.image(img,width=300)
col2.title("Arpan Ghosh")
col2.markdown("Hi, I am a Computer Science student with a Commerce background from Class-11, currently pursuing BCA from [Institute of Engineering and Management (IEM)](https://iem.edu.in/). I aspire to become a Software developer. I have completed my primary and secondary education from [St.Augustine's Day School School, Shyamnagar (STADS)](https://staugustineday.com/shyamnagar) which is affilated to [Council for Indian School Certificate (CISE)](https://www.cisce.org/).")
st.markdown("-----")


st.write("Hey there! This is Arpan. I am in the last year of my college pursuing Bachelor’s Degree on Computer Application.") 
st.write('Life has thoroughly taught me, again and again, to be opportunistic, and I believe I have picked it up quite well. Working smart is my second nature, for instance how efficiently the task is done is more important to me than just getting the task done. Majoring in Computer Science, I am an enthusiast for the cutting-edge inventions and innovations in this respective field and look forward to having my hands on them someday. Being from a commerce background in high school is indeed a great advantage because I started programming while I was in Class-10. I was introduced how businesses operates in Class 11 so I could clearly bridge the gap between IT and Business.')
st.write('One thing that coding has taught me is that there are numerous ways of circumventing a problem and debugging it, this eventually broadened my perspective and helped me to carve out that open-mindedness. Not only does that help me encompass the dynamic approach of coding but also opens up a lot of creative faucets in my life. Although I am a team player, my learning curve is different from others as I first prefer self-study and then I opt for group discussion. Somewhere I believe that it’s never too late to venture out for something new. We can become whoever we want to, the only thing that is required is COURAGE. There’s no ending to life’s learning and you never know who might end up giving you a life-changing advice, hence, I respect the opinion of everyone irrespective of their age or their designation. This makes me need an extra pair of eyes at times, which turns out to be the most important reality check to me. It helps me get rid of my biases and prejudices.')
st.write('One of the major takeaways that coding has taught me is that I cannot make all the mistakes myself and go through the process of hit and trial with everything, which means, not only I get to learning from my own mistakes but also, I get to learn from other’s mistakes. Now that is not only a valuable lesson in coding but in life as well, Chanakya was right! So far into life, I cannot emphasize more, the importance of good time management. This makes me the person who cuts to the chase and likes being straightforward with my approach.')
st.write('My ending note would be: Discipline, Dedication, Perseverance and a little bit of Faith can move the biggest mountains in life, we only need to have the courage to set forth for the venture we are sceptical about. If you’ve read so far, know that we have already met.')
st.markdown("-----")


st.sidebar.markdown("## Side Panel" )
st.sidebar.markdown("This is my portfolio which is made using the framework Streamlit. You can browse around using this panel to explore more about me.")
st.sidebar.subheader(' Quick  Explore')
if st.sidebar.checkbox('Basic info'):
    st.title('About me:')
    st.write('Name - Arpan Ghosh')
    st.write('Age - 21')
    st.write('DOB - 24/08/2001')
    st.write('Gender - Male')
    st.write('Education - Undergraduate')
    st.write('Location - Kolkata, West Bengal, India')
    st.write('Languages - English, Hindi, Bengali')
    st.markdown("-----")

if st.sidebar.checkbox('Interest & hobbies'):
    st.title('Interest in:')
    st.write('Backend Developer')
    st.write('Interested in Learning new technologies')
    st.write('Web Development')

    st.write('Education - Undergraduate')
    st.title('Hobbies:')
    st.write('Swimming')
    st.write('Travelling')
    st.write('Cricket')
    st.write('Gaming')
    st.markdown("-----")

if st.sidebar.checkbox('Strength & Weakness'):
    st.title('Strength:')
    st.write('Problem Solving')
    st.write('Public Speaking')
    st.write('Time Management')
    st.write('Presentation')
    st.write('Communication')
    st.write('Team Player')
    st.write('Teaching')

    st.title('Weakness:')
    st.write('Overthinking Problem')
    st.write('Trust Issues')
    st.write('Gets too much stressed and depressed.')
    st.markdown("-----")

if st.sidebar.checkbox('My Education Qualification'):
    st.title('ICSE [Class X]')
    st.write('Passing year - 2018')
    st.write('Percentage - 88.4%')
    st.write('School - St. Augustine’s Day School, Shyamnagar')

    st.title('ISC [Class XII]')
    st.write('Passing year - 2020')
    st.write('Percentage - 86%')
    st.write('School - St.Augustine’s Day School, Shyamnagar')

    
    st.title('Undergraduation')
    st.write('Passing year - 2023')
    st.write('SGPA - 9.56 [till 3rd Semester].')
    st.write('College - Institute of Engineering and Management')
    st.markdown("-----")
    
if st.sidebar.checkbox('Technical Skillsets:'):
    st.title('Programming languages:')
    st.write('OOPs Using JavaSE17')
    st.write('Python(Basic')
    st.write('JavaScript and TypeScript')

    st.title("Database:")
    st.write('Oracle SQL, Mysql and MongoDB')
    st.title('FrontEnd Development: -')
    st.write('HTML, CSS, React, Bootstrap and Angular')
    st.title('Frameworks: - ')
    st.write('Flask, Django and Streamlit')
    st.title('Backend Development: -')
    st.write('NodeJS,Express and Spring Boot')
    st.title('AI/ML: - ')
    st.write('Seaborn, Pandas and Scikit-Learn')
    st.title('Backend as a Service(BaaS): -')
    st.write('FireBase and Heroku')
    st.title('Software Known: -')
    st.write('Windows11(including CMD), Visual Studio Code, Google Chrome, Jupyter, MS-Office, Postman, Eclipse.')
    st.title('Others: -')
    st.write('Git CLI')
    st.markdown("-----")

if st.sidebar.checkbox('Work exp.'):
    st.title("Work experience:")
    st.write('Technical Content Writer at CoreLabs  -  1month(2021)')
    st.write('Digital Marketing at Applex  -  2 months(2021)')
    st.markdown("-----")


if st.sidebar.checkbox('Contact me'):
    st.title("Professional:")
    st.write('Email - arpanghoshiembca2023@gmail.com')
    st.write('Mobile - 7003378772 / 9883952010')
    st.write('[Linkedin](https://www.linkedin.com/in/ArpanGhosh2408/)')
    st.write('[Github](https://github.com/arpanghosh2416)')
    st.markdown("-----")
if st.sidebar.checkbox('GoodBye'):
    st.write('Hope you like my portfolio and my email is always there as well as both are WhatsApp Numbers. Feel free to text me or contact me.')
    st.write('You can also check my Github Portfolio on the visiting page.')
    st.markdown("-----")
    st.write('This is the end of my Portfolio.')

