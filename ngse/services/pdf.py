from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import black, gray

#################Page 1######################
def NGSE01(c, ans):
    c.showPage()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(gray)
    c.drawString(58, 800, "Form NGSE-01")


def header(c, ans):
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(gray)
    c.drawString(58, 800, "Form NGSE-01")
    c.setFont('Helvetica-Bold', 16)
    c.setFillColor(black)
    c.drawCentredString(306, 760, 'National Graduate School of Engineering')
    c.setFont('Helvetica', 12)
    c.drawCentredString(306, 748, 'College of Engineering')
    c.drawCentredString(306, 736, 'UNIVERSITY OF THE PHILIPPINES')
    c.drawCentredString(306, 725, 'Diliman, Quezon City 1101 Philippines')

    c.setFont('Helvetica-Bold', 20)
    c.drawCentredString(306, 680, 'APPLICATION FORM')
    c.setFont('Helvetica-Bold', 12)
    c.drawCentredString(306, 670, 'Admission to the Graduate Program')
    photobox(c, ans)


def photobox(c, ans):
    c.setStrokeColor(gray)
    c.rect(475, 705, 90, 90, stroke=1, fill=0)
    c.setFont('Times-Italic', 10)
    c.setFillColor(gray)
    c.drawCentredString(520, 760, "Staple two pieces")
    c.drawCentredString(520, 750, "of passport-sized")
    c.drawCentredString(520, 740, "photographs here")
    name(c, ans)


def name(c, ans):
    c.setStrokeColor(black)
    c.setFont('Helvetica', 14)
    c.setFillColor(black)
    c.rect(40, 635, 526, 25, stroke=1, fill=0)
    ################NAME#########################
    c.drawCentredString(140, 642, ans['lastname'])
    c.drawCentredString(306, 642, ans['givenname'])
    c.drawCentredString(472, 642, ans['middlename'])
    #################NAME#########################
    c.setFont('Times-Italic', 10)
    c.setFillColor(black)
    c.drawCentredString(140, 625, "Last Name")
    c.drawCentredString(306, 625, "Given Name")
    c.drawCentredString(472, 625, "Middle/Maiden Name")
    instruct(c, ans)


def instruct(c, ans):
    c.setStrokeColor(black)
    c.rect(40, 580, 526, 20, stroke=1, fill=0)
    c.setFont('Helvetica-Bold', 15)
    c.setFillColor(black)
    c.drawCentredString(306, 584, "INSTRUCTIONS")
    c.rect(40, 353, 526, 247, stroke=1, fill=0)
    c.setFont('Helvetica', 9)
    array = []
    curr = 568
    for i in xrange(20):
        array.append(curr)
        curr = curr - 13
    c.drawString(45, array[0], "1. Accomplish properly Form NGSE-01.")
    c.drawString(45, array[1],
                 "2. Pay a nonrefundable application fee of PHP100.00 for Filipino and resident foreign applicants at the Cashier's Office. For ")
    c.drawString(45, array[2],
                 "non-resident applicants, send a check of USD 20.00 payable to the 'University of the Philippines' together with the application")
    c.drawString(45, array[3], "documents.")
    c.drawString(45, array[4],
                 "3. Request three (3) former professors or technical experts acting as your supervisor as references to accomplish Form NGSE-02.")
    c.drawString(45, array[5],
                 "Each accomplished form should be enclosed in a sealed envelope, with a signature across the seal. Accomplished forms may be")
    c.drawString(45, array[6], "returned to the applicant or may be sent directly to the NGSE Office.")
    c.drawString(45, array[7], "4. Submit all the accomplished forms together with the following requirements:")
    c.drawString(45, array[8],
                 "	- One (1) official copy and two (2) photocopies of Transcript of Records bearing the school seal and the registrar's signature")
    c.drawString(45, array[9], "   - Application fee receipt")
    c.drawString(45, array[10], "   - Three (3) recent passport size pictures")
    c.drawString(45, array[11],
                 "   - Original and one (1) photocopy of NSO Birth Certificate (for Filipino applicants)")
    c.drawString(45, array[12], "   - Photocopy of passport (for foreign applicants)")
    c.drawString(45, array[13],
                 "   - TOEFL official score (Only for foreign applicants whose native language or primary medium of instruction in secondary school")
    c.drawString(45, array[14],
                 "   and college is not English). A score of at least 61 in the internetbased Test of English as a Foreign Language (Educational")
    c.drawString(45, array[15], "   Testing Service, Princeton, New Jersey, 08540 USA) is required.")
    c.drawString(45, array[16],
                 "5. Wait for the final decision on your application, which will be communicated to you by email and/or phone.")
    NGSE(c, ans)


def NGSE(c, ans):
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(305, 310, "For National Graduate School of Engineering Office Use Only")
    c.setFont('Helvetica', 9)
    c.setFillColor(gray)
    c.drawCentredString(305, 300, "(To the Applicant: Do not fill this portion)")
    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    c.drawString(50, 278, "Date of Submission:")
    c.line(150, 278, 250, 278)
    c.drawString(310, 278, "O.R. Number:")
    c.line(380, 278, 500, 278)
    c.drawString(84, 268, "Received by:")
    c.line(150, 268, 250, 268)
    c.rect(310, 230, 200, 40, stroke=1)
    Dept(c, ans)


def Dept(c, ans):
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(305, 210, "For Department/Institute/Program Admission Committee Use Only")
    c.setFont('Helvetica', 9)
    c.setFillColor(gray)
    c.drawCentredString(305, 200, "(To the Applicant: Do not fill this portion)")
    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    c.drawString(50, 180, "The Department/Institute/Program Admission Committee recommends that the applicant be")
    c.rect(58, 160, 10, 10, stroke=1)
    c.drawString(75, 162, "admitted as a graduate degree student")
    c.rect(58, 144, 10, 10, stroke=1)
    c.drawString(75, 146,
                 "admitted as a non-degree student (probationary admission) subject to the following condition(s):")
    c.line(80, 134, 540, 134)
    c.line(80, 124, 540, 124)
    c.line(80, 114, 540, 114)
    c.rect(58, 100, 10, 10, stroke=1)
    c.drawString(75, 102, "refused admission")
    c.line(70, 70, 350, 70)
    c.setFont('Helvetica-Bold', 9)
    c.drawCentredString(210, 60, "Department Chairman/Institute Director/Program Coordinator")
    c.drawCentredString(210, 50, "Printed Name")
    c.line(440, 70, 500, 70)
    c.drawCentredString(470, 60, "Date")


#############Page 2####################

def ProgramOfStudy(c, ans):
    NGSE01(c, ans)
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 760, "I.   PROGRAM OF STUDY")
    c.setFont('Helvetica', 10)
    #########Degree Program##########
    c.drawString(50, 740, "1.a.	 Degree Program: Master of Science in Computer Science")
    #########Thesis Option###########
    c.drawString(50, 725, "1.b.	 THESIS OPTION")
    #########Full-Time###############
    c.drawString(50, 710, "1.c.	 Full-Time")
    ThesisOption(c, ans)  ###IF THESIS OPTION###
    ######Start of Study#####
    c.drawString(50, 635, "1.e.	 Intended start of program study: First Semester AY 2020-2021")
    ######Scholarship#######
    c.drawString(50, 620, "1.f.	  Applying for another scholarship/grant? Yes")
    c.drawString(100, 605, "		 Name of Scholarship Program: ERDT")
    c.drawString(50, 590, "1.g.	 For THESIS OPTION:")
    c.drawString(100, 575, "		 Name of Potential Adviser:")


def ThesisOption(c, ans):
    c.drawString(50, 695, "1.d.	 For THESIS OPTION:")
    c.drawString(100, 680, "RANK 1:	CSG")
    c.drawString(100, 665, "RANK 2:	NDSG")
    c.drawString(100, 650, "RANK 3:	CVMIG")


def PersonalInfo(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 550, "II.  PERSONAL INFORMATION")
    c.setFont('Helvetica', 10)
    c.drawString(50, 530, "2.a.")
    c.drawString(100, 530, "Last Name: " + ans['lastname'])
    c.drawString(100, 515, "Given Name: " + ans['givenname'])
    c.drawString(100, 500, "Middle Name: " + ans['middlename'])
    c.drawString(100, 470, "Country of Origin: " + ans['countryoforigin'])
    c.drawString(100, 485, "Citizenship: " + ans['citizenship'])
    c.drawString(350, 530, "Gender: " + ans['sex'])
    c.drawString(350, 515, "Birth Date: " + ans['birthdate'])
    c.drawString(350, 500, "Birth Place: " + ans['birthplace'])
    c.drawString(350, 485, "Civil Status: " + ans['civilstatus'])

    c.drawString(50, 440, "2.b.")
    c.drawString(100, 440, "Current Address: " + ans['currentaddress'])
    c.drawString(100, 425, "Postal Code: " + ans['currentpostal'])
    c.drawString(100, 410, "Permanent Address:" + ans['permanentaddress'])
    c.drawString(100, 395, "Postal Code: " + ans['permanentpostal'])

    c.drawString(50, 365, "2.c.")
    c.drawString(100, 365, "Telephone Number: " + ans['telephonenumber'])
    c.drawString(100, 350, "Fax Number: " + ans['faxnumber'])
    c.drawString(100, 335, "Email Address: " + ans['emailaddress'])

    c.drawString(50, 315, "2.d.")
    c.drawString(100, 315, "Father's Name: " + ans['fathersname'])
    c.drawString(100, 300, "Mpther's Name: " + ans['mothersname'])

    c.drawString(50, 270, "2.e.")
    c.drawString(100, 270, "Emergency Contact Person: " + ans['emergencyname'])
    # c.drawString(100, 290, "Complete Name: ")
    c.drawString(100, 255, "Complete Address: " + ans['emergencyaddress'])
    c.drawString(100, 240, "Relationship: " + ans['emergencyrelationship'])
    c.drawString(100, 220, "Contact Number: " + ans['emergencynumber'])


def EmploymentInfo(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 195, "III.  EMPLOYMENT INFORMATION")
    c.setFont('Helvetica', 10)
    c.drawString(50, 175, "3.a.")
    c.drawString(100, 175, "Current Employment Status: " + ans['curremploymentstatus'])

    c.drawString(50, 155, "3.b.")
    c.drawString(100, 155, "Current Employed Applicants(Full-Time/Part-Time)")
    c.drawString(100, 140, "Position:" + ans['curremployedposition'])
    c.drawString(100, 125, "Company Name: " + ans['curremployedcompanyname'])
    c.drawString(100, 110, "Office Address: " + ans['curremployedofficeaddr'])
    c.drawString(100, 95, "E-mail Address: " + ans['curremployedcompanyemail'])
    c.drawString(350, 140, "Length of Service: " + ans['curremployedlengthofservice'])
    c.drawString(350, 125, "Telephone Number: " + ans['curremployedcompanytelenum'])
    c.drawString(350, 110, "Fax Number: " + ans['curremployedfaxnum'])
    c.drawString(350, 95, "Company Website: " + ans['curremployedcompanywebsite'])

    c.drawString(50, 75, "3.c.")
    c.drawString(100, 75, "Self-Employed Applicants")
    c.drawString(100, 60, "Business Name: " + ans['selfemployedbusinessname'])
    c.drawString(100, 45, "Business Address:" + ans['selfemployedbusinessaddress'])
    c.drawString(100, 30, "E-mail/Website: " + ans['selfemployedbusinessemail'])
    c.drawString(350, 60, "Type of Business: " + ans['selfemployedbusinesstype'])
    c.drawString(350, 45, "Telephone Number: " + ans['selfemployedbusinesstelnum'])
    c.drawString(350, 30, "Years of Operation: " + ans['selfemployedyearsofoper'])

    ################Page 3###############

    NGSE01(c, ans)
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(50, 760, "3.d.")
    c.drawString(100, 760, "Employment History")
    c.rect(65, 650, 500, 100, stroke=1)


def AcadBg(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 630, "IV. ACADEMIC BACKGROUND")
    c.setFont('Helvetica', 10)
    c.drawString(50, 610, "4.a")
    c.drawString(100, 610, "Secondary Education")
    c.drawString(100, 595, "Last High School Attended")
    c.drawString(100, 580, "School Name: " + ans['secondaryeducschoolname'])
    c.drawString(100, 565, "School Address: " + ans['secondaryeducschooladdress'])
    c.drawString(350, 610, "Date Started: " + ans['secondaryeducdatestarted'])
    c.drawString(350, 595, "Date Graduated: " + ans['secondaryeducdategraduated'])

    c.drawString(50, 550, "4.b")
    c.drawString(100, 550, "Tertiary Education")
    c.rect(65, 435, 500, 100, stroke=1)
    c.drawString(100, 525, "this is me")

    c.drawString(50, 415, "4.c")
    c.drawString(100, 415, "Post-Graduate Studies")
    c.rect(65, 300, 500, 100, stroke=1)

    c.drawString(50, 280, "4.d")
    c.drawString(100, 280, "Scholastic Honors & Awards Received")
    c.rect(65, 165, 500, 100, stroke=1)

    c.drawString(50, 145, "4.e")
    c.drawString(100, 145, "Recent Scientific Publications")
    c.rect(65, 30, 500, 100, stroke=1)

    #############Page 4##############
    NGSE01(c, ans)
    c.setFillColor(black)
    c.setFont('Helvetica', 10)

    c.drawString(50, 760, "4.f")
    c.drawString(100, 760, "Recent Scientific Conference Presentations")
    c.rect(65, 645, 500, 100, stroke=1)

    c.drawString(50, 625, "4.g")
    c.drawString(100, 625, "Other Qualifications")
    c.rect(65, 510, 500, 100, stroke=1)


def EnglishProf(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 490, "V. ENGLISH PROFICIENCY")
    c.setFont('Helvetica', 10)

    c.drawString(50, 470, "First Language: " + ans['firstlang'])
    c.drawString(50, 455, "Primary Medium of Instruction")
    c.drawString(100, 440, "Secondary Level: " + ans['mediumofinstruction2nd'])
    c.drawString(100, 425, "Tertiary Level: " + ans['mediumofinstruction3rd'])

    c.drawString(50, 410, "Test of English Proficiency")
    c.drawString(100, 395, "Date Taken: " + ans['engproficiencydatetaken'])
    c.drawString(100, 380, "Exam Score: " + ans['engproficiencyscore'])


def ProgramProf(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 360, "VI. PROGRAMMING PROFICIENCY")
    c.setFont('Helvetica', 10)

    c.drawString(100, 340, "Programming Language: " + ans['lang1'])
    c.drawString(100, 325, "Programming Language: " + ans['lang2'])
    c.drawString(100, 310, "Programming Language: " + ans['lang3'])
    c.drawString(100, 295, "Programming Language: " + ans['lang4'])
    c.drawString(100, 280, "Programming Language: " + ans['lang5'])

    c.drawString(350, 340, "Level of Proficiency: " + ans['prof1'])
    c.drawString(350, 325, "Level of Proficiency: " + ans['prof2'])
    c.drawString(350, 310, "Level of Proficiency: " + ans['prof3'])
    c.drawString(350, 295, "Level of Proficiency: " + ans['prof4'])
    c.drawString(350, 280, "Level of Proficiency: " + ans['prof5'])

    c.drawString(65, 255, "Projects/Applications")
    c.rect(65, 170, 500, 80, stroke=1)


def Essay(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 150, "VII. ADMISSION ESSAY")


def References(c, ans):
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 130, "VIII. REFERENCES")
    c.rect(65, 20, 500, 100, stroke=1)


def AppDec(c, ans):
    ###########Page 5########
    NGSE01(c, ans)
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(black)
    c.drawString(40, 760, "IX. APPLICANT'S DECLARATION")
    c.setFont('Helvetica', 10)

    c.drawString(100, 740,
                 "I declare that the information supplied in this application and the documentation supporting it are")
    c.drawString(70, 730,
                 "true and complete. I acknowledge that the provision of incorrect information or documentation relating to my ")
    c.drawString(70, 720,
                 "application may result in cancellation of admission or enrolment. If admitted to the National Graduate School ")
    c.drawString(70, 710,
                 "of Engineering, I solemnly agree to abide by the rules and regulations of the College of Engineering and the ")
    c.drawString(70, 700, "University of the Philippines.")

    c.line(70, 660, 350, 660)
    c.setFont('Helvetica', 9)
    c.drawCentredString(210, 650, "Signature Over Printed Name")
    c.line(440, 660, 500, 660)
    c.drawCentredString(470, 650, "Date")


def NGSE02(c):
    c.showPage()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(gray)
    c.drawString(58, 800, "Form NGSE-02")
    c.setFillColor(black)
    c.setFont('Helvetica', 9)
    return 790, 790


def page(c, ans):
    # NGSE02(c)
    c.setFont('Helvetica-Bold', 12)
    c.setFillColor(black)
    c.drawCentredString(306, 790, 'National Graduate School of Engineering')
    c.setFont('Helvetica', 10)
    c.drawCentredString(306, 778, 'College of Engineering')
    c.drawCentredString(306, 766, 'UNIVERSITY OF THE PHILIPPINES')
    c.drawCentredString(306, 754, 'Diliman, Quezon City 1101 Philippines')
    c.setFont('Helvetica-Bold', 18)
    c.drawCentredString(306, 720, 'LETTER OF RECOMMENDATION')
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(306, 702, 'NATIONAL GRADUATE SCHOOL OF ENGINEERING (NGSE) ADMISSION')

    c.setFont('Helvetica', 10)
    c.rect(60, 670, 136, 20, stroke=1)
    c.drawString(62, 677, "APPLICANT'S EVALUATION")
    c.setFillColor(gray)
    c.drawString(200, 677, "To be filled out by the recommender.")
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 9)
    c.drawString(60, 655, "Note to Recommender: ")
    c.setFont('Helvetica', 9)
    c.drawString(160, 655,
                 "Any pertinent information regarding the applicant and your evaluation of the applicant's ability to")
    # c.drawString(540, 640, "N")
    c.drawString(60, 645, "undertake graduate studies and research will be held in strict confidence.")
    c.drawString(60, 620, "How long have you known applicant?")

    curlen = 605
    tempcur = 605

    tempcur, curlen = rectangle(ans['recommenderessay1'], curlen, tempcur, c)
    c.drawString(60, curlen, "In what capacity have you known the applicant?")
    tempcur -= 15;
    curlen -= 15
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    tempcur, curlen = rectangle(ans['recommenderessay2'], curlen, tempcur, c)

    c.drawString(60, curlen, "If the applicant was a student in some of your classes, what were these subjects?")
    tempcur -= 15;
    curlen -= 15
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    tempcur, curlen = rectangle(ans['recommenderessay3'], curlen, tempcur, c)

    c.drawString(60, curlen,
                 "What do you consider as the applicant's outstanding talents or strengths in relation to graduate study")
    tempcur -= 15;
    curlen -= 15
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    tempcur, curlen = rectangle(ans['recommenderessay4'], curlen, tempcur, c)

    c.drawString(60, curlen,
                 "What do you consider as his/her weakness or deficiencies in relation to graduate study?")
    tempcur -= 15;
    curlen -= 15
    if curlen <= 50:  tempcur, curlen = NGSE02(c)
    tempcur, curlen = rectangle(ans['recommenderessay5'], curlen, tempcur, c)

    # ins = 'Please rate the applicant on the following characteristics in comparison with other students in the same disciplines who are known to you and who have had more or less the same amount of training and experience. Indicate size of the group with which applicant is being compared and its educational level.'

    # tempcur, curlen = rectangle(ins , curlen, tempcur)
    tempcur -= 20;
    curlen -= 20

    c.drawString(60, curlen,
                 "Please rate the applicant on the following characteristics in comparison with other students in the same disciplines who are")
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen,
                 "known to you and who have had more or less the same amount of training and experience.  Indicate size of the group with")
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "which applicant is being compared and its educational level.")
    tempcur -= 20;
    curlen -= 20
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(200, curlen, "Group Size: " + ans['groupSize'])
    c.drawString(290, curlen, "Education Level: " + ans['educLevel'])
    c.rect(250, curlen - 2, 30, 10, stroke=1)

    c.rect(357, curlen - 2, 100, 10, stroke=1)

    tempcur -= 20;
    curlen -= 20
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "1. Intellectual ability: " + ans['recommenderq1'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "2. Academic preparation for proposed field of study: " + ans['recommenderq2'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "3. Motivation for proposed field of study: " + ans['recommenderq3'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "4. Originality, creativity, and imagination: " + ans['recommenderq4'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "5. Analytical and problem-solving ability: " + ans['recommenderq5'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "6. Initiative and independence: " + ans['recommenderq6'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "7. Honesty and Integrity: " + ans['recommenderq7'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "8. Conscientiousness and ability to work independently: " + ans['recommenderq8'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "9. Ability to work with others: " + ans['recommenderq9'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "10. Oral communication skills: " + ans['recommenderq10'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "11. Written communication skills: " + ans['recommenderq11'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "12. Emotional Maturity: " + ans['recommenderq12'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "13. Potential as a researcher in the discipline: " + ans['recommenderq13'])
    tempcur -= 10;
    curlen -= 10
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "14. Potential as a teacher in the discipline: " + ans['recommenderq14'])
    tempcur -= 30;
    curlen -= 30
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    c.drawString(60, curlen, "Additional information and comments about the applicants.")
    tempcur -= 15;
    curlen -= 15
    if curlen <= 50:  tempcur, curlen = NGSE02(c)
    tempcur, curlen = rectangle(ans['recommenderessay6'], curlen, tempcur, c)

    tempcur -= 15;
    curlen -= 15
    c.drawString(60, curlen, "I therefore " + ans[
        'recommendation'] + " the applicant for admission to the National Graduate School of Engineering in UP Diliman.")


def rectangle(ans, curlen, tempcur, c):
    start = 0;
    end = 95
    while (start < len(ans)):
        c.drawString(60, curlen, ans[start:end])
        curlen -= 10
        start = end + 1
        end = end + 95
    c.rect(60, curlen, 490, tempcur - curlen + 10, stroke=1)
    curlen -= 20  # this will be the new tempcur and curlen
    if curlen <= 50:  tempcur, curlen = NGSE02(c)

    return curlen, curlen
